# Tax Module - Knowledge Source

> This file is the central knowledge hub for the **Tax** module within Dynamics 365 Finance.

---


---


> **Microsoft Learn Reference:** [Tax](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/indirect-taxes-overview)

## Module Overview

The Tax module in Dynamics 365 Finance provides comprehensive sales tax configuration, calculation, and reporting. It supports tax codes, tax groups, item tax groups, tax authorities, settlement periods, withholding tax, conditional sales tax, and the Tax Calculation service for complex multi-jurisdictional tax scenarios.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Sales Tax Configuration** | Define tax codes, tax rates, and tax calculation parameters |
| **Tax Groups** | Create sales tax groups and item sales tax groups for tax determination |
| **Tax Authorities & Periods** | Set up tax authorities, settlement periods, and reporting intervals |
| **Tax Calculation Service** | Use the cloud-based Tax Calculation service for multi-jurisdiction tax |
| **Withholding Tax** | Configure and calculate withholding tax for vendor and customer transactions |
| **Tax Settlement & Reporting** | Settle sales tax and generate regulatory tax reports |
| **Conditional Sales Tax** | Handle tax scenarios where tax is due only upon payment |
| **EU Intrastat Reporting** | Generate Intrastat declarations for EU trade reporting |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template files define the data entities required for migrating and configuring this module:

#### 130 - Tax (`130 - Tax.json`)

Tax configuration entities for sales tax, VAT, withholding tax, and related indirect tax setup.

| Seq | Entity Name | Target Entity |
|-----|-------------|---------------|
| 10 | Sales tax authorities | TaxAuthorityEntity |
| 10 | Sales tax exempt code | TaxExemptCodeEntity |
| 10 | Sales tax exempt numbers | TaxVATNumTableEntity |
| 10 | Sales tax groups | TaxGroupEntity |
| 10 | Sales tax parameters preset entity | TaxParametersPresetEntity |
| 10 | Sales tax reporting codes | TaxReportingCodeEntity |
| 10 | Transaction codes | IntrastatTransactionCodeEntity |
| 10 | Withholding tax codes | TaxWithholdingTaxCodeEntity |
| 20 | Withholding tax groups | TaxWithholdingGroupEntity |
| 20 | Withholding tax limits | TaxWithholdingTaxCodeLimitEntity |
| 20 | Withholding tax code values | TaxWithholdingTaxCodeValueEntity |
| 20 | Sales tax period setup | TaxPeriodEntity |
| 20 | Sales tax ledger posting groups V2 | TaxPostingGroupEntityV2 |
| 30 | Withholding tax group details | TaxWithholdingGroupDataEntity |
| 30 | Sales tax codes | TaxCodeEntity |
| 40 | Sales tax item groups | TaxItemGroupEntity |
| 40 | Sales tax group details | TaxGroupDataEntity |
| 40 | Sales tax code limits | TaxCodeLimitEntity |
| 40 | Sales tax code values | TaxCodeValueEntity |
| 50 | Sales tax parameters | TaxParametersEntity |


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Tax** module.

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

### Source to pay

*29 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze procurement and sourcing | 1 | — |
| Develop procurement and sourcing strategy | 8 | — |
| Manage accounts payable | 20 | — |

### Order to cash

