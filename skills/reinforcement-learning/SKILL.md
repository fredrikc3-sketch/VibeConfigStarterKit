---
name: reinforcement-learning
description: Use whenever a challenge, error, workaround, or non-obvious discovery is encountered during ANY phase of D365 F&O work. Captures the issue in `ChallengeJournal/challenge_journal.json`, classifies it (Rule / Discovery / Gap / Sequence), routes the insight to the correct destination (module `.md` file, DMF template, or process catalogue), and verifies the update so the next similar challenge is resolved faster. Also: ALWAYS query the journal BEFORE risky operations to apply known preventive measures.
---

# Reinforcement Learning Loop

> **Every challenge is a learning opportunity. Every resolution is a future shortcut.**

## When to invoke this skill
- Before any risky operation → query the journal for prior failures.
- After any error / unexpected result → log the challenge.
- After confirming a workaround works → route the insight to the right knowledge store.

## The cycle

```
DETECT → JOURNAL → ANALYZE → ROUTE → UPDATE → VERIFY
   ↑                                              ↓
   └────────── future operations benefit ←────────┘
```

| Step | Action | Output |
|---|---|---|
| **DETECT** | Notice an error or unexpected behavior | — |
| **JOURNAL** | Append entry to `ChallengeJournal/challenge_journal.json` | New JSON entry |
| **ANALYZE** | One-off vs trend? Which module(s)? | Diagnosis |
| **ROUTE** | Classify → choose destination | Plan |
| **UPDATE** | Edit module `.md` / DMF JSON / process catalogue | Updated knowledge |
| **VERIFY** | Re-run the failing operation; confirm success | Closed entry |

## Routing matrix

| Trigger | Destination | Section |
|---|---|---|
| New error encountered | `ChallengeJournal/challenge_journal.json` | New entry |
| Config dependency discovered | Module `.md` | "Critical Configuration Rules" |
| Workaround found | Module `.md` | "Implementation Discoveries" |
| Entity sequence issue | DMF template `.json` | `EntitySequence` reorder + comment |
| Process gap identified | Module `.md` | "Business Process Catalogue Reference" |
| Naming/auth quirk | `skills/fo-mcp-server/SKILL.md` (consider) | Update if generally applicable |

## Journal entry shape
The canonical schema is [`schemas/challenge-journal.schema.json`](../../schemas/challenge-journal.schema.json) (schema version `2.0`, flat shape). Minimum fields:
`id`, `date`, `module`, `phase`, `category`, `severity`, `symptom`, `rootCause`, `resolution`, `sourceFilesUpdated[]`, `knowledgeUpdates[]`, `status`, `dedupHash`.

Optional but encouraged: `projectId`, `recurrenceCount`, `supersedes[]`, `supersededBy`, `preventionEffective`.

## Deduplication (mandatory before insert)
1. Compute `dedupHash = SHA-1(module + "|" + category + "|" + symptom.operation + "|" + rootCause)`.
2. Search `challenge_journal.json` for an entry with the same `dedupHash`.
3. If found → **do not insert a new entry**. Increment `recurrenceCount` on the existing entry, append today's date to `recurrenceDates[]`, and update `lastSeen`.
4. If not found → insert a new entry with `recurrenceCount = 1`.

## Supersede chains (when knowledge changes)
When a new fix contradicts a previously documented one (e.g., MS Learn updated, F&O version bump):
1. Mark the old entry: `resolution.status = "superseded"`, `supersededBy = <new id>`.
2. The new entry lists `supersedes: [<old id>, ...]`.
3. Both entries remain queryable; pre-flight lookup ignores `superseded` entries.

## KPI tracking
Each successful pre-flight match (a journal entry actively prevented a recurrence) bumps:
- `entry.preventionEffective.preventedCount += 1` and `lastPreventedAt = today`.
- `_metadata.kpi.preventedRecurrences += 1` (file-level counter).
On resolution of new entries, update `_metadata.kpi.averageTimeToResolveMinutes` (running avg).

## Project-ID namespacing (multi-tenant)
When the agent is operating under a `projectId` (set in `run-state.json`):
- New journal entries get `projectId = <id>`.
- Pre-flight lookup filters first by exact `projectId`, then falls back to `projectId = null` (global learnings) if no project-scoped match is found.
- See `skills/d365-knowledge-routing/SKILL.md` §5 for the full namespacing convention covering Documentation, ChallengeJournal, and per-project `.discoveries/` overlays.

## Pre-operation query (mandatory)
Before any module deployment, validation step, or risky tool call:
1. Open `ChallengeJournal/challenge_journal.json`.
2. Filter for entries where `module` matches and `status = "resolved"`.
3. Apply documented preventive measures from the resolution.

## Cardinal rules
- **Never** silently work around an issue. Log it.
- **Never** stop at "it works now" — route the insight so the next implementation benefits.
- **Always** update source files if the fix changed deployed state — source is authoritative.
- **Always** verify the journal entry by re-attempting the failed operation after the fix.
