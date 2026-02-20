# Accounts Receivable Module - Knowledge Source

> This file is the central knowledge hub for the **Accounts Receivable** module within Dynamics 365 Finance.

---


---


> **Microsoft Learn Reference:** [Accounts Receivable](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/accounts-receivable)

## Module Overview

The Accounts Receivable module manages the customer billing and collections lifecycle in Dynamics 365 Finance. It handles customer master data, free text invoices, customer payments, credit management, collections, payment schedules, and subscription billing. It integrates with Sales & Marketing, General Ledger, and Cash & Bank Management.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Customer Management** | Create and manage customer master records, payment terms, and posting profiles |
| **Free Text Invoices** | Create invoices not linked to sales orders for ad-hoc billing |
| **Payment Processing** | Record customer payments, process payment journals, and manage deposits |
| **Credit Management** | Set credit limits, manage credit holds, and evaluate customer creditworthiness |
| **Collections** | Track overdue balances, send collection letters, and manage aging reports |
| **Interest & Penalties** | Calculate and charge interest on overdue balances |
| **Customer Settlements** | Settle open customer transactions against payments |
| **Subscription Billing** | Manage recurring billing schedules and revenue recognition |
| **Revenue Recognition** | Automate multi-element revenue allocation and recognition |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 140 - Accounts Receivable (`140 - Accounts receivable.json`)

Accounts Receivable configuration and master data entities.

| Seq | Entity Name | Target Entity | Category |
|-----|-------------|---------------|----------|
| 10 | Aging period definitions | AgingPeriodDefinitionEntity | AP and AR Shared - Setup |
| 10 | Business segments | smmBusinessSegmentEntity | AR - Customer attributes |
| 10 | Cash discount | CashDiscountEntity | AP and AR Shared - Setup |
| 10 | Collection letter setup | CollectionLetterCourseEntity | AR - Parameters |
| 10 | Commission customer group | CommissionCustomerGroupEntity | AR - Customer attributes |
| 10 | Commission item group | CommissionProductGroupEntity | AR - Customer attributes |
| 10 | Commission sales group | CommissionSalesRepresentativeGroupEntity | AR - Customer attributes |
| 10 | Customer bank accounts | CustomerBankAccountEntity | |
| 10 | Customer charge groups | CustChargeCustomerGroupEntity | AR - Customer attributes |
| 10 | Customer definitions | CustCustomerBaseEntity | |
| 10 | Customer details V2 | CustCustomerDetailV2Entity | |
| 10 | Customer groups | CustCustomerGroupEntity | AR - Customers |
| 10 | Customer payment fee | CustomerPaymentFeeEntity | AR - Customer payment setup |
| 10 | Customer payment method | CustomerPaymentMethodEntity | AR - Customer payment setup |
| 10 | Customer reasons | CustCustomerReasonEntity | AR - Customer attributes |
| 10 | Customer write-off reason codes | CustWriteOffFinancialReasonsSetupEntity | |
| 10 | Delivery charges groups | DlvChargeDeliveryGroupEntity | AP and AR Shared - Setup |
| 10 | Expedite codes | MCRExpediteCodeEntity | AR - Customer attributes |
| 10 | Interest codes | CustInterestCodeEntity | AR - Parameters |
| 10 | Item charge groups | InventChargeProductGroupEntity | AR - Customer attributes |
| 10 | Line discount customer groups | PriceDiscLineDiscountCustomerGroupEntity | AR - Customer attributes |
| 10 | Line of business | LineOfBusinessEntity | AP and AR Shared - Setup |
| 10 | Payment calendar | PaymentCalendarEntity | |
| 10 | Payment day lines | PaymentDayEntity | AP and AR Shared - Setup |
| 10 | Payment schedule | PaymentScheduleEntity | AP and AR Shared - Setup |
| 10 | Price customer groups | PriceDiscPriceCustomerGroupEntity | AR - Customer attributes |
| 10 | Printed form notes | FormLetterPrintedFormNoteEntity | AR - Parameters |
| 10 | Sales charge codes | SalesChargeEntity | AR - Customer attributes |
| 10 | Sales districts | smmSalesDistrictEntity | AR - Customer attributes |
| 10 | Sales order pools | SalesOrderPoolEntity | AR - Customer attributes |
| 10 | Statistics group | CustCustomerStatisticsGroupEntity | AR - Customer attributes |
| 10 | Terms of delivery | DeliveryTermsEntity | AP and AR Shared - Setup |
| 10 | Terms of payment | PaymentTermEntity | AP and AR Shared - Setup |
| 10 | Total discount customer groups | PriceDiscTotalDiscountCustomerGroupEntity | AR - Customer attributes |
| 20 | Business subsegments | smmBusinessSubsegmentEntity | AR - Customer attributes |
| 20 | Commission calculation | CommissionCalculationEntity | AR - Customer attributes |
| 20 | Customer payment method specification | CustomerPaymentMethodSpecificationEntity | AR - Customer payment setup |
| 20 | Interest codes with fees | CustInterestCodeWithFeeEntity | |
| 20 | Interest codes with ranges | CustInterestCodeWithRangeEntity | |
| 20 | Modes of delivery | DlvDeliveryModeEntity | AR - Customer attributes |
| 20 | Payment schedule lines | PaymentScheduleLineEntity | AP and AR Shared - Setup |
| 22 | Customer facing form printing configurations | CustFormletterCustomerFacingFormPrintingConfigurationEntity | |
| 24 | Free text invoice form printing configurations | CustFormletterCustomerFreeTextInvoiceFormPrintingConfigurationEntity | |
| 26 | Customer account statement form printing configurations | CustFormletterCustomerAccountStatementFormPrintingConfigurationEntity | |
| 28 | Interest note form printing configurations | CustFormletterCustomerInterestNoteFormPrintingConfigurationEntity | |
| 29 | Collection letter form printing configurations | CustFormletterCustomerCollectionLetterFormPrintingConfigurationEntity | |
| 30 | Customer posting profiles | CustCustomerPostingProfileHeaderEntity | AR - Parameters |
| 40 | Customer ledger accounts | CustCustomerPostingProfileLineEntity | AR - Parameters |
| 40 | Customer parameters | CustomerParametersEntity | AR - Setup |

