# Reinforcement Learning Loop — Instruction Set

> **Purpose**: Defines how the agent learns from every challenge, workaround, and discovery encountered during D365 F&O configuration and rollout. Ensures that knowledge is **never lost** — every insight is captured, routed to the correct knowledge store, and available for future operations.

---

## 1 · Core Principle

> **Every challenge is a learning opportunity. Every resolution is a future shortcut.**

The agent operates on a feedback-driven model. Unlike a stateless assistant, this agent **actively updates its own knowledge base** so that:
- The same mistake is never made twice
- Known workarounds are applied proactively
- Configuration rules evolve based on real-world experience
- The team benefits from accumulated implementation intelligence

---

## 2 · The Feedback Loop

```
┌──────────────────────────────────────────────────────────────────┐
│                    REINFORCEMENT LEARNING CYCLE                  │
│                                                                  │
│   ┌─────────┐    ┌──────────────┐    ┌──────────────────┐       │
│   │ DETECT  │───→│ JOURNAL      │───→│ ANALYZE PATTERN  │       │
│   │ Problem │    │ Log entry    │    │ One-off or trend?│       │
│   └─────────┘    └──────────────┘    └────────┬─────────┘       │
│                                               │                  │
│                                      ┌────────▼─────────┐       │
│                                      │ ROUTE KNOWLEDGE  │       │
│                                      │ Where should this │       │
│                                      │ insight live?     │       │
│                                      └────────┬─────────┘       │
│                                               │                  │
│   ┌─────────┐    ┌──────────────┐    ┌────────▼─────────┐       │
│   │ VERIFY  │←───│ UPDATE       │←───│ CLASSIFY         │       │
│   │ Change  │    │ Knowledge    │    │ Rule / Discovery  │       │
│   │ works   │    │ Store        │    │ / Gap / Sequence │       │
│   └─────────┘    └──────────────┘    └──────────────────┘       │
│        │                                                         │
│        └──→ Future operations benefit from this knowledge ──→ ↑  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 3 · When to Trigger the Loop

The reinforcement loop activates whenever ANY of these occur:

| Trigger | Example |
|---------|---------|
| **Error encountered** | DMF import fails with "Foreign key violation" |
| **Unexpected behavior** | Configuration saved but doesn't take effect |
| **Workaround needed** | Standard approach fails, alternative path works |
| **Dependency discovered** | Module B must be configured before Module A (not in docs) |
| **Sequence issue** | DMF entity must load before another (EntitySequence wrong) |
| **Performance issue** | Batch job takes hours instead of minutes |
| **Data quality issue** | Source data needs transformation before import |
| **Process gap** | Business process has no standard D365 solution |
| **Documentation gap** | Microsoft Learn is missing or incorrect for a scenario |
| **User confusion** | Multiple users struggle with the same configuration step |

---

## 4 · Step-by-Step Execution

### Step 1: DETECT — Identify the Problem

When something goes wrong or an unexpected situation arises:

**FIRST**: Immediately open the relevant module’s `.md` knowledge file and read:
- **Critical Configuration Rules** — is there already a rule covering this scenario?
- **Implementation Discoveries** — has this problem been solved before?
- **Configuration Phases** — was a prerequisite step missed?

If the module knowledge article already describes the issue and its resolution, apply it directly. Only if the issue is NOT covered in the module knowledge, proceed with full DETECT logging:

```
CAPTURE:
  - Exact error message (copy verbatim)
  - Module and sub-module affected
  - Menu path or entity involved
  - Configuration phase and step number
  - What was attempted
  - What actually happened
  - What was expected to happen
