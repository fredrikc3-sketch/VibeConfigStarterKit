---
name: module-deployment-worker
description: Sub-agent skill that deploys ONE D365 F&O module to a live environment during Phase 2.1. Invoked by `module-fanout` from `d365-deployment`. The worker pre-checks upstream state, walks the module's deployment plan (data entities → form config → actions) using the Dynamics 365 ERP MCP server (`data_*` → `form_*` → `api_*`), validates the deployed state, logs failures via `reinforcement-learning`, and returns the standard fan-out output contract. Pairs MANDATORILY with the `fo-mcp-server` skill — every MCP tool call must follow those rules.
---

# Module Deployment Worker (Layer 3)

> One sub-agent. One module. One live deployment. Push, verify, log, return.

> **Mandatory pairing**: Load `fo-mcp-server/SKILL.md` first. Every `data_*`, `form_*`, `api_*` call must obey those rules.

---

## You receive (from `module-fanout`)
- `module`, `dmfSeq`, `modulePath`, `dmfTemplate`
- The module's section of `Documentation/rollout-plan.md`
- The module's CSV data files + `parameter-settings.md` rows

## You must produce
- Live configuration in F&O for this module.
- Module's row in `Documentation/deployment-log.md`.
- Journal entries for any failures.
- Standard fan-out output contract.

---

## Procedure

### 1. Pre-deployment check
- Verify upstream waves' modules show ✅ Deployed in `deployment-log.md`. If not, return `failed` with the missing prerequisite.
- Read `<modulePath>` (Critical Configuration Rules + Implementation Discoveries).
- Search `ChallengeJournal/challenge_journal.json` for `module = <name>` AND `status = resolved` — apply documented preventive measures.

### 2. Deploy data entities (Priority 1)
For each entity flagged for data-entity deployment in the module's rollout plan:
1. `data_find_entity_type` → confirm exists.
2. `data_get_entity_metadata` → field schema.
3. `data_find_entities` (or `data_find_entities_sql` on F&O 10.0.48+) → check existing.
4. Existing → `data_update_entities`. New → `data_create_entities`.
5. Verify by reading back; spot-check key fields.
6. On failure: §Failure handling.

### 3. Deploy form-based configuration (Priority 2)
Walk every `parameter-settings.md` row scoped to your module:
1. `form_find_menu_item` → `form_open_menu_item`.
2. Navigate to the right tab/grid via `form_open_or_close_tab`, `form_filter_form/grid`, `form_select_grid_row`.
3. `form_click_control` (New/Edit) → `form_set_control_values` → `form_open_lookup` for lookups → `form_save_form`.
4. `form_close_form` when the form section is done.

### 4. Execute post-deployment actions (Priority 3)
For Activate / Publish / Generate / Post:
1. `api_find_actions` to discover.
2. `api_invoke_action` to execute.
3. Fall back to clicking the action button via form tools if not exposed via API.

### 5. Validate
- Read back records via `data_*` tools — counts and key fields match the source CSVs.
- Inspect parameters via `form_*` — match `parameter-settings.md`.
- Compute `entitiesSucceeded / entitiesProcessed`.

### 6. Log + return

Append your row to `deployment-log.md`:
```
| <module> | <dmfSeq> | X/X | Y/Y | Z/Z | ✅/⚠️/❌ | <status> | <journal ids> |
```

Return the standard fan-out contract with `metrics` populated:
```json
{
  "metrics": {
    "entitiesProcessed": N,
    "entitiesSucceeded": N,
    "formStepsCompleted": N,
    "actionsInvoked": N
  }
}
```

---

## Failure handling (per the `fo-mcp-server` rule set)

```
ON FAILURE:
  1. STOP — read module .md (Critical Rules, Discoveries) BEFORE attempting any workaround.
  2. Capture exact error message verbatim.
  3. Classify:
     - Missing prerequisite → return `failed` with prerequisite info; do NOT proceed.
     - Invalid value         → fix source CSV; retry.
     - Entity not found      → fall back to form tools; if also unavailable, return `partial`.
     - Permission denied     → return `failed` with security-role info.
     - Duplicate key         → switch create→update.
  4. Log via `reinforcement-learning` skill.
  5. Update source files if the fix changed deployed state.
  6. Update module .md if a new rule/discovery emerged.
  7. Retry once.
  8. If still failing, return `failed` with full journal trail.
```

---

## Rules
- **You only touch your assigned module.** Do not deploy entities owned by other modules — even if you see they're missing.
- **Source files are authoritative.** Never patch the live environment without updating the source CSV / parameter-settings.
- **Pair with `fo-mcp-server`.** Plural entity sets, V2+ naming, no deep insert, internal names not labels, 25-row cap awareness.
- **Pair with `reinforcement-learning`.** Pre-flight journal lookup; post-failure journal write.
- **Stay in your context window.** Do not load other modules' knowledge.
