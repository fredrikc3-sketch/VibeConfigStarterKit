# General Ledger Module - Knowledge Source

> This file is the central knowledge hub for the **General Ledger** module within Dynamics 365 Finance.

---


---


> **Microsoft Learn Reference:** [General Ledger](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-ledger)

## Module Overview

The General Ledger module is the heart of financial management in Dynamics 365 Finance. It provides the chart of accounts, financial dimensions, account structures, journal processing, period-end closing, financial consolidations, currency revaluations, and intercompany accounting. All other financial modules post their transactions into the General Ledger.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Chart of Accounts** | Define main accounts, account categories, and account structures |
| **Financial Dimensions** | Create and manage dimensions for detailed financial tracking and reporting |
| **Journal Processing** | Enter, approve, and post general journal entries with voucher templates |
| **Period Close & Year-End** | Perform period closings, year-end close, and opening transactions |
| **Financial Consolidations** | Consolidate multiple legal entities for group reporting |
| **Currency Revaluation** | Revalue foreign currency balances for reporting accuracy |
| **Intercompany Accounting** | Process and settle intercompany transactions between legal entities |
| **Ledger Allocations** | Distribute amounts across accounts using fixed or variable allocation rules |
| **Financial Reporting** | Generate balance sheets, income statements, and custom financial reports |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template files define the data entities required for migrating and configuring this module:

#### 020 - GL Shared (`020 - GL Shared.json`)

Shared configuration entities loaded before per-company GL setup.

| Seq | Entity Name | Target Entity | Category |
|-----|-------------|---------------|----------|
| 10 | Chart of accounts | LedgerChartOfAccountsEntity | GL - COA shared |
| 10 | Financial dimensions | DimensionAttributeEntity | GL - COA shared |
| 10 | Fiscal calendar | FiscalYearEntity | GL - Fiscal calendar shared |
| 10 | Main account categories | MainAccountCategoryEntity | GL - COA shared |
| 20 | Dimension attribute activation | DimensionAttributeActivationEntity | GL - COA shared |
| 20 | Financial dimension format | DimensionIntegrationFormatEntity | GL - COA shared |
| 20 | Financial dimension translations | DimensionAttributeTranslationEntity | GL - COA shared |
| 20 | Fiscal calendar period | FiscalPeriodEntity | GL - Fiscal calendar shared |
| 20 | Main account | MainAccountEntity | GL - COA shared |
| 30 | Advanced rule structures active group | LedgerAdvancedRuleStructureActiveOnlyGroupEntity | |
| 30 | Consolidation groups and accounts | LedgerConsolidateAccountGroupEntity | GL - COA shared |
| 30 | Financial dimension sets | FinancialDimensionSetEntity | GL - COA shared |
| 30 | Financial dimension value translations | FinancialDimensionValueTranslationEntity | GL - COA shared |
| 30 | Financial dimension values | FinancialDimensionValueEntity | GL - COA shared |
| 40 | Account structures active group | LedgerAccountStructureActiveOnlyGroupEntity | |
| 40 | Number sequence code | NumberSequenceTableEntity | SYS - Number sequences |
| 50 | Number sequence group | NumberSequenceGroupEntity | SYS - Number sequences |
| 50 | Number sequence references | NumberSequencesReferenceEntity | SYS - Number sequences |

#### 025 - General Ledger (`025 - General ledger.json`)

Per-company GL configuration entities.

