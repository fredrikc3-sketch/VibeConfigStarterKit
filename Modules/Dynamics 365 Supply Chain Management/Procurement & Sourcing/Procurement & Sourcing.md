# Procurement & Sourcing Module - Knowledge Source

> This file is the central knowledge hub for the **Procurement & Sourcing** module within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Procurement & Sourcing](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/procurement-sourcing-overview)

## Module Overview

The Procurement & Sourcing module in Dynamics 365 Supply Chain Management manages the complete procurement lifecycle from requisitioning through purchase order receipt. It supports purchase requisitions, RFQs, purchase agreements, vendor collaboration, procurement catalogs, and category-based purchasing with policy enforcement.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Purchase Requisitions** | Employee-initiated requests for goods and services with workflow approval |
| **Purchase Orders** | Create, confirm, and manage purchase orders with change management |
| **Request for Quotation (RFQ)** | Solicit and compare vendor quotes for competitive bidding |
| **Purchase Agreements** | Establish long-term vendor contracts with commitment tracking |
| **Vendor Collaboration** | Enable vendors to view POs, submit invoices, and manage consignment |
| **Procurement Catalogs** | Define internal and external catalogs for guided purchasing |
| **Procurement Policies** | Set purchasing policies for spending limits, approvals, and categories |
| **Charges & Auto-charges** | Configure automatic charges for procurement transactions |
| **Product Receipt** | Record product receipts and three-way matching against orders |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 320 - Procurement and Sourcing (`320 - Procurement and sourcing.json`)

Procurement and sourcing configuration entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Trade agreement journal names | TradeAgreementJournalNameEntity | Procurement - Journals | 30 |
| 10 | Purchase agreement classifications | PurchAgreementClassificationEntity | Procurement - Agreements | 30 |
| 10 | Request for quotation scoring method | RFQScoringMethodEntity | Procurement - RFQ | 30 |
| 10 | Request for quotation solicitation types | RFQSolicitationTypeEntity | Procurement - RFQ | 30 |
| 10 | Vendor evaluation criteria | VendEvaluationCriteriaEntity | Procurement - Vendors | 30 |
| 10 | Vendor evaluation criteria groups | VendEvaluationCriteriaGroupEntity | Procurement - Vendors | 30 |
| 10 | Vendor rebate groups | VendRebateGroupEntity | Procurement - Pricing | 30 |
| 10 | Vendor rebate parameters | VendRebateParametersEntity | Procurement - Pricing | 30 |
| 10 | Modes of delivery | ModesOfDeliveryEntity | Procurement - Delivery | 30 |
| 10 | Discount groups - Customer line | DiscountGroupCustomerLineEntity | Procurement - Pricing | 30 |
| 10 | Discount groups - Customer multiline | DiscountGroupCustomerMultilineEntity | Procurement - Pricing | 30 |
| 10 | Discount groups - Vendor line | DiscountGroupVendorLineEntity | Procurement - Pricing | 30 |
| 10 | Discount groups - Vendor multiline | DiscountGroupVendorMultilineEntity | Procurement - Pricing | 30 |
| 20 | Procurement document default values | ProcurementDocumentDefaultEntity | Procurement - Defaults | 40 |
| 20 | Procurement document policy rules | ProcurementDocumentPolicyRuleEntity | Procurement - Policies | 40 |
| 20 | Form printing configurations | FormPrintingConfigurationEntity | Procurement - Forms | 40 |
| 20 | Approved vendor lists | ApprovedVendorListEntity | Procurement - Vendors | 40 |
| 20 | Price tolerances | PriceToleranceEntity | Procurement - Tolerances | 40 |
| 20 | Invoice tolerances | InvoiceToleranceEntity | Procurement - Tolerances | 40 |

**DMF Load Order Notes:**
- **Seq 10** contains foundational setup — journal names, agreement classifications, RFQ configuration, vendor evaluation, rebate groups, discount groups, delivery modes
- **Seq 20** contains dependent entities — procurement defaults, policy rules, form printing, approved vendor lists, and tolerance settings
- Trade agreement journal names must exist before trade agreements can be created
- Purchase agreement classifications must exist before purchase agreements
- Vendor groups and vendor records should be loaded before approved vendor lists

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (journal names, classifications, scoring, evaluation, discount groups, delivery modes)
- **Level 40:** Dependent entities (procurement defaults, policies, approved vendor lists, tolerances)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Procurement & Sourcing** module.

### Source to pay

