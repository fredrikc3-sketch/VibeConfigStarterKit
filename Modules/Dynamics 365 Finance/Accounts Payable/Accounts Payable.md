# Accounts Payable Module - Knowledge Source

> This file is the central knowledge hub for the **Accounts Payable** module within Dynamics 365 Finance.

---


---


> **Microsoft Learn Reference:** [Accounts Payable](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounts-payable)

## Module Overview

The Accounts Payable module manages the full vendor payment lifecycle in Dynamics 365 Finance. It handles vendor master data, purchase order invoicing, invoice matching (two-way and three-way), payment processing, cash discounts, prepayments, and 1099 reporting. It integrates tightly with Procurement, General Ledger, and Cash & Bank Management.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Vendor Management** | Create and manage vendor master records, bank accounts, and payment terms |
| **Invoice Processing** | Record vendor invoices manually or via automation (OCR, electronic invoicing) |
| **Invoice Matching** | Match invoices against purchase orders and product receipts (2-way, 3-way matching) |
| **Payment Processing** | Generate vendor payment proposals, create payments, and manage payment journals |
| **Cash Discounts** | Configure and apply early payment discounts automatically |
| **Vendor Settlements** | Settle open vendor transactions and manage credit notes |
| **Charges & Auto-charges** | Define charges codes and automatic charges for purchase transactions |
| **Prepayments** | Manage vendor prepayments and prepayment invoices |
| **1099 Reporting** | Track and report 1099 tax information for US vendors |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 120 - Accounts Payable (`120 - Accounts payable.json`)

Accounts Payable configuration and master data entities.

| Seq | Entity Name | Target Entity | Category |
|-----|-------------|---------------|----------|
| 10 | 1099 fields | Tax1099FieldsEntity | |
| 10 | Aging period definitions | AgingPeriodDefinitionEntity | AP and AR Shared - Setup |
| 10 | Business segments | smmBusinessSegmentEntity | AP - Vendor attributes |
| 10 | Buyer groups | InventBuyerGroupEntity | AP - Vendor attributes |
| 10 | Cash discount | CashDiscountEntity | AP and AR Shared - Setup |
| 10 | Delivery charges groups | DlvChargeDeliveryGroupEntity | AP and AR Shared - Setup |
| 10 | Destination code | DeliveryDestinationEntity | AP - Vendor attributes |
| 10 | Expedite codes | MCRExpediteCodeEntity | AP - Vendor attributes |
| 10 | Item charge groups | InventChargeProductGroupEntity | AP - Vendor attributes |
| 10 | Line discount vendor groups | PriceDiscLineDiscountVendorGroupEntity | AP - Vendor attributes |
| 10 | Line of business | LineOfBusinessEntity | AP and AR Shared - Setup |
| 10 | Payment calendar | PaymentCalendarEntity | |
| 10 | Payment day lines | PaymentDayEntity | AP and AR Shared - Setup |
| 10 | Payment schedule | PaymentScheduleEntity | AP and AR Shared - Setup |
| 10 | Price vendor groups | PriceDiscPriceVendorGroupEntity | AP - Vendor attributes |
| 10 | Procurement charge codes | PurchProcurementChargeEntity | AP - Vendor attributes |
| 10 | Product categories | EcoResProductCategoryEntity | |
| 10 | Product category hierarchies | EcoResProductCategoryHierarchyEntity | |
| 10 | Product category hierarchy translations | EcoResProductCategoryHierarchyTranslationEntity | |
| 10 | Product category translations | EcoResProductCategoryTranslationEntity | |
| 10 | Purchase pools | PurchPurchaseOrderPoolEntity | AP - Vendor attributes |
| 10 | Sales tax groups | TaxGroupEntity | |
| 10 | Terms of delivery | DeliveryTermsEntity | AP and AR Shared - Setup |
| 10 | Terms of payment | PaymentTermEntity | AP and AR Shared - Setup |
| 10 | Total discount vendor groups | PriceDiscTotalDiscountVendorGroupEntity | AP - Vendor attributes |
| 10 | Vendor charges group | VendChargeVendorGroupEntity | AP - Vendor attributes |
| 10 | Vendor exception groups | VendorExceptionGroupEntity | AP - Vendor attributes |
| 10 | Vendor invoice policy rule types | VendInvoicePolicyRuleTypeEntity | |
| 10 | Vendor payment fee | VendorPaymentFeeEntity | AP - Vendor payment setup |
| 10 | Vendor payment format | VendorPaymentFormatEntity | |
| 10 | Vendor payment method | VendorPaymentMethodEntity | AP - Vendor payment setup |
| 10 | Vendor price tolerance groups | VendorPriceToleranceGroupEntity | |
| 10 | Vendor reasons | VendVendorReasonsEntity | AP - Vendor attributes |
| 10 | Vendor, form parameters | VendorFormSetupEntity | |
| 20 | Business subsegments | smmBusinessSubsegmentEntity | AP - Vendor attributes |
| 20 | Modes of delivery | DlvDeliveryModeEntity | AP - Vendor attributes |
| 20 | Multiline discount vendor groups | PriceDiscMultilineDiscountVendorGroupEntity | AP - Vendor attributes |
| 20 | Payment schedule lines | PaymentScheduleLineEntity | AP and AR Shared - Setup |
| 20 | Product category hierarchy roles | EcoResProductCategoryHierarchyRoleEntity | |
| 20 | Vendor groups | VendVendorGroupEntity | AP - Vendors |
| 20 | Vendor invoice form printing configurations | VendFormletterVendorInvoiceFormPrintingConfigurationEntity | |
| 20 | Vendor payment method specification | VendorPaymentMethodSpecificationEntity | AP - Vendor payment setup |
| 30 | Payment calendar rule | PaymentCalendarRuleEntity | |
| 35 | Vendors V2 | VendVendorV2Entity | |
| 40 | Vendor bank accounts | VendVendorBankAccountEntity | AP - Vendors |
| 45 | Vendor posting profile | VendorPostingProfileHeaderEntity | AP - Parameters |
| 50 | Vendor ledger accounts | VendorPostingProfileLineEntity | AP - Parameters |
| 60 | Vendor parameters | vendVendorParametersEntity | AP - Parameters |

