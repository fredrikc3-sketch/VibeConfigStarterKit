---
name: d365-validation-testing
description: Use after deployment to validate the F&O environment by executing every end-to-end business-process test scenario from `Documentation/test-scenarios.json` start-to-finish (Source-to-Pay, Order-to-Cash, Record-to-Report, etc.). Drives the fix-loop — when a test fails, fix the SOURCE configuration file, re-deploy via the `d365-deployment` skill, then re-test. This is Phase 2 Step 2.2 of the implementation lifecycle. Pair with `fo-mcp-server` and `reinforcement-learning`.
---

# E2E Validation & Testing (Phase 2.2)

> **Iron rule**: tests follow business processes **start to finish**. Never test fragments.

## Inputs
- `Documentation/test-scenarios.json` (from Phase 1.3).
- `Documentation/e2e-test-plan.md`.
- `Documentation/test-data-requirements.md`.
- Live deployed F&O environment.

## Outputs
- `Documentation/e2e-test-results.md` — pass/fail per step.
- Updated source files if any fix required them.
- New `ChallengeJournal/challenge_journal.json` entries for every failure.

---

## Execution model — DELEGATED via `module-fanout`

> Scenario execution is dispatched as sub-agents running the `module-validation-worker` skill. Each worker owns the slice of scenarios where its module is on the critical path. The orchestrator (this skill) handles re-deploy requests and global coverage tracking.

### Procedure

### 1. Prepare test data
- Load test data per `test-data-requirements.md`.
- Verify prerequisite master data (vendors, customers, items, etc.) exist.

### 2. Slice scenarios by primary module
For each scenario in `test-scenarios.json`, determine its **primary module** (the module whose configuration the scenario most heavily exercises — typically the module owning the terminal step). Group scenarios by primary module → that's your dispatch table.

Cross-module scenarios (e.g. Source-to-Pay touches Procurement + AP) are assigned to the module that owns the most steps; the worker accesses other modules' state read-only via MCP.

### 3. Invoke `module-fanout`
- `worker = module-validation-worker`.
- One wave; `executionMode = parallel` for modules with disjoint scenario sets, `sequential` for modules whose scenarios share state.

### 4. Handle re-deploy requests
Each worker may return `redeployRequests[]` when a test exposed a source-file error. The orchestrator:
1. Aggregates re-deploy requests across all workers from the wave.
2. Invokes the `d365-deployment` skill (which itself uses `module-fanout` with `module-deployment-worker`) for the affected modules only.
3. Once re-deployment completes, dispatches a follow-up validation wave for **only the workers that had pending scenarios**, instructing them to resume from the affected step.

### 5. Repeat until all scenarios pass or escalation threshold (3 fix-cycles per scenario) is reached.

### Fix loop (orchestrator-coordinated)

```
WORKER REPORTS FAILED STEP
   ↓
Worker categorises (source / data / env-bug) per `module-validation-worker`
   ↓
SOURCE-FILE ERROR
   → Worker fixes the source file
   → Worker returns redeployRequest
   → Orchestrator invokes d365-deployment for that module
   → Orchestrator dispatches follow-up validation wave
DATA ERROR
   → Worker fixes test data, retries inline (no orchestrator round-trip)
ENV BUG
   → Worker logs to journal, marks ❌, moves on
```

**Never** patch the live environment without updating the source file. Source files are authoritative.

### Result tracking
`Documentation/e2e-test-results.md` template:

```markdown
## Scenario: <id> — <name>
| Step | Action | Tool | Expected | Actual | Status | Notes |
|---|---|---|---|---|---|---|
| 1 | Create PR | data_create_entities | PR-0001 | PR-0001 | ✅ | — |
| 2 | Approve | api_invoke_action | Approved | Failed | ❌ | CJ-2026-0007 |
```

### 5. Coverage check
Before declaring Phase 2 complete:
- Every applicable end-to-end process from `d365-knowledge-routing` §5 has at least one passing scenario.
- Every requirement in `requirement-matrix.json` traces to at least one passing test step.
- Every challenge logged during deployment has been verified resolved.

## Hand-off
When all scenarios pass and coverage holds, hand off to the `d365-documentation` skill (Phase 3).