---

### Shared Entities (AP & AR)

Several entities are shared between Accounts Payable and Accounts Receivable and are typically loaded via the AP template (120) first:

| Entity Name | Target Entity | Used In |
|-------------|---------------|---------|
| Aging period definitions | AgingPeriodDefinitionEntity | AP + AR |
| Cash discount | CashDiscountEntity | AP + AR |
| Delivery charges groups | DlvChargeDeliveryGroupEntity | AP + AR |
| Line of business | LineOfBusinessEntity | AP + AR |
| Payment calendar | PaymentCalendarEntity | AP + AR |
| Payment day lines | PaymentDayEntity | AP + AR |
| Payment schedule | PaymentScheduleEntity | AP + AR |
| Payment schedule lines | PaymentScheduleLineEntity | AP + AR |
| Terms of delivery | DeliveryTermsEntity | AP + AR |
| Terms of payment | PaymentTermEntity | AP + AR |


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Accounts Receivable** module.

### Order to cash

*86 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze sales performance | 22 | — |
| Develop sales policies | 7 | — |
| Manage accounts receivable | 37 | — |
| Manage credit and collections | 19 | [Learn more](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/pattern-manually-set-check-customer-credit-limits) |
| Manage sales orders | 1 | — |

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
| Aging period definitions | `AgingPeriodDefinitionEntity` | `AgingPeriodDefinitions` | verified |
| Cash discount | `CashDiscountEntity` | `CashDiscounts` | verified |
| Customer bank accounts | `CustomerBankAccountEntity` | `CustomerBankAccounts` | auto-exact |
| Customer definitions | `CustCustomerBaseEntity` | `CustomersV3` | verified |
| Customer groups | `CustCustomerGroupEntity` | `CustomerGroups` | verified |
| Customer payment fee | `CustomerPaymentFeeEntity` | `CustomerPaymentFees` | verified |
| Customer payment method | `CustomerPaymentMethodEntity` | `CustomerPaymentMethods` | verified |
| Customer reasons | `CustCustomerReasonEntity` | `CustomerReasons` | verified |
| Customer write-off reason codes | `CustWriteOffFinancialReasonsSetupEntity` | `WriteOffFinancialReasonsSetups` | verified |
| Line discount customer groups | `PriceDiscLineDiscountCustomerGroupEntity` | `LineDiscountCustomerGroups` | verified |
| Line of business | `LineOfBusinessEntity` | `LineOfBusinesses` | manual-unverified |
| Payment calendar | `PaymentCalendarEntity` | `PaymentCalendars` | verified |
| Payment day lines | `PaymentDayEntity` | `PaymentDays` | verified |
| Payment schedule | `PaymentScheduleEntity` | `PaymentSchedules` | verified |
| Price customer groups | `PriceDiscPriceCustomerGroupEntity` | `PriceCustomerGroups` | verified |
| Sales charge codes | `SalesChargeEntity` | `SalesCharge` | auto-exact |
| Sales order pools | `SalesOrderPoolEntity` | `SalesOrderPools` | verified |
| Statistics group | `CustCustomerStatisticsGroupEntity` | `CustomerStatisticsGroups` | verified |
| Terms of delivery | `DeliveryTermsEntity` | `DeliveryTerms` | verified |
| Terms of payment | `PaymentTermEntity` | `PaymentTerms` | verified |
| Total discount customer groups | `PriceDiscTotalDiscountCustomerGroupEntity` | `TotalDiscountCustomerGroups` | verified |
| Customer payment method specification | `CustomerPaymentMethodSpecificationEntity` | `CustomerPaymentMethodSpecifications` | verified |
| Modes of delivery | `DlvDeliveryModeEntity` | `DeliveryModesV2` | verified |
| Payment schedule lines | `PaymentScheduleLineEntity` | `PaymentScheduleLines` | verified |
| Customer posting profiles | `CustCustomerPostingProfileHeaderEntity` | `CustomerPostingProfiles` | verified |
| Customer ledger accounts | `CustCustomerPostingProfileLineEntity` | `CustomerPostingProfileLines` | verified |
| Customer parameters | `CustomerParametersEntity` | `CustomerParameters` | auto-exact |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Business segments | `smmBusinessSegmentEntity` |
| Collection letter setup | `CollectionLetterCourseEntity` |
| Commission customer group | `CommissionCustomerGroupEntity` |
| Commission item group | `CommissionProductGroupEntity` |
| Commission sales group | `CommissionSalesRepresentativeGroupEntity` |
| Customer charge groups | `CustChargeCustomerGroupEntity` |
| Customer details V2 | `CustCustomerDetailV2Entity` |
| Delivery charges groups | `DlvChargeDeliveryGroupEntity` |
| Expedite codes | `MCRExpediteCodeEntity` |
| Interest codes | `CustInterestCodeEntity` |
| Item charge groups | `InventChargeProductGroupEntity` |
| Printed form notes | `FormLetterPrintedFormNoteEntity` |
| Sales districts | `smmSalesDistrictEntity` |
| Business subsegments | `smmBusinessSubsegmentEntity` |
| Commission calculation | `CommissionCalculationEntity` |
| Interest codes with fees | `CustInterestCodeWithFeeEntity` |
| Interest codes with ranges | `CustInterestCodeWithRangeEntity` |
| Customer facing form printing configurations | `CustFormletterCustomerFacingFormPrintingConfigurationEntity` |
| Free text invoice form printing configurations | `CustFormletterCustomerFreeTextInvoiceFormPrintingConfigurationEntity` |
| Customer account statement form printing configurations | `CustFormletterCustomerAccountStatementFormPrintingConfigurationEntity` |
| Interest note form printing configurations | `CustFormletterCustomerInterestNoteFormPrintingConfigurationEntity` |
| Collection letter form printing configurations | `CustFormletterCustomerCollectionLetterFormPrintingConfigurationEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to AR operations including Order to Cash:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key AR-related business process areas:
- Order to Cash (end-to-end)
- Customer invoicing and collections
- Payment receipt and settlement
- Credit management
- Foreign currency revaluation (AR)
- Period close (AR subledger reconciliation)

---

## Microsoft Learn Sources

### Primary Learning Paths

| Resource | URL |
|----------|-----|
| **Work with accounts receivable in Dynamics 365 Finance** | https://learn.microsoft.com/en-us/training/paths/work-accounts-receivable-dyn365-finance/ |
| **Implement AR, credit, collections, and revenue recognition** | https://learn.microsoft.com/en-us/training/paths/implement-accounts-receivable-credit-collections-revenue-recognition/ |
| Set up accounts receivable in Dynamics 365 Finance | https://learn.microsoft.com/en-us/training/modules/configure-accounts-receivable-dyn365-finance/ |
| Get started with accounts receivable daily procedures | https://learn.microsoft.com/en-us/training/modules/accounts-receivable-daily-procedures-dyn365-finance/ |
| Set up credit and collections | https://learn.microsoft.com/en-us/training/modules/configure-credit-collections-dyn365-finance/ |
| Process credit and collections | https://learn.microsoft.com/en-us/training/modules/process-credit-collections-dyn365-finance/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Accounts receivable home page | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/accounts-receivable |
| Configure AR and credit and collections | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/accounts-receivables-set-up-overview |
| Customer posting profiles | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/customer-posting-profiles |
| Credit and collections in AR | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/collections-credit-accounts-receivable |
| Free text invoices | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/configure-customer-invoices |
| Recurring invoices | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/set-up-process-recurring-invoices |
| SEPA direct debit overview | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/sepa-direct-debit-overview |
| Bills of exchange | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/set-up-bills-exchange |
| Centralized payments for AR | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/centralized-payments-accounts-receivable |
| Close Accounts receivable | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/close-accounts-receivable |
| Posting profiles overview | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/pstg-prfles-ovrvw |
| Recommended practices for posting profiles | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/recommended-practices-pstg-prfles |
| Foreign currency revaluation for AP and AR | https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/foreign-currency-revaluation-accounts-payable-accounts-receivable |

---

## 6-Phase Configuration Sequence

### Phase 1: Prerequisites (GL & Bank)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Payment journals | General ledger > Journal setup > Journal names | Journal templates for payments |
| Currencies | General ledger > Currencies > Currencies | Currency codes for AR transactions |
| Exchange rate types | General ledger > Currencies > Exchange rate types | Rate type classification |
| Exchange rates | General ledger > Currencies > Currency exchange rates | Daily/periodic rates |
| Bank accounts | Cash and bank management > Bank accounts > Bank accounts | Bank accounts for payment methods |
| Financial dimensions | General ledger > Chart of accounts > Dimensions > Financial dimensions | Dimensions used in AR posting |

### Phase 2: Shared Payment Setup

> Note: These entities are typically loaded via the Accounts Payable module first. Verify they exist before proceeding.

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| PaymentTerm | Accounts payable > Payment setup > Terms of payment | Payment due date calculation |
| PaymentDayLine | Accounts payable > Payment setup > Payment days | Specific day-of-week/month payment rules |
| PaymentSchedule | Accounts payable > Payment setup > Payment schedules | Installment payment plans |
| CashDisc | Accounts payable > Payment setup > Cash discounts | Early payment discount terms |
| AgingPeriodDefinition | Accounts payable > Payment setup > Aging period definitions | Aging analysis intervals |
| DeliveryTerm | Accounts payable > Setup > Delivery > Terms of delivery | Delivery condition codes |
| DeliveryMode | Accounts payable > Setup > Delivery > Modes of delivery | Transport method codes |
| PaymentCalendar | Accounts payable > Payment setup > Payment calendar | Business calendar for payment dates |

### Phase 3: AR Module Configuration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| CustGroup | Accounts receivable > Customers > Customer groups | Customer groupings for posting/settlement |
| CustPaymMode | Accounts receivable > Payments setup > Methods of payment | Payment method definitions |
| CustPaymFee | Accounts receivable > Payments setup > Payment fee | Customer payment fees |
| CustFormSetup | Accounts receivable > Setup > Form setup | Document format configuration |
| CollectionLetterCourse | Accounts receivable > Setup > Collection letters | Collection letter sequences |
| CustInterestCode | Accounts receivable > Setup > Interest > Interest codes | Interest calculation codes |
| MarkupTable (Sales) | Accounts receivable > Charges setup > Charges code | Sales charge codes |
| CustChargeGroup | Accounts receivable > Charges setup > Customer charges group | Customer charge group codes |
| CommissionCustomerGroup | Accounts receivable > Setup > Commissions > Customer groups | Commission customer grouping |
| CommissionProductGroup | Accounts receivable > Setup > Commissions > Item groups | Commission item grouping |
| CommissionSalesGroup | Accounts receivable > Setup > Commissions > Sales groups | Commission sales rep grouping |

### Phase 4: Posting Profiles & Parameters

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| CustPosting (Header) | Accounts receivable > Setup > Customer posting profiles | AR posting profile definitions |
| CustPosting (Lines) | (Within posting profile) | AR summary account assignments |
| CustParm | Accounts receivable > Setup > Accounts receivable parameters | AR module-wide settings |

**Posting Profile Priority:**

| Account Code | Account/Group Number | Search Priority |
|--------------|---------------------|-----------------|
| **Table** | Specific customer account | 1 (most specific) |
| **Group** | Customer group | 2 |
| **All** | Blank | 3 (least specific) |

### Phase 5: Customer Master Data

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| CustTable | Accounts receivable > Customers > All customers | Customer master records |
| CustBankAccount | (Within customer record) | Customer bank accounts |

### Phase 6: Credit & Collections Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| CustCollectionsAgent | Accounts receivable > Setup > Collections > Collections agents | Agent assignment |
| CustCollectionsTeam | Accounts receivable > Setup > Collections > Collections team | Collections team |
| CustPool | Accounts receivable > Setup > Collections > Customer pools | Customer pool queries |
| CaseCategory | Accounts receivable > Setup > Cases > Case categories | Collections case categories |

---

## Posting Profile Design

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     CUSTOMER POSTING PROFILE DESIGN                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   POSTING PROFILE: "GEN" (General)                                       │
│   ┌────────────────────────────────────────────────────────┐            │
│   │ Account Code: All                                       │            │
│   │ Summary Account: 1300 (Accounts Receivable - Trade)     │            │
│   │ Settlement: Yes                                          │            │
│   │ Interest: Yes                                            │            │
│   │ Collection Letter: Yes                                   │            │
│   └────────────────────────────────────────────────────────┘            │
│                                                                          │
│   POSTING PROFILE: "IC" (Intercompany)                                   │
│   ┌────────────────────────────────────────────────────────┐            │
│   │ Account Code: Group → IC Customer Group                  │            │
│   │ Summary Account: 1513 (IC Receivable)                    │            │
│   │ Settlement: Yes                                          │            │
│   └────────────────────────────────────────────────────────┘            │
│                                                                          │
│   KEY ACCOUNTS:                                                          │
│   • Summary Account → Trade AR (Balance Sheet asset)                    │
│   • Liquidity Account → Cash flow forecast (optional)                   │
│   • Sales Tax Prepayment → Prepayment tax account                       │
│   • Discount Account → Sales discount given                             │
│   • Collection Letter Sequence → Linked collection letter               │
│   • Interest Code → Interest calculation for late payment               │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## AR Business Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ORDER TO CASH - AR PROCESS FLOW                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. CUSTOMER INVOICING                                                   │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Sales order invoices (from packing slips)              │          │
│     │ • Free text invoices (not linked to sales orders)        │          │
│     │ • Recurring invoices (scheduled generation)              │          │
│     │ • Project invoices                                       │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  2. PAYMENT RECEIPT                                                      │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Customer payment journal                               │          │
│     │ • Bills of exchange                                      │          │
│     │ • SEPA direct debit                                      │          │
│     │ • Credit card payments                                   │          │
│     │ • Electronic payments                                    │          │
│     │ • Centralized payments (multi-entity)                    │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  3. SETTLEMENT                                                           │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Automatic or manual settlement                         │          │
│     │ • Cash discount application                              │          │
│     │ • Partial payments                                       │          │
│     │ • Cross-company settlement                               │          │
│     │ • Customer reimbursement                                 │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  4. CREDIT & COLLECTIONS                                                 │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Aging analysis (snapshots)                             │          │
│     │ • Collection letters (auto-generation)                   │          │
│     │ • Interest notes (calculation & posting)                 │          │
│     │ • Collections workspace                                  │          │
│     │ • Write-off processing                                   │          │
│     │ • NSF payment handling                                   │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  5. PERIOD CLOSE                                                         │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Foreign currency revaluation                           │          │
│     │ • AR to GL reconciliation                                │          │
│     │ • Customer aging report                                  │          │
│     │ • Customer account statements                            │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Credit & Collections

### Collection Letter Process

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      COLLECTION LETTER FLOW                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   Invoice Overdue → Collection Letter 1 (Reminder)                      │
│          │                                                               │
│          ▼ (+ N days)                                                    │
│   Still Unpaid → Collection Letter 2 (Stronger warning)                 │
│          │                                                               │
│          ▼ (+ N days)                                                    │
│   Still Unpaid → Collection Letter 3 (Final notice)                     │
│          │                                                               │
│          ▼                                                               │
│   Collections Workspace → Agent action required                         │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Interest Calculation

| Interest Type | Description |
|---------------|-------------|
| **By amount** | Fixed interest amount per period |
| **By range** | Interest rate varies by amount overdue |
| **By earnings** | Interest based on earnings code |

---

## FY27 Environment - Validated Menu Items

*Verified against FY27 environment - February 2026*

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `CustParameters` | Accounts receivable parameters | AR Setup |
| `CustGroup` | Customer groups | AR Setup |
| `CustPosting` | Customer posting profiles | AR Setup |
| `CustTable` | All customers | AR Customers |
| `CustBankAccounts` | Customer bank accounts | AR Customers |
| `CustPaymMode` | Methods of payment - Customers | AR Payments |
| `CustPaymFee` | Payment fee | AR Payments |
| `CustFreeInvoice` | Free text invoices | AR Invoices |
| `SalesInvoiceJour` | Invoice journal | AR Invoices |
| `LedgerJournalTable3` | Customer payment journal | AR Payments |
| `CollectionLetterJour` | Collection letters | AR Collections |
| `CustInterestNote` | Interest notes | AR Collections |
| `CustCollections` | Collections | AR Collections |
| `CustAgingSnapshot` | Customer aging snapshot | AR Collections |
| `CustAgingReport` | Customer aging report | AR Reports |
| `MarkupTable_Sales` | Charges code | AR Charges |
| `CustChargeGroup` | Customer charges group | AR Charges |
| `SalesAutoCharges` | Automatic charges | AR Charges |
| `CustCollectionsWorkspace` | Credit and collections workspace | Workspace |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **General Ledger** must be configured before AR (chart of accounts, dimensions, fiscal calendar)
2. **Bank accounts** must exist before setting up payment methods
3. **Terms of payment** must be created before customer records (typically via AP setup)
4. **Customer groups** must exist before creating customer records
5. **Posting profiles** must be configured before any AR transactions
6. **Posting profile** must be set in AR **parameters** as the default profile
7. **Journal names** must exist before creating payment journals
8. **Number sequences** must be configured in AR parameters for vouchers, invoices, etc.
9. **Tax setup** (sales tax codes, groups, posting groups) must be complete before invoice posting

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Posting profile has not been set up" | AR Parameters missing default posting profile | Set posting profile in AR parameters |
| "Account number for transaction type Sales Tax does not exist" | Tax accounts missing PostingType = Tax | Update main account PostingType via OData, then configure Ledger Posting Groups |
| "Voucher already used" | Duplicate voucher number | Check number sequence setup in AR parameters |
| "Currency not defined" | Missing exchange rate for transaction currency | Add exchange rate for the date and currency pair |
| "You must select a value in the [Dimension] field" | Account structure requires dimension but posting profile has none | Update account structure to allow blank values (`"";*`) |
| "Payment method not defined" | Customer has no payment method assigned | Assign default payment method on customer record |
| "Bank account not valid for payment method" | Method of payment not linked to bank account | Configure bank account on method of payment |
| "Settlement cannot be performed" | Currency mismatch between invoice and payment | Enable multi-currency on bank account or use correct currency |
| "Number must be defined as Continuous" (Denmark) | Legal entity requires continuous number sequences | Set Continuous = Yes on relevant number sequences |

---

## ⚠️ Critical Implementation Discoveries

### Posting Profile Must Be Set in Module Parameters

**Discovery:** Creating posting profiles alone is not sufficient. The default posting profile must be explicitly set in:
- **Accounts receivable parameters** (Accounts receivable > Setup > Accounts receivable parameters > Ledger and sales tax tab)

Without this, all customer invoice posting will fail with "Posting profile has not been set up."

### Tax Account PostingType for Invoice Posting

**Discovery (cross-reference from GL):** Free text invoice posting fails with:
> "Account number for transaction type Sales Tax does not exist"

**Root Cause:** Main accounts for tax exist in chart of accounts BUT `PostingType` field is set to "None" instead of "Tax."

**Solution - Two-Step Process:**
1. Update main account PostingType to "Tax" via OData
2. Configure Ledger Posting Groups via UI (Tax > Setup > Sales tax > Ledger posting groups)

**Key Insight:** Every country implementation requires verification that tax accounts have correct PostingType. This should be part of the standard implementation checklist.

### Intercompany AR Account Setup

**Discovery from Swedish/Norwegian Implementation:** Intercompany transactions require dedicated GL accounts distinct from regular AR for proper elimination and tracking.

**Required IC Account Pairs:**

| Purpose | Originating Co. | Counterparty Co. | Relationship |
|---------|-----------------|-------------------|-------------|
| **IC Receivable** | 1513 (AR koncern) | 2443 (AP koncern) | What counterparty owes |

**Critical Configuration:**
1. GL Chart of Accounts (IC account 1513 created)
2. Separate **IC Customer Group** (e.g., "INT")
3. **Posting profile** with Group = IC customer group → IC summary account (1513)
4. **Intercompany Parameters** (accounts linked as IC pairs)
5. Dedicated IC journals (e.g., SWE-IC, NOR-IC)

### Journal Names - Create Before Testing

**Best Practice:** Create all required AR journal names during initial configuration:

| Journal Type | Purpose | Type Code |
|--------------|---------|-----------|
| CustPayment | Customer payment processing | 14 |
| CustFTI | Free text invoice | 14 |

---

## Database Logging for Posting Profiles

**Best Practice:** Set up database logging to audit changes to AR posting profiles and parameters tables.

| Page Name | Navigation Path | Table Name |
|-----------|----------------|------------|
| Accounts receivable parameters | AR > Setup > AR parameters | CustParm |
| Customer posting profiles | AR > Setup > Customer posting profile | CustPosting |
| Methods of payment (Customer) | AR > Payments setup > Methods of payment | CustPaymMode |
| Payment fee (Customer) | AR > Payments setup > Payment fee | CustPaymFee |
| Charges code | AR > Charges setup > Charges code | MarkupTable |
| Cash discounts | AP > Payment setup > Cash discounts | CashDisc |

---

## Customer Master Data Key Fields

| Field | Purpose | Configuration Source |
|-------|---------|---------------------|
| Customer account | Unique identifier | Number sequence |
| Customer group | Posting/settlement grouping | Customer groups |
| Terms of payment | Invoice due date rules | Terms of payment |
| Method of payment | Payment type/format | Methods of payment |
| Payment schedule | Installment plan | Payment schedules |
| Cash discount | Early payment terms | Cash discounts |
| Currency | Transaction currency | Currency setup |
| Sales tax group | Tax calculation group | Tax setup |
| Posting profile | Override default profile | Posting profiles |
| Collection letter sequence | Dunning progression | Collection letters |
| Interest code | Late payment interest | Interest codes |
| Credit limit | Maximum outstanding balance | Credit management |
| Statistics group | Customer analytics grouping | Statistics groups |

---

## AR Posting Account Types

| Posting Type | Typical Account | Description |
|--------------|-----------------|-------------|
| Customer balance | 1300-1399 | Trade AR summary account |
| Revenue | 3xxx-4xxx | Sales revenue accounts |
| Discount | 3xxx | Sales discount given |
| Sales tax payable | 2610 | Output VAT / Sales tax payable |
| Write-off | 6xxx | Bad debt expense |
| Collection letter fee | 3xxx | Collection letter fee income |
| Interest | 8xxx | Interest income |

---

## Data Migration Sequence

```
 1. Shared Payment Setup (verify loaded via AP module)
    1.1 Terms of payment
    1.2 Payment days
    1.3 Payment schedules + lines
    1.4 Cash discounts
    1.5 Payment calendars + rules
    1.6 Aging period definitions
    1.7 Terms of delivery
    1.8 Modes of delivery
    1.9 Line of business

 2. Accounts Receivable Setup
    2.1 Customer groups
    2.2 Customer payment methods + specifications
    2.3 Customer payment fees
    2.4 Sales charge codes
    2.5 Customer charge groups
    2.6 Commission groups (customer, item, sales)
    2.7 Interest codes (+ fees, ranges)
    2.8 Collection letter setup
    2.9 Form printing configurations

 3. Posting Profiles & Parameters
    3.1 Customer posting profiles (header + lines)
    3.2 Accounts receivable parameters

 4. Master Data
    4.1 Customer definitions (base)
    4.2 Customer details V2 (with exclusions for employee responsible)
    4.3 Customer bank accounts
