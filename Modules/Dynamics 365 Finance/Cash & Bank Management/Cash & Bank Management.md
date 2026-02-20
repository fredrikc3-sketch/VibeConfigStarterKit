# Cash & Bank Management Module - Knowledge Source

> This file is the central knowledge hub for the **Cash & Bank Management** module within Dynamics 365 Finance.

---


---


> **Microsoft Learn Reference:** [Cash & Bank Management](https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/cash-bank-management)

## Module Overview

The Cash & Bank Management module in Dynamics 365 Finance manages bank accounts, bank transactions, bank reconciliation, and cash flow forecasting. It supports advanced bank reconciliation with matching rules, positive pay files, postdated checks, and letters of credit and guarantee for trade finance.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Bank Account Management** | Set up and manage bank accounts, bank groups, and bank transaction types |
| **Bank Reconciliation** | Reconcile bank statements with advanced matching rules and automation |
| **Cash Flow Forecasting** | Forecast cash positions using AI-powered predictions and manual entries |
| **Positive Pay** | Generate positive pay files for check fraud prevention |
| **Postdated Checks** | Manage checks with future dates for both receivables and payables |
| **Letters of Credit** | Create and manage letters of credit for international trade |
| **Letters of Guarantee** | Manage bank guarantee facilities and tracking |
| **Bank Statement Import** | Import electronic bank statements in various formats (MT940, BAI2, CAMT.053) |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 100 - Bank (`100 - Bank.json`)

Cash and bank management configuration entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Bank groups | BankGroupEntity | Bank - Setup | 30 |
| 10 | Bank transaction types | BankTransactionTypeEntity | Bank - Setup | 30 |
| 10 | Bank facility groups | BankFacilityGroupEntity | Bank - Setup | 30 |
| 10 | Bank facility types | BankFacilityTypeEntity | Bank - Setup | 30 |
| 10 | Bank transaction groups | BankTransactionGroupEntity | Bank - Setup | 30 |
| 10 | Customer charge groups | CustChargeGroupEntity | Bank - Shared | 30 |
| 10 | Payment purpose codes | PaymentPurposeCodeEntity | Bank - Setup | 30 |
| 20 | Bank accounts | BankAccountEntity | Bank - Accounts | 40 |
| 20 | Reconciliation matching rules | BankReconciliationMatchingRuleEntity | Bank - Reconciliation | 40 |
| 20 | Reconciliation matching rule sets | BankReconciliationMatchingRuleSetEntity | Bank - Reconciliation | 40 |
| 20 | Transaction code mapping | BankTransactionCodeMappingEntity | Bank - Reconciliation | 40 |
| 30 | Check layout | BankCheckLayoutEntity | Bank - Setup | 50 |
| 30 | Bank statement import | BankStatementImportEntity | Bank - Reconciliation | 50 |
| 40 | Bank posting profiles | BankPostingProfileEntity | Bank - Parameters | 60 |
| 50 | Bank parameters | BankParametersEntity | Bank - Parameters | 150 |

