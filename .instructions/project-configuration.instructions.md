# Project Configuration — Analysis & Preparation Playbook

> **Purpose**: Defines the agent's process for analysing requirements, building configuration file sets, planning rollout, and validating completeness — all **before** any deployment touches the environment. This is the "think first, act later" phase.

> **If MCP tools are needed** during analysis (e.g. querying entity metadata, exploring form structures, or validating existing data), read `.instructions/fo-interaction.instructions.md` first for tool usage rules.

---

## 1 · Process Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 1 — ANALYSIS & PREPARATION                                      │
│                                                                         │
│  1.1  Analyse Requirements → Build Requirement Profile                  │
│    ↓                                                                    │
│  1.2  Build Configuration Files → DMF-ready JSON + supplementary data   │
│    ↓                                                                    │
│  1.3  Build Rollout Plan → Deployment sequence + E2E test plan          │
│    ↓                                                                    │
│  1.4  Validate & Fill Gaps → Cross-check everything, close holes        │
│    ↓                                                                    │
│  1.5  Approval Gate → All artefacts reviewed before deployment begins   │
└─────────────────────────────────────────────────────────────────────────┘
```

> **Cardinal Rule**: No deployment happens until Phase 1 is complete. Every sub-step produces documentation that is committed to the workspace.

---

## 2 · Step 1.1 — Analyse Requirements & Build Requirement Profile

### Objective
Take raw requirement documents from the `Requirements/` folder and decompose them into a structured **Requirement Profile** mapped to D365 F&O capabilities.

### Execution

```
1. INGEST
   - Read ALL files in the Requirements/ folder (Word, PDF, Excel, text, etc.)
   - Extract every functional requirement, constraint, and assumption
   - Identify the business processes being described

2. MAP TO D365 CAPABILITIES
   - For each requirement, identify:
     a. Which D365 module(s) can fulfil it
     b. Which specific feature, entity, or parameter is relevant
     c. Whether it's standard config, data migration, or a process gap
   - Use these knowledge sources for mapping:
     • Module .md knowledge files (via knowledge-routing.instructions.md)
     • Business Process Catalogue (ProcessCatalogue.json / ProcessCatalogue_flat.json)
     • DMF/OData mapping (dmf_odata_mapping.json)
   - Consult Microsoft Learn documentation for capability verification

3. CLASSIFY EACH REQUIREMENT
   Assign each requirement to one of these categories:

   | Category | Meaning | Action |
   |----------|---------|--------|
   | ✅ Standard Config | D365 supports this out of the box | Map to module phase + entity |
   | 📦 Data Migration | Requires data to be loaded | Map to DMF template + entity |
   | ⚙️ Parameter Setting | Module parameter toggle or value | Map to specific form + field |
   | 🔄 Workflow / Process | Needs workflow or business rule | Map to workflow type + conditions |
   | 🔌 Integration | Requires external connection | Map to OData / dual-write / API |
   | ⚠️ Gap | No standard D365 capability | Document gap + proposed approach |
   | ❓ Clarification Needed | Requirement is ambiguous | Flag for user input |

4. BUILD REQUIREMENT PROFILE
   Create/update: `Documentation/requirement-profile.md`

   Structure:
   - Executive Summary (scope, modules, timelines)
   - Requirement Matrix (ID → Description → Category → Module → Entity → Status)
   - Gap Analysis (gaps identified + proposed solutions)
   - Assumptions & Constraints
   - Open Questions for Client
```

### Documentation Output
| Artefact | Location | Format |
|----------|----------|--------|
| Requirement Profile | `Documentation/requirement-profile.md` | Markdown |
| Requirement Matrix | `Documentation/requirement-matrix.json` | Structured JSON |
| Gap Analysis | Embedded in requirement-profile.md | Markdown table |

### Continuous Documentation Rule
After every mapping decision, update the requirement profile immediately. Never batch documentation — write as you go.

---

## 3 · Step 1.2 — Build Configuration Files

### Objective
Translate the Requirement Profile into a complete set of configuration files that can be deployed to D365 F&O. These files are the **source of truth** for what gets deployed.

### Execution

```
1. DETERMINE IN-SCOPE MODULES
   - From the Requirement Profile, list all modules that have mapped requirements
   - Use knowledge-routing.instructions.md §3 to establish the dependency order
   - Include upstream dependencies even if they have no direct requirements
     (e.g., GL Shared is always needed if any Finance module is in scope)

