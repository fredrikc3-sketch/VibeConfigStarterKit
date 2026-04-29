---
name: phase-orchestrator
description: Top-level dispatcher for the D365 F&O implementation lifecycle. Use FIRST on any new user request — it classifies the request (Phase 1 analysis, Phase 1 config, Phase 2 deployment, Phase 2 testing, Phase 3 docs, troubleshooting), checks prerequisite gates (e.g. Phase 1 approval before Phase 2), picks the right phase skill, and manages hand-offs between phases. Drives the `module-fanout` skill when a phase needs per-module parallelism. Keeps the main agent's context lean by delegating heavy work to sub-agents instead of loading everything inline.
---

# Phase Orchestrator (Layer 0/1)

> The brain that decides **which phase skill to run, in what order, with what gates**. It does not execute the work itself — it dispatches.

---

## Decision flow

```
                       USER REQUEST
                            │
                            ▼
                ┌───────────────────────┐
                │  CLASSIFY             │
                │  (intent + artefacts) │
                └───────────┬───────────┘
                            │
        ┌─────────┬─────────┼─────────┬─────────┬─────────┐
        ▼         ▼         ▼         ▼         ▼         ▼
     Analysis  Config    Deploy    Testing    Docs   Trouble-
     (1.1)    (1.2-1.5)  (2.1)     (2.2)      (3)    shoot
        │         │         │         │         │         │
        ▼         ▼         ▼         ▼         ▼         ▼
   d365-req-  d365-      d365-      d365-     d365-    reinforce-
   analysis   config-    deploy-    valida-   docu-    ment-
              builder    ment       tion-     menta-   learning
                                    testing   tion
        │         │         │         │
        │         ▼         ▼         ▼
        │     module-fanout (Layer 1) → spawns Layer 3 workers
```

---

## Classification table

| Signal in request | Phase | Skill to invoke |
|---|---|---|
| "analyse / analyze requirements", new docs in `Requirements/` | 1.1 | `d365-requirements-analysis` |
| "build config", "DMF", "rollout plan", "test plan", "approval gate" | 1.2–1.5 | `d365-config-builder` |
| "deploy", "push to F&O", "go-live" | 2.1 | `d365-deployment` |
| "test", "validate", "E2E", "scenario", "fix-loop" | 2.2 | `d365-validation-testing` |
| "rollout report", "environment HTML", "final docs" | 3 | `d365-documentation` |
| Error, failure, "doesn't work", unexpected behaviour | — | `reinforcement-learning` (always pair) |

When ambiguous, ask the user **one** clarifying question.

---

## Prerequisite gates

Before invoking each phase skill, verify the prior phase gate has passed:

| To start | Required artefacts | Required state |
|---|---|---|
| `d365-config-builder` | `Documentation/requirement-profile.md`, `requirement-matrix.json` | All matrix rows have a non-`Open` status |
| `d365-deployment` | `rollout-plan.md`, `e2e-test-plan.md`, `validation-report.md`, `gap-resolutions.md` | All 9 approval-gate items pass (see `d365-config-builder` §1.5) |
| `d365-validation-testing` | `deployment-log.md` | All in-scope modules ✅ Deployed or ⚠️ Partial-with-documented-gap |
| `d365-documentation` | `e2e-test-results.md` | Coverage check passes (every applicable E2E process has ≥1 passing scenario) |

If a gate fails, **do NOT advance**. Report the failing items and either fix them in-phase or return to the prior phase.

---

## Hand-off protocol

When a phase completes:
1. The phase skill writes a one-line completion record to `Documentation/phase-handoff.md`:
   ```
   - 2026-04-29 09:30 | Phase 1.5 complete | Gate: 9/9 passed | Next: Phase 2.1
   ```
2. Phase orchestrator re-evaluates: classify the next user instruction OR auto-advance if the user said "do everything".
3. **Never auto-advance past a failed gate.** Always surface to the user.

---

## When to use sub-agents

The orchestrator itself stays in the main context. It triggers sub-agents only when invoking the `module-fanout` skill. Rule of thumb:

| Work shape | Approach |
|---|---|
| Single module, simple ask | Stay in main context, call leaf skills directly |
| Multiple modules, repetitive per-module work (config building, deployment, module-scoped testing) | **Spawn sub-agents via `module-fanout`** |
| Cross-module reasoning (gap analysis, dependency check, validation report) | Stay in main context |
| Long-running operation that may produce a lot of intermediate output | Sub-agent (use `task` tool) |

---

## Cardinal rules
- **One phase at a time.** Never interleave Phase 1 and Phase 2 work.
- **Always check the gate before advancing.**
- **Always pair `reinforcement-learning`** when error signals appear.
- **Never load module knowledge in the main context** if you can fan it out to a sub-agent — keeps the orchestration light.
