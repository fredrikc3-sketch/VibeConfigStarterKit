<p align="center">
  <img src="Media/FinanceOperations_scalable.svg" alt="Dynamics 365 Finance & Operations" width="72">
</p>

<h1 align="center">Dynamics 365<br><sub>Finance & Operations</sub></h1>

<p align="center"><strong>Implementation Accelerator Template</strong></p>

<p align="center">
An AI-driven workspace for configuring, deploying, and documenting Dynamics 365 Finance & Operations environments — powered by structured knowledge, automated MCP tooling, and a self-improving reinforcement learning loop.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0-blue" alt="Version 1.0">
  <img src="https://img.shields.io/badge/modules-47-2563eb" alt="47 Modules">
  <img src="https://img.shields.io/badge/DMF_templates-24-059669" alt="24 DMF Templates">
  <img src="https://img.shields.io/badge/business_processes-5%2C767-7c3aed" alt="5,767 Business Processes">
</p>

---

> **Visual Guide**: Open [`index.html`](index.html) in a browser for the full interactive workspace guide with Mermaid diagrams, collapsible sections, and visual charts.

---

## Why This Baseline?

Traditional D365 F&O implementations rely on consultant memory, scattered spreadsheets, and tribal knowledge. This workspace replaces all of that with a **structured, AI-readable knowledge base** that makes every implementation faster, more consistent, and self-improving.

| Benefit | Description |
|---------|-------------|
| 🧠 **Structured Knowledge** | 47 module knowledge articles, 24 DMF templates, 5,767 business processes — all organized and instantly accessible to the AI agent |
| 🤖 **Autonomous Deployment** | The agent deploys configuration directly to D365 F&O via MCP tools — data entities first, form navigation as fallback, API actions for activation |
| 🔄 **Self-Improving** | Every challenge encountered is logged to the Challenge Journal and fed back into module knowledge. The system gets smarter with every project |
| 📋 **Source-of-Truth Files** | Configuration files are always authoritative. If the environment drifts, fix the source first, then re-deploy |
| 🧪 **End-to-End Testing** | Tests follow complete business processes from start to finish — Source-to-Pay, Order-to-Cash, Record-to-Report — never fragments |
| 📖 **Auto-Generated Docs** | Phase 3 produces HTML documentation of the rollout narrative and environment configuration — visual, interactive, single-file deliverables |

---

## How It Works

The workspace operates as a layered knowledge system. The **master orchestrator** (`.github/copilot-instructions.md`) is automatically loaded by GitHub Copilot and routes every task to the right instruction files and module knowledge.

```
User Request
  → Master Orchestrator (classifies task, selects mode)
    → Instruction Files (playbook for the mode)
      → Module Knowledge (.md articles + .json DMF templates)
        → D365 F&O Environment (via MCP Server)
          → Reinforcement Learning (challenges fed back to knowledge)
```

### Operating Modes

| Mode | Trigger | What Happens |
|------|---------|--------------|
| **Mode A** — Phase 1 | New project / requirements change | Analyse → build config → plan rollout → validate → approve |
| **Mode B** — Phase 2 | Phase 1 approval passes | Deploy via MCP → validate → E2E test → fix loop |
| **Mode C** — Phase 3 | Phase 2 validation complete | Generate rollout-report.html + environment-config.html |
| **Mode D** — Troubleshooting | Error / unexpected behavior | Check module knowledge → check journal → fix → log |

---

## The 3-Phase Process

Every project follows a strict three-phase lifecycle. No phase begins until the previous one is complete.

### Phase 1 — Analysis & Preparation

> *Think first, act later. No deployment happens until every artefact is complete.*

1. **Step 1.1 — Analyse Requirements**: Read all documents in `Requirements/`. Classify each requirement (Standard Config, Data Migration, Parameter Setting, Workflow, Integration, Gap, Clarification).
2. **Step 1.2 — Build Configuration Files**: Create DMF template JSON, data CSV files, and parameter settings for each in-scope module in dependency order.
3. **Step 1.3 — Build Rollout Plan + E2E Test Plan**: Sequence all modules by DMF template number (010→650). Build test scenarios tracing complete business processes.
4. **Step 1.4 — Validate & Fill Gaps**: Cross-check every requirement against config files, deployment steps, and test scenarios.
5. **Step 1.5 — Approval Gate**: 9-point checklist verifying everything is complete.

### Phase 2 — Deployment & Validation