```

### Step 2: JOURNAL — Log to Challenge Journal

**Immediately** create an entry in `ChallengeJournal/challenge_journal.json`.

See `ChallengeJournal/JOURNAL_SCHEMA.md` for the full schema. Quick reference:

```json
{
  "id": "CJ-YYYY-NNNN",
  "timestamp": "ISO-8601",
  "module": "Module name",
  "subModule": "Sub-module name",
  "phase": "Configuration phase",
  "severity": "critical | high | medium | low",
  "category": "config-dependency | data-quality | entity-sequence | workaround | process-gap | performance | documentation-gap",
  "symptom": "What happened (exact error text)",
  "rootCause": "Why it happened",
  "resolution": "How it was fixed",
  "prevention": "How to avoid it next time",
  "status": "open | investigating | resolved | archived",
  "affectedEntities": ["EntityName1", "EntityName2"],
  "relatedJournalEntries": ["CJ-YYYY-NNNN"],
  "knowledgeUpdates": [
    {
      "target": "path/to/file.md",
      "section": "Section name",
      "action": "added | updated",
      "summary": "What was changed"
    }
  ]
}
```

### Step 3: ANALYZE — Pattern Recognition

After logging, assess whether this is:

| Classification | Signal | Action |
|---------------|--------|--------|
| **One-off** | First occurrence, unlikely to repeat | Journal entry sufficient |
| **Recurring pattern** | 2+ occurrences of similar issue | Escalate to module knowledge update |
| **Systemic issue** | Affects multiple modules or processes | Update master instructions + all affected modules |
| **Platform limitation** | D365 cannot do this natively | Document as a known gap with workaround |

### Step 4: ROUTE — Determine Knowledge Destination

Based on the classification, route the insight to the appropriate knowledge store:

| Insight Type | Destination File | Target Section |
|-------------|-----------------|----------------|
| Configuration dependency rule | Module `.md` file | `## Critical Configuration Rules` |
| Workaround / gotcha | Module `.md` file | `## Implementation Discoveries` |
| Entity load order fix | DMF template `.json` | Adjust `EntitySequence` value |
| OData entity issue | `dmf_odata_mapping.json` | Update `match_method` or add note |
| Business process gap | Module `.md` file | `## Business Process Catalogue Reference` |
| Cross-module dependency | `.instructions/knowledge-routing.instructions.md` | §3 Dependency Rules |
| Config sequence change | `.instructions/project-configuration.instructions.md` | Relevant Step (1.1–1.4) |
| Rollout procedure issue | `.instructions/project-rollout.instructions.md` | Relevant Step (2.1–2.2) |

### Step 5: UPDATE — Write to Knowledge Store

Apply the update to the destination file. Follow these formats:

#### For Critical Configuration Rules (in module `.md`):
```markdown
### Rule: [Short descriptive title]
- **Discovered**: [Date]
- **Context**: [What scenario triggered this]
- **Rule**: [Clear, actionable statement of what must be done]
- **Consequence if Ignored**: [What goes wrong if this rule is violated]
- **Journal Reference**: CJ-YYYY-NNNN
```

#### For Implementation Discoveries (in module `.md`):
```markdown
### Discovery: [Short descriptive title]
- **Discovered**: [Date]
- **Problem**: [What went wrong]
- **Root Cause**: [Why it happened]
- **Solution**: [Step-by-step fix]
- **Prevention**: [How to avoid it in the future]
- **Error Message**: `[Exact error text if applicable]`
- **Journal Reference**: CJ-YYYY-NNNN
```

#### For Entity Sequence Fixes (in DMF template `.json`):
- Change the `EntitySequence` value of the affected entity
- Add a comment to the entity `Description` field: `"Resequenced from X to Y per CJ-YYYY-NNNN"`

### Step 6: VERIFY — Validate the Knowledge Update

After updating, verify:
1. The knowledge file is still valid (no formatting errors, no broken JSON)
2. The new rule/discovery is findable by keyword search
3. If it's a sequence change, re-validate the dependency chain
4. Mark the Challenge Journal entry status as `resolved`

---

## 5 · Pre-Operation Journal Check

**Before ANY risky operation**, the agent MUST:

### A. Consult Module Knowledge Article
```
BEFORE each module operation:
  1. Open the module's .md knowledge file
  2. Read the Critical Configuration Rules section
  3. Read the Implementation Discoveries section
  4. Note any rules or discoveries relevant to the current operation
  5. Apply preventive measures proactively
```