**DMF Load Order Notes:**
- **Seq 10** contains foundational lookup data — bank groups, transaction types, facility types, charge groups
- **Seq 20** contains bank accounts and reconciliation rules — depends on bank groups from Seq 10
- **Seq 30** contains check layout and statement import — depends on bank accounts from Seq 20
- **Seq 40** contains posting profiles — maps bank transactions to GL accounts
- **Seq 50** contains bank parameters — loaded last as it references all other setup

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Lookup/attribute entities (bank groups, transaction types)
- **Level 40:** Bank accounts, reconciliation rules
- **Level 50:** Check layouts, statement imports
- **Level 60:** Posting profiles
- **Level 150:** Module parameters (loaded last)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Cash & Bank Management** module.

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

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Bank groups | `BankGroupEntity` | `BankGroups` | verified |
| Bank transaction types | `BankTransactionTypeEntity` | `BankTransactionTypes` | verified |
| Bank transaction groups | `BankTransactionGroupEntity` | `BankTransactionGroups` | verified |
| Payment purpose codes | `PaymentPurposeCodeEntity` | `PaymentPurposeCodes` | auto-exact |
| Bank accounts | `BankAccountEntity` | `BankAccounts` | verified |
| Check layout | `BankCheckLayoutEntity` | `BankCheckLayouts` | auto-exact |
| Bank parameters | `BankParametersEntity` | `BankParameters` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Bank facility groups | `BankFacilityGroupEntity` |
| Bank facility types | `BankFacilityTypeEntity` |
| Customer charge groups | `CustChargeGroupEntity` |
| Reconciliation matching rules | `BankReconciliationMatchingRuleEntity` |
| Reconciliation matching rule sets | `BankReconciliationMatchingRuleSetEntity` |
| Transaction code mapping | `BankTransactionCodeMappingEntity` |
| Bank statement import | `BankStatementImportEntity` |
| Bank posting profiles | `BankPostingProfileEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Cash & Bank Management:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Cash & Bank Management-related business process areas:
- **Record to Report** (bank reconciliation, cash position management)
- **Bank reconciliation** (manual and advanced bank reconciliation)
- **Cash flow forecasting** (cash flow projections and analysis)
- **Payment processing** (check printing, electronic payments, positive pay)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure cash and bank management in Dynamics 365 Finance** | https://learn.microsoft.com/en-us/training/modules/configure-cash-bank-management-dyn365-finance/ |
| Understand bank transaction types and groups | https://learn.microsoft.com/en-us/training/modules/configure-cash-bank-management-dyn365-finance/2-types-groups |
| Set up cash and bank management parameters | https://learn.microsoft.com/en-us/training/modules/configure-cash-bank-management-dyn365-finance/3-parameters |
| Configure banks and bank check layout | https://learn.microsoft.com/en-us/training/modules/configure-cash-bank-management-dyn365-finance/6-check-layout |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Cash and bank management home page | https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/cash-bank-management |
| Advanced bank reconciliation overview | https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/advanced-bank-reconciliation-overview |
| Configure advanced bank reconciliation | https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/configure-advanced-bank-reconciliation |
| Set up advanced bank reconciliation import | https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/set-up-advanced-bank-reconciliation-import-process |
| Bank reconciliation matching rules | https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/set-up-bank-reconciliation-matching-rules |
| Cash flow forecasting | https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/cash-flow-forecasting |
| Positive pay overview | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/positive-pay-overview |
| Bank statement import using Electronic reporting | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/import-bai2-er |
| Foreign currency revaluation for AP and AR | https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/foreign-currency-revaluation-accounts-payable-accounts-receivable |
| Letters of credit and import collections | https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/letters-of-credit-import-collections |
| Letters of guarantee | https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/letters-of-guarantee |
| Cash application in advanced bank reconciliation | https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/apply-cash-adv-bank-rec |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites (GL & Organization)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Main accounts | General ledger > Chart of accounts > Accounts > Main accounts | Bank-related GL accounts |
| Currencies | General ledger > Currencies > Currencies | Bank account currencies |
| Number sequences | Organization administration > Number sequences | Reconciliation ID, statement ID |
| Financial dimensions | General ledger > Chart of accounts > Dimensions | Bank-related dimensions |

### Phase 2: Bank Foundation Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| BankGroup | Cash and bank management > Setup > Bank groups | Bank institution grouping |
| BankTransactionType | Cash and bank management > Setup > Bank transaction types | Transaction classification |
| BankTransactionGroup | Cash and bank management > Setup > Bank transaction groups | Transaction grouping |
| BankFacilityGroup | Cash and bank management > Setup > Bank facility groups | Credit facility groups |
| BankFacilityType | Cash and bank management > Setup > Bank facility types | Credit facility types |
| PaymentPurposeCode | Cash and bank management > Setup > Payment purpose codes | Purpose codes for payments |

### Phase 3: Bank Accounts

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| BankAccountTable | Cash and bank management > Bank accounts > Bank accounts | Bank account master records |
| BankCheckLayout | (Within bank account) | Check printing format |
| BankStatementFormat | Cash and bank management > Setup > Advanced bank reconciliation setup > Bank statement format | Statement import format |

### Phase 4: Reconciliation Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| BankReconciliationMatchingRule | Cash and bank management > Setup > Advanced bank reconciliation setup > Reconciliation matching rules | Auto-matching rules |
| BankReconciliationMatchingRuleSet | Cash and bank management > Setup > Advanced bank reconciliation setup > Reconciliation matching rule sets | Rule set grouping |
| BankTransactionCodeMapping | Cash and bank management > Setup > Bank transaction code mapping | Statement code to transaction type mapping |

### Phase 5: Posting Profiles & Parameters

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| BankPostingProfile | Cash and bank management > Setup > Bank posting profiles | GL account mapping per bank |
| BankParameters | Cash and bank management > Setup > Cash and bank management parameters | Module parameters |

---

## Bank Reconciliation Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  ADVANCED BANK RECONCILIATION FLOW                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. IMPORT BANK STATEMENT                                                │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Import via BAI2, MT940, ISO20022 format                │          │
│     │ • Electronic reporting (ER) format configuration         │          │
│     │ • Statement lines created automatically                  │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  2. AUTOMATIC MATCHING                                                   │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Run matching rules against bank transactions           │          │
│     │ • Match by amount, date, reference, check number         │          │
│     │ • One-to-one and one-to-many matching                    │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  3. MANUAL MATCHING                                                      │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Review unmatched transactions                          │          │
│     │ • Manual match statement lines to bank transactions      │          │
│     │ • Generate payment journals for new items                │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  4. RECONCILIATION                                                       │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Review reconciliation worksheet                        │          │
│     │ • Validate ending balance                                │          │
│     │ • Post reconciliation                                    │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `BankParameters` | Cash and bank management parameters | Setup |
| `BankGroup` | Bank groups | Setup |
| `BankTransactionType` | Bank transaction types | Setup |
| `BankAccountTable` | Bank accounts | Accounts |
| `BankReconciliationMatchingRules` | Reconciliation matching rules | Reconciliation |
| `BankReconciliationMatchingRuleSets` | Reconciliation matching rule sets | Reconciliation |
| `BankStatementFormat` | Bank statement format | Reconciliation |
| `BankReconciliationWorksheet` | Bank reconciliation | Reconciliation |
| `BankStatements` | Bank statements | Statements |
| `BankCheckLayout` | Check layout | Setup |
| `CashFlowForecast` | Cash flow forecasts | Analysis |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **GL accounts** must exist before creating bank accounts (main account for bank balance)
2. **Bank groups** should be set up before bank accounts
3. **Bank transaction types** define how transactions post — required before bank processing
4. **Bank accounts** must exist before AP/AR payment methods reference them
5. **Advanced bank reconciliation** must be enabled per bank account before using reconciliation worksheets
6. **Matching rules** should be defined before running automatic reconciliation
7. **Bank statement format** must be configured before importing statements
8. **Posting profiles** must be set up before bank transactions post to GL

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Bank account not found" | Bank account not created or wrong company | Create bank account in correct legal entity |
| "Statement import failed" | Format mismatch or invalid file | Verify bank statement format configuration |
| "Reconciliation out of balance" | Unmatched items or incorrect ending balance | Review unmatched transactions |
| "Advanced bank reconciliation not enabled" | Feature not turned on for bank account | Enable on bank account Reconciliation tab |
| "Transaction type not configured" | Bank transaction type missing | Add bank transaction types |
| "Check number already used" | Duplicate check number | Verify check number sequence |
