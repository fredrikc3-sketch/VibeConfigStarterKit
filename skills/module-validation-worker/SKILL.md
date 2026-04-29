---
name: module-validation-worker
description: ⚠️ SUB-AGENT ONLY — never invoke from main context. Invoked by `module-fanout` from `d365-validation-testing`. Executes the E2E test scenarios touching ONE module's process slice during Phase 2.2. Drives every assigned scenario through the D365 F&O MCP server start-to-finish, captures pass/fail per step, runs the localized fix-loop (fix source → request re-deploy via orchestrator → re-test), logs failures, and returns the standard fan-out output contract (see `schemas/fan-out-contract.schema.json`). Pairs MANDATORILY with `fo-mcp-server` and `reinforcement-learning`.
---

# Module Validation Worker (Layer 3)

> One sub-agent. A slice of E2E scenarios. Walk each from start to finish. Never test fragments.

> **Mandatory pairings**: `fo-mcp-server` (tool rules), `reinforcement-learning` (failure logging).

---

## You receive (from `module-fanout`)
- `module`, `modulePath`
- Filtered slice of `Documentation/test-scenarios.json` — only scenarios where this module is on the critical path
- `Documentation/test-data-requirements.md` rows scoped to this module

## You must produce
- **Per-worker results file**: `Documentation/_status/2.2/<module>.json` (orchestrator merges into `e2e-test-results.md`).
- Source-file fixes if any test exposed a config error.
- Re-deployment requests routed back to the orchestrator via `redeployRequests[]` in the output contract (do NOT re-deploy yourself).
- Journal **inbox** entries for every failure.
- Standard fan-out output contract per `schemas/fan-out-contract.schema.json`.

---

## Procedure

### 1. Prepare
- Verify your test data prerequisites exist (master records: vendors, customers, items, etc.). If missing, return `failed` with the missing data list.
- Read `<modulePath>` Implementation Discoveries section — known test gotchas.

### 2. Execute each scenario start-to-finish
For each scenario in your slice:
1. Trace the full process (e.g., for Order-to-Cash: customer → quotation → SO → packing slip → invoice → payment).
2. Drive each step using MCP tools per `fo-mcp-server` (data > form > action priority).
3. Capture **expected vs actual after every step** — not just at the end.
4. If a step passes → continue.
5. If a step fails → §Fix loop.

### 3. Fix loop (for THIS scenario)

```
TEST STEP FAILS
   ↓
Diagnose: read module .md + Challenge Journal first
   ↓
Categorize:
  a) SOURCE-FILE ERROR (wrong config value, missing entity row)
       → Fix the source file
       → Add `redeployRequest` to your output contract for the orchestrator
       → Pause this scenario (mark step as ⏸ pending re-deploy)
       → Continue with NEXT scenario in your slice while waiting
  b) DATA ERROR (test data wrong, but config is right)
       → Fix test data
       → Retry the step
  c) GENUINE ENV BUG (code issue, role issue, environment problem)
       → Log to journal as `category: Other`
       → Mark scenario as ❌ failed
       → Move on
```

### 4. Re-run after orchestrator confirms re-deploy
When the orchestrator confirms a re-deploy completed, restart the affected scenario from the failing step (or from the start if state was corrupted).

### 5. Log + return

`e2e-test-results.md` row template:
```markdown
## Scenario: <id> — <name>
| Step | Action | Tool | Expected | Actual | Status | Notes |
|---|---|---|---|---|---|---|
| 1 | Create PR | data_create_entities | PR-0001 | PR-0001 | ✅ | — |
| 2 | Approve | api_invoke_action | Approved | Failed | ❌ | CJ-2026-0007 |
```

Output contract additions specific to this worker:
```json
{
  "metrics": {
    "scenariosAssigned": N,
    "scenariosPassed": N,
    "scenariosFailed": N,
    "scenariosPendingRedeploy": N,
    "stepsExecuted": N
  },
  "redeployRequests": [
    { "module": "<other-module-or-self>", "reason": "...", "sourceFilesUpdated": [...] }
  ]
}
```

---

## Rules
- **Never test fragments.** Every scenario starts from its documented entry point and runs to its terminal step.
- **Never write to shared files.** `e2e-test-results.md` and `challenge_journal.json` are orchestrator-merged from per-worker outputs.
- **Never patch the live environment without updating the source.** Source files are authoritative.
- **Never re-deploy yourself.** Surface `redeployRequests` to the orchestrator. Re-deployment crosses module boundaries.
- **Coverage discipline**: every scenario in your slice must end in ✅, ❌, or ⏸ (pending re-deploy). No scenario left unexecuted.
- **Pair with `fo-mcp-server` and `reinforcement-learning`.**
- **Stay in your context window.**