2. FOR EACH MODULE (in dependency order):

   a. READ the module knowledge source (.md file)
      - Understand the configuration phases
      - Note the N-Phase Configuration Sequence
      - Identify Critical Configuration Rules
      - Check Implementation Discoveries for known gotchas

   b. READ the existing DMF template (.json file) if one exists
      - Understand the entity list and EntitySequence
      - Note ExecutionUnit parallelism rules

   c. BUILD / UPDATE the configuration data
      For each entity in the module:
        - Determine which fields need values based on requirements
        - Source the values from documents in Requirements/, client data, or defaults
        - Create data records in the format expected by the DMF entity
        - If an entity has no OData/DMF mapping → note for form-based config

   d. PRODUCE configuration artefacts:
      - Updated DMF template JSON (if entity list or sequence changes)
      - Data files (CSV/Excel) with the actual values to import
      - Parameter settings document (for settings configured via forms)
      - Notes on what must be done via F&O MCP form navigation

3. CROSS-MODULE CONFIGURATION
   After all modules are processed:
   - Verify posting profile references across modules (GL ↔ AP ↔ AR ↔ Inventory)
   - Verify dimension sets are consistent across reporting needs
   - Verify number sequence assignments don't conflict
   - Verify tax setup covers all transaction types in scope
```

### Configuration File Conventions

#### DMF Template JSON
Follow the existing workspace convention:
```json
{
  "Description": "Module description",
  "SourceEntityList": [
    {
      "SourceEntityName": "Human-readable entity name",
      "TargetEntity": "D365EntityName",
      "Description": "Purpose of this entity",
      "EntitySequence": "10",
      "ExecutionUnit": "1",
      "LevelInExecutionUnit": "10"
    }
  ],
  "TemplateId": "NNN - Template Name"
}
```

#### Data Files
- One CSV/Excel file per entity per DMF template
- File name: `{EntitySequence}_{TargetEntity}.csv`
- Header row matches D365 entity field names exactly
- Values use D365 enum labels (not integer codes)

#### Parameter Settings Document
For settings that don't have DMF entities:
```markdown
## Module: [Name]
### Form: [Menu Path]
| Tab | Field | Value | Justification |
|-----|-------|-------|--------------|
| General | Parameter X | Enabled | Requirement REQ-001 |
```

### Documentation Output
| Artefact | Location | Format |
|----------|----------|--------|
| Module config summaries | `Documentation/config-{module-name}.md` | Markdown |
| Updated DMF templates | `Modules/{path}/{NNN - Name}.json` | JSON |
| Data files | `Modules/{path}/Data/` | CSV |
| Parameter settings | `Documentation/parameter-settings.md` | Markdown |

---

## 4 · Step 1.3 — Build Rollout Plan & E2E Test Plan

### Objective
Create a deployment sequence plan and an end-to-end (E2E) test plan that validates every configured capability by following business processes from **start to finish**.

### Execution — Rollout Plan

```
1. ESTABLISH DEPLOYMENT SEQUENCE
   - Order modules by DMF template number (010 → 650)
   - Within each module, order by EntitySequence
   - For each entity, determine the deployment method:

     ┌─────────────────────────────────────────────────────────┐
     │  DEPLOYMENT METHOD DECISION TREE                        │
     │                                                         │
     │  Does the entity exist in dmf_odata_mapping.json        │
     │  with match_method = "verified"?                        │
     │    YES → Deploy via DATA ENTITY (OData)                 │
     │    NO  → Does the entity have an OData endpoint         │
     │          in odata.xml?                                   │
     │            YES → Attempt data entity, verify, fallback  │
     │            NO  → Deploy via FORM NAVIGATION (MCP)       │
     └─────────────────────────────────────────────────────────┘

2. BUILD DEPLOYMENT STEPS
   For each module in sequence:
   
   Step N.1: Pre-deployment check
     - Verify upstream modules are deployed and validated
     - Read the module knowledge article (.md) for critical rules and known discoveries
     - Check Challenge Journal for known issues
   
   Step N.2: Deploy data entities (OData / Data Tools)
     - List entities in EntitySequence order
     - Specify: entity name, OData path, record count, key fields
     - Include rollback approach if entity creation fails
   
   Step N.3: Deploy form-based configuration (F&O MCP Form Tools)
     - List forms that need MCP navigation
     - Specify: menu item name, control names, tab names, field values
     - Include the exact navigation sequence
   
   Step N.4: Execute actions (F&O MCP API/Action Tools)
     - List post-deployment actions (activate, publish, generate, etc.)
     - Specify: action name, menu path, parameters
     - These are actions not available via data entities
   
   Step N.5: Module validation
     - List validation checks for this module
     - Specify: what to check, expected result, how to check it

3. IDENTIFY CRITICAL PATH
   - Which modules block others?
   - What's the minimum viable deployment to start testing?
   - Where are the highest-risk steps?
   - What is the estimated execution time per module?
