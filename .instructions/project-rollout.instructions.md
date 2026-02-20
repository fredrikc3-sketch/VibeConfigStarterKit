# Project Rollout — Deployment, Validation & Documentation Playbook

> **Purpose**: Defines the agent's process for deploying configuration to D365 F&O using the MCP server, validating the environment with end-to-end testing, and producing comprehensive HTML documentation of the entire project.

> **Prerequisite**: Phase 1 (Analysis & Preparation) must be complete with all artefacts passing the Approval Gate. See `project-configuration.instructions.md`.

> **Required companion**: Before using ANY MCP tool (`mcp_finance_opera_data_*`, `mcp_finance_opera_form_*`, `mcp_finance_opera_api_*`), you MUST have read `.instructions/fo-interaction.instructions.md`. That file contains the authoritative rules for tool selection, naming conventions, data operation protocols, form navigation rules, and reasoning protocol.

---

## 1 · Process Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 2 — DEPLOYMENT                                                   │
│                                                                         │
│  2.1  Deploy configuration via F&O MCP Server                           │
│       Data entities first → Form navigation as fallback → Actions       │
│    ↓                                                                    │
│  2.2  Validate deployed environment + E2E testing                       │
│       Fix issues → Update source files → Re-deploy → Re-test            │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│  PHASE 3 — DOCUMENTATION                                                │
│                                                                         │
│  3.1  Document the entire rollout process (HTML)                        │
│    ↓                                                                    │
│  3.2  Document the configured environment visually (HTML)               │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2 · Step 2.1 — Deploy Configuration via F&O MCP Server

### Objective
Push all prepared configuration from Phase 1 into the D365 F&O environment using the MCP server tools. Prioritise data entities; use form navigation for anything not covered by entities.

### Deployment Method Hierarchy

> **Priority order — always try the highest-priority method first:**

```
Priority 1: DATA ENTITIES (OData via MCP Data Tools)
  → Fastest, most reliable, bulk-capable
  → Use: mcp_finance_opera_data_* tools
  → Source: dmf_odata_mapping.json (match_method = "verified")

Priority 2: FORM NAVIGATION (MCP Form Tools)
  → For parameters, settings, and entities without OData support
  → Use: mcp_finance_opera_form_* tools
  → Source: Module .md knowledge (menu paths, control names)

Priority 3: API / ACTIONS (MCP API Tools)
  → For operations like Activate, Publish, Generate, Post
  → Use: mcp_finance_opera_api_* tools
  → Source: Module .md knowledge (action descriptions)
```

### Deployment Execution Protocol

Follow the rollout plan from `Documentation/rollout-plan.md` **in exact sequence**.