```

---

## ⚠️ Best Practices

```
┌────────────────────────────────────────────────────────────────┐
│          ACCOUNTS RECEIVABLE IMPLEMENTATION BEST PRACTICES       │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  POSTING PROFILES                                              │
│  ✓ Always configure a default "All" posting profile            │
│  ✓ Use Group-level profiles for IC and special categories      │
│  ✓ Set default profile in AR Parameters immediately            │
│  ✓ Enable database logging on posting profile tables           │
│  ✓ Test invoicing immediately after posting profile setup      │
│                                                                 │
│  CUSTOMER GROUPS                                               │
│  ✓ Create groups based on reporting/posting requirements       │
│  ✓ Separate IC customers into dedicated groups                 │
│  ✓ Use groups to drive payment terms defaults                  │
│  ✓ Keep group structure manageable (3-10 groups)               │
│                                                                 │
│  PAYMENT SETUP                                                 │
│  ✓ Configure payment methods before creating customers         │
│  ✓ Link bank accounts to payment methods explicitly            │
│  ✓ Test SEPA direct debit mandates before go-live              │
│  ✓ Verify multi-currency settings on bank accounts for IC      │
│                                                                 │
│  CREDIT & COLLECTIONS                                          │
│  ✓ Define collection letter sequence with escalating severity  │
│  ✓ Configure aging period definitions for standard reporting   │
│  ✓ Set up collections agents and assign customer pools         │
│  ✓ Schedule periodic aging snapshots                           │
│  ✓ Configure write-off reason codes before production use      │
│                                                                 │
│  TAX SETUP                                                     │
│  ✓ Verify tax account PostingType = Tax before invoice testing │
│  ✓ Configure Ledger Posting Groups via UI (not OData)          │
│  ✓ Test with a free text invoice early in implementation       │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

