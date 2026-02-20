# Public Sector Functionality Module - Knowledge Source

> This file is the central knowledge hub for **Public Sector Functionality** within Dynamics 365 Finance.

---


---


> **Microsoft Learn Reference:** [Public Sector Functionality](https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/public-sector-functionality)

## Module Overview

Public Sector functionality in Dynamics 365 Finance extends standard financial capabilities with features tailored for government and public organizations. It includes fund accounting, derived financial hierarchies, preliminary budgets, posting definitions for advanced ledger entries, purchase agreement classification, and features for grant management and regulatory compliance.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Fund Accounting** | Track financial resources by fund with balance sheet by fund reporting |
| **Derived Financial Hierarchies** | Analyze posted transactions using hierarchical classification |
| **Preliminary Budgets** | Create provisional budgets before final budget approval |
| **Advanced Ledger Entries** | Create, adjust, and reverse ledger entries for reclassification |
| **Posting Definitions** | Control GL posting with granular rules based on source documents |
| **Purchase Agreement Classification** | Classify purchase agreements per government reporting needs |
| **Grant Management** | Track grants, funding sources, and compliance requirements |
| **Vendor Certification** | Track vendor certifications for compliance (minority status, etc.) |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Public sector features extend standard Finance modules with government-specific configurations.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Public Sector-related business process areas:
- **Fund accounting** (fund-based financial management)
- **Budget analysis** (preliminary budgets, apportionments)
- **Purchasing policies** (government procurement regulations)
- **Grant management** (federal/state grants, compliance)
- **Vendor certifications** (minority, women-owned, etc.)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure public sector in Dynamics 365 Finance** | https://learn.microsoft.com/en-us/training/paths/configure-public-sector-dyn365-finance/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Public sector home page | https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/public-sector-functionality |
| Fund accounting | https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/funds-public-sector |
| Derived financial hierarchies | https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/derived-financial-hierarchies-public-sector |
| Preliminary budgets | https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/preliminary-budgets-apportionments-public-sector |
| Budget analysis | https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/budget-analysis-public-sector |
| Purchase order line amounts | https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/purchase-order-line-amounts |
| Vendor certifications | https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/manage-vendor-certifications |
| Free text invoice lines | https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/free-text-invoices-public-sector |
| Year-end processing | https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/year-end-processing-public-sector |
| Advanced ledger entries | https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/advanced-ledger-entries-public-sector |
| Spending limits and budget encumbrances | https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/budgeting-public-sector |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Enable public sector configuration | System administration > Setup > License configuration > Public Sector | Turn on public sector features |
| General ledger setup | General ledger > Ledger setup | Base accounting configuration |
| Fiscal calendar | General ledger > Calendars > Fiscal calendars | Fiscal year definition |
| Chart of accounts with fund dimension | General ledger > Chart of accounts | Fund-based COA |

### Phase 2: Fund Accounting

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Fund types | General ledger > Setup > Fund > Fund types | Governmental, proprietary, fiduciary |
| Funds | General ledger > Setup > Fund > Funds | Individual fund records |
| Derived financial hierarchies | General ledger > Setup > Account structures > Derived financial hierarchies | Fund-based reporting hierarchies |
| Posting definitions | General ledger > Setup > Posting > Posting definitions | Fund-specific posting behaviors |
| Advanced ledger entries | General ledger > Journal entries > Advanced ledger entries | Interfund transfers |

### Phase 3: Budgeting (Public Sector)

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Preliminary budgets | Budgeting > Budget register entries > Preliminary budget | Before-approval budget entries |
| Apportionments | Budgeting > Budget register entries > Apportionments | Approved spending authority |
| Budget control configuration | Budgeting > Setup > Budget control > Budget control configuration | Encumbrance & spending limits |
| Budget analysis | Budgeting > Inquiries > Budget analysis | Budget vs. actual + encumbrances |

### Phase 4: Procurement & Grants

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Vendor certifications | Procurement and sourcing > Vendors > Vendor certifications | Government vendor compliance |
| Certification types | Procurement and sourcing > Setup > Certification type | Minority, women-owned, etc. |
| Grant management | Project management and accounting > Grants > Grants | Grant creation and tracking |
| Purchase agreements | Procurement and sourcing > Purchase agreements | Government contracts |

