# Challenge Journal — Schema Pointer

> **Canonical schema**: [`../schemas/challenge-journal.schema.json`](../schemas/challenge-journal.schema.json) (version `2.0`).

This document used to embed the schema inline. As of v2.2 the schema lives in a single canonical JSON Schema file under `schemas/` and is enforced by `tools/validate_repo.py` (and the CI quality gate). This file is kept only as a pointer plus minimal usage examples.

## File layout

```
ChallengeJournal/
├── challenge_journal.json     ← Aggregate journal (orchestrator-merged)
└── _inbox/
    └── <runId>/
        └── <module>-CJ-*.json ← Per-worker drops; the orchestrator merges with dedup
```

Workers MUST write to `_inbox/<runId>/`. They MUST NOT edit `challenge_journal.json` directly — that file is rewritten by the orchestrator after every wave (concurrent-write safety).

## Minimum required fields per entry (v2.0)

`id`, `date`, `module`, `phase`, `category`, `severity`, `symptom`, `rootCause`, `resolution`, `sourceFilesUpdated`, `knowledgeUpdates`, `status`, `dedupHash`.

Optional but encouraged: `projectId`, `recurrenceCount`, `recurrenceDates[]`, `lastSeen`, `supersedes[]`, `supersededBy`, `preventionEffective`.

## Example entry

```json
{
  "id": "CJ-2026-0007",
  "date": "2026-04-29",
  "module": "General Ledger",
  "phase": "2.1",
  "category": "deployment",
  "severity": "error",
  "projectId": "acme-uat",
  "symptom": {
    "operation": "data_create_entities on LedgerJournalHeadersV2",
    "error": "Posting profile not found",
    "context": "Wave 4, parallel with AP/AR"
  },
  "rootCause": "Module-level posting profile depends on AR Customer Groups (Wave 4) — race condition when both run in same wave.",
  "resolution": {
    "summary": "Move LedgerJournalHeadersV2 to Wave 5; serialize after AR.",
    "steps": ["Edit Modules/dependency-graph.json: add dependsOn:[120] to module 130"],
    "status": "resolved"
  },
  "sourceFilesUpdated": ["Modules/dependency-graph.json"],
  "knowledgeUpdates": ["Modules/Dynamics 365 Finance/General Ledger/GeneralLedger.md#critical-rules"],
  "status": "resolved",
  "dedupHash": "sha1:7c1c8a4e9f2b...",
  "recurrenceCount": 1,
  "preventionEffective": { "preventedCount": 0, "lastPreventedAt": null }
}
```

## Mechanics
See [`../skills/reinforcement-learning/SKILL.md`](../skills/reinforcement-learning/SKILL.md) for:
- Dedup hash computation
- Supersede chains
- KPI tracking
- Project-id namespacing
- Pre-flight lookup protocol
