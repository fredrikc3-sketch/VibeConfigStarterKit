---
name: d365-knowledge-routing
description: Use when you need a file path. Provides the keyword router and DMF dependency rules so any task can find the right module knowledge file (`.md`), DMF template (`.json`), or supporting artefact. The full 47-module index and end-to-end process matrix live in the sidecar `module-index.md` — load that ONLY when you need exhaustive lookups. Do NOT load this skill speculatively; only when a path is unknown.
---

# D365 F&O Knowledge Routing

> The decision logic for "which file holds the answer". The bulky reference tables are in `module-index.md` — load on demand.

---

## 1 · How to use this skill

```
HAVE        →  USE
keyword     →  §3 Keyword router (here)
DMF seq #   →  §2 DMF dependency rules (here)
exhaustive  →  module-index.md  (47-module table + process matrix)
   lookup
```

For most tasks the keyword router and dependency rules below are enough.
Open `module-index.md` only when you need a complete table — e.g. when
populating the dispatch table for `module-fanout`.

---

## 2 · DMF Dependency Rules (decision-time)

Authoritative graph: **`Modules/dependency-graph.json`** — never duplicate elsewhere.
The rules below are a human-readable summary; the JSON is the source of truth.

| DMF prefix range | Tier | Always depends on |
|---|---|---|
| 010 | Foundation | — |
| 020, 022 | GL Shared / Workflow | 010 |
| 025 | General Ledger | 020 |
| 100–160 | Finance modules | 025 |
| 300 | Inventory | 025 |
| 310–395 | SCM Tier 1 | 300 |
| 400–430 | SCM Tier 2 | 300 (+ 310 / 410 as applicable) |
| 500 | Retail | 300 + 100 + 330 |
| 600 | Expense | 025 + 120 |
| 650 | Project Accounting | 025 |

Wave construction: read `Modules/dependency-graph.json` `waves[]`. Do not hand-roll waves.

---

## 3 · Keyword → Module Router

| Keyword | Route to |
|---|---|
| chart of accounts, financial dimensions, journal, fiscal calendar, ledger | General Ledger |
| vendor, purchase invoice, payment proposal, vendor group | Accounts Payable |
| customer, free text invoice, collection letter, customer group | Accounts Receivable |
| bank account, reconciliation, cash position | Cash & Bank Management |
| depreciation, asset book, asset group | Fixed Assets Management |
| budget model, budget plan, budget control | Budgeting |
| sales tax, tax group, withholding tax | Tax |
| expense report, travel requisition, per diem | Expense Management |
| item, product, released product, item group | Product Information Management |
| warehouse, location, wave, work template | Warehouse Management |
| purchase order, RFQ, purchase agreement | Procurement & Sourcing |
| sales order, quotation, sales agreement | Sales & Marketing |
| production order, BOM, route, kanban | Production Control |
| formula, batch order, co-product | Process Manufacturing |
| transfer order, counting journal, inventory close | Inventory Management |
| quality order, test, nonconformance | Quality Management |
| shipping, load, freight, carrier | Transportation Management |
| demand forecast, planned order, master plan | Master Planning |
| costing version, cost price, cost group | Cost Management |
| retail channel, POS, e-commerce, call center | Commerce |
| project contract, WBS, project invoice | Project Operations |
| worker, position, department, job | Personnel Management |
| leave plan, absence, time off | Leave & Absence |
| benefit plan, enrollment, life event | Benefits Management |
| security role, duty, privilege | Role-Based Security |
| legal entity, operating unit, org hierarchy | Organization Administration |
| LCS, environment, deployment, code package | Lifecycle Services |

For path lookup once a module is identified, see `module-index.md`.

---

## 4 · Cross-Module Reference Files

| File | Purpose | When to load |
|---|---|---|
| `Modules/dependency-graph.json` | Authoritative dep graph + wave plan | Wave construction (always) |
| `Modules/D365_Finance_Operations_Modules_Overview.md` | Module catalogue | Initial orientation |
| `Modules/D365_Quick_Reference.md` | Compact module + capability summary | Quick lookup |
| `Modules/dmf_odata_mapping.json` | DMF ↔ OData entity mapping | OData ops, integration |
| `Business Process/ProcessCatalogue.json` | Hierarchical process tree | Business process questions |
| `ChallengeJournal/challenge_journal.json` | Challenge log | Before risky ops; after issues |

---

## 5 · Project-ID Namespacing (multi-tenant)

When operating in a multi-project workspace, prefix mutable artefacts with `<projectId>/`:

| Artefact | Single-project path | Multi-project path |
|---|---|---|
| Documentation | `Documentation/...` | `Documentation/<projectId>/...` |
| Challenge Journal | `ChallengeJournal/challenge_journal.json` | `ChallengeJournal/<projectId>/challenge_journal.json` |
| Module discoveries | (mutates `Modules/.../*.md`) | `Modules/.discoveries/<projectId>/<module>.md` |
| Run state | `Documentation/run-state.json` | `Documentation/<projectId>/run-state.json` |

Canonical files in `Modules/` and `Business Process/` are **read-only across projects**.
Mutating them cross-contaminates other projects' knowledge.