---

### Shared Entities (AP & AR)

Several entities are shared between Accounts Payable and Accounts Receivable and should be loaded once (typically via the AP template as it is loaded first):

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

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Accounts Payable** module.

### Source to pay

*29 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze procurement and sourcing | 1 | — |
| Develop procurement and sourcing strategy | 8 | — |
| Manage accounts payable | 20 | — |

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
| 1099 fields | `Tax1099FieldsEntity` | `Tax1099Fields` | verified |
| Aging period definitions | `AgingPeriodDefinitionEntity` | `AgingPeriodDefinitions` | verified |
| Buyer groups | `InventBuyerGroupEntity` | `BuyerGroups` | manual-unverified |
| Cash discount | `CashDiscountEntity` | `CashDiscounts` | verified |
| Line discount vendor groups | `PriceDiscLineDiscountVendorGroupEntity` | `LineDiscountVendorGroups` | verified |
| Line of business | `LineOfBusinessEntity` | `LineOfBusinesses` | manual-unverified |
| Payment calendar | `PaymentCalendarEntity` | `PaymentCalendars` | verified |
| Payment day lines | `PaymentDayEntity` | `PaymentDays` | verified |
| Payment schedule | `PaymentScheduleEntity` | `PaymentSchedules` | verified |
| Price vendor groups | `PriceDiscPriceVendorGroupEntity` | `PriceVendorGroups` | verified |
| Product categories | `EcoResProductCategoryEntity` | `ProductCategories` | verified |
| Product category hierarchies | `EcoResProductCategoryHierarchyEntity` | `ProductCategoryHierarchies` | verified |
| Purchase pools | `PurchPurchaseOrderPoolEntity` | `PurchaseOrderPools` | manual-unverified |
| Sales tax groups | `TaxGroupEntity` | `TaxGroups` | verified |
| Terms of delivery | `DeliveryTermsEntity` | `DeliveryTerms` | verified |
| Terms of payment | `PaymentTermEntity` | `PaymentTerms` | verified |
| Total discount vendor groups | `PriceDiscTotalDiscountVendorGroupEntity` | `TotalDiscountVendorGroups` | verified |
| Vendor exception groups | `VendorExceptionGroupEntity` | `VendorExceptionGroups` | verified |
| Vendor payment fee | `VendorPaymentFeeEntity` | `VendorPaymentFees` | verified |
| Vendor payment method | `VendorPaymentMethodEntity` | `VendorPaymentMethods` | verified |
| Vendor price tolerance groups | `VendorPriceToleranceGroupEntity` | `VendorPriceToleranceGroups` | verified |
| Modes of delivery | `DlvDeliveryModeEntity` | `DeliveryModesV2` | verified |
| Multiline discount vendor groups | `PriceDiscMultilineDiscountVendorGroupEntity` | `MultilineDiscountVendorGroups` | verified |
| Payment schedule lines | `PaymentScheduleLineEntity` | `PaymentScheduleLines` | verified |
| Product category hierarchy roles | `EcoResProductCategoryHierarchyRoleEntity` | `ProductCategoryHierarchyRoles` | verified |
| Vendor groups | `VendVendorGroupEntity` | `VendorGroups` | verified |
| Vendor payment method specification | `VendorPaymentMethodSpecificationEntity` | `VendorPaymentMethodSpecifications` | verified |
| Vendors V2 | `VendVendorV2Entity` | `VendorsV2` | verified |
| Vendor bank accounts | `VendVendorBankAccountEntity` | `VendorBankAccounts` | verified |
| Vendor posting profile | `VendorPostingProfileHeaderEntity` | `PostingProfileHeaders` | verified |
| Vendor ledger accounts | `VendorPostingProfileLineEntity` | `PostingProfileLines` | verified |
| Vendor parameters | `vendVendorParametersEntity` | `VendorParameters` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Business segments | `smmBusinessSegmentEntity` |
| Delivery charges groups | `DlvChargeDeliveryGroupEntity` |
| Destination code | `DeliveryDestinationEntity` |
| Expedite codes | `MCRExpediteCodeEntity` |
| Item charge groups | `InventChargeProductGroupEntity` |
| Procurement charge codes | `PurchProcurementChargeEntity` |
| Product category hierarchy translations | `EcoResProductCategoryHierarchyTranslationEntity` |
| Product category translations | `EcoResProductCategoryTranslationEntity` |
| Vendor charges group | `VendChargeVendorGroupEntity` |
| Vendor invoice policy rule types | `VendInvoicePolicyRuleTypeEntity` |
| Vendor payment format | `VendorPaymentFormatEntity` |
| Vendor reasons | `VendVendorReasonsEntity` |
| Vendor, form parameters | `VendorFormSetupEntity` |
| Business subsegments | `smmBusinessSubsegmentEntity` |
| Vendor invoice form printing configurations | `VendFormletterVendorInvoiceFormPrintingConfigurationEntity` |
| Payment calendar rule | `PaymentCalendarRuleEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to AP operations including Procure to Pay:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key AP-related business process areas:
- Procure to Pay (end-to-end)
- Vendor invoice processing and matching
- Payment processing and settlement
- Foreign currency revaluation (AP)
- Period close (AP subledger reconciliation)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Work with accounts payable in Dynamics 365 Finance** | https://learn.microsoft.com/en-us/training/paths/work-accounts-payable-dyn365-finance/ |
| Configure Accounts payable in Dynamics 365 Finance | https://learn.microsoft.com/en-us/training/modules/configure-accounts-payable-dyn365-finance/ |
| Process purchase order invoices | https://learn.microsoft.com/en-us/training/modules/purchase-order-invoices-finance/ |
| Work with accounts payable daily procedures | https://learn.microsoft.com/en-us/training/modules/work-accounts-payable-daily-finance/ |
| Work with accounts payable invoice matching | https://learn.microsoft.com/en-us/training/modules/work-invoice-matching-finance/ |
| Accounting distributions, invoice validations, and settlements | https://learn.microsoft.com/en-us/training/modules/accounting-distributions-invoice-validation-dyn365-finance/ |
| Set up and use Intelligent OCR for vendor invoices | https://learn.microsoft.com/en-us/training/modules/ocr-vendor-invoices-finance/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Accounts payable home page | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounts-payable |
| Configure Accounts payable overview | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounts-payable-overview |
| Vendor posting profiles | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-posting-profiles |
| Vendor invoice automation | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-invoice-automation |
| Invoice capture overview | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/invoice-capture-overview |
| AP invoice matching overview | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounts-payable-invoice-matching |
| Three-way matching policies | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/three-way-matching-policies |
| Positive pay overview | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/positive-pay-overview |
| Centralized payments for AP | https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/centralized-payments-accounts-payable |
| Posting profiles overview | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/pstg-prfles-ovrvw |
| Recommended practices for posting profiles | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/recommended-practices-pstg-prfles |
| Foreign currency revaluation for AP and AR | https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/foreign-currency-revaluation-accounts-payable-accounts-receivable |

---

## 6-Phase Configuration Sequence

### Phase 1: Prerequisites (GL & Bank)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Payment journals | General ledger > Journal setup > Journal names | Journal templates for payments |
| Currencies | General ledger > Currencies > Currencies | Currency codes for AP transactions |
| Exchange rate types | General ledger > Currencies > Exchange rate types | Rate type classification |
| Exchange rates | General ledger > Currencies > Currency exchange rates | Daily/periodic rates |
| Bank accounts | Cash and bank management > Bank accounts > Bank accounts | Bank accounts for payment methods |
| Financial dimensions | General ledger > Chart of accounts > Dimensions > Financial dimensions | Dimensions used in AP posting |

### Phase 2: Shared Payment Setup

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

### Phase 3: AP Module Configuration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| VendGroup | Accounts payable > Vendors > Vendor groups | Vendor groupings for posting/settlement |
| VendPaymMode | Accounts payable > Payment setup > Methods of payment | Payment method definitions |
| VendPaymFee | Accounts payable > Payment setup > Payment fee | Vendor payment fees |
| VendorFormSetup | Accounts payable > Setup > Form setup | Document format configuration |
| VendInvoicePolicy | Accounts payable > Policy setup > Vendor invoice policies | Invoice validation policies |
| MarkupTable (Purch) | Accounts payable > Charges setup > Charges code | Procurement charge codes |
| VendChargeGroup | Accounts payable > Charges setup > Vendor charges group | Vendor charge group codes |
| InventChargeGroup | Accounts payable > Charges setup > Item charge groups | Item charge group codes |

### Phase 4: Posting Profiles & Parameters

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| VendPosting (Header) | Accounts payable > Setup > Vendor posting profiles | AP posting profile definitions |
| VendPosting (Lines) | (Within posting profile) | AP summary account assignments |
| VendParm | Accounts payable > Setup > Accounts payable parameters | AP module-wide settings |

**Posting Profile Priority:**

| Account Code | Account/Group Number | Search Priority |
|--------------|---------------------|-----------------|
| **Table** | Specific vendor account | 1 (most specific) |
| **Group** | Vendor group | 2 |
| **All** | Blank | 3 (least specific) |

### Phase 5: Vendor Master Data

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| VendTable | Accounts payable > Vendors > All vendors | Vendor master records |
| VendBankAccount | (Within vendor record) | Vendor bank accounts |

### Phase 6: Invoice Matching & Advanced Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| VendInvoiceMatchingTotals | Accounts payable > Setup > Invoice matching > Invoice totals tolerances | Invoice total tolerance |
| VendInvoiceMatchingPolicy | Accounts payable > Setup > Invoice matching > Matching policy | Two-way / three-way matching |
| VendPriceTolerance | Accounts payable > Setup > Invoice matching > Price tolerances | Unit price tolerance |
| AutoCharges | Accounts payable > Setup > Charges > Automatic charges | Auto-assigned charges |

---

## Posting Profile Design

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      VENDOR POSTING PROFILE DESIGN                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   POSTING PROFILE: "GEN" (General)                                       │
│   ┌────────────────────────────────────────────────────────┐            │
│   │ Account Code: All                                       │            │
│   │ Summary Account: 2100 (Accounts Payable - Trade)        │            │
│   │ Settlement: Yes                                          │            │
│   └────────────────────────────────────────────────────────┘            │
│                                                                          │
│   POSTING PROFILE: "IC" (Intercompany)                                   │
│   ┌────────────────────────────────────────────────────────┐            │
│   │ Account Code: Group → IC Vendor Group                    │            │
│   │ Summary Account: 2443 (IC Payable)                       │            │
│   │ Settlement: Yes                                          │            │
│   └────────────────────────────────────────────────────────┘            │
│                                                                          │
│   KEY ACCOUNTS:                                                          │
│   • Summary Account → Trade AP (Balance Sheet liability)                │
│   • Liquidity Account → Cash flow forecast (optional)                   │
│   • Sales Tax Prepayment → Prepayment tax account                       │
│   • Discount Account → Purchase discount taken                          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## AP Business Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     PROCURE TO PAY - AP PROCESS FLOW                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. VENDOR INVOICE RECEIPT                                               │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Enter vendor invoice manually                          │          │
│     │ • Receive electronically via data entity                 │          │
│     │ • Use Invoice Capture (OCR) for scanned invoices         │          │
│     │ • Create via Invoice register / Approval journal         │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  2. INVOICE VALIDATION                                                   │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Invoice matching (2-way or 3-way)                      │          │
│     │   - Price matching (PO price vs invoice price)           │          │
│     │   - Quantity matching (receipt qty vs invoice qty)        │          │
│     │   - Totals matching (PO total vs invoice total)          │          │
│     │ • Vendor invoice policies                                │          │
│     │ • Workflow approval                                      │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  3. POSTING & ACCOUNTING                                                 │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Accounting distributions define GL posting             │          │
│     │ • Posting profile determines AP summary account          │          │
│     │ • Subledger journal entries created                      │          │
│     │ • Tax calculated and posted                              │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  4. PAYMENT PROCESSING                                                   │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Payment proposal (by due date / cash discount)         │          │
│     │ • Payment journal creation                               │          │
│     │ • Payment method (check, electronic, wire, etc.)         │          │
│     │ • Positive pay file generation                           │          │
│     │ • Centralized payments (multi-entity)                    │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  5. SETTLEMENT                                                           │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Automatic or manual settlement                         │          │
│     │ • Cash discount application                              │          │
│     │ • Partial payments                                       │          │
│     │ • Cross-company settlement                               │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Invoice Matching

### Matching Policy Types

| Policy | Description | Validates |
|--------|-------------|-----------|
| **Two-way matching** | Compares invoice to purchase order | Unit price |
| **Three-way matching** | Compares invoice to PO and product receipt | Unit price + Quantity |
| **Not required** | No automatic matching | N/A |

### Tolerance Configuration

| Tolerance Type | Purpose | Page |
|----------------|---------|------|
| Invoice totals | Total variance allowed per invoice | Invoice totals tolerances |
| Price tolerance | Per-unit price variance allowed | Price tolerances |
| Item price tolerance groups | Tolerance by item group | Item price tolerance groups |
| Vendor price tolerance groups | Tolerance by vendor group | Vendor price tolerance groups |
| Charges tolerance | Charges variance allowed | Charges tolerances |

---

## FY27 Environment - Validated Menu Items

*Verified against FY27 environment - February 2026*

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `VendParameters` | Accounts payable parameters | AP Setup |
| `VendGroup` | Vendor groups | AP Setup |
| `VendPosting` | Vendor posting profiles | AP Setup |
| `VendTable` | All vendors | AP Vendors |
| `VendBankAccounts` | Vendor bank accounts | AP Vendors |
| `PaymentTerms` | Terms of payment | Shared Setup |
| `CashDisc` | Cash discounts | Shared Setup |
| `PaymentDay` | Payment days | Shared Setup |
| `PaymentSched` | Payment schedules | Shared Setup |
| `VendPaymMode` | Methods of payment - Vendors | AP Payments |
| `VendPaymFee` | Payment fee | AP Payments |
| `VendEditInvoice` | Pending vendor invoices | AP Invoices |
| `VendInvoiceJour` | Invoice journal | AP Invoices |
| `LedgerJournalTable3` | Vendor payment journal | AP Payments |
| `VendInvoiceMatchingTotals` | Invoice totals tolerances | AP Matching |
| `VendInvoiceMatchingPolicy` | Matching policy | AP Matching |
| `VendPriceTolerance` | Price tolerances | AP Matching |
| `MarkupTable_Purch` | Charges code | AP Charges |
| `VendChargeGroup` | Vendor charges group | AP Charges |
| `PurchAutoCharges` | Automatic charges | AP Charges |
| `VendInvoiceWorkspace` | Vendor invoice entry workspace | Workspace |
| `VendPaymentWorkspace` | Vendor payments workspace | Workspace |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **General Ledger** must be configured before AP (chart of accounts, dimensions, fiscal calendar)
2. **Bank accounts** must exist before setting up payment methods
3. **Terms of payment** must be created before vendor records
4. **Vendor groups** must exist before creating vendor records
5. **Posting profiles** must be configured before any AP transactions
6. **Posting profile** must be set in AP **parameters** as the default profile
7. **Journal names** must exist before creating payment journals
8. **Number sequences** must be configured in AP parameters for vouchers, invoices, etc.
9. **Tax setup** (sales tax codes, groups, posting groups) must be complete before invoice posting

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Posting profile has not been set up" | AP Parameters missing default posting profile | Set posting profile in AP parameters |
| "Account number for transaction type Sales Tax does not exist" | Tax accounts missing PostingType = Tax | Update main account PostingType via OData, then configure Ledger Posting Groups |
| "Voucher already used" | Duplicate voucher number | Check number sequence setup in AP parameters |
| "Currency not defined" | Missing exchange rate for transaction currency | Add exchange rate for the date and currency pair |
| "You must select a value in the [Dimension] field" | Account structure requires dimension but posting profile has none | Update account structure to allow blank values (`"";*`) |
| "Payment method not defined" | Vendor has no payment method assigned | Assign default payment method on vendor record |
| "Bank account not valid for payment method" | Method of payment not linked to bank account | Configure bank account on method of payment |
| "Invoice matching discrepancy" | Invoice price/qty differs from PO beyond tolerance | Review tolerances or override match via workflow |
| "Settlement cannot be performed" | Currency mismatch between invoice and payment | Enable multi-currency on bank account or use correct currency |
| "Number must be defined as Continuous" (Denmark) | Legal entity requires continuous number sequences | Set Continuous = Yes on relevant number sequences |

---

## ⚠️ Critical Implementation Discoveries

### Posting Profile Must Be Set in Module Parameters

**Discovery:** Creating posting profiles alone is not sufficient. The default posting profile must be explicitly set in:
- **Accounts payable parameters** (Accounts payable > Setup > Accounts payable parameters > Ledger and sales tax tab)

Without this, all vendor invoice posting will fail with "Posting profile has not been set up."

### Tax Account PostingType for Invoice Posting

**Discovery (cross-reference from GL):** Vendor invoice posting fails with:
> "Account number for transaction type Sales Tax does not exist"

**Root Cause:** Main accounts for tax exist in chart of accounts BUT `PostingType` field is set to "None" instead of "Tax."

**Solution - Two-Step Process:**
1. Update main account PostingType to "Tax" via OData
2. Configure Ledger Posting Groups via UI (Tax > Setup > Sales tax > Ledger posting groups)

**Key Insight:** Every country implementation requires verification that tax accounts have correct PostingType. This should be part of the standard implementation checklist.

### Intercompany AP Account Setup

**Discovery from Swedish/Norwegian Implementation:** Intercompany transactions require dedicated GL accounts distinct from regular AP for proper elimination and tracking.

**Required IC Account Pairs:**

| Purpose | Originating Co. | Counterparty Co. | Relationship |
|---------|-----------------|-------------------|-------------|
| **IC Payable** | 2443 (AP koncern) | 1513 (AR koncern) | What we owe counterparty |

**Critical Configuration:**
1. GL Chart of Accounts (IC account 2443 created)
2. Separate **IC Vendor Group** (e.g., "INT")
3. **Posting profile** with Group = IC vendor group → IC summary account (2443)
4. **Intercompany Parameters** (accounts linked as IC pairs)
5. Dedicated IC journals (e.g., SWE-IC, NOR-IC)

### Bank Account Multi-Currency for IC Payments

**Discovery:** Cross-currency intercompany payments fail if bank account doesn't allow additional currencies.

**Error:** "Currency XXX not allowed for account YYYY"

**Solution:** Update bank account via OData:
```json
{
  "AllowTransactionsInAdditionalCurrencies": "Yes"
}
```

### Journal Names - Create Before Testing

**Best Practice:** Create all required AP journal names during initial configuration:

| Journal Type | Purpose | Type Code |
|--------------|---------|-----------|
| VendInvoice | Vendor invoice registration | 25 |
| VendPayment | Vendor payment disbursement | 42 |

---

## Database Logging for Posting Profiles

**Best Practice:** Set up database logging to audit changes to AP posting profiles and parameters tables.

| Page Name | Navigation Path | Table Name |
|-----------|----------------|------------|
| Accounts payable parameters | AP > Setup > AP parameters | VendParm |
| Vendor posting profile | AP > Setup > Vendor posting profile | VendPosting |
| Methods of payment (Vendor) | AP > Payment setup > Methods of payment | VendPaymMode |
| Payment fee (Vendor) | AP > Payment setup > Payment fee | VendPaymFee |
| Charges code | AP > Charges setup > Charges code | MarkupTable |
| Cash discounts | AP > Payment setup > Cash discounts | CashDisc |

---

## Vendor Master Data Key Fields

| Field | Purpose | Configuration Source |
|-------|---------|---------------------|
| Vendor account | Unique identifier | Number sequence |
| Vendor group | Posting/settlement grouping | Vendor groups |
| Terms of payment | Invoice due date rules | Terms of payment |
| Method of payment | Payment type/format | Methods of payment |
| Payment schedule | Installment plan | Payment schedules |
| Cash discount | Early payment terms | Cash discounts |
| Currency | Transaction currency | Currency setup |
| Sales tax group | Tax calculation group | Tax setup |
| Posting profile | Override default profile | Posting profiles |
| Payment days | Payment day rules | Payment days |
| 1099 box (US) | Tax reporting category | 1099 fields |

---

## AP Posting Account Types

| Posting Type | Typical Account | Description |
|--------------|-----------------|-------------|
| Vendor balance | 2100-2199 | Trade AP summary account |
| Purchase expenditure for product | 5xxx-6xxx | Expense/COGS accounts |
| Purchase expenditure, un-invoiced | 2200 | Accrued liabilities (receipt not invoiced) |
| Purchase accrual | 2201 | Product receipt accrual clearing |
| Discount | 5xxx | Purchase discount taken |
| Sales tax payable | 2610 | Output VAT / Sales tax payable |
| Sales tax receivable | 1576 | Input VAT / Sales tax receivable |

---

## Data Migration Sequence

```
 1. Shared Payment Setup
    1.1 Terms of payment
    1.2 Payment days
    1.3 Payment schedules + lines
    1.4 Cash discounts
    1.5 Payment calendars + rules
    1.6 Aging period definitions
    1.7 Terms of delivery
    1.8 Modes of delivery
    1.9 Line of business

 2. Accounts Payable Setup
    2.1 Vendor groups
    2.2 Vendor payment methods + specifications
    2.3 Vendor payment fees
    2.4 Procurement charge codes
    2.5 Vendor charge groups
    2.6 Buyer groups / Price groups / Discount groups
    2.7 Product category hierarchies + categories
    2.8 Vendor invoice policies

 3. Posting Profiles & Parameters
    3.1 Vendor posting profiles (header + lines)
    3.2 Accounts payable parameters

 4. Master Data
    4.1 Vendors V2 (with exclusions for bank account, site, warehouse)
    4.2 Vendor bank accounts