*86 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze sales performance | 22 | — |
| Develop sales policies | 7 | — |
| Manage accounts receivable | 37 | — |
| Manage credit and collections | 19 | [Learn more](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/pattern-manually-set-check-customer-credit-limits) |
| Manage sales orders | 1 | — |

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Sales tax authorities | `TaxAuthorityEntity` | `TaxAuthorities` | verified |
| Sales tax exempt code | `TaxExemptCodeEntity` | `TaxExemptCodes` | verified |
| Sales tax groups | `TaxGroupEntity` | `TaxGroups` | verified |
| Transaction codes | `IntrastatTransactionCodeEntity` | `IntrastatTransactionCodes` | auto-exact |
| Withholding tax codes | `TaxWithholdingTaxCodeEntity` | `WithholdingTaxCodes` | verified |
| Withholding tax groups | `TaxWithholdingGroupEntity` | `TaxWithholdingGroups` | auto-exact |
| Withholding tax limits | `TaxWithholdingTaxCodeLimitEntity` | `WithholdingTaxCodeLimits` | verified |
| Withholding tax code values | `TaxWithholdingTaxCodeValueEntity` | `WithholdingTaxCodeValues` | verified |
| Sales tax period setup | `TaxPeriodEntity` | `TaxPeriodHeads` | verified |
| Withholding tax group details | `TaxWithholdingGroupDataEntity` | `TaxWithholdingGroupDetails` | verified |
| Sales tax codes | `TaxCodeEntity` | `TaxCodes` | verified |
| Sales tax item groups | `TaxItemGroupEntity` | `TaxItemGroups` | verified |
| Sales tax group details | `TaxGroupDataEntity` | `TaxGroupDatas` | auto-exact |
| Sales tax code limits | `TaxCodeLimitEntity` | `TaxCodeLimits` | verified |
| Sales tax code values | `TaxCodeValueEntity` | `TaxCodeValuesV2` | verified |
| Sales tax parameters | `TaxParametersEntity` | `TaxParameters` | auto-exact |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Sales tax exempt numbers | `TaxVATNumTableEntity` |
| Sales tax parameters preset entity | `TaxParametersPresetEntity` |
| Sales tax reporting codes | `TaxReportingCodeEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Tax operations including tax settlement, reporting, and compliance:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (CSV):** `../../../Business Process/ProcessCatalogue.csv`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Tax-related business process areas in the catalogue:
- Tax settlement and reporting
- Sales tax calculation on transactions
- Withholding tax processing
- VAT reporting and compliance
- Intrastat reporting

---

## Microsoft Learn Sources

### Primary Learning Paths

| Resource | URL |
|----------|-----|
| **Set up taxes in Dynamics 365 Finance** | https://learn.microsoft.com/en-us/training/modules/set-up-taxes-finance/ |
| **Work with taxes in Dynamics 365 Finance** | https://learn.microsoft.com/en-us/training/modules/work-taxes-finance/ |

### Learning Path Modules - Set Up Taxes

| Resource | URL |
|----------|-----|
| Introduction | https://learn.microsoft.com/en-us/training/modules/set-up-taxes-finance/introduction |
| Configure ledger posting groups | https://learn.microsoft.com/en-us/training/modules/set-up-taxes-finance/configure-ledger-posting-groups |
| Configure sales tax authorities | https://learn.microsoft.com/en-us/training/modules/set-up-taxes-finance/configure-sales-tax-authorities |
| Exercise - Set up sales tax authorities | https://learn.microsoft.com/en-us/training/modules/set-up-taxes-finance/exercise-set-up-sales-tax-authorities |
| Configure sales tax settlement periods | https://learn.microsoft.com/en-us/training/modules/set-up-taxes-finance/configure-sales-tax-settlemen-periods |
| Exercise - Set up sales tax settlement periods | https://learn.microsoft.com/en-us/training/modules/set-up-taxes-finance/exercise-set-up-sales-tax-settlement-periods |
| Create sales tax codes | https://learn.microsoft.com/en-us/training/modules/set-up-taxes-finance/create-sales-tax-codes |
| Configure sales tax groups and item sales tax groups | https://learn.microsoft.com/en-us/training/modules/set-up-taxes-finance/configure-sales-tax-groups-item-tax-groups |
| Exercise - Set up sales tax codes and sales tax groups | https://learn.microsoft.com/en-us/training/modules/set-up-taxes-finance/exercise-set-up-sales-tax-codes-groups |

### Learning Path Modules - Work With Taxes

| Resource | URL |
|----------|-----|
| Withholding tax | https://learn.microsoft.com/en-us/training/modules/work-taxes-finance/withholding-tax |
| Sales tax exemption | https://learn.microsoft.com/en-us/training/modules/work-taxes-finance/sales-tax-exemption |
| Conditional sales tax | https://learn.microsoft.com/en-us/training/modules/work-taxes-finance/conditional-sales-tax |
| Sales tax on transactions | https://learn.microsoft.com/en-us/training/modules/work-taxes-finance/sales-tax-transactions |
| Set up sales tax reporting codes | https://learn.microsoft.com/en-us/training/modules/work-taxes-finance/set-up-codes |
| Prepare periodic filing | https://learn.microsoft.com/en-us/training/modules/work-taxes-finance/prepare-periodic-filing |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Sales tax overview | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/indirect-taxes-overview |
| Set up sales tax codes | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-sales-tax-codes |
| Set up sales tax authorities | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-sales-tax-authorities |
| Set up sales tax settlement periods | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-sales-tax-settlement-periods |
| Set up sales tax reporting codes | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-sales-tax-reporting-codes |
| Set up sales tax groups and item sales tax groups | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-sales-tax-groups-item-sales-tax-groups |
| Set up ledger posting groups for sales tax | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-ledger-posting-groups-sales-tax |
| View posted sales tax transactions | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/view-posted-sales-tax-transactions |
| Set up global withholding tax | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/set-up-global-withholding-tax |
| Withholding tax in purchase transactions | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/withholding-tax-in-purchase-transactions |
| Withholding tax in sales transactions | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/withholding-tax-in-sales-transactions |
| Tax Calculation service (Globalization Studio) | https://learn.microsoft.com/en-us/dynamics365/finance/localizations/global/global-get-started-with-tax-calculation-service |

---

## Tax Framework Overview

The sales tax framework in Dynamics 365 Finance supports many types of indirect taxes:

- **Sales Tax / VAT** - Value-added tax on goods and services
- **Goods and Services Tax (GST)** - Used in countries such as India, Australia
- **Unit-Based Fees** - Per-unit tax calculations
- **Withholding Tax** - Tax withheld at source on payments

### Tax Entity Relationships

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      TAX ENTITY RELATIONSHIPS                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   ┌──────────────────┐        ┌──────────────────────┐                   │
│   │  Sales Tax Code   │───────▶│  Settlement Period   │                  │
│   │  (Rate & Rules)   │        │  (Reporting Interval)│                  │
│   └────────┬─────────┘        └──────────┬───────────┘                   │
│            │                              │                              │
│            │                              ▼                              │
│            │                   ┌──────────────────────┐                  │
│            │                   │  Sales Tax Authority  │                  │
│            │                   │  (Government Entity)  │                  │
│            │                   └──────────────────────┘                   │
│            │                                                             │
│            ▼                                                             │
│   ┌──────────────────┐        ┌──────────────────────┐                   │
│   │  Ledger Posting   │        │ Sales Tax Reporting  │                  │
│   │  Group            │        │ Codes                │                  │
│   │  (GL Accounts)    │        │ (Tax Return Lines)   │                  │
│   └──────────────────┘        └──────────────────────┘                   │
│                                                                          │
│   TRANSACTION LEVEL:                                                     │
│   ┌──────────────────┐        ┌──────────────────────┐                   │
│   │  Sales Tax Group  │        │ Item Sales Tax Group │                  │
│   │  (Party: Cust/    │        │ (Resource: Item/     │                  │
│   │   Vendor)         │        │  Procurement Cat.)   │                  │
│   └────────┬─────────┘        └──────────┬───────────┘                   │
│            │                              │                              │
│            └──────────┬───────────────────┘                              │
│                       ▼                                                  │
│            ┌──────────────────────┐                                      │
│            │  INTERSECTION =       │                                     │
│            │  Applicable Tax Codes │                                     │
│            └──────────────────────┘                                      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 6-Phase Configuration Sequence

### Phase 1: GL Account Prerequisites

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| MainAccount | General ledger > Chart of accounts > Accounts > Main accounts | Tax GL accounts must exist first |

**⚠️ Critical:** Tax accounts must have `PostingType = Tax` set before they can be used in Ledger Posting Groups. Without this, invoice posting fails with:
> "Account number for transaction type Sales Tax does not exist"

### Phase 2: Ledger Posting Groups

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| TaxAccountGroup | Tax > Setup > Sales tax > Ledger posting groups | Maps tax codes to GL accounts |

**Key Accounts to Configure:**
- Sales tax payable (output tax)
- Sales tax receivable (input tax)
- Use tax payable / Use tax expense
- Settlement account (clearing during settlement)

### Phase 3: Tax Authorities & Settlement Periods

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| TaxAuthority | Tax > Indirect taxes > Sales tax > Sales tax authorities | Tax authority definition |
| TaxPeriod | Tax > Indirect taxes > Sales tax > Sales tax settlement periods | Reporting/payment intervals |

**Sales Tax Authority Setup:**
- Report layout determines the format of the tax settlement report
- Can be linked to a vendor account for payment processing
- Settlement period intervals (monthly, quarterly, annually) are defined per authority

### Phase 4: Sales Tax Codes

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| TaxCode | Tax > Indirect taxes > Sales tax > Sales tax codes | Tax rate definitions |
| TaxCodeValue | (Within sales tax code) | Tax rate values/percentages |
| TaxCodeLimit | (Within sales tax code) | Minimum/maximum tax limits |
| TaxReportingCode | Tax > Setup > Sales tax > Sales tax reporting codes | Tax return line mapping |

**Sales Tax Code Configuration:**
- Each code stores tax rates and calculation rules
- Must be linked to a settlement period
- Must be linked to a ledger posting group
- Supports multiple rate types: Standard VAT, Reduced VAT, VAT 0%, Excise, Other

### Phase 5: Tax Groups

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| TaxGroup | Tax > Indirect taxes > Sales tax > Sales tax groups | Party-level tax grouping |
| TaxGroupData | (Within sales tax group) | Tax codes in group |
| TaxItemGroup | Tax > Indirect taxes > Sales tax > Item sales tax groups | Resource-level tax grouping |
| TaxExemptCode | Tax > Setup > Sales tax > Sales tax exempt codes | Exemption reasons |
| TaxVATNumTable | Tax > Setup > Sales tax > Tax exempt numbers | VAT registration numbers |

**How Tax Determination Works:**
- **Sales Tax Group** = assigned to customer/vendor (party)
- **Item Sales Tax Group** = assigned to item/procurement category (resource)
- **Intersection** of both groups determines which tax codes apply to a transaction

### Phase 6: Tax Parameters & Advanced Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| TaxParameters | Tax > Setup > Sales tax > Sales tax parameters | Global tax parameters |
| TaxParametersPreset | (System initialization) | Default parameter values |

**Tax Parameters Key Settings:**
- Conditional sales tax (cash-basis VAT)
- Tax calculation rounding rules
- Tax direction defaults
- Withholding tax minimum invoice amount

---

## Withholding Tax Setup

Withholding tax is a separate tax framework within the Tax module for taxes withheld at source on vendor/customer payments.

### Withholding Tax Configuration Sequence

| Step | Table | Menu Path | Purpose |
|------|-------|-----------|---------|
| 1 | WithholdingTaxAuthority | Tax > Setup > Withholding tax > Withholding tax authorities | WHT authority |
| 2 | WithholdingTaxPeriod | Tax > Setup > Withholding tax > Withholding tax settlement periods | WHT reporting periods |
| 3 | TaxWithholdingLedgerPostingGroup | Tax > Setup > Withholding tax > Withholding tax ledger posting group | WHT GL account mapping |
| 4 | TaxWithholdingTaxCode | Tax > Indirect taxes > Withholding tax > Withholding tax codes | WHT rates |
| 5 | TaxWithholdingGroup | Tax > Indirect taxes > Withholding tax > Withholding tax groups | WHT group assignment |
| 6 | ItemWithholdingTaxGroup | Tax > Setup > Withholding tax > Item withholding tax groups | Item-level WHT |

**Withholding Tax GL Account Requirements:**
- **Withholding tax** account: Main account with `PostingType = Withholding tax`
- **Withholding tax offset** account: Main account with `PostingType = Withholding tax offset`

**Enabling on Transactions:**
- Vendor: Set `Calculate withholding tax = Yes` on vendor record (Invoice and delivery tab)
- Customer: Set `Calculate withholding tax = Yes` on customer record (Invoice and delivery tab)
- Item: Set `Calculate withholding tax = Yes` on released product (Purchase/Sell tab)

---

## Sales Tax on Transactions

On every transaction (sales/purchase document lines, journals), a **sales tax group** and **item sales tax group** must be present for tax calculation:

- Default groups are inherited from master data (customer, vendor, item, procurement category)
- Groups can be manually overridden on individual transactions
- The **Sales tax transaction** page shows calculated tax per document line or whole document
- Certain documents (vendor invoice, general journals) allow manual adjustment of calculated tax

---

## Sales Tax Settlement & Reporting

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SALES TAX SETTLEMENT FLOW                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. ACCUMULATION                                                         │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ Sales tax posted to receivable/payable accounts during │          │
│     │ normal transaction processing (invoicing, journals)     │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  2. SETTLEMENT (Settle and post sales tax)                               │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ Tax > Declarations > Sales tax > Settle and post sales │          │
│     │ tax                                                     │          │
│     │ • Select settlement period                              │          │
│     │ • Specify from/to date                                  │          │
│     │ • Offsets receivable/payable to settlement account      │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  3. PAYMENT                                                              │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ If authority linked to vendor account:                  │          │
│     │ • Settlement creates open vendor invoice                │          │
│     │ • Include in regular payment proposal                   │          │
│     │ Otherwise: Manual bank payment                          │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  4. REPORTING                                                            │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Sales tax payment by code report                      │          │
│     │ • Tax reporting codes map to tax return lines           │          │
│     │ • Country-specific VAT declarations                     │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Conditional Sales Tax

Conditional sales tax (cash-basis VAT) is a legal requirement in some countries/regions where tax is paid proportionally to actual payment received, not at invoicing time.

**Configuration:**
1. Enable **Conditional sales tax** checkbox on General ledger parameters page
2. Set up dedicated sales tax codes for conditional tax
3. Create dedicated sales tax groups
4. Create dedicated ledger posting groups for conditional tax

**Behavior:**
- Invoice posting: Tax recorded but not yet payable
- Payment posting: Tax becomes payable proportionally to payment amount
- Must be reported in the sales tax book but excluded from the tax payment report until paid

---

## Tax Calculation Service (Globalization Studio)

For advanced tax requirements, D365 Finance offers the **Tax Calculation** microservice accessible via Globalization Studio:

**Key Capabilities:**
- Automatic tax group determination via applicability rules
- Multi-VAT registration number support
- Tax configuration version management
- Centralized tax feature management across legal entities

**High-Level Flow:**
1. Transaction created in Finance (SO, PO, etc.)
2. Default sales tax group and item sales tax group applied from master data
3. Tax Calculation service matches transaction against applicability rules
4. Overrides groups if matched; otherwise uses defaults
5. Determines final tax codes via intersection
6. Returns calculated tax to Finance

---

## FY27 Environment - Validated Menu Items

*Verified against FY27 environment (USMF) - February 2026*

### Tax Setup Forms

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `TaxParameters` | Sales tax parameters | Tax Setup |
| `TaxAccountGroup` | Ledger posting groups | Posting |
| `TaxAuthority` | Sales tax authorities | Tax Setup |
| `TaxPeriod` | Sales tax settlement periods | Tax Setup |
| `TaxTable` | Sales tax codes | Tax Codes |
| `TaxGroupSetup` | Sales tax groups | Tax Groups |
| `TaxItemGroupSetup` | Item sales tax groups | Tax Groups |
| `TaxReportingCode` | Sales tax reporting codes | Reporting |
| `TaxExemptCodeTable` | Sales tax exempt codes | Exemptions |

### Withholding Tax Forms

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `TaxWithholdTable` | Withholding tax codes | WHT Setup |
| `TaxWithholdGroup` | Withholding tax groups | WHT Groups |
| `TaxWithholdAuthority_IN` | Withholding tax authorities | WHT Setup |
| `TaxWithholdPeriod_IN` | Withholding tax settlement periods | WHT Setup |

### Tax Declarations & Reporting

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `TaxReport` | Settle and post sales tax | Settlement |
| `TaxReporting` | Sales tax payment by code | Reporting |
| `TaxTrans` | Posted sales tax | Inquiry |
| `TaxSpecPerLedgerTrans` | Sales tax specification by ledger transaction | Inquiry |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Main accounts** must exist and have `PostingType = Tax` before ledger posting group setup
2. **Ledger posting groups** must be configured before sales tax codes
3. **Sales tax authorities** must exist before settlement periods
4. **Settlement periods** must be created before sales tax codes
5. **Sales tax codes** must exist before being added to sales tax groups
6. **Sales tax groups** and **item sales tax groups** must exist before transaction processing
7. **Tax parameters** should be finalized before go-live

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Account number for transaction type Sales Tax does not exist" | Main account PostingType not set to Tax | Set PostingType = Tax on GL account via OData or form |
| "Posting type must be Sales Tax for account" | OData Ledger Posting Group creation attempted | Configure Ledger Posting Groups via UI only |
| "Sales tax settlement period not found" | No period defined for authority | Create settlement period linked to authority |
| "No sales tax codes found" | Empty intersection of tax group and item tax group | Verify both groups contain matching tax codes |
| "Tax code not valid for date" | Tax code value not defined for transaction date | Add tax rate value for the applicable date range |
| "Settlement already exists for period" | Duplicate settlement attempt | Check previous settlement runs |

---

## ⚠️ Critical Configuration Discoveries

### Main Account PostingType for Tax Accounts

**Issue:** Tax accounts must have `PostingType = Tax` before they can be used in Ledger Posting Groups. This applies to **ALL country implementations**.

**Error Without Correct Setup:**
> "Account number for transaction type Sales Tax does not exist"

**Solution - Two-Step Process:**

#### Step 1: Update Main Account PostingType via OData

Identify tax accounts in chart of accounts based on the chart of accounts for each country (e.g., 1576, 1776 for Germany; 2610-2640 for Sweden)

**OData Update Pattern:**
```json
{
  "ODataPath": "MainAccounts(dataAreaId='<company>',MainAccountId='<account>',ChartOfAccounts='<chart>')",
  "UpdatedFieldValues": { "PostingType": "Tax" }
}
```

#### Step 2: Configure Ledger Posting Groups via UI

**Menu Path:** Tax > Setup > Sales tax > Ledger posting groups

**Why UI Required:**
- OData creation fails with validation error: "Posting type must be Sales Tax for account"
- The form enforces proper dimension validation
- Settlement account must match existing ledger dimensions

### Ledger Posting Groups - UI Only Configuration

**Discovery:** OData creation of Tax Ledger Posting Groups fails with validation errors.

**Solution:** Use the TaxAccountGroup form (Tax > Setup > Sales tax > Ledger posting groups) to configure:
- Sales tax payable account
- Sales tax receivable account
- Use tax expense / Use tax payable
- Settlement account

### Testing Validation Checklist

After Tax configuration for each legal entity:
- [ ] Create and post a free text invoice → verify tax postings to correct GL accounts
- [ ] Create and post a vendor invoice → verify tax postings to correct GL accounts
- [ ] Run tax settlement → verify clearing entries
- [ ] Post a transaction with withholding tax (if applicable) → verify WHT accounts

**Key Insight:** Every country implementation requires verification that tax accounts have correct PostingType. This should be part of the standard implementation checklist.

---

## Data Migration Sequence

```
1. Main Accounts (with PostingType = Tax)
2. Ledger Posting Groups
3. Sales Tax Authorities
4. Sales Tax Settlement Periods
5. Sales Tax Exempt Codes
6. Sales Tax Exempt Numbers (VAT Registration)
7. Sales Tax Reporting Codes
8. Withholding Tax Codes
9. Withholding Tax Groups
10. Sales Tax Codes (with rates/values)
11. Sales Tax Groups (with tax code assignments)
12. Item Sales Tax Groups
13. Sales Tax Parameters
14. Intrastat Transaction Codes
```

---

## Related Modules

| Module | Relationship |
|--------|--------------|
| **General Ledger** | Tax accounts post to GL; Chart of Accounts must include tax accounts with correct PostingType |
| **Accounts Payable** | Purchase tax calculated on vendor invoices; withholding tax on vendor payments |
| **Accounts Receivable** | Sales tax calculated on customer invoices; withholding tax on customer payments |
| **Procurement & Sourcing** | Tax groups default from purchase orders and procurement categories |
| **Sales & Marketing** | Tax groups default from sales orders and customer master |
| **Project Management & Accounting** | Tax on project invoices and expense transactions |
| **Expense Management** | Tax on employee expense reports |

---

## References

- [Sales tax overview](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/indirect-taxes-overview)
- [Set up sales tax codes](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-sales-tax-codes)
- [Set up sales tax authorities](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-sales-tax-authorities)
- [Set up sales tax settlement periods](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-sales-tax-settlement-periods)
- [Set up ledger posting groups for sales tax](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-ledger-posting-groups-sales-tax)
- [Set up sales tax groups and item sales tax groups](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-sales-tax-groups-item-sales-tax-groups)
- [Set up sales tax reporting codes](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-sales-tax-reporting-codes)
- [Set up global withholding tax](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/set-up-global-withholding-tax)
- [Withholding tax in purchase transactions](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/withholding-tax-in-purchase-transactions)
- [Withholding tax in sales transactions](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/withholding-tax-in-sales-transactions)
- [View posted sales tax transactions](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/view-posted-sales-tax-transactions)
- [Tax Calculation service overview](https://learn.microsoft.com/en-us/dynamics365/finance/localizations/global/global-get-started-with-tax-calculation-service)
- [Data management overview](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-entities-data-packages)

---
