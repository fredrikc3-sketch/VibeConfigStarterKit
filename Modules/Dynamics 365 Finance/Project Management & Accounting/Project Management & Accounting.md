# Project Management & Accounting Module - Knowledge Source

> This file is the central knowledge hub for **Project Management & Accounting** within Dynamics 365 Finance.

---


---


> **Microsoft Learn Reference:** [Project Management & Accounting](https://learn.microsoft.com/en-us/dynamics365/finance/project-management/project-management-accounting-home-page)

## Module Overview

The Project Management & Accounting module in Dynamics 365 Finance provides financial management for projects including cost tracking, revenue recognition, WIP calculations, project invoicing, and project budgeting. It supports multiple project types (fixed-price, time & material, investment) and integrates with Dynamics 365 Project Operations for end-to-end project lifecycle management.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Project Creation & Structure** | Define projects with WBS, project groups, and funding sources |
| **Project Budgeting** | Create and track budgets for project costs and revenue |
| **Cost Tracking** | Record and track project costs from hours, expenses, items, and fees |
| **Revenue Recognition** | Recognize revenue using completed contract or percentage of completion methods |
| **WIP Calculations** | Calculate work-in-progress and post estimates to the general ledger |
| **Project Invoicing** | Generate customer invoices based on project milestones or time & material |
| **Intercompany Projects** | Manage cross-company project billing and cost sharing |
| **Project Reports** | Analyze project profitability, cost variance, and utilization |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Project configuration uses dedicated project setup forms within Finance.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Project Management & Accounting-related business process areas:
- **Project creation and structure** (WBS, project groups, contracts)
- **Project transactions** (hours, expenses, items, fees)
- **Revenue recognition** (estimates, WIP, revenue accruals)
- **Project invoicing** (time & material, fixed-price)
- **Project budgeting and cost control**

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure Project management and accounting in Dynamics 365 Finance** | https://learn.microsoft.com/en-us/training/paths/configure-project-management-accounting-dyn365-finance/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Project management and accounting overview | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/project-overview |
| Project contracts | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/project-contracts |
| Project groups | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/project-groups |
| Work breakdown structures | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/work-breakdown-structures |
| Project budgets | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/project-budgets |
| Project estimates | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/project-estimates |
| Revenue recognition for projects | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/revenue-recognition-overview |
| Project invoicing | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/project-invoicing |
| Project categories | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-accounting/configure-project-categories |
| Hour, expense, and item journals | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/project-journals |
| Committed costs | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/committed-costs |
| Intercompany project accounting | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/intercompany-project |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| General ledger setup | General ledger > Ledger setup | Posting accounts |
| Project parameters | Project management and accounting > Setup > Project management and accounting parameters | Module-level settings |
| Number sequences | (Within project parameters) > Number sequences | Project, contract, invoice numbers |
| Financial dimensions | General ledger > Chart of accounts > Dimensions | Project dimension if used |

### Phase 2: Project Categories & Groups

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Project categories | Project management and accounting > Setup > Categories > Project categories | Transaction category definitions |
| Category groups | Project management and accounting > Setup > Categories > Category groups | Grouping for reporting |
| Project groups | Project management and accounting > Setup > Posting > Project groups | Posting profiles (T&M, Fixed-price, etc.) |
| Ledger posting setup | Project management and accounting > Setup > Posting > Ledger posting setup | GL account assignments |
| Line properties | Project management and accounting > Setup > Line properties | Chargeable, non-chargeable |

### Phase 3: Project Contract & Project Creation

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Funding sources | Project management and accounting > Projects > Project contracts > (contract) > Funding sources | Customer/grant funding |
| Project contracts | Project management and accounting > Projects > Project contracts | Contract header (billing rules) |
| Projects | Project management and accounting > Projects > All projects | Project records |
| Work breakdown structure | (Within project) > Plan > WBS | Task hierarchy |
| Project team | (Within project) > Plan > Project team | Resource assignments |

### Phase 4: Transactions & Cost Control

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Hour journals | Project management and accounting > Journals > Hour | Time entry |
| Expense journals | Project management and accounting > Journals > Expense | Expense posting |
| Item journals | Project management and accounting > Journals > Item | Material consumption |
| Fee journals | Project management and accounting > Journals > Fee | Fee transactions |
| Project budgets | Project management and accounting > Projects > (project) > Budget | Budget creation and approval |

### Phase 5: Revenue Recognition & Invoicing

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Estimates | Project management and accounting > Periodic > Estimates > (Create/Post) | WIP and revenue calculation |
| Eliminate estimates | Project management and accounting > Periodic > Estimates > Eliminate | Reverse WIP at completion |
| Invoice proposals | Project management and accounting > Project invoices > Invoice proposals | Generate customer invoices |
| Post invoices | (Within invoice proposal) > Post | Post and send invoices |

---

## Project Types and Billing

| Project Type | Revenue | Costs | Invoicing | Use Case |
|-------------|---------|-------|-----------|----------|
| **Time and material** | On posting | On posting | Actual transactions | Consulting, hourly work |
| **Fixed-price** | % complete or completed contract | On posting | Milestones/schedule | Construction, deliverables |
| **Investment** | None (capitalized) | On posting | None | Internal capital projects |
| **Cost project** | None | On posting | None | Internal cost tracking |
| **Internal** | None | On posting | None | Internal activities |
| **Time** | Recognized | Recognized | None | Non-billable time tracking |

---

## Project Lifecycle Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      PROJECT LIFECYCLE FLOW                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. CONTRACT & PROJECT SETUP                                             │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Create project contract → funding source (customer)    │          │
│     │ • Create project → assign project group (T&M/FP/etc.)   │          │
│     │ • Build WBS → milestones and deliverables                │          │
│     │ • Assign resources → project team                        │          │
│     │ • Set budget → approval workflow                         │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  2. EXECUTION (Transactions)                                             │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Hours (timesheets / hour journals)                      │          │
│     │ • Expenses (expense reports / expense journals)           │          │
│     │ • Items (item requirements / item journals)              │          │
│     │ • Fees (fee journals)                                    │          │
│     │ • Vendor invoices (purchase orders)                      │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  3. COST CONTROL & WIP                                                   │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Budget vs. actual monitoring                           │          │
│     │ • Create estimates → calculate WIP / revenue accrual     │          │
│     │ • Post estimates → GL entries for WIP                    │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  4. INVOICING                                                            │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • T&M: Invoice proposal from posted transactions         │          │
│     │ • Fixed-price: Invoice on milestones / schedule          │          │
│     │ • Post invoice → AR and GL                               │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  5. CLOSE-OUT                                                            │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Eliminate estimates (reverse WIP)                       │          │
│     │ • Final invoice                                          │          │
│     │ • Set project stage to Finished                          │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `ProjProjectsListPage` | All projects | Projects |
| `ProjProjectContractsListPage` | Project contracts | Projects |
| `ProjInvoiceProposalListPage` | Invoice proposals | Invoicing |
| `ProjEstimate` | Estimates | Periodic |
| `ProjParameters` | Project parameters | Setup |
| `ProjCategory` | Project categories | Setup |
| `ProjGroup` | Project groups | Setup |
| `ProjJournalHour` | Hour journals | Journals |
| `ProjJournalExpense` | Expense journals | Journals |
| `ProjBudget` | Project budgets | Budgets |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Project parameters** must be configured before creating projects
2. **Project categories** must exist for each transaction type (hour, expense, item, fee)
3. **Project groups** control posting behavior — select carefully (T&M vs. Fixed-price)
4. **Ledger posting setup** must map categories to GL accounts
5. **Project contracts** with funding sources must exist before creating billable projects
6. **Budget approval workflow** must be active before budget submissions
7. **Estimates must run** before WIP and revenue recognition posts to GL

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No posting account found" | Ledger posting setup incomplete | Configure posting accounts for category/group |
| "Budget exceeded" | Transaction exceeds approved budget | Request budget revision or override |
| "Category not allowed" | Category not assigned to project group | Add category to project group mapping |
| "Funding limit exceeded" | Contract funding depleted | Increase funding limit on contract |
| "Estimate already posted" | Duplicate estimate run | Reverse and recreate estimate |
| "Cannot invoice" | No uninvoiced transactions or wrong project type | Check project type and transaction status |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Project Management & Accounting** module.

### Project to profit

*9 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Develop project strategy | 1 | — |
| Manage project delivery | 1 | — |
| Manage project financials | 3 | — |
| Plan projects | 4 | — |

### Record to report

*236 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze financial performance | 26 | — |
| Close financial periods | 41 | — |
| Define accounting policies | 82 | — |
| Manage budgets | 25 | — |
| Manage cash | 26 | — |
| Record financial transactions | 36 | — |