```
FOR EACH MODULE in deployment order (010 → 650):

  ┌─────────────────────────────────────────────────────────────┐
  │  STEP 2.1.1 — PRE-DEPLOYMENT CHECK                         │
  │                                                              │
  │  1. Verify upstream modules are deployed and validated       │
  │  2. Read module knowledge source (.md) for critical rules    │
  │  3. Check ChallengeJournal for known issues with this module │
  │  4. Load the deployment steps from rollout-plan.md           │
  └─────────────────────────────────────────────────────────────┘
         ↓
  ┌─────────────────────────────────────────────────────────────┐
  │  STEP 2.1.2 — DEPLOY DATA ENTITIES                         │
  │                                                              │
  │  For each entity marked for data-entity deployment:          │
  │                                                              │
  │  a. FIND the entity type:                                    │
  │     → data_find_entity_type to confirm entity exists         │
  │     → data_get_entity_metadata to get field schema           │
  │                                                              │
  │  b. CHECK for existing data:                                 │
  │     → data_find_entities with $filter to see what exists     │
  │     → If record exists: data_update_entities (PATCH)         │
  │     → If record is new: data_create_entities (POST)          │
  │                                                              │
  │  c. CREATE / UPDATE entities:                                │
  │     → Use PLURAL entity name in OData path                   │
  │     → For V2+ entities: plural before V (e.g., HeadersV2)   │
  │     → NO deep insert — create parent then child separately   │
  │     → For enums: Style has Namespace.Pattern'Value'          │
  │                                                              │
  │  d. VERIFY the deployment:                                   │
  │     → data_find_entities to confirm records created          │
  │     → Spot-check key field values                            │
  │                                                              │
  │  e. DOCUMENT results:                                        │
  │     → Record: entity name, records created/updated, status   │
  │     → If failure: log to Challenge Journal immediately       │
  └─────────────────────────────────────────────────────────────┘
         ↓
  ┌─────────────────────────────────────────────────────────────┐
  │  STEP 2.1.3 — DEPLOY FORM-BASED CONFIGURATION              │
  │                                                              │
  │  For each item marked for form-based deployment:             │
  │                                                              │
  │  a. OPEN the form:                                           │
  │     → form_find_menu_item to locate the menu item            │
  │     → form_open_menu_item to open the form                   │
  │                                                              │
  │  b. NAVIGATE to the correct context:                         │
  │     → form_open_or_close_tab to switch to the right tab      │
  │     → form_filter_grid / form_filter_form to find records    │
  │     → form_select_grid_row to select specific records        │
  │                                                              │
  │  c. CREATE or MODIFY:                                        │
  │     → form_click_control to click New / Edit buttons         │
  │     → form_set_control_values to set field values            │
  │     → form_save_form to save changes                         │
  │                                                              │
  │  d. EXECUTE ACTIONS:                                         │
  │     → form_click_control for button-based actions            │
  │     → form_open_lookup for lookup-driven fields              │
  │                                                              │
  │  e. CLOSE when done:                                         │
  │     → form_close_form when module configuration is complete  │
  │                                                              │
  │  f. DOCUMENT:                                                │
  │     → Record: form name, action taken, values set, status    │
  │     → If failure: log to Challenge Journal immediately       │
  └─────────────────────────────────────────────────────────────┘
         ↓
  ┌─────────────────────────────────────────────────────────────┐
  │  STEP 2.1.4 — EXECUTE POST-DEPLOYMENT ACTIONS              │
  │                                                              │
  │  For actions like Activate, Publish, Generate:               │
  │                                                              │
  │  a. Check if action is available via API:                    │
  │     → api_find_actions to discover available actions         │
  │     → api_invoke_action to execute                           │
  │                                                              │
  │  b. If not available via API, use form navigation:           │
  │     → Open the form → click the action button               │
  │     → Wait for completion → verify result                   │
  │                                                              │
  │  c. DOCUMENT: action name, result, any errors               │
  └─────────────────────────────────────────────────────────────┘
         ↓
  ┌─────────────────────────────────────────────────────────────┐
  │  STEP 2.1.5 — MODULE VALIDATION                            │
  │                                                              │
  │  Run the validation checks from rollout-plan.md:             │
  │  - Verify records exist via data entity queries              │
  │  - Verify parameters are set via form inspection             │
  │  - Compare deployed state against configuration files        │
  │  - Mark module as: ✅ Deployed | ⚠️ Partial | ❌ Failed     │
  └─────────────────────────────────────────────────────────────┘
```

### Deployment Status Tracking

Maintain a running deployment log:

| Module | DMF Seq | Data Entities | Form Config | Actions | Validation | Status | Notes |
|--------|---------|--------------|-------------|---------|-----------|--------|-------|
| Org Admin | 010 | 35/35 | 3/3 | 1/1 | ✅ Pass | ✅ Complete | — |
| GL Shared | 020 | 28/30 | 2/2 | 0/0 | ⚠️ 2 issues | 🔄 In Progress | See CJ-2026-0001 |
| ... | ... | ... | ... | ... | ... | ... | ... |

### Error Handling During Deployment

```
WHEN AN ENTITY DEPLOYMENT FAILS:
  1. STOP — Read the module knowledge article (.md file) immediately
     - Check Critical Configuration Rules for relevant constraints
     - Check Implementation Discoveries for known solutions
     - If the issue is already documented, apply the known fix
  2. Capture the exact error from the MCP tool response
  3. Classify the error:
     - Missing prerequisite → Deploy the prerequisite first
     - Invalid value → Check data file, correct the value, retry
     - Entity not found → Fall back to form-based deployment
     - Permission denied → Check security role, escalate
     - Duplicate key → Check if record already exists, use update instead
  4. Log to ChallengeJournal/challenge_journal.json
  5. Update the source configuration file if data was incorrect
  6. Update the module knowledge article if a new rule or discovery was found
  7. Retry the deployment
  8. If retry fails → document as a blocker → move to next entity → return later

WHEN A FORM DEPLOYMENT FAILS:
  1. STOP — Read the module knowledge article (.md file) immediately
     - The module .md may document the correct navigation path
     - Check Implementation Discoveries for known form issues
  2. Capture the error or unexpected form state
  3. Try alternative navigation paths (module .md may list alternatives)
  3. Check if a different menu item opens the same form
  4. Log to Challenge Journal
  5. Update module knowledge source if navigation has changed
```