### B. Check the Challenge Journal
```
BEFORE each module operation:
  1. Read ChallengeJournal/challenge_journal.json
  2. Filter entries by:
     - module == current module
     - status != "archived"
  3. If matching entries found:
     - Read the resolution and prevention fields
     - Apply preventive measures BEFORE proceeding
     - Note in your response: "Applying lesson from CJ-YYYY-NNNN"
  4. If no matching entries:
     - Proceed with standard approach
     - Stay alert for new challenges to journal
```

### What Counts as "Risky"
- Any DMF import execution
- Changing posting profiles or account structures
- Modifying number sequences on a live system
- Enabling or disabling features/configuration keys
- Running inventory close or fiscal period close
- Modifying security roles with SoD implications
- Changing workflow configurations

---

## 6 · Knowledge Quality Standards

### What Makes a Good Knowledge Entry

| Quality | Bad Example | Good Example |
|---------|------------|-------------|
| **Specific** | "GL doesn't work" | "GL journal posting fails when Financial Dimension 'Department' has no default value on Main Account 60100" |
| **Actionable** | "Fix the posting" | "Navigate to GL > Chart of accounts > Main accounts > 60100 > Financial dimensions tab > Set Department default to '000'" |
| **Reproducible** | "Sometimes fails" | "Fails on journal type 'Daily' when lines exceed 500. Works when split into batches of 200." |
| **Preventable** | "Watch out for this" | "Before importing 025 - General ledger.json, verify all main accounts in 020 - GL Shared.json have been assigned to an account structure" |

### Mandatory Fields
Every knowledge entry MUST include:
- The **exact error message** or **observable symptom**
- The **module and menu path** where it occurred
- The **resolution** (not just "it was fixed")
- A **Challenge Journal reference** (CJ-YYYY-NNNN)

---

## 7 · Metrics and Self-Assessment

Periodically (after each module configuration or rollout phase), the agent should assess:

| Metric | How to Measure | Target |
|--------|---------------|--------|
| **Journal entries created** | Count of new entries | Every challenge logged |
| **Knowledge updates made** | Count of module `.md` updates | Every resolution fed back |
| **Repeat issues** | Challenges matching existing journal entries | Should decrease over time |
| **Pre-emptive catches** | Times journal check prevented a known issue | Should increase over time |
| **Resolution time** | Time from detection to resolution | Should decrease over time |

### Self-Check Questions
After completing a module configuration:
1. Did I check the Challenge Journal before starting? ✅/❌
2. Did I log every issue I encountered? ✅/❌
3. Did I update the module knowledge with discoveries? ✅/❌
4. Did I update DMF templates if needed? ✅/❌
5. Would a future agent be able to avoid my mistakes using the knowledge I left? ✅/❌

---

## 8 · Knowledge Propagation Rules

Some discoveries affect more than one location. Follow these propagation rules:

| Discovery Scope | Update Locations |
|----------------|-----------------|
| Affects one entity in one module | Module `.md` only |
| Affects multiple entities in one module | Module `.md` + DMF template `.json` |
| Affects cross-module dependencies | Module `.md` + `knowledge-routing.instructions.md` |
| Affects configuration sequence | Module `.md` + `project-configuration.instructions.md` |
| Affects rollout process | Module `.md` + `project-rollout.instructions.md` |
| Affects OData integration | Module `.md` + `dmf_odata_mapping.json` |
| Affects platform behavior | Master `copilot-instructions.md` + all relevant modules |

---

## 9 · Journal Maintenance

### Monthly Cleanup
1. Review all `resolved` entries older than 30 days
2. Verify the knowledge has been propagated to module files
3. Change status to `archived`
4. Keep `archived` entries in the journal (never delete — they're the learning history)

### Quarterly Review
1. Analyze journal patterns: which modules generate the most issues?
2. Identify systemic gaps in module knowledge files
3. Propose proactive knowledge improvements
4. Update this instruction file if the RL process itself needs improvement

---

*Last Updated: February 20, 2026*
*Version: 1.0*
