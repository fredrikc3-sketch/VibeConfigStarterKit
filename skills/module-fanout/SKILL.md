---
name: module-fanout
description: Use whenever a phase skill needs to perform repetitive per-module work across multiple D365 F&O modules (config building in Phase 1.2, deployment in Phase 2.1, validation in Phase 2.2). Defines the sub-agent dispatch pattern, the input/output contract every worker must honour, the parallelization rules (parallel within DMF `ExecutionUnit`, sequential across), the wave/batch sequencing for DMF order (010 → 650), result aggregation, and failure-handling/retry semantics. Pairs each module-level call with the appropriate worker skill (`module-config-worker`, `module-deployment-worker`, `module-validation-worker`).
---

# Module Fan-Out Pattern (Layer 1)

> Spawns one sub-agent per module. Each sub-agent runs in its **own context window** and brings its own module knowledge. The main agent only sees structured results.

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

The caller produces a **dispatch table** before calling fan-out:

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

```json
{
  "module": "General Ledger",
  "phase": "2.1",
  "status": "complete | partial | failed",
  "artefactPaths": [
    "Modules/Dynamics 365 Finance/General Ledger/Data/10_LedgerChartOfAccounts.csv",
    "Documentation/config-general-ledger.md"
  ],
  "metrics": {
    "entitiesProcessed": 28,
    "entitiesSucceeded": 28,
    "formStepsCompleted": 3,
    "actionsInvoked": 1
  },
  "issues": [
    { "severity": "warning", "summary": "Posting profile X used default", "detail": "..." }
  ],
  "journalEntries": [ "CJ-2026-0007" ],
  "nextSteps": [ "Re-run validation step 4 after fix" ]
}
```

The orchestrator aggregates these into the phase-level status table. Workers MUST NOT mutate orchestrator state directly — they only write source files, journal entries, and return the contract.

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
  IF any module returned status != "complete" AND wave.executionMode == "sequential":
     STOP — surface to user, do not start next wave
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

## Aggregation

After every wave, append to `Documentation/<phase>-status.md`:

```markdown
## Wave 2 — ExecutionUnit 1
| Module | DMF Seq | Status | Entities | Issues | Journal |
|---|---|---|---|---|---|
| General Ledger | 020 | ✅ complete | 28/28 | 0 | — |
| Workflow | 022 | ⚠️ partial | 5/6 | 1 | CJ-2026-0008 |
```
