---
name: module-fanout
description: Use whenever a phase skill needs to perform repetitive per-module work across multiple D365 F&O modules (config building in Phase 1.2, deployment in Phase 2.1, validation in Phase 2.2). Defines the sub-agent dispatch pattern, the input/output contract every worker must honour, the parallelization rules (parallel within DMF `ExecutionUnit`, sequential across), the wave/batch sequencing for DMF order (010 → 650), result aggregation, and failure-handling/retry semantics. Pairs each module-level call with the appropriate worker skill (`module-config-worker`, `module-deployment-worker`, `module-validation-worker`).
---

# Module Fan-Out Pattern (Layer 2)

> Spawns one sub-agent per module. Each sub-agent runs in its **own context window** and brings its own module knowledge. The main agent only sees structured results.

> **Source of truth for waves**: `Modules/dependency-graph.json`. Never hand-roll the wave list — read it from JSON.

> **Output contract schema**: `schemas/fan-out-contract.schema.json`. Every worker MUST conform.

---

## When to use

A phase skill calls `module-fanout` whenever it has a list of modules to process the same way. Typical callers:

| Caller | Worker | Phase |
|---|---|---|
| `d365-config-builder` | `module-config-worker` | 1.2 |
| `d365-deployment` | `module-deployment-worker` | 2.1 |
| `d365-validation-testing` | `module-validation-worker` | 2.2 |

---

## Input contract

The caller derives a **dispatch table** by **reading `Modules/dependency-graph.json`** (do not duplicate wave numbers in skill prose). For partial-redeploy / fix-loop, pass an explicit `moduleFilter` to restrict to specific `dmfSeq`s.

```json
{
  "phase": "2.1",
  "worker": "module-deployment-worker",
  "waves": [
    {
      "waveId": 1,
      "executionMode": "sequential",
      "modules": [
        { "module": "Organization Administration", "dmfSeq": "010", "modulePath": "Modules/Administration/Organization Administration/Organization Administration.md", "dmfTemplate": "Modules/Administration/Organization Administration/010 - System Setup.json" }
      ]
    },
    {
      "waveId": 2,
      "executionMode": "parallel",
      "modules": [
        { "module": "General Ledger", "dmfSeq": "020", "modulePath": "...", "dmfTemplate": "..." },
        { "module": "Workflow",       "dmfSeq": "022", "modulePath": "...", "dmfTemplate": "..." }
      ]
    }
  ]
}
```

Wave construction rules:
- One wave per logical step in the dependency graph.
- `executionMode = parallel` when modules share an `ExecutionUnit` and have no cross-module dependency.
- `executionMode = sequential` when there is an order dependency.

---

## Worker prompt template

For every module in a wave, the orchestrator dispatches a sub-agent (use the `task` tool with `agent_type: general-purpose`) with this prompt skeleton:

```
You are running the `<worker-skill>` skill for the D365 F&O implementation accelerator.

MODULE: <module>
DMF SEQUENCE: <dmfSeq>
MODULE KNOWLEDGE: <modulePath>
DMF TEMPLATE: <dmfTemplate>
PHASE: <phase>

Required inputs (read these in your sub-agent context):
- <list of files>

Required skills (load these via SKILL.md frontmatter):
- <worker-skill>
- fo-mcp-server (if Phase 2.x)
- reinforcement-learning

Scope requirements (filtered to this module):
<json subset of requirement-matrix.json>

Output contract: return JSON matching the schema below.
```

---

## Output contract (every worker must return)

Workers MUST conform to `schemas/fan-out-contract.schema.json`. The orchestrator validates each return value against that schema before merging.

```json
{
  "module": "General Ledger",
  "projectId": "acme-uat",
  "runId": "RUN-2026-04-29-001",
  "phase": "2.1",
  "status": "complete",
  "artefactPaths": [
    "Modules/Dynamics 365 Finance/General Ledger/Data/10_LedgerChartOfAccounts.csv",
    "Documentation/_status/2.1/General Ledger.json"
  ],
  "perWorkerStatusFile": "Documentation/_status/2.1/General Ledger.json",
  "desiredStateHash": "sha1:7c1c…",
  "deployedStateHash": "sha1:7c1c…",
  "metrics": { "entitiesProcessed": 28, "entitiesSucceeded": 28, "formStepsCompleted": 3, "actionsInvoked": 1 },
  "issues": [ { "severity": "warning", "summary": "Posting profile X used default" } ],
  "journalEntries": [ "CJ-2026-0007" ],
  "nextSteps": [ "Re-run validation step 4 after fix" ]
}
```

