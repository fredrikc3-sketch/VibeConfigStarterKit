# Challenge Journal — Schema & Usage Guide

This document defines the schema for `challenge_journal.json` and provides usage instructions for the AI agent.

---

## Purpose

The Challenge Journal is the **central log** where every problem encountered, every workaround discovered, and every configuration gotcha is recorded. It serves as:

1. **Operational memory** — the agent checks it before risky operations
2. **Learning corpus** — patterns emerge from accumulated entries
3. **Audit trail** — every issue and resolution is traceable
4. **Knowledge pipeline** — entries are routed to module knowledge files

---

## File Location

```
ChallengeJournal/challenge_journal.json
```

---

## Schema

### Root Structure

```json
{
  "_metadata": {
    "schema_version": "1.0",
    "description": "D365 F&O Implementation Challenge Journal",
    "last_updated": "ISO-8601 timestamp",
    "total_entries": 0,
    "stats": {
      "open": 0,
      "investigating": 0,
      "resolved": 0,
      "archived": 0
    }
  },
  "entries": []
}
```

### Entry Schema

Each entry in the `entries` array follows this structure:

```json
{
  "id": "CJ-2026-0001",
  "timestamp": "2026-02-20T14:30:00Z",
  "lastUpdated": "2026-02-20T16:45:00Z",

  "classification": {
    "module": "Dynamics 365 Finance",
    "subModule": "General Ledger",
    "phase": "Phase 5 - Ledger Setup",
    "dmfTemplate": "025 - General ledger.json",
    "severity": "high",
    "category": "config-dependency"
  },

  "problem": {
    "symptom": "Journal posting fails with error: 'Account structure XXXX does not allow the value YYYY for dimension Department'",
    "errorMessage": "Account structure Corporate does not allow the value 200 for dimension Department",
    "menuPath": "General ledger > Journal entries > General journals",
    "entityAffected": "LedgerJournalEntity",
    "whatWasAttempted": "Posted a daily journal with Department dimension value 200",
    "whatHappened": "Posting failed with validation error",
    "whatWasExpected": "Journal should post successfully"
  },

  "analysis": {
    "rootCause": "Account structure 'Corporate' was configured with a limited set of Department dimension values. Value 200 was added to the Department dimension but not added to the account structure's allowed values.",
    "isRecurring": false,
    "relatedEntries": [],
    "platformLimitation": false
  },

  "resolution": {
    "status": "resolved",
    "steps": [
      "Navigate to General ledger > Chart of accounts > Structures > Configure account structures",
      "Select the 'Corporate' account structure",
      "Click Edit",
      "On the Department segment, add value 200 to the allowed values",
      "Click Activate to publish the updated structure",
      "Re-attempt the journal posting"
    ],
    "prevention": "Before importing dimension values via DMF (020 - GL Shared.json), ensure the account structure is either set to 'Allow all values' for the dimension or the specific values are included in the structure's filter.",
    "timeToResolve": "45 minutes"
  },

  "knowledgeUpdates": [
    {
      "target": "Modules/Dynamics 365 Finance/General Ledger/General Ledger.md",
      "section": "Critical Configuration Rules",
      "action": "added",
      "summary": "Added rule: Account structure dimension filters must include all dimension values that will be used in transactions"
    }
  ],

  "tags": ["account-structure", "dimension", "posting-failure", "GL"]
}
```

---

## Field Reference

### IDs

| Field | Format | Example |
|-------|--------|---------|
| `id` | `CJ-YYYY-NNNN` (year + sequential 4-digit number) | `CJ-2026-0001` |

### Severity Levels

| Level | Criteria |
|-------|----------|
| `critical` | Blocks go-live or causes data corruption |
| `high` | Blocks a business process or module configuration |
| `medium` | Causes errors but has a workaround |
| `low` | Cosmetic, documentation, or minor inconvenience |

### Categories

| Category | Description |
|----------|-------------|
| `config-dependency` | Configuration step depends on another that wasn't completed |
| `data-quality` | Source data doesn't meet target entity requirements |
| `entity-sequence` | DMF entities loaded in wrong order |
| `workaround` | Standard approach doesn't work; alternative found |
| `process-gap` | Business process has no standard D365 solution |
| `performance` | Operation is unacceptably slow |
| `documentation-gap` | Microsoft Learn docs are missing or incorrect |
| `security` | Security role / permission issue |
| `integration` | OData, dual-write, or business event issue |

### Status Values

| Status | Meaning |
|--------|---------|
| `open` | Problem identified, not yet resolved |
| `investigating` | Actively working on root cause and resolution |
| `resolved` | Fix applied and verified; knowledge updated |
| `archived` | Resolved entry aged 30+ days; kept for history |

---

## Usage Instructions for the Agent

### Creating a New Entry

1. Determine the next sequential ID: read `_metadata.total_entries`, increment by 1
2. Build the entry JSON following the schema above
3. Append to the `entries` array
4. Update `_metadata.total_entries` and `_metadata.stats`
5. Update `_metadata.last_updated` with current timestamp

### Searching the Journal

Before any risky operation:
```
1. Read challenge_journal.json
2. Filter: entries where classification.module matches current module
3. Filter: entries where status is NOT "archived"
4. If matches found: read resolution.prevention and apply proactively
5. Cite the journal entry ID in your response
```

### Updating an Entry

When new information is discovered about an existing entry:
1. Update the `lastUpdated` timestamp
2. Add to `analysis.relatedEntries` if connected to another entry
3. Update `resolution.steps` if a better fix is found
4. Add to `knowledgeUpdates` if additional files were updated
5. Change `status` as appropriate

### Resolving an Entry

When a fix is confirmed:
1. Set `resolution.status` to `"resolved"`
2. Ensure `resolution.steps` is complete and actionable
3. Ensure `resolution.prevention` explains how to avoid the issue
4. Verify all `knowledgeUpdates` have been applied to the target files
5. Update `_metadata.stats`

---

## Examples of Good Entries

### Example 1: Config Dependency
```json
{
  "id": "CJ-2026-0002",
  "classification": {
    "module": "Dynamics 365 Supply Chain Management",
    "subModule": "Inventory Management",
    "phase": "Phase 3 - Posting Profiles",
    "category": "config-dependency",
    "severity": "high"
  },
  "problem": {
    "symptom": "Cannot save inventory posting profile — main account field shows 'No valid accounts found'",
    "menuPath": "Inventory management > Setup > Posting > Posting"
  },
  "analysis": {
    "rootCause": "The main accounts referenced in the posting profile had not been released to the current legal entity. Chart of accounts was shared but account assignments were missing."
  },
  "resolution": {
    "status": "resolved",
    "prevention": "Always verify main accounts are assigned to the legal entity's ledger before configuring any module posting profiles. Run GL > Inquiries > Trial balance to confirm accounts are visible."
  }
}
```

### Example 2: Entity Sequence
```json
{
  "id": "CJ-2026-0003",
  "classification": {
    "module": "Administration",
    "subModule": "Organization Administration",
    "dmfTemplate": "010 - System Setup.json",
    "category": "entity-sequence",
    "severity": "medium"
  },
  "problem": {
    "symptom": "DMF import of 'Address format lines' fails with foreign key error referencing 'Address format'",
    "entityAffected": "LogisticsAddressFormatLineEntity"
  },
  "resolution": {
    "status": "resolved",
    "steps": ["Changed EntitySequence of 'Address format' from 20 to 10 so it loads before 'Address format lines'"],
    "prevention": "Parent entities must always have a lower EntitySequence than child entities in DMF templates"
  }
}
```

---

*Last Updated: February 20, 2026*
*Version: 1.0*
