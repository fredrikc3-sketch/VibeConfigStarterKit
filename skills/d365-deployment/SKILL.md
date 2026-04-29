---
name: d365-deployment
description: Use after the Phase 1 approval gate passes to deploy configuration to a Dynamics 365 F&O environment via the Dynamics 365 ERP MCP server. Walks each module in DMF dependency order (010 → 650) through pre-deployment checks, data-entity deployment (Priority 1 — `data_*` tools), form-based deployment (Priority 2 — `form_*` tools), post-deployment actions (Priority 3 — `api_*` tools), and per-module validation. This is Phase 2 Step 2.1. ALWAYS pair with the `fo-mcp-server` skill (which holds the operational rules for every MCP tool call) and the `reinforcement-learning` skill (for failure logging).
---

# Deployment via the F&O MCP Server (Phase 2.1)

> **Required companion skills**: `fo-mcp-server` (tool rules), `d365-knowledge-routing` (file paths), `reinforcement-learning` (failure logging).

## Inputs
- Approved `Documentation/rollout-plan.md`.
- All source configuration files from Phase 1.
- Module `.md` knowledge files.

## Outputs
- Live configuration in the F&O environment.
- `Documentation/deployment-log.md` (running log).
- New entries in `ChallengeJournal/challenge_journal.json` for any failures.

---

## Method hierarchy

```
Priority 1 — Data entities (data_* tools)
   Source mapping: dmf_odata_mapping.json (match_method = "verified")
Priority 2 — Form navigation (form_* tools)
   Source: module .md (menu paths, control names)
Priority 3 — API / actions (api_* tools)
   Source: module .md (action descriptions)
```

Always try Priority 1 first. See `fo-mcp-server/SKILL.md` for the full rule set.

---

## Execution model — DELEGATED via `module-fanout`

> Per-module deployment is dispatched as sub-agents running the `module-deployment-worker` skill. The deployment orchestrator (this skill) stays in the main context and only sees the structured fan-out contract returned by each worker.

### Build the deployment dispatch table
1. Read `rollout-plan.md`. Group modules into **waves** matching their DMF dependency level:
   - Wave 1: 010 (no dependencies)
   - Wave 2: 020, 022 (depend on 010)
   - Wave 3: 025
   - Wave 4: 100, 120, 130, 140, 150, 160 (depend on 025) — **parallel within wave**
   - Wave 5: 300 (depends on 025)
   - Wave 6: 310, 320, 330, 395 (depend on 300) — **parallel within wave**
   - Wave 7: 400, 405, 410, 412, 418, 420, 430 (depend on 300+) — **parallel within wave**
   - Wave 8: 500 (depends on 300+ and 100+)
   - Wave 9: 600 (depends on 025)
   - Wave 10: 650 (depends on 025)
2. Within each wave, mark `executionMode = parallel` unless modules share a critical resource (e.g., number sequences) — when in doubt, sequential.
3. **Invoke `module-fanout`** with `worker = module-deployment-worker`. Each sub-agent runs §Per-module loop below in its own context.
4. **Wait for the wave to return** before dispatching the next wave. If any module returns `failed`, STOP — do not start the next wave.

---

## Per-module loop (run inside each sub-agent — see `module-deployment-worker`)

### 2.1.1 — Pre-deployment check
1. Verify upstream modules are deployed and validated.
2. Read the module `.md` for Critical Configuration Rules.
3. Search `ChallengeJournal/challenge_journal.json` for prior failures involving this module.
4. Load the module's section from `rollout-plan.md`.

### 2.1.2 — Deploy data entities
For each entity in the module's DMF template:
1. `data_find_entity_type` to confirm it exists.
2. `data_get_entity_metadata` for the field schema.
3. `data_find_entities` (or `data_find_entities_sql` on F&O 10.0.48+) to check what's already there.
4. Existing record → `data_update_entities` (PATCH). New → `data_create_entities` (POST).
5. Verify by reading back; spot-check key fields.
6. Record outcome in `deployment-log.md`. On failure: see §Error handling.

Naming reminders: plural entity sets, V2+ uses `HeadersV2` not `HeaderV2s`, no deep insert, enums use `Namespace.Pattern'Value'`.

### 2.1.3 — Deploy form-based configuration
For each form-deployed item:
1. `form_find_menu_item` → `form_open_menu_item`.
2. Navigate via `form_open_or_close_tab`, `form_filter_form`, `form_filter_grid`, `form_select_grid_row`.
3. `form_click_control` (New/Edit) → `form_set_control_values` → `form_open_lookup` for lookup fields → `form_save_form`.
4. Use **internal names**, never display labels.
5. `form_close_form` when done.

### 2.1.4 — Post-deployment actions
For Activate / Publish / Generate / Post:
1. `api_find_actions` to discover.
2. `api_invoke_action` to execute.
3. If unavailable via API, fall back to clicking the action button on the form.

### 2.1.5 — Module validation
- Read-back the data via the data tools.
- Inspect parameters via the form tools.
- Compare against the source files (DMF JSON / CSV / parameter-settings).
- Mark module: ✅ Deployed | ⚠️ Partial | ❌ Failed.

---

## Deployment log table

```markdown
| Module | DMF Seq | Data entities | Form config | Actions | Validation | Status | Notes |
|---|---|---|---|---|---|---|---|
| Org Admin | 010 | 35/35 | 3/3 | 1/1 | ✅ | ✅ Complete | — |
| GL Shared | 020 | 28/30 | 2/2 | 0/0 | ⚠️ 2 issues | 🔄 In Progress | CJ-2026-0001 |
```

---

## Error handling

When a deployment step fails:
1. **STOP** — read the module `.md` first (Critical Configuration Rules → Implementation Discoveries). The fix may already be documented.
2. Capture the exact error verbatim.
3. Classify:
   - Missing prerequisite → deploy prerequisite first, retry.
   - Invalid value → fix source data file, retry.
   - Entity not found → fall back to form deployment.
   - Permission denied → check security role, escalate.
   - Duplicate key → switch from create to update.
4. Log the challenge via the `reinforcement-learning` skill.
5. Update source files if the fix changed deployed state.
6. Update the module `.md` if a new rule or discovery emerged.
7. Retry.

## Hand-off
When all modules show ✅ Deployed (or ⚠️ Partial with documented gaps), hand off to the `d365-validation-testing` skill for E2E testing.
