---
name: d365-knowledge-routing
description: Use to look up which module knowledge file (`.md`), DMF template (`.json`), or supporting artefact to read for a given Dynamics 365 F&O concept. Provides the full module → file path index for all 47 sub-modules across Finance, SCM, HR, Commerce and Project Operations, the DMF template load order (010 → 650), the keyword router for free-text routing, and the end-to-end business-process → module matrix. Load FIRST on any task that touches a specific module, entity, or process.
---

# D365 F&O Knowledge Routing

> The single source of truth for "which file holds the answer".

---

## 1 · Module → File Path

### Administration
| Sub-Module | Knowledge | DMF Templates |
|---|---|---|
| Organization Administration | `Modules/Administration/Organization Administration/Organization Administration.md` | `010 - System Setup.json`, `022 - Workflow.json` |
| Role-Based Security | `Modules/Administration/Role-Based Security/Role-Based Security.md` | — |
| Lifecycle Services | `Modules/Administration/Lifecycle Services/Lifecycle Services.md` | — |
| Cloud & On-Premises Deployment | `Modules/Administration/Cloud & On-Premises Deployment/Cloud & On-Premises Deployment.md` | — |

### Dynamics 365 Finance
| Sub-Module | Knowledge | DMF Templates |
|---|---|---|
| General Ledger | `Modules/Dynamics 365 Finance/General Ledger/General Ledger.md` | `020 - GL Shared.json`, `025 - General ledger.json` |
| Cash & Bank Management | `Modules/Dynamics 365 Finance/Cash & Bank Management/Cash & Bank Management.md` | `100 - Bank.json` |
| Accounts Payable | `Modules/Dynamics 365 Finance/Accounts Payable/Accounts Payable.md` | `120 - Accounts payable.json` |
| Tax | `Modules/Dynamics 365 Finance/Tax/Tax.md` | `130 - Tax.json` |
| Accounts Receivable | `Modules/Dynamics 365 Finance/Accounts Receivable/Accounts Receivable.md` | `140 - Accounts receivable.json` |
| Fixed Assets Management | `Modules/Dynamics 365 Finance/Fixed Assets Management/FixedAssets.md` | `150 - Fixed assets.json` |
| Budgeting | `Modules/Dynamics 365 Finance/Budgeting/Budgeting.md` | `160 - Budgeting.json` |
| Expense Management | `Modules/Dynamics 365 Finance/Expense Management/Expense Management.md` | `600 - Expense.json` |
| Cost Accounting | `Modules/Dynamics 365 Finance/Cost Accounting/Cost Accounting.md` | — |
| Project Mgmt & Accounting | `Modules/Dynamics 365 Finance/Project Management & Accounting/Project Management & Accounting.md` | — |
| Public Sector | `Modules/Dynamics 365 Finance/Public Sector Functionality/Public Sector Functionality.md` | — |
| Compliance & Audit | `Modules/Dynamics 365 Finance/Compliance & Audit/Compliance & Audit.md` | — |