*90 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze procurement and sourcing | 5 | — |
| Develop procurement and sourcing strategy | 27 | [Learn more](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/procurement-catalogs) |
| Manage accounts payable | 4 | — |
| Manage supplier relationships | 32 | — |
| Procure goods and services | 10 | — |
| Source and contract goods and services | 12 | — |

### Inventory to deliver

*179 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze warehouse operations | 14 | — |
| Maintain inventory levels | 37 | — |
| Manage freight and transportation | 9 | — |
| Manage inventory quality | 50 | — |
| Manage warehouse operations | 23 | — |
| Process inbound goods | 22 | — |
| Process outbound goods | 24 | — |

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Trade agreement journal names | `TradeAgreementJournalNameEntity` | `TradeAgreementJournalNames` | verified |
| Purchase agreement classifications | `PurchAgreementClassificationEntity` | `PurchaseAgreementClassifications` | manual-unverified |
| Modes of delivery | `ModesOfDeliveryEntity` | `DeliveryModesV2` | verified |
| Approved vendor lists | `ApprovedVendorListEntity` | `ProductApprovedVendors` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Request for quotation scoring method | `RFQScoringMethodEntity` |
| Request for quotation solicitation types | `RFQSolicitationTypeEntity` |
| Vendor evaluation criteria | `VendEvaluationCriteriaEntity` |
| Vendor evaluation criteria groups | `VendEvaluationCriteriaGroupEntity` |
| Vendor rebate groups | `VendRebateGroupEntity` |
| Vendor rebate parameters | `VendRebateParametersEntity` |
| Discount groups - Customer line | `DiscountGroupCustomerLineEntity` |
| Discount groups - Customer multiline | `DiscountGroupCustomerMultilineEntity` |
| Discount groups - Vendor line | `DiscountGroupVendorLineEntity` |
| Discount groups - Vendor multiline | `DiscountGroupVendorMultilineEntity` |
| Procurement document default values | `ProcurementDocumentDefaultEntity` |
| Procurement document policy rules | `ProcurementDocumentPolicyRuleEntity` |
| Form printing configurations | `FormPrintingConfigurationEntity` |
| Price tolerances | `PriceToleranceEntity` |
| Invoice tolerances | `InvoiceToleranceEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Procurement & Sourcing:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Procurement-related business process areas:
- **Procure to Pay** (requisition, RFQ, purchase order, receiving, invoicing)
- **Vendor management** (vendor onboarding, evaluation, collaboration)
- **Purchase agreements** (blanket orders, contract management)
- **Trade agreements** (price/discount management)
- **Procurement categories** (indirect procurement)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and use procurement and sourcing in Dynamics 365 Supply Chain Management** | https://learn.microsoft.com/en-us/training/paths/configure-use-procurement-sourcing-dyn365-supply-chain-mgmt/ |
| Get started with procurement | https://learn.microsoft.com/en-us/training/modules/get-started-procurement-sourcing-dyn365-supply-chain-mgmt/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Procurement and sourcing home page | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/procurement-sourcing-overview |
| Purchase order overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-overview |
| Purchase requisitions | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-requisitions-overview |
| Request for quotations | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/request-quotations |
| Purchase agreements | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-agreements |
| Vendor collaboration | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/vendor-collaboration-work-external-vendors |
| Procurement categories | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/procurement-catalogs |
| Vendor rebates | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/vendor-rebates |
| Three-way matching | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/three-way-matching-policies |
| Set up procurement policies | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/set-up-procurement-parameters |
| Approved vendor lists | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/maintain-approved-vendors |
| Trade agreements | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/trade-agreement-certification |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites (Organization & GL)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Legal entities | Organization administration > Organizations > Legal entities | Company setup |
| Main accounts | General ledger > Chart of accounts > Accounts > Main accounts | Procurement accounts |
| Number sequences | Organization administration > Number sequences | PO, requisition, RFQ numbers |
| Vendor groups | Accounts payable > Setup > Vendor groups | Vendor classification |
| Vendors | Accounts payable > Vendors > All vendors | Vendor master data |

### Phase 2: Procurement Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| TradeAgreementJournalName | Procurement > Setup > Trade agreement journal names | Trade agreement journals |
| PurchAgreementClassification | Procurement > Setup > Purchase agreement classifications | Agreement types |
| RFQScoringMethod | Procurement > Setup > Request for quotation > Scoring methods | RFQ evaluation scoring |
| RFQSolicitationType | Procurement > Setup > Request for quotation > Solicitation types | RFQ type definitions |
| ModesOfDelivery | Procurement > Setup > Distribution > Modes of delivery | Delivery methods |

### Phase 3: Vendor Management

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| VendEvaluationCriteria | Procurement > Setup > Vendor evaluation > Criteria | Evaluation criteria definitions |
| VendEvaluationCriteriaGroup | Procurement > Setup > Vendor evaluation > Criteria groups | Criteria groupings |
| ApprovedVendorList | Procurement > Setup > Vendors > Approved vendor list | Pre-approved vendor/item combinations |

### Phase 4: Pricing & Discounts

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| DiscountGroup - VendorLine | Procurement > Setup > Pricing > Discount groups | Vendor line discount groups |
| DiscountGroup - VendorMultiline | Procurement > Setup > Pricing > Discount groups | Vendor multiline discount groups |
| VendRebateGroup | Procurement > Setup > Pricing > Vendor rebate groups | Rebate group definitions |
| VendRebateParameters | Procurement > Setup > Pricing > Vendor rebate parameters | Rebate module parameters |

### Phase 5: Policies, Tolerances & Defaults

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| ProcurementDocumentDefault | Procurement > Setup > Procurement > Document defaults | PO document defaults |
| ProcurementDocumentPolicyRule | Procurement > Setup > Policies > Purchasing policies | Procurement policy rules |
| PriceTolerance | Procurement > Setup > Prices > Price tolerances | Price matching tolerances |
| InvoiceTolerance | Procurement > Setup > Prices > Invoice tolerances | Invoice matching tolerances |
| FormPrintingConfiguration | Procurement > Setup > Forms > Form setup | Form printing settings |

---

## Procure-to-Pay Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     PROCURE-TO-PAY PROCESS FLOW                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. REQUISITION & SOURCING                                               │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Purchase requisition (internal request)                │          │
│     │ • Request for quotation (RFQ) to vendors                 │          │
│     │ • Evaluate bids using scoring methods                    │          │
│     │ • Select vendor and award RFQ                            │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  2. PURCHASE ORDERING                                                    │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Create purchase order (manual, from requisition, RFQ)  │          │
│     │ • Apply trade agreements / purchase agreements            │          │
│     │ • Purchase order approval workflow                       │          │
│     │ • Confirm purchase order to vendor                       │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  3. RECEIVING                                                            │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Product receipt (physical receipt of goods)             │          │
│     │ • Quality inspection (if quality management active)      │          │
│     │ • Put away to warehouse location                         │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  4. INVOICING & PAYMENT                                                  │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Vendor invoice registration                            │          │
│     │ • Three-way matching (PO vs receipt vs invoice)          │          │
│     │ • Invoice approval and posting                           │          │
│     │ • Payment processing (in AP)                             │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `PurchTable` | All purchase orders | Orders |
| `PurchReqTable` | All purchase requisitions | Requisitions |
| `RFQCaseTable` | All requests for quotations | RFQ |
| `PurchAgreement` | Purchase agreements | Agreements |
| `TradeAgreementJournalNames` | Trade agreement journal names | Setup |
| `ProcParameters` | Procurement and sourcing parameters | Setup |
| `VendTable` | All vendors | Vendors |
| `ApprovedVendorList` | Approved vendor list | Setup |
| `VendEvaluationCriteria` | Vendor evaluation criteria | Setup |
| `PurchPolicy` | Purchasing policies | Policies |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Vendor master records** must exist before approved vendor lists, purchase orders, or agreements
2. **Trade agreement journal names** must exist before trade agreement journals can be created
3. **Purchase agreement classifications** define agreement types — must exist before agreements
4. **Procurement policies** should be configured before users begin creating requisitions
5. **Matching policies** (2-way, 3-way) must be configured for invoice validation
6. **Price/invoice tolerances** should be set before invoice processing begins
7. **RFQ scoring methods** must exist before RFQ evaluation
8. **Procurement categories** should be configured for indirect purchasing

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Vendor not found" | Vendor not created in legal entity | Create vendor record |
| "Purchase order matching failed" | Invoice exceeds tolerance | Review tolerances or override with approval |
| "No active trade agreement" | Trade agreement expired or not found | Create/extend trade agreement |
| "Vendor not approved for item" | Item not on approved vendor list | Add vendor/item to approved list |
| "RFQ cannot be sent" | Missing vendor email or portal setup | Configure vendor communication |
| "Purchase requisition workflow error" | Workflow not configured | Set up purchase requisition workflow |