### Critical MCP Tool Usage Rules

> **Full reference**: `.instructions/fo-interaction.instructions.md` — the authoritative source for ALL F&O MCP interaction rules. The summary below is for quick reference during deployment.

| Rule | Detail |
|------|--------|
| **Tool selection hierarchy** | Data tools (Priority 1) → Form tools (Priority 2) → API tools (Priority 3) |
| **Get metadata first** | Always call `data_find_entity_type` + `data_get_entity_metadata` before creating |
| **Entity names must be plural** | `SalesOrderHeaders` not `SalesOrderHeader` |
| **V2+ entities: plural before V** | `SalesOrderHeadersV2` not `SalesOrderHeaderV2s` |
| **No deep insert** | Create parent entity first, then child entities separately |
| **Enum filtering syntax** | `$filter=Status has Microsoft.Dynamics.DataEntities.StatusEnum'Active'` |
| **Use control/tab/column names** | Never use display labels — use the internal name identifiers |
| **Never ask for menu item types** | The `form_find_menu_item` tool groups menu items by type automatically |
| **Max 25 rows per form query** | F&O MCP returns max 25 rows — filter to get the right records |
| **Reason step by step** | Plan before each tool call, reflect after, check objective |
| **Never stop early** | Continue until all tasks complete or unrecoverable error |
| **Never substitute on failure** | If creation fails, do NOT retrieve existing data instead |

---

## 3 · Step 2.2 — Validate Deployed Environment & E2E Testing

### Objective
Verify the deployed environment matches the configuration files and run the full E2E test plan from `Documentation/e2e-test-plan.md`, following every process from start to finish.

### Pre-Test Validation

```
1. CONFIGURATION SPOT-CHECK
   For each deployed module:
   - Query 3-5 key entities via data_find_entities
   - Compare returned values against configuration data files
   - Open 2-3 key forms via form navigation, verify parameter settings
   - Document: Match ✅ | Mismatch ❌ (with details)

2. POSTING PROFILE VERIFICATION
   - For each module with posting profiles (GL, AP, AR, Inventory, FA):
     → Query the posting profile entity or open the form
     → Verify main account assignments are correct
     → Verify default profiles are set

3. NUMBER SEQUENCE VERIFICATION
   - Query number sequence entities
   - Verify formats, ranges, and assignments match config files
   - Verify no conflicts between legal entities

4. CROSS-MODULE LINK VERIFICATION
   - Do GL dimension values match what's referenced in AP/AR/Inventory?
   - Do vendor/customer groups reference valid posting profiles?
   - Do items reference valid item groups, dimension groups, model groups?
```

### E2E Test Execution

```
FOR EACH TEST SCENARIO in e2e-test-plan.md (in sequence order):

  1. SETUP
     - Verify prerequisite test data exists
     - If missing → create it via data entities or forms
     - Record the starting state (e.g. opening balances)

  2. EXECUTE — Walk the full process path, start to finish
     For each step in the test scenario:
     
     a. Perform the action:
        → If step.method = "data-entity":
           Use data_create_entities / data_update_entities
        → If step.method = "form-navigation":
           Use form tools to navigate, enter data, execute actions
     
     b. Verify the step result:
        → Check the expectedResult from the test scenario
        → Query the entity or inspect the form state
        → If result matches → PASS → continue to next step
        → If result doesn't match → FAIL → classify and handle:
     
     c. On step failure:
        → Is it a config issue? → Fix config → update source files → re-deploy
        → Is it a data issue? → Fix data → update data files → retry step
        → Is it a sequence issue? → Adjust test sequence → document why
        → Log failure to Challenge Journal regardless

  3. FINAL VALIDATIONS
     Run the scenario's finalValidations list:
     - GL entries balance (query trial balance or GL transactions)
     - Inventory quantities are correct (query on-hand)
     - Sub-ledger balances match GL (AP/AR ageing vs GL)
     - Workflow approvals completed (if applicable)

  4. DOCUMENT RESULTS
     For each scenario, record:
     {
       scenarioId: "E2E-001",
       result: "PASS | FAIL | PARTIAL",
       stepsCompleted: 8,
       stepsTotal: 10,
       failures: [ { step: 6, error: "...", resolution: "..." } ],
       requirementsValidated: ["REQ-001", "REQ-005"],
       challengeJournalEntries: ["CJ-2026-0005"]
     }
```