### Phase 5: Year-End & Reporting

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Year-end close (public sector) | General ledger > Period close > Year-end close | Fund-based year-end processing |
| CAFR reporting | (via financial reporting) | Comprehensive Annual Financial Report |
| 1099 processing | Accounts payable > Periodic > 1099 processing | Vendor tax reporting |

---

## Public Sector Fund Accounting Model

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  PUBLIC SECTOR FUND ACCOUNTING MODEL                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  FUND TYPES                                                              │
│  ┌──────────────────────────────────────────────────────────┐           │
│  │                                                            │           │
│  │  GOVERNMENTAL              PROPRIETARY         FIDUCIARY   │           │
│  │  ┌──────────────┐         ┌──────────────┐   ┌─────────┐ │           │
│  │  │ General Fund  │         │ Enterprise    │   │ Trust    │ │           │
│  │  │ Special Revenue│        │ Internal Svc  │   │ Agency   │ │           │
│  │  │ Capital Project│        └──────────────┘   └─────────┘ │           │
│  │  │ Debt Service   │                                        │           │
│  │  └──────────────┘                                         │           │
│  │                                                            │           │
│  └──────────────────────────────────────────────────────────┘           │
│                                                                          │
│  BUDGET FLOW                                                             │
│  ┌───────────────┐    ┌───────────────┐    ┌───────────────┐           │
│  │ Preliminary    │ →  │ Original       │ →  │ Apportionments│           │
│  │ Budget         │    │ Budget         │    │ (Approved     │           │
│  │ (Draft)        │    │ (Adopted)      │    │  Spending)    │           │
│  └───────────────┘    └───────────────┘    └───────────────┘           │
│                                                     │                    │
│                                                     ▼                    │
│  SPENDING CONTROL                                                        │
│  ┌──────────────────────────────────────────────────────────┐           │
│  │ Pre-Encumbrance → Encumbrance → Expenditure               │           │
│  │ (Requisition)     (PO)          (Invoice/Payment)         │           │
│  │                                                            │           │
│  │ Budget control checks at each stage                        │           │
│  └──────────────────────────────────────────────────────────┘           │
│                                                                          │
│  YEAR-END                                                                │
│  ┌──────────────────────────────────────────────────────────┐           │
│  │ • Close nominal accounts per fund                          │           │
│  │ • Carry forward encumbrances to new year                   │           │
│  │ • Fund balance reporting                                   │           │
│  └──────────────────────────────────────────────────────────┘           │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `LedgerFund` | Funds | Setup |
| `LedgerFundType` | Fund types | Setup |
| `LedgerDerivedFinHierarchyLegal` | Derived financial hierarchies | Setup |
| `BudgetPreliminaryBudget` | Preliminary budgets | Budgeting |
| `BudgetApportionments` | Apportionments | Budgeting |
| `BudgetAnalysis` | Budget analysis | Inquiries |
| `LedgerAdvancedLedgerEntry` | Advanced ledger entries | Journals |
| `VendCertification` | Vendor certifications | Procurement |
| `ProjGrant` | Grants | Projects |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Public sector license configuration key** must be enabled before any public sector features appear
2. **Fund dimension** must be part of the account structure
3. **Fund types** must be defined before individual funds
4. **Posting definitions** should be configured for fund-based posting behavior
5. **Preliminary budgets** must be created before apportionments
6. **Budget control** must be activated to enforce spending limits
7. **Year-end close** must process each fund individually

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Public sector features not visible" | Configuration key not enabled | Enable under license configuration |
| "Budget check failed" | Spending exceeds apportionment | Request additional apportionment |
| "Fund balance mismatch" | Interfund transactions not balanced | Use advanced ledger entries for interfund |
| "Encumbrance not relieved" | PO not properly invoiced | Post vendor invoice against PO |
| "Year-end close error" | Nominal accounts not mapped | Configure closing account per fund |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Public Sector Functionality** module.

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

