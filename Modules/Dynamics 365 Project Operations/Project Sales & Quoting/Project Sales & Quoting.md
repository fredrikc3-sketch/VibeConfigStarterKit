# Project Sales & Quoting Module - Knowledge Source

> This file is the central knowledge hub for **Project Sales & Quoting** within Dynamics 365 Project Operations.

---


---


> **Microsoft Learn Reference:** [Project Sales & Quoting](https://learn.microsoft.com/en-us/dynamics365/project-operations/sales/sales-overview)

## Module Overview

Project Sales & Quoting in Dynamics 365 Project Operations manages the presales process for project-based engagements. It covers project opportunities, project quotes with detailed estimate lines, pricing dimensions, contract negotiations, and project contract creation upon deal closure.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Project Opportunities** | Track project-based sales opportunities through pipeline stages |
| **Project Quotes** | Create detailed project quotes with estimate lines and pricing |
| **Pricing Dimensions** | Configure pricing by role, category, organizational unit, and transaction type |
| **Quote Analytics** | Analyze quote profitability and margin before conversion |
| **Contract Creation** | Convert won quotes to project contracts with funding limits |
| **Multiple Price Lists** | Support role-based and cost-plus pricing strategies |
| **Quote Approval** | Route quotes through approval workflows |
| **Integration with CRM** | Leverage Dynamics 365 Sales for opportunity management |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Project sales and quoting are managed through Dataverse-based opportunities, quotes, and contracts.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Project Sales & Quoting-related business process areas:
- **Opportunities** (project-based sales pipeline)
- **Project quotes** (detailed pricing and scope)
- **Quote line details** (time, expense, material estimates)
- **Project contracts** (won quotes → active contracts)
- **Pricing dimensions** (role-based, org unit-based pricing)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Manage project sales in Dynamics 365 Project Operations** | https://learn.microsoft.com/en-us/training/paths/manage-project-sales-project-operations/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Sales process overview | https://learn.microsoft.com/en-us/dynamics365/project-operations/sales/sales-overview |
| Project-based opportunities | https://learn.microsoft.com/en-us/dynamics365/project-operations/sales/opportunity-header |
| Project quotes | https://learn.microsoft.com/en-us/dynamics365/project-operations/sales/quote-header |
| Quote line details | https://learn.microsoft.com/en-us/dynamics365/project-operations/sales/quote-line-details |
| Manage quote line billing | https://learn.microsoft.com/en-us/dynamics365/project-operations/sales/manage-quoted-values-budget-limits-quote-line |
| Project contracts | https://learn.microsoft.com/en-us/dynamics365/project-operations/sales/project-contract-header |
| Contract lines and billing methods | https://learn.microsoft.com/en-us/dynamics365/project-operations/sales/contracts-manage-project-price-lists |
| Pricing dimensions | https://learn.microsoft.com/en-us/dynamics365/project-operations/pricing-costing/pricing-dimensions-overview |
| Price lists | https://learn.microsoft.com/en-us/dynamics365/project-operations/pricing-costing/price-list-setup |
| Not-to-exceed limits | https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/manage-nte-project-contracts-sales |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Organization units | Settings > Organization units | Contracting and owning units |
| Bookable resource categories (Roles) | Settings > Bookable resource categories | Consultant, Developer, Architect, etc. |
| Currencies and exchange rates | Settings > Currencies | Multi-currency support |
| Customer accounts | Accounts (Dataverse) | Client records |

### Phase 2: Pricing Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Pricing dimensions | Settings > Pricing dimensions | What drives price (role, org unit) |
| Cost price lists | Settings > Price lists > Cost | Internal cost rates |
| Sales price lists | Settings > Price lists > Sales | Bill rates to customers |
| Role prices | (Within price list) > Role prices | Price per role per org unit |
| Category prices | (Within price list) > Category prices | Expense category pricing |
| Price list date effectivity | (Within price list) > Date range | Valid from / valid to |

### Phase 3: Sales Pipeline

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Create opportunity | Opportunities > New | Initial sales lead |
| Opportunity lines | (Within opportunity) > Lines | Project-based line items |
| Create quote (from opportunity) | (Within opportunity) > Create quote | Formal price proposal |
| Quote lines | (Within quote) > Quote lines | Scope and pricing details |
| Quote line estimates | (Within quote line) > Quote line details | Detailed T&M or fixed-price estimates |
| Customer approval | (External process) | Client accepts quote |

### Phase 4: Contract & Project Creation

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Close quote as Won | (Within quote) > Close as Won | Converts to contract |
| Project contract | (Auto-created from quote) | Active contract record |
| Contract lines | (Within contract) > Contract lines | Billing method, NTE limits |
| Create project from contract | (Within contract line) > Create project | Link project to contract |
| Invoice schedule | (Within contract line) > Invoice schedule | Milestone or periodic billing |

---

## Sales Pipeline Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     SALES PIPELINE FLOW                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────────┐      │
│  │ LEAD /    │ →  │OPPORTUNITY│ →  │  QUOTE    │ →  │  CONTRACT     │      │
│  │ PROSPECT  │    │           │    │           │    │               │      │
│  └──────────┘    └──────────┘    └──────────┘    └──────────────┘      │
│                                                                          │
│  OPPORTUNITY                                                             │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Client, expected revenue, probability                   │             │
│  │ • Project-based lines (scope overview)                    │             │
│  │ • Expected close date                                     │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  QUOTE                                                                   │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ Quote Header                                              │             │
│  │ ├── Quote Line 1: "Process Consulting" (T&M)             │             │
│  │ │    ├── Sr. Consultant: 200h × $250/h = $50,000          │             │
│  │ │    ├── Consultant: 400h × $175/h = $70,000              │             │
│  │ │    └── Expenses (estimated): $15,000                    │             │
│  │ │    Total: $135,000                                      │             │
│  │ │                                                         │             │
│  │ └── Quote Line 2: "Development" (Fixed Price)             │             │
│  │      ├── Milestone 1: Design sign-off — $30,000           │             │
│  │      ├── Milestone 2: UAT complete — $50,000              │             │
│  │      └── Milestone 3: Go-live — $20,000                   │             │
│  │      Total: $100,000                                      │             │
│  │                                                           │             │
│  │ Grand Total: $235,000                                     │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                    ┌─────────┴────────────┐                              │
│                    ▼                      ▼                              │
│           ┌─────────────┐       ┌──────────────┐                        │
│           │ CLOSE AS WON │       │ CLOSE AS LOST │                        │
│           │ → Contract    │       │ → Archive      │                        │
│           │ → Project     │       │                │                        │
│           └─────────────┘       └──────────────┘                        │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Billing Methods

| Method | Description | Invoice Trigger | Use Case |
|--------|-------------|-----------------|----------|
| **Time and Material** | Bill actuals (hours × rate + expenses) | Periodic or on-demand | Consulting, advisory |
| **Fixed Price** | Bill on milestones or schedule | Milestone completion | Implementation, deliverables |
| **Not-to-Exceed (NTE)** | T&M with a cap | Actual up to NTE limit | Capped T&M engagements |

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `OpportunityListPage` | Opportunities | Sales |
| `QuoteListPage` | Project quotes | Sales |
| `ContractListPage` | Project contracts | Sales |
| `PriceListSetup` | Price lists | Setup |
| `PricingDimensions` | Pricing dimensions | Setup |
| `RolePrices` | Role prices | Pricing |
| `InvoiceSchedule` | Invoice schedules | Billing |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Organization units** and **roles** must be defined before price lists
2. **Price lists** (cost and sales) must be configured before quotes have accurate pricing
3. **Pricing dimensions** determine how prices are resolved (role + org unit is most common)
4. **Opportunity** must exist before a quote can be created from it
5. **Quote must be closed as Won** to generate a contract
6. **Contract lines** determine billing method — cannot change after invoicing begins
7. **Invoice schedules** for fixed-price must be set before milestone billing

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No price found for role" | Role price not in attached price list | Add role price to the price list |
| "Quote already closed" | Trying to edit a closed quote | Revise quote (creates new revision) |
| "Contract line billing method locked" | Invoice already created | Cannot change — create new line if needed |
| "NTE limit exceeded" | Actuals exceed not-to-exceed amount | Review scope or increase NTE |
| "Missing pricing dimension" | Custom dimension not configured | Configure in pricing dimensions setup |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Project Sales & Quoting** module.

### Project to profit

*131 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze project performance | 14 | — |
| Develop project strategy | 6 | — |
| Manage project contracts | 18 | — |
| Manage project delivery | 42 | — |
| Manage project financials | 25 | — |
| Plan projects | 26 | — |