```

---

## ⚠️ Best Practices

```
┌────────────────────────────────────────────────────────────────┐
│            ACCOUNTS PAYABLE IMPLEMENTATION BEST PRACTICES        │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  POSTING PROFILES                                              │
│  ✓ Always configure a default "All" posting profile            │
│  ✓ Use Group-level profiles for IC and special categories      │
│  ✓ Set default profile in AP Parameters immediately            │
│  ✓ Enable database logging on posting profile tables           │
│  ✓ Test invoicing immediately after posting profile setup      │
│                                                                 │
│  VENDOR GROUPS                                                 │
│  ✓ Create groups based on reporting/posting requirements       │
│  ✓ Separate IC vendors into dedicated groups                   │
│  ✓ Use groups to drive payment terms defaults                  │
│  ✓ Keep group structure manageable (3-10 groups)               │
│                                                                 │
│  PAYMENT SETUP                                                 │
│  ✓ Configure payment methods before creating vendors           │
│  ✓ Link bank accounts to payment methods explicitly            │
│  ✓ Test bank file export format with bank before go-live       │
│  ✓ Enable positive pay for check payments                      │
│  ✓ Verify multi-currency settings on bank accounts for IC      │
│                                                                 │
│  INVOICE MATCHING                                              │
│  ✓ Start with tolerances that match business requirements      │
│  ✓ Use 3-way matching for physical goods                       │
│  ✓ Use 2-way matching for services                             │
│  ✓ Configure workflow for matching exceptions                  │
│                                                                 │
│  TAX SETUP                                                     │
│  ✓ Verify tax account PostingType = Tax before invoice testing │
│  ✓ Configure Ledger Posting Groups via UI (not OData)          │
│  ✓ Test with a vendor invoice early in implementation          │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