### Fix-Loop Protocol

When E2E testing reveals issues, the agent enters a fix loop:

```
┌─────────────┐     ┌──────────────┐     ┌────────────────┐     ┌──────────┐
│ Issue found  │────→│ Fix source   │────→│ Re-deploy      │────→│ Re-test  │
│ in E2E test  │     │ config files │     │ affected entity │     │ scenario │
└─────────────┘     └──────────────┘     └────────────────┘     └──────────┘
       ↑                                                              │
       └──────────── If still failing ────────────────────────────────┘
```

**Critical rule**: When fixing an issue, **always update the source files** (config .md, data files, DMF templates, parameter settings). The source files must always reflect the deployed state. Never fix only in the environment — fix the source first, then re-deploy.

### Validation Status Tracking

| Scenario ID | Process | Steps | Result | Requirements Validated | Issues |
|------------|---------|-------|--------|----------------------|--------|
| E2E-001 | Order to Cash | 10/10 | ✅ PASS | REQ-001, REQ-005 | — |
| E2E-002 | Source to Pay | 7/8 | ⚠️ PARTIAL | REQ-010 | CJ-2026-0005 |
| E2E-003 | Record to Report | 0/6 | ⏳ PENDING | — | Awaiting E2E-001, E2E-002 |

### Phase 2 Exit Criteria

| # | Criterion | Status |
|---|-----------|--------|
| 1 | All modules deployed (✅ status in deployment log) | ⬜ |
| 2 | All E2E test scenarios pass or have accepted known issues | ⬜ |
| 3 | All source files updated to reflect the actual deployed state | ⬜ |
| 4 | All issues logged in Challenge Journal with resolutions | ⬜ |
| 5 | Module knowledge sources updated with new discoveries | ⬜ |

---

## 4 · Step 3.1 — Document the Rollout Process (HTML)

### Objective
Produce a comprehensive, visual HTML document that narrates the entire rollout — from requirements analysis through deployment and testing.

### Content Structure

Build: `Documentation/html/rollout-report.html`

```html
<!-- Single-file HTML with embedded CSS/JS -->
<!-- Use a clean, professional design (light theme, Inter font) -->

Sections:
1. PROJECT OVERVIEW
   - Project scope and objectives
   - Modules in scope
   - Timeline summary
   - Key stakeholders

2. REQUIREMENTS ANALYSIS
   - Requirement summary (from requirement-profile.md)
   - Capability mapping visualization
   - Gap analysis results
   - Decisions and trade-offs made

3. CONFIGURATION DESIGN
   - Per-module configuration summary
   - Entity counts and data volumes
   - Cross-module dependencies (visual diagram)
   - Parameter settings overview

4. DEPLOYMENT EXECUTION
   - Deployment sequence (timeline/Gantt view)
   - Per-module deployment log with:
     → Entities deployed (count, method: data entity vs. form)
     → Time taken
     → Issues encountered and resolutions
   - Deployment method breakdown (pie chart: data entity vs. form vs. API)

5. TESTING & VALIDATION
   - E2E test scenario results (pass/fail matrix)
   - Per-scenario detail with step results
   - Issue resolution log
   - Requirements traceability matrix
     (Requirement → Config → Deployment → Test → Result)

6. CHALLENGES & LEARNINGS
   - Summary of Challenge Journal entries from this project
   - Categorised by type (config-dependency, data-quality, etc.)
   - Lessons learned for future projects
   - Knowledge base updates made

7. APPENDICES
   - Full requirement matrix
   - Complete deployment log
   - Entity reference (all entities deployed with field details)
```

### Design Requirements
- Single-file HTML (embedded CSS, minimal JS for interactivity)
- Professional styling — clean typography, subtle colour coding
- Collapsible sections for detail drill-down
- Tables with sorting capability (basic JS)
- Status indicators: ✅ ⚠️ ❌ with colour coding
- Print-friendly layout

---

## 5 · Step 3.2 — Document the Configured Environment (HTML)

### Objective
Produce a visual reference document showing the configured environment — what is set up, how it connects, and where to find things. This serves as ongoing operational reference documentation.