```

### Execution — E2E Test Plan

```
1. MAP REQUIREMENTS TO BUSINESS PROCESSES
   - For each requirement in the profile, trace it to the
     Business Process Catalogue (ProcessCatalogue.json)
   - Identify the end-to-end process it belongs to
   - ** CRITICAL: Follow the process from START to FINISH **
     Never test fragments — always walk the full business process path

2. BUILD TEST SCENARIOS
   For each in-scope business process:

   Test Scenario = {
     id: "E2E-001",
     processName: "Order to Cash",
     processPath: "Business Process Catalog > Order to Cash > ...",
     prerequisiteData: { customers: [...], items: [...], warehouses: [...] },
     steps: [
       {
         step: 1,
         action: "Create sales order",
         module: "Sales & Marketing",
         method: "data-entity | form-navigation",
         entityOrForm: "SalesOrderHeadersV2 | SalesTable",
         input: { ... },
         expectedResult: "Sales order created with status Open",
         validation: "Verify order appears in Sales order list"
       },
       ...through to final step...
     ],
     finalValidations: [
       "GL entries balance (debits = credits)",
       "Inventory reduced by correct quantity",
       "Customer balance updated in AR",
       "Revenue posted to correct account"
     ],
     requirementsCovered: ["REQ-001", "REQ-005", "REQ-012"]
   }

3. SEQUENCE TEST SCENARIOS
   - Some processes produce data consumed by others
   - Source-to-Pay creates vendors/POs → used by Record-to-Report
   - Order-to-Cash creates transactions → used by Record-to-Report
   - Run foundational processes first, reporting processes last

4. ESTABLISH TEST DATA REQUIREMENTS
   - What master data must exist before testing?
   - What can be deployed in Phase 2 vs. created during test execution?
   - Document test data for each scenario explicitly
```

### Documentation Output
| Artefact | Location | Format |
|----------|----------|--------|
| Rollout Deployment Plan | `Documentation/rollout-plan.md` | Markdown |
| E2E Test Plan | `Documentation/e2e-test-plan.md` | Markdown |
| Test Scenarios (structured) | `Documentation/test-scenarios.json` | JSON |
| Test Data Requirements | `Documentation/test-data-requirements.md` | Markdown |

---

## 5 · Step 1.4 — Validate & Fill Gaps

### Objective
Cross-check all produced artefacts against the original requirements. Find and fill every hole before deployment begins.

### Execution

```
1. COMPLETENESS CHECK — Requirements Coverage
   For each requirement in the Requirement Profile:
   - ✅ Has a mapped module and entity? 
   - ✅ Has configuration file data prepared?
   - ✅ Has a deployment step in the rollout plan?
   - ✅ Is covered by at least one E2E test scenario?
   - ❌ If any check fails → flag as gap → resolve immediately

2. CONSISTENCY CHECK — Cross-File Validation
   - DMF template entity lists match the entities referenced in config docs
   - Data file columns match entity field schema in module knowledge
   - Parameter settings reference valid form paths (verify against module .md)
   - Test scenarios reference forms and fields that exist in the configuration
   - All module dependencies are satisfied in the deployment sequence

3. COMPLETENESS CHECK — Module Configuration
   For each in-scope module:
   - Every phase from the module .md knowledge has been addressed
   - Critical Configuration Rules have been respected
   - Known Implementation Discoveries have been accounted for
   - Posting profiles, number sequences, and dimensions are complete

4. GAP RESOLUTION
   For each identified gap:
   a. Determine if it's a missing config, missing data, or a true D365 gap
   b. If missing config/data → create the missing artefact
   c. If true D365 gap → document the workaround or customisation needed
   d. Update the Requirement Profile with the resolution
   e. Update the rollout plan if new deployment steps are needed
   f. Update the test plan if new test scenarios are needed

5. CHALLENGE JOURNAL CHECK
   - Review ChallengeJournal/challenge_journal.json for every in-scope module
   - Verify the rollout plan accounts for all known challenges
   - Add preventive steps to the deployment plan where applicable
