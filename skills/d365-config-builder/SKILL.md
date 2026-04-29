---
name: d365-config-builder
description: Use after the requirement profile is complete to translate requirements into deployable configuration files (DMF JSON templates, CSV data files, parameter-settings markdown), produce the cross-module rollout plan and end-to-end test plan, validate completeness, and run the Phase 1 approval gate. Covers Phase 1 Steps 1.2 → 1.5 of the D365 F&O implementation lifecycle. Source files produced here are the AUTHORITATIVE source of truth for everything that gets deployed in Phase 2.
---

# Configuration Builder & Rollout Planner (Phase 1.2 – 1.5)

> Source files are authoritative. If the environment ever drifts, fix the source first, then re-deploy.

## Inputs
- `Documentation/requirement-profile.md` + `requirement-matrix.json` (from `d365-requirements-analysis`).
- Module `.md` knowledge files (paths via `d365-knowledge-routing`).
- Existing DMF template `.json` files in `Modules/.../`.
- `Modules/dmf_odata_mapping.json`.

## Outputs
| Step | Artefact | Location |
|---|---|---|
| 1.2 | Updated DMF templates | `Modules/{path}/{NNN - Name}.json` |
| 1.2 | Per-entity data files | `Modules/{path}/Data/{seq}_{entity}.csv` |
| 1.2 | Per-module config summary | `Documentation/config-{module}.md` |
| 1.2 | Parameter settings | `Documentation/parameter-settings.md` |
| 1.3 | Rollout plan | `Documentation/rollout-plan.md` |
| 1.3 | E2E test plan | `Documentation/e2e-test-plan.md` |
| 1.3 | Test scenarios | `Documentation/test-scenarios.json` |
| 1.3 | Test data requirements | `Documentation/test-data-requirements.md` |
| 1.4 | Validation report | `Documentation/validation-report.md` |
| 1.4 | Gap resolutions | `Documentation/gap-resolutions.md` |

---

## Step 1.2 — Build configuration files (DELEGATED via `module-fanout`)

> **Performance note**: per-module work is dispatched as parallel sub-agents. The orchestrator (this skill) stays small; each module's deep knowledge stays in its sub-agent's own context window.

### Procedure
1. **Determine in-scope modules** from the requirement matrix; include upstream dependencies even with no direct requirements (e.g., GL Shared whenever any Finance module is in scope).
2. **Build the dispatch table** (a wave per `ExecutionUnit`, fully parallel within a wave). Use `d365-knowledge-routing` for module paths and DMF templates.
3. **Slice the requirement matrix** — for each module produce the filtered subset of `requirement-matrix.json` rows mapped to that module.
4. **Invoke the `module-fanout` skill** with `worker = module-config-worker`. Each sub-agent reads its assigned module's `.md`, derives field values, writes its DMF JSON + CSVs + parameter-settings rows + `config-{module}.md`, and returns the standard contract.
5. **Aggregate results**. Append each module's row to `Documentation/phase1-status.md`.
6. **Cross-module reconciliation** (do this in the main context, AFTER fan-out):
   - Posting profile references across GL ↔ AP ↔ AR ↔ Inventory.
   - Dimension consistency across reporting needs.
   - Number sequence assignments — no conflicts.
   - Tax setup covers all transaction types in scope.

If any worker returned `failed` or `partial`, surface to the user and remediate before proceeding to Step 1.3.

### DMF template JSON shape
```json
{
  "Description": "Module description",
  "TemplateId": "NNN - Template Name",
  "SourceEntityList": [
    {
      "SourceEntityName": "Human-readable",
      "TargetEntity": "D365EntityName",
      "Description": "Purpose",
      "EntitySequence": "10",
      "ExecutionUnit": "1",
      "LevelInExecutionUnit": "10"
    }
  ]
}
```

### CSV files
- One per entity per template: `{EntitySequence}_{TargetEntity}.csv`.
- Header row matches D365 entity field names exactly.
- Use enum **labels**, not integer codes.

### Parameter settings markdown
```markdown
## Module: <Name>
### Form: <Menu Path>
| Tab | Field | Value | Justification |
|---|---|---|---|
| General | Param X | Enabled | REQ-001 |
```

---

## Step 1.3 — Build rollout plan + E2E test plan

### Rollout plan (`rollout-plan.md`)
- Order modules by DMF template number (010 → 650), then by `EntitySequence`.
- For each entity, decide deployment method (decision tree):

```
Has verified OData mapping in dmf_odata_mapping.json?
├── YES → Data entity (Priority 1) — use data_* tools
└── NO  → Has menu path in module .md?
         ├── YES → Form navigation (Priority 2) — use form_* tools
         └── NO  → Manual / API action (Priority 3) — use api_* tools
```

- Include validation steps per module (read-back queries, parameter inspection).
- Include rollback notes per module where relevant.

### E2E test plan (`e2e-test-plan.md`)
- One scenario per applicable end-to-end process (Source-to-Pay, Order-to-Cash, etc. — see `d365-knowledge-routing` §5).
- Each scenario walks the process **start to finish** — never test fragments.
- Each step lists: precondition, MCP tool path, expected result, validation query.

### Structured test scenarios (`test-scenarios.json`)
Mirror the markdown for programmatic execution. Minimum fields per scenario:
`id`, `process`, `modules[]`, `steps[]` (each step: `action`, `tool`, `inputs`, `expected`).

---

## Step 1.4 — Validate & fill gaps

Cross-check matrix:

| Source | Must appear in |
|---|---|
| Every `requirement-matrix.json` row | Either a deployment step OR a gap resolution |
| Every DMF entity in scope | The rollout plan |
| Every parameter setting | The rollout plan |
| Every E2E scenario | At least one validation step in rollout plan |

Produce `validation-report.md` summarising coverage, plus `gap-resolutions.md` for everything classified `Gap` in the matrix.

---

## Step 1.5 — Approval gate (9-point checklist)

The agent must answer "yes" to all 9 before invoking `d365-deployment`:

1. Every requirement in `requirement-matrix.json` has a status of `Mapped`, `Confirmed`, `Deferred`, or `Rejected` (no `Open`).
2. Every in-scope module has a `config-{module}.md`.
3. Every DMF template referenced has been updated and saved.
4. Every entity needing form-based config is in `parameter-settings.md`.
5. `rollout-plan.md` covers every entity and parameter from steps 1–4.
6. `e2e-test-plan.md` covers every applicable end-to-end process.
7. `test-scenarios.json` mirrors the test plan.
8. `validation-report.md` shows 100% coverage with no unresolved holes.
9. `gap-resolutions.md` exists for every gap, with an approved approach.

When all 9 pass, hand off to the `d365-deployment` skill.