| Seq | Entity Name | Target Entity | Category |
|-----|-------------|---------------|----------|
| 10 | Calendar | WorkCalendarEntity | SYS - Organization calendar |
| 10 | Date intervals | LedgerDateIntervalEntity | GL - Ledger setup |
| 10 | Default descriptions | LedgerDefaultDescriptionsEntity | GL - Ledger journals |
| 10 | Dimension parameters | DimensionParametersEntity | |
| 10 | Financial reasons | LedgerFinancialReasonEntity | GL - Ledger journals |
| 10 | Journal descriptions | LedgerJournalDescriptionsEntity | GL - Ledger journals |
| 10 | Ledger | LedgerEntity | GL - Ledger setup |
| 10 | Document types | DocuTypeEntity | |
| 10 | Organization email template | EmailTemplateOrganizationEntity | |
| 15 | Ledger parameters | LedgerParametersEntity | GL - Ledger setup |
| 18 | Subledger journal transfer rule | SubledgerJournalTransferRuleEntity | |
| 20 | Organization email template message | EmailTemplateMessageOrganizationEntity | |
| 20 | Ledger fiscal calendar year | LedgerFiscalYearEntity | GL - Ledger setup |
| 20 | Journal names | LedgerJournalNameEntity | GL - Ledger journals |
| 20 | Ledger account alias | DimensionAliasEntity | |
| 20 | Balance control accounts | LedgerBalanceControlEntity | |
| 20 | Working times | WorkCalendarDayEntity | SYS - Organization calendar |
| 25 | Ledger fiscal calendar period | LedgerFiscalPeriodEntity | GL - Ledger setup |
| 30 | Main account legal entity overrides | MainAccountLegalEntityOverrideEntity | |
| 30 | Financial dimension value legal entity overrides | FinancialDimensionValueLegalEntityOverrideEntity | GL - Ledger setup |
| 30 | Workflow organization parameters | WorkflowParametersOrganizationEntity | |
| 40 | Accounts for automatic transactions | LedgerAutomaticTransactionAccountEntity | GL - Ledger setup |
| 50 | Ledger allocation rule | LedgerAllocationRuleEntity | GL - Allocations |
| 52 | Ledger allocation basis | LedgerAllocationBasisRuleEntity | GL - Allocations |
| 54 | Ledger allocation basis source | LedgerAllocationBasisRuleSourceEntity | GL - Allocations |
| 56 | Ledger allocation rule destination | LedgerAllocationRuleDestinationEntity | GL - Allocations |
| 58 | Ledger allocation rule source | LedgerAllocationRuleSourceEntity | GL - Allocations |


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **General Ledger** module.

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
| Chart of accounts | `LedgerChartOfAccountsEntity` | `ChartOfAccounts` | verified |
| Financial dimensions | `DimensionAttributeEntity` | `DimensionAttributes` | verified |
| Fiscal calendar | `FiscalYearEntity` | `FiscalYears` | verified |
| Main account categories | `MainAccountCategoryEntity` | `MainAccountCategories` | verified |
| Dimension attribute activation | `DimensionAttributeActivationEntity` | `DimensionAttributeActivations` | verified |
| Financial dimension format | `DimensionIntegrationFormatEntity` | `DimensionIntegrationFormats` | verified |
| Financial dimension translations | `DimensionAttributeTranslationEntity` | `DimensionAttributeTranslations` | verified |
| Fiscal calendar period | `FiscalPeriodEntity` | `FiscalPeriods` | verified |
| Main account | `MainAccountEntity` | `MainAccounts` | verified |
| Consolidation groups and accounts | `LedgerConsolidateAccountGroupEntity` | `LedgerConsolidateAccountGroups` | manual-unverified |
| Financial dimension sets | `FinancialDimensionSetEntity` | `FinancialDimensionSets` | verified |
| Financial dimension value translations | `FinancialDimensionValueTranslationEntity` | `FinancialDimensionValueTranslations` | verified |
| Financial dimension values | `FinancialDimensionValueEntity` | `FinancialDimensionValues` | verified |
| Number sequence references | `NumberSequencesReferenceEntity` | `NumberSequencesReferences` | verified |
| Calendar | `WorkCalendarEntity` | `WorkCalendars` | verified |
| Date intervals | `LedgerDateIntervalEntity` | `LedgerDateIntervals` | manual-unverified |
| Default descriptions | `LedgerDefaultDescriptionsEntity` | `LedgerJournalDescriptions` | verified |
| Dimension parameters | `DimensionParametersEntity` | `DimensionParameters` | verified |
| Financial reasons | `LedgerFinancialReasonEntity` | `LedgerFinancialReasons` | verified |
| Journal descriptions | `LedgerJournalDescriptionsEntity` | `LedgerJournalDescriptions` | verified |
| Ledger | `LedgerEntity` | `Ledgers` | verified |
| Document types | `DocuTypeEntity` | `DocumentTypes` | verified |
| Ledger parameters | `LedgerParametersEntity` | `LedgerParameters` | manual-unverified |
| Ledger fiscal calendar year | `LedgerFiscalYearEntity` | `LedgerFiscalYears` | manual-unverified |
| Journal names | `LedgerJournalNameEntity` | `JournalNames` | verified |
| Ledger account alias | `DimensionAliasEntity` | `DimensionAliases` | manual-unverified |
| Balance control accounts | `LedgerBalanceControlEntity` | `BalanceControls` | verified |
| Working times | `WorkCalendarDayEntity` | `WorkCalendarDays` | verified |
| Ledger fiscal calendar period | `LedgerFiscalPeriodEntity` | `LedgerFiscalPeriodsV2` | verified |
| Main account legal entity overrides | `MainAccountLegalEntityOverrideEntity` | `MainAccountLegalEntities` | verified |
| Financial dimension value legal entity overrides | `FinancialDimensionValueLegalEntityOverrideEntity` | `FinancialDimensionValueLegalEntityOverridesV2` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Advanced rule structures active group | `LedgerAdvancedRuleStructureActiveOnlyGroupEntity` |
| Account structures active group | `LedgerAccountStructureActiveOnlyGroupEntity` |
| Number sequence code | `NumberSequenceTableEntity` |
| Number sequence group | `NumberSequenceGroupEntity` |
| Organization email template | `EmailTemplateOrganizationEntity` |
| Subledger journal transfer rule | `SubledgerJournalTransferRuleEntity` |
| Organization email template message | `EmailTemplateMessageOrganizationEntity` |
| Workflow organization parameters | `WorkflowParametersOrganizationEntity` |
| Accounts for automatic transactions | `LedgerAutomaticTransactionAccountEntity` |
| Ledger allocation rule | `LedgerAllocationRuleEntity` |
| Ledger allocation basis | `LedgerAllocationBasisRuleEntity` |
| Ledger allocation basis source | `LedgerAllocationBasisRuleSourceEntity` |
| Ledger allocation rule destination | `LedgerAllocationRuleDestinationEntity` |
| Ledger allocation rule source | `LedgerAllocationRuleSourceEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to General Ledger operations including Record to Report, period close, and financial reporting:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (CSV):** `../../../Business Process/ProcessCatalogue.csv`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key GL-related business process areas in the catalogue:
- Record to Report (end-to-end)
- Period close and year-end close
- Financial consolidation and reporting
- Intercompany accounting
- Fixed asset subledger reconciliation to GL

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and use the general ledger** | https://learn.microsoft.com/en-us/training/paths/configure-use-general-ledger-dyn365-finance/ |
| Get started with Dynamics 365 Finance | https://learn.microsoft.com/en-us/training/modules/get-started-financial-management-dyn365-finance/ |
| Configure currencies | https://learn.microsoft.com/en-us/training/modules/configure-currencies-dyn365-finance/ |
| Create fiscal calendars, years, and periods | https://learn.microsoft.com/en-us/training/modules/create-fiscal-calendars-years-periods-dyn365-finance/ |
| Get started with chart of accounts | https://learn.microsoft.com/en-us/training/modules/get-started-chart-accounts-finance/ |
| Set up chart of accounts | https://learn.microsoft.com/en-us/training/modules/set-up-chart-accounts-finance/ |
| Set up financial dimensions | https://learn.microsoft.com/en-us/training/modules/set-up-financial-dimensions-finance/ |
| Set up ledgers and journals | https://learn.microsoft.com/en-us/training/modules/configure-ledgers-journals-dyn365-finance/ |
| Perform general ledger daily procedures | https://learn.microsoft.com/en-us/training/modules/general-ledger-daily-procedures-dyn365-finance/ |
| Intercompany accounting | https://learn.microsoft.com/en-us/training/modules/intercompany-accounting-dyn365-finance/ |
| Configure ledger allocations and accruals | https://learn.microsoft.com/en-us/training/modules/configure-ledger-allocations-accruals-dyn365-finance/ |
| Configure and perform periodic processes | https://learn.microsoft.com/en-us/training/modules/configure-periodic-processes-dyn365-finance/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Configure ledgers | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/configure-ledger |
| Year-end close | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/year-end-close |
| Financial dimensions | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-dimensions |
| Plan the chart of accounts | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/plan-chart-of-accounts |

---

## 8-Phase Configuration Sequence

### Phase 1: Legal Entity Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| CompanyInfo | Organization administration > Organizations > Legal entities | Legal entity master |
| OMOperatingUnit | Organization administration > Organizations > Operating units | Departments, cost centers |
| OMHierarchyType | Organization administration > Organizations > Organization hierarchies | Hierarchy types |
| DirPartyTable | Organization administration > Global address book | Party records |
| NumberSequenceTable | Organization administration > Number sequences | Voucher numbering |

**🔍 Number Sequence Country-Specific Requirements:**

**Denmark (and potentially other countries):** Certain number sequences MUST be configured as **Continuous = Yes** due to legal/tax requirements. This is critical for:
- General journal transfer numbers (Gene_XXX reference)
- Financial voucher sequences
- Invoice numbering

**Discovery:** When posting product receipts in Denmark, the system failed with error:
> "The General journal transfer number must be defined as Continuous for Danish legal entities"

**Resolution:**
1. Navigate to: Organization administration > Number sequences > Number sequences
2. Filter for the specific number sequence code (e.g., Gene_815)
3. Set **Continuous = Yes**
4. Important: Continuous number sequences have performance implications - use only when legally required

**Best Practice:** When configuring legal entities for Denmark, Norway, Sweden, or other countries with strict document numbering requirements, always verify continuous number sequence requirements with local tax regulations.

### Phase 2: Fiscal Calendar

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| FiscalCalendar | General ledger > Ledger setup > Fiscal calendars | Calendar definition |
| FiscalCalendarYear | (Within fiscal calendar) | Fiscal year periods |
| FiscalCalendarPeriod | (Within fiscal calendar) | Monthly/quarterly periods |
| LedgerFiscalCalendar | General ledger > Ledger setup > Ledger calendar | Period status control |

### Phase 3: Currency Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| Currency | General ledger > Currencies > Currencies | Currency codes |
| ExchangeRateType | General ledger > Currencies > Exchange rate types | Rate type classification |
| ExchangeRate | General ledger > Currencies > Currency exchange rates | Daily/periodic rates |
| ExchangeRateCurrencyPair | (Within exchange rates) | Currency pair setup |
| LedgerExchAdjPosting | General ledger > Currencies > Currency revaluation accounts | Gain/loss accounts |
| ExchangeRateProviderConfiguration | General ledger > Currencies > Configure exchange rate providers | Automated rate import |

### Phase 4: Chart of Accounts

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| LedgerChartOfAccounts | General ledger > Chart of accounts > Chart of accounts | CoA container |
| MainAccount | General ledger > Chart of accounts > Accounts > Main accounts | GL accounts |
| MainAccountCategory | General ledger > Chart of accounts > Accounts > Main account categories | Account groupings |
| MainAccountTemplate | General ledger > Chart of accounts > Accounts > Main account templates | Account templates |
| MainAccountLegalEntity | (Within main account) | Per-company overrides |
| LedgerConsolidateAccountGroup | General ledger > Chart of accounts > Accounts > Consolidation account groups | Consolidation mapping |

### Phase 5: Financial Dimensions

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| DimensionAttribute | General ledger > Chart of accounts > Dimensions > Financial dimensions | Dimension definition |
| DimensionAttributeValue | (Within dimension) | Dimension values |
| DimensionHierarchy | General ledger > Chart of accounts > Structures > Configure account structures | Account structures |
| DimensionRule | General ledger > Chart of accounts > Structures > Advanced rule structures | Conditional rules |
| DimensionFocus | General ledger > Chart of accounts > Dimensions > Financial dimension sets | Reporting sets |
| FinancialDimensionDefaultTemplate | General ledger > Chart of accounts > Dimensions > Financial dimension default templates | Default combinations |

### Phase 6: Ledger Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| Ledger | General ledger > Ledger setup > Ledger | Ledger configuration |
| LedgerParameters | General ledger > Ledger setup > General ledger parameters | GL parameters |
| LedgerAccountAlias | General ledger > Chart of accounts > Accounts > Ledger account alias | Account shortcuts |
| LedgerBalanceControlAccounts | General ledger > Chart of accounts > Accounts > Balance control accounts | Mandatory balancing |
| JournalizingDefinition | General ledger > Posting setup > Posting definitions | Posting rules |
| TransactionTextLedger | General ledger > Ledger setup > Default descriptions | Auto descriptions |
| LedgerSystemAccounts | General ledger > Posting setup > Accounts for automatic transactions | System accounts |

### Phase 7: Journal Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| LedgerJournalName | General ledger > Journal setup > Journal names | Journal templates |
| LedgerJournalTable | General ledger > Journal entries > General journals | Journal batches |
| LedgerJournalTrans | (Within journal) | Journal lines |
| LedgerAllocationRule | General ledger > Allocations > Ledger allocation rules | Allocation rules |
| LedgerAllocationBasis | General ledger > Allocations > Ledger allocation basis | Allocation basis |

### Phase 8: Advanced & Closing

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| LedgerFiscalCloseGroup | General ledger > Period close > Year-end close > Year-end close template setup | Close templates |
| LedgerClosingTable | General ledger > Period close > Year-end close | Year-end close |
| LedgerPeriodCloseProject | General ledger > Period close > Financial period close workspace | Period close tasks |
| LedgerConsolidationConfig | General ledger > Consolidations > Consolidation | Consolidation setup |
| IntercompanyAccounts | General ledger > Intercompany accounting setup | Intercompany setup |
| LedgerEliminationRule | General ledger > Consolidations > Elimination rules | Elimination rules |
| FinancialReportingSetup | General ledger > Inquiries and reports > Financial reports | Financial reporting |

---

## ⚠️ Critical Implementation Discoveries

### Intercompany GL Account Setup
**Discovery from Swedish Implementation:****
Intercompany transactions require dedicated GL accounts distinct from regular AP/AR for proper elimination and tracking.

**Required IC Account Pairs:**

| Purpose | Sweden Account | Norway Account | Relationship |
|---------|---|---|---|
| **IC Receivable** | 1513 (AR koncern) | 2443 (AP koncern) | What Norway owes Sweden |
| **IC Payable** | 2443 (AP koncern) | 1513 (AR koncern) | What Sweden owes Norway |
| **Revenue Elimination** | 3300 (IC Revenue) | 3300 (IC Revenue) | IC sales offset |
| **COGS Elimination** | 4011 (COGS finished goods) | 4010 (COGS parts) | Different per company |

**Critical Configuration:**
GL account pairs must be configured in:
1. **GL Chart of Accounts** (accounts 1513, 2443 created and defined)
2. **Intercompany Parameters** (accounts linked as IC pairs)
3. **Vendor/Customer Posting Profiles** (IC profiles → IC accounts)
4. **Journal Setup** (Dedicated journals: e.g., SWE-IC, NOR-IC)

**Why Separate Accounts Matter:**
- ✅ Eliminates properly in consolidated statements
- ✅ Tracks IC flow separately from external transactions
- ✅ Validates IC relationships during posting
- ✅ Simplifies reconciliation between companies
- ❌ Regular AP/AR accounts miss IC elimination requirement

### Chart of Accounts Dimension Strategy
**Discovery from Swedish Implementation:**
Swedish BAS-SE chart contains 120 accounts. Key planning consideration: use chart for **transaction categories**, dimensions for **operational detail**.

**Account Structure by Type (Swedish Example):**
- **1000-1900:** Assets (inventory 1450, AR 1510, IC AR 1513, cash 1910-1950)
- **2000-2900:** Liabilities & Equity (AP 2440, IC AP 2443, VAT 2610-2640, equity 2081)
- **3000-3900:** Revenue (product 3010-3011, IC 3300, export 3400, other 3510-3990)
- **4000-4900:** COGS (purchases 4010-4011, freight 4510-4520, adjustments 4990)
- **5000-7900:** Expenses (admin 5000s, payroll 7000s, depreciation 7800s)
- **8000-8999:** Finance & Tax (interest 8100s, dividends 8200s, income tax 8910)

**Best Practice - Use Dimensions for Location/Department:**
- ❌ DON'T create separate revenue accounts per site (3010-SWE-MAIN, 3010-SWE-DIST)
- ✅ DO create dimension values (DEPT: SWE-MAIN, SWE-DIST) and use on GL entries
- **Result:** Single 3010 account with site dimension tagged → cleaner chart, simpler reporting

**Swedish Implementation:** Used 3010 vs 3011 for **product type** (accessories vs finished goods), SiteWH dimension for **location tracking**. This kept chart manageable at 120 accounts while allowing multi-site reporting.

---

## Main Account Types

| Type | Description | Balance Treatment |
|------|-------------|-------------------|
| **Balance sheet** | Assets, Liabilities, Equity | Carries forward to next year |
| **Profit and loss** | Revenue, Expenses | Closes to retained earnings |
| **Total** | Aggregation for reporting | No posting allowed |
| **Reporting** | Financial reporting only | No posting allowed |
| **Blank** | Not specified | No posting allowed |

### Main Account Categories

| Category | Type | Examples |
|----------|------|----------|
| Cash | Balance sheet | Bank accounts, petty cash |
| Accounts Receivable | Balance sheet | Trade AR, other receivables |
| Inventory | Balance sheet | Raw materials, WIP, finished goods |
| Fixed Assets | Balance sheet | Land, buildings, equipment |
| Accounts Payable | Balance sheet | Trade AP, accrued liabilities |
| Equity | Balance sheet | Common stock, retained earnings |
| Revenue | Profit and loss | Sales, service revenue |
| Cost of Goods Sold | Profit and loss | Direct materials, direct labor |
| Operating Expenses | Profit and loss | SG&A, depreciation |

---

## Financial Dimensions

### System-Backed Dimensions

| Dimension | Backed By | Use Case |
|-----------|-----------|----------|
| **BusinessUnit** | Operating Units | Divisional reporting |
| **Department** | Operating Units | Departmental expense tracking |
| **CostCenter** | Operating Units | Cost allocation |
| **Project** | Projects | Project accounting |
| **Customer** | Customer master | Customer-level analysis |
| **Vendor** | Vendor master | Vendor-level analysis |
| **Worker** | Worker master | Employee expense tracking |
| **Item** | Item master | Item-level costing |

### Custom Dimensions

User-defined dimensions without system backing:
- Campaign
- Region
- Product Line
- Grant
- Fund

---

## Account Structure Design

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         ACCOUNT STRUCTURE DESIGN                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   ┌────────────────┐   ┌────────────────┐   ┌────────────────┐             │
│   │  MAIN ACCOUNT  │ - │  BUSINESS UNIT │ - │  DEPARTMENT    │             │
│   │    (Required)  │   │   (Required)   │   │   (Required)   │             │
│   └────────────────┘   └────────────────┘   └────────────────┘             │
│          │                    │                    │                        │
│          ▼                    ▼                    ▼                        │
│   ┌────────────────┐   ┌────────────────┐   ┌────────────────┐             │
│   │   110000-      │   │   001-099      │   │   100-999      │             │
│   │   999999       │   │                │   │                │             │
│   └────────────────┘   └────────────────┘   └────────────────┘             │
│                                                                          │
│   ADVANCED RULES (Optional)                                                  │
│   ┌──────────────────────────────────────────────────────────┐              │
│   │ IF MainAccount = 6xxxxx (Expense)                        │              │
│   │ THEN CostCenter is REQUIRED                              │              │
│   └──────────────────────────────────────────────────────────┘              │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Ledger Configuration Components

### Ledger Setup (Per Legal Entity)

| Component | Description | Shared? |
|-----------|-------------|---------|
| **Chart of Accounts** | Main account list | Yes - can share |
| **Fiscal Calendar** | Year/period definition | Yes - can share |
| **Accounting Currency** | Primary reporting currency | No - per entity |
| **Reporting Currency** | Secondary currency (optional) | No - per entity |
| **Exchange Rate Type** | Default rate type | No - per entity |
| **Account Structures** | Dimension combinations | Yes - can share |
| **Balancing Dimension** | Interunit balancing | No - per entity |

---

## Journal Types

| Journal Type | Use Case | Menu Item Name |
|--------------|----------|----------------|
| **General journal** | Standard GL entries | `LedgerJournalTable3` |
| **Daily journal** | Recurring entries | `LedgerJournalTableDailyGlobal` |
| **Allocation journal** | Cost allocations | `LedgerJournalTable3` |
| **Elimination journal** | Consolidation eliminations | `LedgerJournalTable3` |
| **Intercompany journal** | Cross-company entries | `LedgerJournalTable3` |
| **Periodic journal** | Recurring templates | `LedgerJournalTable3` |

### Voucher Allocation Options

| Option | Behavior |
|--------|----------|
| **One voucher number only** | All lines share one voucher |
| **One voucher number per entry** | New voucher each line |
| **Automatic voucher** | System assigns vouchers |
| **Manual voucher** | User enters voucher |

---

## Year-End Close Process

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           YEAR-END CLOSE FLOW                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. PREPARATION                                                              │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ ✓ Post all transactions for the fiscal year               │
│     │ ✓ Run foreign currency revaluations                       │
│     │ ✓ Complete period close checklists                        │
│     │ ✓ Verify main account types (P&L vs Balance Sheet)        │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  2. YEAR-END CLOSE TEMPLATE                                                  │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Select legal entities                                    │
│     │ • Define retained earnings account                         │
│     │ • Configure dimension transfer (Close All / Close Single) │
│     │ • Set balance sheet dimension transfer                     │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  3. EXECUTION                                                                │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ P&L Accounts ──▶ Close to Retained Earnings               │
│     │ Balance Sheet ──▶ Carry Forward Opening Balances          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  4. VERIFICATION                                                             │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Verify opening balances in new year                      │
│     │ • Confirm retained earnings balance                        │
│     │ • Close prior year periods (set to On Hold)               │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Year-End Close Dimension Options

| Option | Behavior | Use When |
|--------|----------|----------|
| **Close All** | Maintains detailed dimensions in retained earnings | Need dimension-level retained earnings analysis |
| **Close Single** | Summarizes to single dimension value | Want simplified retained earnings |
| **Transfer balance sheet dimensions** | Carries dimensions to opening balances | Need full dimension continuity |

---

## FY27 Environment - Validated Menu Items

*Verified against FY27 environment (USMF) - February 2026*

### Core Setup Forms

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `LedgerParameters` | General ledger parameters | GL Setup |
| `FiscalCalendars` | Fiscal calendars | Calendar |
| `MainAccountDetails` | Main accounts | CoA |
| `MainAccountCategory` | Main account categories | CoA |
| `DimensionDetails` | Financial dimensions | Dimensions |
| `DimensionFocusTable` | Financial dimension sets | Dimensions |
| `DimensionConfigureAccountStructure` | Configure account structures | Structures |
| `DimensionConfigureAccountRuleStructure` | Advanced rule structures | Structures |

### Currency & Exchange

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `ExchangeRate` | Currency exchange rates | Currency |
| `ExchangeRateType` | Exchange rate types | Currency |
| `ExchangeRateProviderConfiguration` | Configure exchange rate providers | Currency |
| `CurrencyLedgerGainLossAccount` | Currency revaluation accounts | Currency |
| `LedgerExchAdjPosting` | Currency revaluation posting profile | Currency |

### Journals & Posting

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `LedgerJournalSetup` | Journal names | Journals |
| `LedgerJournalTable3` | General journals | Journals |
| `LedgerJournalTableDailyGlobal` | Global general journals | Journals |
| `GeneralJournalEntryWorkspace` | General journal processing | Workspace |
| `JournalizingDefinition` | Posting definitions | Posting |
| `LedgerAllocationRule` | Ledger allocation rules | Allocations |
| `LedgerAllocationBasisRule` | Ledger allocation basis | Allocations |

### Period Close & Reporting

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `LedgerTransferOpening` | Year end close | Closing |
| `LedgerFiscalCloseGroup` | Year-end close template setup | Closing |
| `LedgerPeriodCloseProjectWorkspace` | Financial period close | Workspace |
| `LedgerPeriodCloseConfiguration` | Financial period close configuration | Closing |
| `FinancialReportingSetup` | Financial reporting setup | Reporting |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Legal Entity** must exist before ledger configuration
2. **Fiscal Calendar** must be created before ledger setup
3. **Currencies** must be defined before ledger assignment
4. **Chart of Accounts** must exist before main account creation
5. **Financial Dimensions** must be created before account structures
6. **Account Structures** must be configured before ledger activation
7. **Ledger** must be configured before any GL transactions
8. **Journal Names** must exist before creating journals

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Account structure not valid" | Dimension combination invalid | Check account structure rules |
| "Period not open" | Fiscal period closed or on hold | Open period in Ledger calendar |
| "Voucher already used" | Duplicate voucher number | Check number sequence setup |
| "Currency not defined" | Missing exchange rate | Add exchange rate for date |
| "Main account not found" | Account doesn't exist | Create main account in CoA |
| "Dimension value not found" | Invalid dimension value | Add value to dimension |
| "Number must be defined as Continuous" (Denmark) | Danish legal entity requires continuous number sequences | Set Continuous = Yes on General journal transfer number sequence |
| "You must select a value in the [Dimension] field" | Account structure requires dimension value but posting profile or transaction has none | Update account structure to allow blank values (see below) |
| "Posting profile has not been set up" | AR/AP Parameters missing posting profile | Configure posting profile in module parameters |

### 🔧 Account Structure Dimension Validation

**Discovery (China Testing Feb 2026):** When invoice posting fails with "You must select a value in the [Dimension] field", this indicates the account structure dimension validation rules are too restrictive.

**Root Cause Analysis:**
1. Account structures define which dimension combinations are valid for posting
2. Each dimension segment can have allowed values configured:
   - `*` = All values allowed BUT blank is NOT allowed
   - `"";*` = Blank AND all values allowed
   - Specific range (e.g., `001..002`) = Only those values allowed
3. When posting profiles don't specify dimensions, the transaction will have blank dimension values
4. If the account structure doesn't allow blank for that dimension, posting fails

**Resolution Steps:**
1. Navigate to: General ledger > Chart of accounts > Structures > Configure account structures
2. Select the failing account structure (e.g., "Manufacturing China - B/S")
3. Click "Edit"
4. For each dimension segment (Level 1, Level 2, etc.):
   - If blank values should be allowed, change value from `*` to `"";*`
   - OR check "Blank values are allowed" checkbox
5. Click "Activate"
6. Wait for activation batch job to complete (check activation status)
7. Repeat for all related account structures (both B/S and P/L)

**Important:** Account structures must be activated after changes. The activation runs as a batch job and may take a few minutes.

**Best Practice:** When configuring new legal entities, especially with localized charts of accounts (Chinese GAAP, etc.):
- Review all account structure dimension segments
- Decide early whether dimensions are mandatory or optional for each account type
- Test posting early in implementation with minimal transactions

### ⚠️ Best Practices

```
┌────────────────────────────────────────────────────────────────┐
│                    CHART OF ACCOUNTS DESIGN                     │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ✓ Use consistent account numbering scheme                     │
│    • 1xxxxx = Assets                                           │
│    • 2xxxxx = Liabilities                                      │
│    • 3xxxxx = Equity                                           │
│    • 4xxxxx = Revenue                                          │
│    • 5xxxxx = Cost of Goods Sold                               │
│    • 6xxxxx = Operating Expenses                               │
│                                                                 │
│  ✓ Leave gaps for future accounts                              │
│  ✓ Use same CoA across legal entities when possible            │
│  ✓ Leverage legal entity overrides for exceptions              │
│  ✓ Keep dimension sets minimal for performance                 │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