> *Push configuration to D365 F&O via the MCP server, then validate with end-to-end testing.*

1. **Step 2.1 — Deploy via F&O MCP Server**: For each module in sequence (010→650): pre-check → data entities → form config → actions → validation.
2. **Step 2.2 — Validate + E2E Testing**: Run every test scenario start to finish. On failure: fix source → re-deploy → re-test.

### Phase 3 — Documentation

> *Generate two single-file HTML deliverables.*

1. **Step 3.1 — rollout-report.html**: Full narrative (project overview, requirements, config design, deployment, testing, challenges, appendices).
2. **Step 3.2 — environment-config.html**: Visual environment reference (org hierarchy, chart of accounts, module cards, integration map).

---

## Module Knowledge Base

The workspace contains structured knowledge for **5 core D365 products** spanning **47 sub-modules**:

| Product | Sub-Modules | Count |
|---------|-------------|-------|
| **Administration** | Organization Admin, Role-Based Security, Lifecycle Services, Cloud Deployment | 4 |
| **Dynamics 365 Finance** | General Ledger, Cash & Bank, AP, AR, Tax, Fixed Assets, Budgeting, Expense Mgmt, Cost Accounting, Project Accounting, Public Sector, Compliance & Audit | 12 |
| **Dynamics 365 Supply Chain Management** | Inventory, PIM, Procurement, Sales & Marketing, Quality, Warehouse, Transportation, Production, Process Mfg, Product Config, Cost Management, Master Planning, Asset Mgmt, Engineering Change, Landed Cost, Rebate Mgmt, Service Mgmt | 17 |
| **Dynamics 365 Human Resources** | Personnel, Leave & Absence, Benefits, Performance, Learning, Employee Self Service, US Payroll, Organization Mgmt | 8 |
| **Dynamics 365 Commerce** | Multi-Channel, Call Center, Customer Engagement, POS, Omnichannel | 5 |
| **Dynamics 365 Project Operations** | Project Accounting, Sales & Quoting, Planning, Delivery, Resource Mgmt, Analytics | 6 |

### DMF Template Load Order

```
010 System Setup (Admin)
 → 020 GL Shared (Finance)
   → 025 General Ledger (Finance)
     → 100 Bank | 120 AP | 130 Tax | 140 AR | 150 Fixed Assets | 160 Budgeting
     → 300 Inventory (SCM)
       → 310 PIM | 320 Procurement | 330 Sales | 395 Quality
       → 400 Warehouse | 405 Transportation | 410 Production | 412 Process Mfg
       → 418 Product Config | 420 Costing | 430 Master Planning | 500 Retail
     → 600 Expense | 650 Project Accounting
```

---

## MCP Tool Interaction

The agent interacts with D365 F&O through three types of MCP tools:

| Priority | Tool Type | Prefix | Use Case |
|----------|-----------|--------|----------|
| 🥇 **1st** | Data Tools | `mcp_finance_opera_data_*` | OData CRUD — fastest, bulk-capable |
| 🥈 **2nd** | Form Tools | `mcp_finance_opera_form_*` | UI navigation — for params/settings not available as entities |
| 🥉 **3rd** | API Tools | `mcp_finance_opera_api_*` | X++ actions — activate, publish, post |

---

## Reinforcement Learning Loop

Every challenge encountered during configuration or deployment is captured, analyzed, and routed back into the knowledge base.

```
DETECT → JOURNAL → ANALYZE → ROUTE → UPDATE → VERIFY
  ↑                                               ↓
  └──── Future operations benefit from fix ←───────┘
```

| Trigger | Destination | Section Updated |
|---------|-------------|-----------------|
| New error encountered | `ChallengeJournal/challenge_journal.json` | New structured JSON entry |
| Config dependency discovered | Module `.md` file | Critical Configuration Rules |
| Workaround found | Module `.md` file | Implementation Discoveries |
| Entity sequence issue | DMF template `.json` | EntitySequence reorder |
| Process gap identified | Module `.md` file | Business Process Reference |

---

## Workspace Structure

### Knowledge Base (pre-built reference data)

<details>
<summary>Business Process, Media, Modules, SourceFiles</summary>