### Content Structure

Build: `Documentation/html/environment-config.html`

```html
<!-- Single-file HTML with embedded CSS/JS -->
<!-- Use visual diagrams, interactive elements -->

Sections:
1. ENVIRONMENT OVERVIEW
   - Legal entities with key attributes
   - Organizational hierarchy (visual tree)
   - Module activation status

2. FINANCE CONFIGURATION
   - Chart of accounts structure (tree visualization)
   - Financial dimension sets
   - Posting profile matrix (module × transaction type → account)
   - Fiscal calendar and period status
   - Currency setup and exchange rate types

3. SUPPLY CHAIN CONFIGURATION
   - Site/Warehouse structure (visual map)
   - Product hierarchy (categories → groups → items)
   - Inventory dimension groups
   - Procurement categories and vendor groups
   - Sales order types and pricing structure

4. MODULE REFERENCE CARDS
   For each configured module, a card showing:
   - Module name and purpose
   - Key parameters and their values
   - Entity count and data volumes
   - Related modules and dependencies
   - Key forms and menu paths
   - Known limitations or special notes

5. INTEGRATION MAP
   - OData entity list with endpoints
   - Data flow diagram (what goes where)
   - Dual-write mappings (if applicable)
   - Business events configured

6. SECURITY MODEL
   - Role assignments summary
   - Duty/privilege matrix
   - Segregation of duties rules

7. REFERENCE LINKS
   - Microsoft Learn links per module
   - Internal knowledge source links (.md files)
   - Challenge Journal link for known issues
```

### Design Requirements
- Single-file HTML (embedded CSS, all data inline)
- Visual emphasis — use diagrams, tree structures, matrices, cards
- Colour-coded by module area (Finance = blue, SCM = green, HR = purple, etc.)
- Interactive elements: expand/collapse, hover details, search/filter
- Serves as a "living document" — note the generation date and data snapshot
- **Reference the module .md knowledge files** for the source data used to build each section

---

## 6 · Continuous Documentation Protocol (Phases 2 & 3)

### During Deployment (Phase 2)

| When | Document What | Where |
|------|--------------|-------|
| Before deploying each module | Pre-deployment status | `Documentation/rollout-plan.md` (update status) |
| After each entity deployment | Entity, count, method, result | Deployment log in rollout-plan.md |
| On any failure | Full error context + resolution | `ChallengeJournal/challenge_journal.json` |
| After fixing a source file | What changed and why | Commit note in the file + Challenge Journal |
| After each E2E test scenario | Step-by-step results | `Documentation/e2e-test-results.md` |
| After fixing issues found in testing | Source file updates | Config files + Challenge Journal |

### During Documentation (Phase 3)

| When | Document What | Where |
|------|--------------|-------|
| Generating HTML reports | Pull from all Phase 1 & 2 artefacts | `Documentation/html/` |
| Discovering missing source data | Fill in the module .md knowledge | Module knowledge sources |
| Finding documentation gaps | Add content to the HTML report | Report file + source docs |

### Source File Update Rule

> **When deployment reveals that a source file is wrong, fix the source file FIRST, then re-deploy from the corrected source.** The source files must always be the authoritative record of the intended configuration. The environment is a reflection of the source files, not the other way around.

---

## 7 · Complete Process Summary

```
PHASE 1 — ANALYSIS & PREPARATION (project-configuration.instructions.md)
  1.1 Analyse requirements → Build requirement profile
  1.2 Build configuration files → DMF JSON + data files + parameter settings
  1.3 Build rollout plan + E2E test plan
  1.4 Validate everything → Fill gaps
  1.5 Approval gate

PHASE 2 — DEPLOYMENT (this file)
  2.1 Deploy to D365 F&O via MCP Server
      → Data entities (Priority 1)
      → Form navigation (Priority 2)
      → API actions (Priority 3)
      → Validate each module
  2.2 Environment validation + E2E testing
      → Run every test scenario start-to-finish
      → Fix issues → Update source files → Re-deploy → Re-test
      → Continue until all scenarios pass

PHASE 3 — DOCUMENTATION (this file)
  3.1 Generate rollout-report.html
      → Complete narrative of the project from requirements to testing
  3.2 Generate environment-config.html
      → Visual reference of the configured environment
```

---

*Last Updated: February 20, 2026*
*Version: 2.0*