### Dynamics 365 Supply Chain Management
| Sub-Module | Knowledge | DMF Templates |
|---|---|---|
| Inventory Management | `Modules/Dynamics 365 Supply Chain Management/Inventory Management/Inventory Management.md` | `300 - Inventory.json` |
| Product Information Mgmt | `Modules/Dynamics 365 Supply Chain Management/Product Information Management/Product Information Management.md` | `310 - Product information management.json` |
| Procurement & Sourcing | `Modules/Dynamics 365 Supply Chain Management/Procurement & Sourcing/Procurement & Sourcing.md` | `320 - Procurement and sourcing.json` |
| Sales & Marketing | `Modules/Dynamics 365 Supply Chain Management/Sales & Marketing/Sales & Marketing.md` | `330 - Sales and marketing.json` |
| Quality Management | `Modules/Dynamics 365 Supply Chain Management/Quality Management/Quality Management.md` | `395 - Quality management.json` |
| Warehouse Management | `Modules/Dynamics 365 Supply Chain Management/Warehouse Management/Warehouse Management.md` | `400 - Warehouse management.json` |
| Transportation Management | `Modules/Dynamics 365 Supply Chain Management/Transportation Management/Transportation Management.md` | `405 - Transportation management.json` |
| Production Control | `Modules/Dynamics 365 Supply Chain Management/Production Control/Production Control.md` | `410 - Production control.json` |
| Process Manufacturing | `Modules/Dynamics 365 Supply Chain Management/Process Manufacturing/Process Manufacturing.md` | `412 - Process manufacturing.json` |
| Product Config Models | `Modules/Dynamics 365 Supply Chain Management/Product Configuration Models/Product Configuration Models.md` | `418 - Product configuration models.json` |
| Cost Management | `Modules/Dynamics 365 Supply Chain Management/Cost Management/Cost Management.md` | `420 - Costing.json` |
| Master Planning | `Modules/Dynamics 365 Supply Chain Management/Master Planning & Demand Planning/Master Planning.md` | `430 - Master planning.json` |
| Asset Management | `Modules/Dynamics 365 Supply Chain Management/Asset Management/Asset Management.md` | — |
| Engineering Change Mgmt | `Modules/Dynamics 365 Supply Chain Management/Engineering Change Management/Engineering Change Management.md` | — |
| Landed Cost | `Modules/Dynamics 365 Supply Chain Management/Landed Cost/Landed Cost.md` | — |
| Rebate Management | `Modules/Dynamics 365 Supply Chain Management/Rebate Management/Rebate Management.md` | — |
| Service Management | `Modules/Dynamics 365 Supply Chain Management/Service Management/Service Management.md` | — |

### Dynamics 365 Human Resources
| Sub-Module | Knowledge | DMF Templates |
|---|---|---|
| Personnel Management | `Modules/Dynamics 365 Human Resources/Personnel Management/Personnel Management.md` | — |
| Employee Self Service | `Modules/Dynamics 365 Human Resources/Employee Self Service/Employee Self Service.md` | — |
| Leave & Absence Management | `Modules/Dynamics 365 Human Resources/Leave & Absence Management/Leave & Absence Management.md` | — |
| Benefits Management | `Modules/Dynamics 365 Human Resources/Benefits Management/Benefits Management.md` | — |
| Performance Development | `Modules/Dynamics 365 Human Resources/Performance Development/Performance Development.md` | — |
| Learning & Training | `Modules/Dynamics 365 Human Resources/Learning & Training/Learning & Training.md` | — |
| US Payroll | `Modules/Dynamics 365 Human Resources/US Payroll/US Payroll.md` | — |
| Organization Management | `Modules/Dynamics 365 Human Resources/Organization Management/Organization Management.md` | — |

### Dynamics 365 Commerce
| Sub-Module | Knowledge | DMF Templates |
|---|---|---|
| Multi-Channel / Retail | `Modules/Dynamics 365 Commerce/Multi-Channel Setup Retail E-Commerce DTC/Retail.md` | `500 - Retail.json` |
| Call Center Operations | `Modules/Dynamics 365 Commerce/Call Center Operations/Call Center Operations.md` | — |
| Customer Engagement | `Modules/Dynamics 365 Commerce/Customer Engagement & Personalization/Customer Engagement & Personalization.md` | — |
| Point of Sale | `Modules/Dynamics 365 Commerce/Point of Sale Modern & Cloud/Point of Sale.md` | — |
| Omnichannel Fulfillment | `Modules/Dynamics 365 Commerce/Omnichannel Fulfillment/Omnichannel Fulfillment.md` | — |

### Dynamics 365 Project Operations
| Sub-Module | Knowledge | DMF Templates |
|---|---|---|
| Project Accounting | `Modules/Dynamics 365 Project Operations/Project Accounting & Invoicing/Project Accounting.md` | `650 - Project accounting.json` |
| Project Sales & Quoting | `Modules/Dynamics 365 Project Operations/Project Sales & Quoting/Project Sales & Quoting.md` | — |
| Project Planning | `Modules/Dynamics 365 Project Operations/Project Planning & Scheduling/Project Planning & Scheduling.md` | — |
| Project Delivery | `Modules/Dynamics 365 Project Operations/Project Delivery & Execution/Project Delivery & Execution.md` | — |
| Resource Management | `Modules/Dynamics 365 Project Operations/Resource Management/Resource Management.md` | — |
| Analytics & KPIs | `Modules/Dynamics 365 Project Operations/Analytics & KPI Tracking/Analytics & KPI Tracking.md` | — |