The orchestrator aggregates these into the phase-level status table.

### Concurrency-safe writes (cardinal rule)

- Workers **never** append to shared files (`deployment-log.md`, `parameter-settings.md`, `e2e-test-results.md`, `challenge_journal.json`).
- Workers write **only** to per-module paths:
  - `Documentation/_status/<phase>/<module>.json` (machine-readable)
  - `Documentation/_status/<phase>/<module>.md` (optional human report)
  - `ChallengeJournal/_inbox/<runId>/<workerId>-CJ-*.json` (one file per challenge)
- The **orchestrator merges** these into the canonical aggregate after `wait-all`:
  - `Documentation/<phase>-status.md` is rewritten (not appended) from the per-module status files.
  - Inbox journal entries are merged into `challenge_journal.json` with deduplication (see `reinforcement-learning`).

This eliminates last-write-wins corruption when multiple workers run in parallel.

### Idempotency

Each worker computes a **`desiredStateHash`** from its source artefacts (DMF JSON, CSVs, parameter rows). On retry:

1. If the previous `deployedStateHash == desiredStateHash`, return `status: "skipped-idempotent"` immediately.
2. Otherwise read current state, diff vs desired, apply only the delta.

This makes wave re-dispatch safe and removes the "double-post" failure mode on retry.

---

## Parallelization & sequencing

```
FOR each wave in waves (in order):
  IF wave.executionMode == "parallel":
     dispatch all module sub-agents at once (use multiple task tool calls in one response)
     wait for ALL to return
  ELSE:
     dispatch one module sub-agent
     wait for it to return
     verify its status before dispatching the next
  aggregate results into the phase status table
  IF any module returned status == "failed":
     STOP — surface failing module + journal entries; do NOT start next wave (regardless of executionMode)
  IF any module returned status == "partial":
     Inspect issues[]; orchestrator decides whether to continue with degraded state OR remediate
  status == "skipped-idempotent" is treated as success
```

Concurrency hints:
- Phase 1.2 (config building) — no live environment, fully parallel **within the same wave** (typically one wave per `ExecutionUnit`).
- Phase 2.1 (deployment) — even within a wave, watch shared resources (e.g. number sequences). When in doubt, sequential.
- Phase 2.2 (testing) — parallel when scenarios touch disjoint module sets.

---

## Failure handling

| Worker returns | Orchestrator action |
|---|---|
| `complete` | Log success, advance |
| `partial` | Inspect `issues[]`, decide: continue with degraded state OR pause + remediate |
| `failed` | STOP the wave, surface the failing module + journal entries to the user, do not advance |

Workers ALWAYS log challenges to `ChallengeJournal/challenge_journal.json` via the `reinforcement-learning` skill before returning.

---

## Retry semantics

- A failing wave can be re-dispatched once source files are fixed.
- Re-dispatch only the failing modules — successful ones in the same wave do not need to be re-run unless their state was invalidated.
- After 2 consecutive failures of the same module, escalate to the user — do not loop forever.

---

## Aggregation (orchestrator-only step)

After every wave, the orchestrator (NOT the workers) **rewrites** `Documentation/<phase>-status.md` from the per-worker status files in `Documentation/_status/<phase>/`:

```markdown
## Wave 2 — ExecutionUnit 1
| Module | DMF Seq | Status | Entities | Issues | Journal |
|---|---|---|---|---|---|
| General Ledger | 020 | ✅ complete | 28/28 | 0 | — |
| Workflow | 022 | ⚠️ partial | 5/6 | 1 | CJ-2026-0008 |
```

The orchestrator also updates `Documentation/run-state.json` (`schemas/run-state.schema.json`) with the wave's outcome — `modulesComplete`, `modulesFailed`, `currentWave`. This file is what enables crash-resume across sessions.
