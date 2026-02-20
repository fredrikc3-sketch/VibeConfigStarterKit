# Expense Management Module - Knowledge Source

> This file is the central knowledge hub for the **Expense Management** module within Dynamics 365 Finance.

---


---


> **Microsoft Learn Reference:** [Expense Management](https://learn.microsoft.com/en-us/dynamics365/finance/expense-management/expense-management)

## Module Overview

The Expense Management module streamlines the process of tracking and reimbursing employee business expenses. It supports expense report creation, receipt capture (with OCR), policy enforcement, workflow-based approval, credit card transaction import, mileage calculation, per diem rules, and integration with project accounting for project-related expenses.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Expense Report Creation** | Create, submit, and track expense reports with line-item details |
| **Receipt Capture** | Scan and attach receipts using OCR-powered mobile capture |
| **Expense Policies** | Define and enforce policies for expense categories, amounts, and approval rules |
| **Workflow Approval** | Route expense reports through configurable approval workflows |
| **Credit Card Integration** | Import corporate credit card transactions and match to expense lines |
| **Per Diem & Mileage** | Calculate per diem allowances and mileage reimbursements automatically |
| **Project Expenses** | Link expenses to projects for cost tracking and billing |
| **Intercompany Expenses** | Process expenses incurred on behalf of other legal entities |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 600 - Expense (`600 - Expense.json`)

Expense management configuration entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Allowance day rates | TrvAllowanceDayRateEntity | Expense - Per Diem | 30 |
| 10 | Allowance rate | TrvAllowanceRateEntity | Expense - Per Diem | 30 |
| 10 | Cash advance accounts | TrvCashAdvanceEntity | Expense - Setup | 30 |
| 10 | Category table | CategoryTableEntity | Expense - Categories | 30 |
| 10 | Credit card import | TrvCreditCardImportEntity | Expense - Credit Card | 30 |
| 10 | Credit card types | TrvCreditCardTypeEntity | Expense - Credit Card | 30 |
| 10 | Display fields | TrvDispFieldsEntity | Expense - Setup | 30 |
| 10 | Expense category | TrvExpenseCategoryEntity | Expense - Categories | 30 |
| 10 | Expense management parameters | TrvParametersEntity | Expense - Parameters | 30 |
| 10 | Expense payment method | TrvPayMethodEntity | Expense - Setup | 30 |
| 10 | Expense purpose | TrvExpensePurposeEntity | Expense - Setup | 30 |
| 10 | Expense subcategory | TrvExpenseSubCategoryEntity | Expense - Categories | 40 |
| 10 | Merchants | TrvMerchantEntity | Expense - Setup | 30 |
| 10 | Mileage rate tiers | TrvMileageRateTierEntity | Expense - Mileage | 30 |
| 10 | Per diem locations | TrvPerDiemLocationEntity | Expense - Per Diem | 30 |
| 10 | Per diem rate | TrvPerDiemRateEntity | Expense - Per Diem | 30 |
| 10 | Shared category | SharedCategoryEntity | Expense - Categories | 30 |
| 10 | Statistics group | TrvStatisticsGroupEntity | Expense - Setup | 30 |
| 10 | Tax recovery configuration | TrvTaxRecoveryConfigEntity | Expense - Tax | 30 |
| 10 | Travel locations | TrvTravelLocationEntity | Expense - Setup | 30 |
| 10 | Valid payment methods per expense category | TrvValidPaymentMethodEntity | Expense - Setup | 40 |
| 20 | Category credit card codes | TrvCreditCardCategoryCodeEntity | Expense - Credit Card | 40 |
| 20 | Category group | CategoryGroupEntity | Expense - Categories | 40 |
| 20 | Expense delegation | TrvExpenseDelegationEntity | Expense - Setup | 40 |

**DMF Load Order Notes:**
- **Seq 10** contains all foundational expense setup — parameters, categories, per diem rates, mileage, credit card types, payment methods
- **Seq 20** contains dependent entities — credit card category codes, category groups, delegation rules
- Shared categories and category tables must be loaded before expense categories
- Expense categories must exist before subcategories and valid payment method assignments
- Per diem locations must be loaded before per diem rates

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (parameters, categories, merchants, locations, rates)
- **Level 40:** Dependent entities (subcategories, valid payment methods, credit card codes, delegations)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Expense Management** module.

### Hire to retire

*12 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Develop people strategy | 2 | — |
| Manage compensation and benefits | 5 | — |
| Manage time and attendance | 3 | — |
| Recruit and onboard talent | 2 | — |

### Project to profit

*9 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Develop project strategy | 1 | — |
| Manage project delivery | 1 | — |
| Manage project financials | 3 | — |
| Plan projects | 4 | — |

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Expense category | `TrvExpenseCategoryEntity` | `ExpenseCategories` | verified |
| Expense subcategory | `TrvExpenseSubCategoryEntity` | `ExpenseSubCategories` | verified |
| Shared category | `SharedCategoryEntity` | `SharedCategories` | verified |
| Category group | `CategoryGroupEntity` | `ProjCategoryGroups` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Allowance day rates | `TrvAllowanceDayRateEntity` |
| Allowance rate | `TrvAllowanceRateEntity` |
| Cash advance accounts | `TrvCashAdvanceEntity` |
| Category table | `CategoryTableEntity` |
| Credit card import | `TrvCreditCardImportEntity` |
| Credit card types | `TrvCreditCardTypeEntity` |
| Display fields | `TrvDispFieldsEntity` |
| Expense management parameters | `TrvParametersEntity` |
| Expense payment method | `TrvPayMethodEntity` |
| Expense purpose | `TrvExpensePurposeEntity` |
| Merchants | `TrvMerchantEntity` |
| Mileage rate tiers | `TrvMileageRateTierEntity` |
| Per diem locations | `TrvPerDiemLocationEntity` |
| Per diem rate | `TrvPerDiemRateEntity` |
| Statistics group | `TrvStatisticsGroupEntity` |
| Tax recovery configuration | `TrvTaxRecoveryConfigEntity` |
| Travel locations | `TrvTravelLocationEntity` |
| Valid payment methods per expense category | `TrvValidPaymentMethodEntity` |
| Category credit card codes | `TrvCreditCardCategoryCodeEntity` |
| Expense delegation | `TrvExpenseDelegationEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Expense Management:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Expense Management-related business process areas:
- **Record to Report** (expense reporting, period close reconciliation)
- **Expense report creation** (employee-submitted expenses, receipts, per diem)
- **Expense approval workflow** (manager approval, policy validation)
- **Credit card reconciliation** (corporate card statement import, matching)
- **Travel requisitions** (pre-trip approval, budget checking)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and use expense management in Dynamics 365 Finance** | https://learn.microsoft.com/en-us/training/modules/configure-use-expense-management-dyn365-finance/ |
| Set up expense management parameters | https://learn.microsoft.com/en-us/training/modules/configure-use-expense-management-dyn365-finance/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Expense management overview | https://learn.microsoft.com/en-us/dynamics365/finance/expense-management/expense-management |
| Plan expense management | https://learn.microsoft.com/en-us/dynamics365/finance/expense-management/plan-expense-management |
| Expense management parameters | https://learn.microsoft.com/en-us/dynamics365/finance/expense-management/expense-management-parameters |
| Expense categories | https://learn.microsoft.com/en-us/dynamics365/finance/expense-management/expense-management-categories |
| Per diem rules | https://learn.microsoft.com/en-us/dynamics365/finance/expense-management/per-diem |
| Mileage rules | https://learn.microsoft.com/en-us/dynamics365/finance/expense-management/mileage-rules |
| Credit card integration | https://learn.microsoft.com/en-us/dynamics365/finance/expense-management/plan-expense-management |
| Expense policies | https://learn.microsoft.com/en-us/dynamics365/finance/expense-management/expense-report-distributions |
| Expense workflow | https://learn.microsoft.com/en-us/dynamics365/finance/expense-management/expense-workflow |
| Cash advances | https://learn.microsoft.com/en-us/dynamics365/finance/expense-management/cash-advance |
| Travel requisitions | https://learn.microsoft.com/en-us/dynamics365/finance/expense-management/travel-req |
| Expense receipt processing | https://learn.microsoft.com/en-us/dynamics365/finance/expense-management/expense-receipt-processing |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites (GL & Organization)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Main accounts | General ledger > Chart of accounts > Accounts > Main accounts | Expense-related GL accounts |
| Financial dimensions | General ledger > Chart of accounts > Dimensions | Expense dimensions (Project, Dept) |
| Workers | Human resources > Workers > Workers | Employee records for expense submitters |
| Number sequences | Organization administration > Number sequences | Expense report numbering |
| Payment journals | General ledger > Journal setup > Journal names | Reimbursement journals |

### Phase 2: Category & Classification Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| SharedCategory | Expense management > Setup > General > Shared categories | Cross-module category sharing |
| CategoryTable | Expense management > Setup > General > Expense categories | Expense category definitions |
| TrvExpenseCategory | (Within category configuration) | Expense-specific category settings |
| TrvExpenseSubCategory | (Within expense category) | Subcategory detail |
| TrvExpensePurpose | Expense management > Setup > General > Expense purpose | Business purpose classification |
| TrvStatisticsGroup | Expense management > Setup > General > Statistics groups | Reporting groups |

### Phase 3: Per Diem & Mileage Configuration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| TrvPerDiemLocation | Expense management > Setup > Calculations > Per diem locations | Location-based per diem |
| TrvPerDiemRate | Expense management > Setup > Calculations > Per diem rates | Daily rate amounts |
| TrvAllowanceRate | Expense management > Setup > Calculations > Allowance rates | Allowance calculations |
| TrvMileageRateTier | Expense management > Setup > Calculations > Mileage rate tiers | Distance-based mileage rates |
| TrvTravelLocation | Expense management > Setup > General > Travel locations | Travel destination list |

### Phase 4: Payment & Credit Card Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| TrvPayMethod | Expense management > Setup > Payment > Payment methods | Expense payment methods |
| TrvCreditCardType | Expense management > Setup > Payment > Credit card types | Corporate card types |
| TrvValidPaymentMethod | (Within expense category) | Allowed payment methods per category |
| TrvMerchant | Expense management > Setup > Payment > Merchants | Merchant definitions |
| TrvCreditCardCategoryCode | Expense management > Setup > Payment > Credit card category codes | MCC to category mapping |

### Phase 5: Parameters & Policies

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| TrvParameters | Expense management > Setup > General > Expense management parameters | Module parameters |
| TrvCashAdvance | Expense management > Setup > General > Cash advance accounts | Cash advance GL accounts |
| TrvDisplayFields | Expense management > Setup > General > Display fields | Custom field visibility |
| TrvExpenseDelegation | Expense management > Setup > General > Expense delegates | Delegation rules |
| TrvTaxRecoveryConfig | Expense management > Setup > Tax > Tax recovery configuration | VAT recovery setup |

---

## Expense Report Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     EXPENSE REPORT PROCESS FLOW                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. EXPENSE CREATION                                                     │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Employee creates expense report                        │          │
│     │ • Add expense lines (category, amount, date, merchant)   │          │
│     │ • Attach receipts (scan, photo, OCR)                     │          │
│     │ • Per diem / mileage auto-calculation                    │          │
│     │ • Import credit card transactions                        │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  2. POLICY VALIDATION                                                    │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Expense policy rules checked                           │          │
│     │ • Per diem limits validated                              │          │
│     │ • Receipt requirements verified                          │          │
│     │ • Budget checking (if enabled)                           │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  3. APPROVAL WORKFLOW                                                    │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Submit for approval                                    │          │
│     │ • Manager review and approve/reject                      │          │
│     │ • Multi-level approval if configured                     │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  4. POSTING & REIMBURSEMENT                                              │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Post expense report to GL                              │          │
│     │ • Create AP payment for employee reimbursement           │          │
│     │ • Tax recovery processing (if applicable)                │          │
│     │ • Intercompany settlement (if multi-entity)              │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `TrvParameters` | Expense management parameters | Setup |
| `TrvExpenseCategories` | Expense categories | Setup |
| `TrvSharedCategories` | Shared categories | Setup |
| `TrvPerDiemLocations` | Per diem locations | Per Diem |
| `TrvPerDiemRates` | Per diem rates | Per Diem |
| `TrvMileageRateTiers` | Mileage rate tiers | Mileage |
| `TrvPayMethods` | Payment methods | Payment |
| `TrvCreditCardTypes` | Credit card types | Payment |
| `TrvCashAdvance` | Cash advances | Cash Advance |
| `TrvExpenseReports` | Expense reports | Transactions |
| `TrvTravelRequisitions` | Travel requisitions | Transactions |
| `TrvExpensePolicies` | Expense policies | Policies |
| `TrvExpenseWorkspace` | Expense management workspace | Workspace |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Workers (employees)** must exist in HR before they can submit expenses
2. **Shared categories** must be created before expense categories
3. **Expense categories** define what types of expenses can be reported
4. **Per diem locations** must exist before per diem rates
5. **Payment methods** must be configured before expense parameters
6. **Expense parameters** must be set (default posting profile, payment method, journal names)
7. **Expense workflow** must be configured before expense reports can be approved
8. **GL accounts** must exist for expense posting (expense accounts, clearing accounts)

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No expense category configured" | Expense categories not set up | Create expense categories |
| "Payment method not valid" | Payment method not allowed for category | Add payment method to category |
| "Per diem rate not found" | Location/date not in per diem table | Add per diem rate for location and date |
| "Workflow not configured" | Expense approval workflow missing | Set up expense report workflow |
| "Worker not found" | Employee not configured as expense user | Verify worker exists in HR |
| "Posting failed - account not found" | GL account missing for expense category | Configure expense posting accounts |