```
Business Process/                    ← 5,767-item APQC process catalogue
├── ProcessCatalogue.json            ← Hierarchical process tree
├── ProcessCatalogue_flat.json       ← Flat indexed version
└── ProcessCatalogue_MindMap.json    ← Visualization tree

Media/                               ← Branding & visual assets
└── FinanceOperations_scalable.svg   ← Product logo

Modules/                             ← 47 module knowledge articles + 24 DMF templates
├── D365_Finance_Operations_Modules_Overview.md
├── D365_Quick_Reference.md
├── dmf_odata_mapping.json           ← DMF ↔ OData entity map
├── Administration/                  ← 4 sub-modules
├── Dynamics 365 Finance/            ← 12 sub-modules
├── Dynamics 365 Supply Chain Management/  ← 17 sub-modules
├── Dynamics 365 Human Resources/    ← 8 sub-modules
├── Dynamics 365 Commerce/           ← 5 sub-modules
└── Dynamics 365 Project Operations/ ← 6 sub-modules

SourceFiles/                         ← Raw reference data
├── odata.xml                        ← Raw OData metadata
└── Prompts.md                       ← Visualization prompts
```

</details>

### Working Folders (project-specific files)

```
ProcessBaseline/
├── .github/
│   └── copilot-instructions.md          ← Master orchestrator (auto-loaded)
├── .instructions/
│   ├── project-configuration.instructions.md  ← Phase 1 playbook
│   ├── project-rollout.instructions.md        ← Phase 2 + Phase 3 playbook
│   ├── fo-interaction.instructions.md         ← MCP tool rules (all phases)
│   ├── knowledge-routing.instructions.md      ← Module → file router
│   └── reinforcement-learning.instructions.md ← Learning loop mechanics
├── ChallengeJournal/
│   ├── challenge_journal.json           ← Running issue + resolution log
│   └── JOURNAL_SCHEMA.md               ← Schema documentation
├── Requirements/                        ← Drop your requirement docs here
├── Documentation/
│   ├── requirement-profile.md           ← Phase 1.1 analysis
│   ├── requirement-matrix.json          ← Structured requirements
│   ├── config-{module}.md               ← Per-module config summaries
│   ├── parameter-settings.md            ← Form-based settings
│   ├── rollout-plan.md                  ← Deployment sequence
│   ├── e2e-test-plan.md                 ← End-to-end test plan
│   ├── test-scenarios.json              ← Structured test cases
│   ├── validation-report.md             ← Cross-check results
│   ├── gap-resolutions.md               ← Gap closure log
│   ├── e2e-test-results.md              ← Phase 2.2 test results
│   └── html/
│       ├── rollout-report.html          ← Phase 3 narrative
│       └── environment-config.html      ← Phase 3 visual reference
└── index.html                           ← Interactive workspace guide
```

---

## Getting Started

1. **Open the workspace in VS Code** — Open the `ProcessBaseline` folder with GitHub Copilot enabled. The master orchestrator loads automatically.

2. **Drop your requirement documents into `Requirements/`** — Place Word docs, PDFs, Excel files, or any text-based requirements.

3. **Ask Copilot to start Phase 1** — *"Analyse the requirements in the Requirements folder and build the requirement profile."*

4. **Review and iterate through Phase 1** — The agent produces configuration files, a rollout plan, and an E2E test plan. All work saves to `Documentation/` continuously.

5. **Approve and deploy** — *"Deploy the configuration following the rollout plan."* The agent pushes everything to D365 F&O via MCP tools.

6. **Generate documentation** — *"Generate the rollout report and environment configuration HTML."* Two single-file HTML deliverables are produced.

### Prerequisites

| Requirement | Details |
|-------------|---------|
| **VS Code** | With GitHub Copilot extension enabled |
| **D365 F&O MCP Server** | Configured in `.vscode/mcp.json` for D365 environment access |
| **Requirement Documents** | Placed in the `Requirements/` folder |
| **Environment Access** | Valid credentials for the target D365 F&O environment |

### Key Principles

- **Source files are authoritative** — if the environment drifts, fix the source first, then re-deploy.
- **Document continuously** — write as you go in every phase, never batch documentation.
- **Follow processes start to finish** — E2E testing must trace complete business processes, never fragments.
- **Consult module knowledge first** — when something doesn't work, read the module .md file before trying fixes.
- **Feed back every discovery** — every challenge, workaround, and rule goes back into the knowledge base.
- **Respect dependency order** — always configure upstream modules before downstream consumers.

---

<p align="center"><sub>Dynamics 365 Finance & Operations — Implementation Accelerator Template · Version 1.0 · February 2026<br>Built from 6 instruction files, 47 module knowledge articles, 24 DMF templates, and 5,767 business process items.</sub></p>