---

## 2 · Cross-Module Reference Files

| File | Purpose | When to load |
|---|---|---|
| `Modules/D365_Finance_Operations_Modules_Overview.md` | Full module list | Initial orientation |
| `Modules/D365_Quick_Reference.md` | Compact module + capability summary | Quick lookup |
| `Modules/dmf_odata_mapping.json` | DMF ↔ OData entity mapping (verified) | OData ops, integration |
| `Business Process/ProcessCatalogue.json` | Hierarchical process tree (5,767 items) | Business process questions |
| `Business Process/ProcessCatalogue_flat.json` | Flat indexed version with `parentId` | Programmatic process lookups |
| `Business Process/ProcessCatalogue_MindMap.json` | Visualization-ready tree | Mind-map output |
| `ChallengeJournal/challenge_journal.json` | Running challenge + resolution log | Before risky ops; after issues |
| `Requirements/` | Source requirement docs | Phase 1.1 |
| `Documentation/` | All project output artefacts | Throughout |

---

## 3 · DMF Template Load Order

The numeric prefix encodes cross-module dependency. **Always respect.**

```
010 System Setup              → Admin / Org Admin
020 GL Shared                 → Finance / GL
022 Workflow                  → Admin / Org Admin
025 General Ledger            → Finance / GL
100 Bank                      → Finance / Cash & Bank
120 Accounts Payable          → Finance / AP
130 Tax                       → Finance / Tax
140 Accounts Receivable       → Finance / AR
150 Fixed Assets              → Finance / FA
160 Budgeting                 → Finance / Budgeting
300 Inventory                 → SCM / Inventory
310 Product Info Mgmt         → SCM / PIM
320 Procurement & Sourcing    → SCM / Procurement
330 Sales & Marketing         → SCM / Sales
395 Quality Management        → SCM / Quality
400 Warehouse Management      → SCM / Warehouse
405 Transportation Mgmt       → SCM / Transportation
410 Production Control        → SCM / Production
412 Process Manufacturing     → SCM / Process Mfg
418 Product Config Models     → SCM / Product Config
420 Costing                   → SCM / Cost Mgmt
430 Master Planning           → SCM / Master Planning
500 Retail                    → Commerce / Multi-Channel
600 Expense                   → Finance / Expense Mgmt
650 Project Accounting        → Project Ops / Accounting
```

### Dependency rules
- **010** has no dependencies — runs first.
- **020, 022** depend on 010.
- **025** depends on 020.
- **100–160** depend on 025 (GL must be configured first).
- **300** depends on 025 (Inventory needs GL posting profiles).
- **310–330** depend on 300.
- **395–430** depend on 300+ (SCM foundations).
- **500** depends on 300+ and 100+ (Commerce needs both).
- **600** depends on 025.
- **650** depends on 025.

---

## 4 · Keyword → Module Router

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

---

## 5 · End-to-End Business Process → Module Matrix

| Process | Primary Modules | DMF Templates |
|---|---|---|
| Acquire to Dispose | Fixed Assets, GL | 150, 025 |
| Design to Retire | PIM, Engineering Change | 310 |
| Forecast to Plan | Master Planning, Inventory | 430, 300 |
| Inventory to Deliver | Inventory, Warehouse, Sales | 300, 400, 330 |
| Order to Cash | Sales, AR, Inventory | 330, 140, 300 |
| Plan to Produce | Production, Master Planning | 410, 430 |
| Project to Profit | Project Ops, GL | 650, 025 |
| Service to Deliver | Service Mgmt, Inventory | 300 |
| Source to Pay | Procurement, AP | 320, 120 |
| Record to Report | GL, Budgeting, Cost Acct | 025, 160 |