```

### Validation Checklist

```
□ Every requirement has a category assignment
□ Every "Standard Config" requirement has a config file entry
□ Every "Data Migration" requirement has a DMF entity + data file
□ Every "Parameter Setting" has a form path + field + value
□ Every "Gap" has a documented approach
□ Every module in scope has deployment steps
□ Every deployment step has a validation check
□ Every business process has an E2E test scenario (start to finish)
□ Every E2E test scenario traces requirements back to the profile
□ DMF template dependency order is correct
□ Data entity vs. form deployment method is specified for every entity
□ No circular dependencies in deployment sequence
□ Test data requirements are specified and sourced
□ Challenge Journal has been consulted for all modules
```

### Documentation Output
| Artefact | Location | Format |
|----------|----------|--------|
| Validation Report | `Documentation/validation-report.md` | Markdown |
| Updated Requirement Profile | `Documentation/requirement-profile.md` | Markdown (updated) |
| Gap Resolution Log | `Documentation/gap-resolutions.md` | Markdown |

---

## 6 · Step 1.5 — Approval Gate

### Objective
Final review checkpoint before any deployment begins. All artefacts must be complete, consistent, and ready.

### Gate Criteria

| # | Check | Status |
|---|-------|--------|
| 1 | Requirement Profile is complete — no ❓ items remaining | ⬜ |
| 2 | All gaps have documented resolutions or accepted workarounds | ⬜ |
| 3 | Configuration files exist for every in-scope module | ⬜ |
| 4 | DMF templates are sequenced correctly with no dependency issues | ⬜ |
| 5 | Data files have been created and field-mapped | ⬜ |
| 6 | Rollout plan covers every module with deployment + validation steps | ⬜ |
| 7 | E2E test plan covers every in-scope business process start-to-finish | ⬜ |
| 8 | Validation report shows no open issues | ⬜ |
| 9 | Challenge Journal has been reviewed and preventive measures incorporated | ⬜ |

### When the Gate Passes
→ Proceed to **Phase 2: Deployment** (see `project-rollout.instructions.md`)

### When the Gate Fails
→ Loop back to the failing step (1.1–1.4) → resolve → re-validate → re-check gate

---

## 7 · Continuous Documentation Protocol

> **This applies to EVERY sub-step in Phase 1.**

### Rules
1. **Write as you go** — never defer documentation to "later"
2. **Update, don't duplicate** — if a file exists, update it; don't create a parallel version
3. **Trace decisions** — every mapping choice should say WHY (link to requirement ID)
4. **Version awareness** — note when files change and what changed
5. **Use the workspace** — all documentation lives in `Documentation/` or module folders; never just in conversation

### Documentation Folder Structure
```
Documentation/
├── requirement-profile.md          ← Step 1.1 output
├── requirement-matrix.json         ← Step 1.1 structured data
├── config-{module-name}.md         ← Step 1.2 per-module summaries
├── parameter-settings.md           ← Step 1.2 form-based settings
├── rollout-plan.md                 ← Step 1.3 deployment sequence
├── e2e-test-plan.md                ← Step 1.3 test plan
├── test-scenarios.json             ← Step 1.3 structured test cases
├── test-data-requirements.md       ← Step 1.3 test data needs
├── validation-report.md            ← Step 1.4 cross-check results
├── gap-resolutions.md              ← Step 1.4 gap closure log
└── html/                           ← Phase 3 final HTML documentation
    ├── rollout-report.html
    └── environment-config.html
```

---

## 8 · Error Handling During Preparation

Even during analysis (before deployment), issues can arise:

| Issue | Example | Action |
|-------|---------|--------|
| Ambiguous requirement | "System should handle returns" — which returns? | Flag as ❓, ask user for clarification |
| Conflicting requirements | Req A says tax-exempt, Req B says tax-inclusive | Document conflict, propose resolution, seek user decision |
| Missing module knowledge | Module .md file lacks phase details | Consult Microsoft Learn, update the module .md, log to journal |
| Entity not in mapping | Need to configure something not in dmf_odata_mapping.json | Mark for form-based deployment, check odata.xml for raw metadata |
| Unknown D365 capability | Unsure if D365 supports a requirement | Search Microsoft Learn, check Process Catalogue, mark as ⚠️ Gap if unconfirmed |
| Unexpected system behavior | Configuration saved but doesn't take effect, or error during setup | **STOP** — immediately read the module knowledge article (.md). Check Critical Configuration Rules and Implementation Discoveries before trying alternatives. |

All issues encountered during preparation are logged to the Challenge Journal, even if they're resolved immediately. This builds the knowledge base for future projects.

---

## 9 · Status Tracking

Maintain a running status table throughout Phase 1:

| Step | Description | Status | Artefacts | Notes |
|------|-------------|--------|-----------|-------|
| 1.1 | Analyse Requirements | ⏳ Pending | — | — |
| 1.2 | Build Config Files | ⏳ Pending | — | — |
| 1.3 | Build Rollout + Test Plan | ⏳ Pending | — | — |
| 1.4 | Validate & Fill Gaps | ⏳ Pending | — | — |
| 1.5 | Approval Gate | ⏳ Pending | — | — |

Update after completing each step. This table serves as a checkpoint for resuming if interrupted.

---

*Last Updated: February 20, 2026*
*Version: 2.0*