---

## Related Modules

| Module | Relationship |
|--------|--------------|
| **General Ledger** | AP posts to GL via posting profiles; shared CoA and dimensions |
| **Accounts Receivable** | Shared payment setup entities; IC counterparty |
| **Cash & Bank Management** | Bank accounts for payment methods; settlement and reconciliation |
| **Tax** | Sales tax codes/groups used in AP invoicing; tax posting groups |
| **Procurement & Sourcing** | Purchase orders flow into AP invoices |
| **Inventory Management** | Product receipts trigger AP accruals |
| **Project Accounting** | Project expenses post to AP |
| **Budgeting** | Budget control on AP invoices and purchase orders |
| **Expense Management** | Employee expense reports create AP vendor invoices |
| **Fixed Assets** | Asset purchases via AP |

---

## References

- [Accounts payable home page](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounts-payable)
- [Configure Accounts payable overview](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounts-payable-overview)
- [Vendor posting profiles](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-posting-profiles)
- [Three-way matching policies](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/three-way-matching-policies)
- [Vendor invoice automation](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-invoice-automation)
- [Invoice capture overview](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/invoice-capture-overview)
- [Positive pay overview](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/positive-pay-overview)
- [Centralized payments for AP](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/centralized-payments-accounts-payable)
- [Posting profiles overview](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/pstg-prfles-ovrvw)
- [Recommended practices for posting profiles](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/recommended-practices-pstg-prfles)
- [Foreign currency revaluation for AP and AR](https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/foreign-currency-revaluation-accounts-payable-accounts-receivable)
- [Data management overview](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-entities-data-packages)

---