---

## Related Modules

| Module | Relationship |
|--------|--------------|
| **General Ledger** | AR posts to GL via posting profiles; shared CoA and dimensions |
| **Accounts Payable** | Shared payment setup entities; IC counterparty |
| **Cash & Bank Management** | Bank accounts for payment methods; settlement and reconciliation |
| **Tax** | Sales tax codes/groups used in AR invoicing; tax posting groups |
| **Sales & Marketing** | Sales orders flow into AR invoices |
| **Inventory Management** | Packing slips trigger AR invoice creation |
| **Project Accounting** | Project invoices post to AR |
| **Budgeting** | Budget control on sales orders |
| **Fixed Assets** | Asset disposals via AR |

---

## References

- [Accounts receivable home page](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/accounts-receivable)
- [Configure AR and credit and collections](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/accounts-receivables-set-up-overview)
- [Customer posting profiles](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/customer-posting-profiles)
- [Credit and collections in AR](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/collections-credit-accounts-receivable)
- [Free text invoices](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/configure-customer-invoices)
- [Recurring invoices](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/set-up-process-recurring-invoices)
- [SEPA direct debit overview](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/sepa-direct-debit-overview)
- [Bills of exchange](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/set-up-bills-exchange)
- [Centralized payments for AR](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/centralized-payments-accounts-receivable)
- [Close Accounts receivable](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/close-accounts-receivable)
- [Posting profiles overview](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/pstg-prfles-ovrvw)
- [Recommended practices for posting profiles](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/recommended-practices-pstg-prfles)
- [Foreign currency revaluation for AP and AR](https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/foreign-currency-revaluation-accounts-payable-accounts-receivable)
- [Data management overview](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-entities-data-packages)

---