---

## Data Migration Sequence

```
1. Legal Entities (CompanyInfo)
2. Organizational Hierarchies
3. Fiscal Calendars
4. Currencies & Exchange Rates
5. Chart of Accounts
6. Main Account Categories
7. Main Accounts
8. Financial Dimensions (with values)
9. Account Structures
10. Advanced Rules (if needed)
11. Ledger Setup
12. GL Parameters
13. Journal Names
14. Posting Definitions
15. Default Descriptions
16. Opening Balances (via journal)
```

---

## Related Modules

| Module | Relationship |
|--------|--------------|
| **Accounts Payable** | Posts to GL via posting profiles |
| **Accounts Receivable** | Posts to GL via posting profiles |
| **Inventory Management** | Posts inventory values to GL |
| **Fixed Assets** | Posts depreciation and disposals |
| **Project Accounting** | Posts project costs and revenue |
| **Budgeting** | Uses same CoA and dimensions |
| **Cost Accounting** | Alternative costing ledger |

---

## ⚠️ Additional Configuration Discoveries

### Journal Names - Create Before Testing

**Best Practice:** Create all required journal names during initial configuration before testing begins:

| Journal Type | Purpose | Type Code |
|--------------|---------|-----------|
| VendInvoice | Vendor invoice registration | 25 |
| CustPayment | Customer payment processing | 14 |
| VendDisb | Vendor payment disbursement | 42 |

### Bank Account Multi-Currency for IC Payments

**Issue:** Cross-currency payments fail if bank account doesn't allow additional currencies.

**Error:**
> "Currency XXX not allowed for account YYYY"

**Solution:** Update bank account via OData:
```json
{
  "AllowTransactionsInAdditionalCurrencies": "Yes"
}
```

---

## References

- [General ledger home page](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-ledger)
- [Configure ledgers](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/configure-ledger)
- [Plan the chart of accounts](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/plan-chart-of-accounts)
- [Financial dimensions](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-dimensions)
- [Year-end close](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/year-end-close)
- [Fiscal calendars, fiscal years, and periods](https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/fiscal-calendars-fiscal-years-periods)
- [Data management overview](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-entities-data-packages)

---