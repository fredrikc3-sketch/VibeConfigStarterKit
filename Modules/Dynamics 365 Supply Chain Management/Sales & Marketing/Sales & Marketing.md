# Sales & Marketing Module - Knowledge Source

> This file is the central knowledge hub for the **Sales & Marketing** module within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Sales & Marketing](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/overview-sales-marketing)

## Module Overview

The Sales & Marketing module in Dynamics 365 Supply Chain Management manages the order-to-cash process from sales quotations through sales order fulfillment. It supports sales quotations, sales orders, sales agreements, pricing and discounts, commissions, customer returns, and intercompany trading. It integrates with CRM for prospect and opportunity management.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Sales Quotations** | Create and manage customer quotations with follow-up tracking |
| **Sales Orders** | Process sales orders with delivery scheduling, picking, packing, and invoicing |
| **Sales Agreements** | Establish long-term customer contracts with volume commitments |
| **Pricing & Discounts** | Configure trade agreements, price lists, and multi-tier discount structures |
| **Commissions** | Calculate and track sales commissions for representatives |
| **Customer Returns** | Manage return material authorizations (RMA) and return processing |
| **Intercompany Trading** | Process sales orders fulfilled through intercompany purchase orders |
| **Direct Delivery** | Ship products directly from vendor to customer (drop shipping) |
| **Order Promising** | Commit delivery dates using ATP (available-to-promise) and CTP calculations |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 330 - Sales and Marketing (`330 - Sales and marketing.json`)

Sales and marketing configuration entities. This is one of the largest DMF templates with approximately 96 entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Business classifications | SalesBusinessClassificationEntity | Sales - Setup | 30 |
| 10 | Business segments | SalesBusinessSegmentEntity | Sales - Setup | 30 |
| 10 | Commission sales groups | SalesCommissionGroupEntity | Sales - Commission | 30 |
| 10 | Commission customer groups | CommissionCustomerGroupEntity | Sales - Commission | 30 |
| 10 | Commission item groups | CommissionItemGroupEntity | Sales - Commission | 30 |
| 10 | Lead management scoring models | LeadScoringModelEntity | Marketing - Lead | 30 |
| 10 | Opportunity classifications | OpportunityClassificationEntity | Marketing - Opportunity | 30 |
| 10 | Activity types | ActivityTypeEntity | Marketing - Activities | 30 |
| 10 | Sales order origins | SalesOrderOriginEntity | Sales - Setup | 30 |
| 10 | Sales order pools | SalesOrderPoolEntity | Sales - Setup | 30 |
| 10 | Sales order hold codes | SalesOrderHoldCodeEntity | Sales - Setup | 30 |
| 10 | Discount groups - Customer line | DiscountGroupCustomerLineEntity | Sales - Pricing | 30 |
| 10 | Discount groups - Customer multiline | DiscountGroupCustomerMultilineEntity | Sales - Pricing | 30 |
| 10 | Rebate parameters | RebateParametersEntity | Sales - Rebates | 30 |
| 10 | Sales agreement classifications | SalesAgreementClassificationEntity | Sales - Agreements | 30 |
| 10 | Modes of delivery | ModesOfDeliveryEntity | Sales - Delivery | 30 |
| 10 | Delivery terms | DeliveryTermsEntity | Sales - Delivery | 30 |
| 10 | Quotation template groups | QuotationTemplateGroupEntity | Sales - Quotation | 30 |
| 20 | Commission calculation setup | CommissionCalculationEntity | Sales - Commission | 40 |
| 20 | Quotation templates | QuotationTemplateEntity | Sales - Quotation | 40 |
| 20 | Sales activity plans | SalesActivityPlanEntity | Marketing - Activities | 40 |
| 20 | Campaign management | CampaignManagementEntity | Marketing - Campaigns | 40 |
| 20 | Lead qualification models | LeadQualificationModelEntity | Marketing - Lead | 40 |
| 20 | Rebate groups | RebateGroupEntity | Sales - Rebates | 40 |
| 20 | Form printing configurations | FormPrintingConfigurationEntity | Sales - Forms | 40 |
| 20 | Procurement document default values | ProcurementDocumentDefaultEntity | Sales - Defaults | 40 |
| 30 | Sales and marketing parameters | SalesAndMarketingParametersEntity | Sales - Parameters | 50 |

**DMF Load Order Notes:**
- **Seq 10** contains foundational setup — business classifications, commission groups, discount groups, order settings (origins, pools, holds), agreement classifications, delivery terms, lead scoring, opportunity classifications
- **Seq 20** contains dependent entities — commission calculations (need commission groups), quotation templates, activity plans, rebate groups, form printing, campaign management
- **Seq 30** contains module parameters
- Commission groups (sales, customer, item) must exist before commission calculation setup
- Discount groups must be defined before trade agreements reference them
- Sales agreement classifications must exist before sales agreements

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (classifications, groups, codes, origins, delivery modes/terms)
- **Level 40:** Dependent entities (calculations, templates, plans, campaigns, rebate groups)
- **Level 50:** Module parameters (loaded last)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Sales & Marketing** module.

### Order to cash

*97 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze sales performance | 13 | — |
| Develop sales policies | 12 | — |
| Manage accounts receivable | 11 | — |
| Manage sales orders | 61 | — |

### Prospect to quote

*36 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Define sales strategy and policies | 9 | — |
| Estimate and quote sales | 11 | — |
| Identify and qualify leads | 1 | — |
| Manage customer relationships | 7 | — |
| Pursue opportunities | 8 | — |

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Commission sales groups | `SalesCommissionGroupEntity` | `SalesCommissionGroups` | manual-unverified |
| Sales order origins | `SalesOrderOriginEntity` | `SalesOrderOriginCodes` | verified |
| Sales order pools | `SalesOrderPoolEntity` | `SalesOrderPools` | verified |
| Sales order hold codes | `SalesOrderHoldCodeEntity` | `SalesOrderHoldCodes` | verified |
| Modes of delivery | `ModesOfDeliveryEntity` | `DeliveryModesV2` | verified |
| Delivery terms | `DeliveryTermsEntity` | `DeliveryTerms` | verified |
| Quotation template groups | `QuotationTemplateGroupEntity` | `SalesQuotationTemplateGroups` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Business classifications | `SalesBusinessClassificationEntity` |
| Business segments | `SalesBusinessSegmentEntity` |
| Commission customer groups | `CommissionCustomerGroupEntity` |
| Commission item groups | `CommissionItemGroupEntity` |
| Lead management scoring models | `LeadScoringModelEntity` |
| Opportunity classifications | `OpportunityClassificationEntity` |
| Activity types | `ActivityTypeEntity` |
| Discount groups - Customer line | `DiscountGroupCustomerLineEntity` |
| Discount groups - Customer multiline | `DiscountGroupCustomerMultilineEntity` |
| Rebate parameters | `RebateParametersEntity` |
| Sales agreement classifications | `SalesAgreementClassificationEntity` |
| Commission calculation setup | `CommissionCalculationEntity` |
| Quotation templates | `QuotationTemplateEntity` |
| Sales activity plans | `SalesActivityPlanEntity` |
| Campaign management | `CampaignManagementEntity` |
| Lead qualification models | `LeadQualificationModelEntity` |
| Rebate groups | `RebateGroupEntity` |
| Form printing configurations | `FormPrintingConfigurationEntity` |
| Procurement document default values | `ProcurementDocumentDefaultEntity` |
| Sales and marketing parameters | `SalesAndMarketingParametersEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Sales & Marketing:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Sales & Marketing-related business process areas:
- **Order to Cash** (quotation, order entry, delivery, invoicing)
- **Lead management** (lead capture, qualification, conversion)
- **Opportunity management** (pipeline tracking, win/loss)
- **Campaign management** (marketing campaigns, target lists)
- **Trade allowances** (rebates, bill-back, merchandising events)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and use sales and marketing in Dynamics 365 Supply Chain Management** | https://learn.microsoft.com/en-us/training/paths/configure-use-sales-marketing-dyn365-supply-chain-mgmt/ |
| Configure sales and marketing | https://learn.microsoft.com/en-us/training/modules/configure-sales-marketing-dyn365-supply-chain-mgmt/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Sales orders overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-orders-overview |
| Sales quotations | https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-quotation-template-mapping |
| Sales agreements | https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-agreements |
| Order promising (ATP/CTP) | https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations |
| Commission setup | https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-commissions |
| Intercompany trading | https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/intercompany-trade-set-up |
| Direct delivery | https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/direct-deliveries |
| Order holds | https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-order-holds |
| Credit management | https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/credit-management-overview |
| Rebate management | https://learn.microsoft.com/en-us/dynamics365/supply-chain/rebate-management/rebate-management-overview |
| Trade allowance management | https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/trade-allowance |
| Prospect to cash integration | https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/prospect-to-cash |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites (Customers, Products, GL)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Customer groups | Accounts receivable > Setup > Customer groups | Customer classification |
| Customers | Accounts receivable > Customers > All customers | Customer master data |
| Released products | Product information management > Products > Released products | Sellable items |
| Main accounts | General ledger > Chart of accounts | Revenue, COGS, discount accounts |
| Number sequences | Organization administration > Number sequences | Sales order, quotation numbers |

### Phase 2: Sales Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| SalesOrderOrigin | Sales and marketing > Setup > Sales orders > Order origins | Track how orders are created |
| SalesOrderPool | Sales and marketing > Setup > Sales orders > Order pools | Group orders for processing |
| SalesOrderHoldCode | Sales and marketing > Setup > Sales orders > Order hold codes | Hold reasons for orders |
| SalesAgreementClassification | Sales and marketing > Setup > Sales agreements > Classifications | Agreement type definitions |
| ModesOfDelivery | Sales and marketing > Setup > Distribution > Modes of delivery | Shipping methods |
| DeliveryTerms | Sales and marketing > Setup > Distribution > Delivery terms | Incoterms (CIF, FOB, etc.) |
| BusinessClassification | Sales and marketing > Setup > Customers > Business classifications | Customer business type |
| BusinessSegment | Sales and marketing > Setup > Customers > Business segments | Market segmentation |

### Phase 3: Pricing & Discounts

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| DiscountGroup - CustomerLine | Sales and marketing > Setup > Pricing > Discount groups | Customer line discount groups |
| DiscountGroup - CustomerMultiline | Sales and marketing > Setup > Pricing > Discount groups | Customer multiline discount groups |
| RebateParameters | Rebate management > Setup > Rebate management parameters | Rebate module settings |
| RebateGroup | Rebate management > Setup > Rebate groups | Customer/item rebate groups |

### Phase 4: Commission & Quotation Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| CommissionSalesGroup | Sales and marketing > Setup > Commissions > Sales groups | Sales rep commission groups |
| CommissionCustomerGroup | Sales and marketing > Setup > Commissions > Customer groups | Customer commission groups |
| CommissionItemGroup | Sales and marketing > Setup > Commissions > Item groups | Item commission groups |
| CommissionCalculation | Sales and marketing > Setup > Commissions > Commission calculation | Commission rates/rules |
| QuotationTemplateGroup | Sales and marketing > Setup > Quotations > Template groups | Quotation template categories |
| QuotationTemplate | Sales and marketing > Setup > Quotations > Templates | Predefined quotation templates |

### Phase 5: Marketing & Parameters

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| ActivityType | Sales and marketing > Setup > Activities > Activity types | Activity classification |
| LeadScoringModel | Sales and marketing > Setup > Leads > Scoring models | Lead scoring criteria |
| SalesActivityPlan | Sales and marketing > Setup > Activities > Activity plans | Activity plan templates |
| CampaignManagement | Sales and marketing > Campaigns | Campaign definitions |
| SalesAndMarketingParameters | Sales and marketing > Setup > Sales and marketing parameters | Module parameters |

---

## Order-to-Cash Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      ORDER-TO-CASH PROCESS FLOW                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. LEAD / OPPORTUNITY                                                   │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Capture lead (marketing campaign, web, manual)        │          │
│     │ • Qualify lead → Create opportunity                     │          │
│     │ • Track opportunity through pipeline stages             │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  2. QUOTATION                                                            │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Create sales quotation (from opportunity or direct)   │          │
│     │ • Apply trade agreements / pricing rules                │          │
│     │ • Send to customer, track follow-up                     │          │
│     │ • Confirm quotation → Convert to sales order            │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  3. SALES ORDER                                                          │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Create/confirm sales order                             │          │
│     │ • Credit check / order hold check                       │          │
│     │ • ATP/CTP delivery date calculation                     │          │
│     │ • Reserve inventory                                      │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  4. FULFILLMENT                                                          │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Pick / pack / ship                                     │          │
│     │ • Post packing slip (delivery note)                     │          │
│     │ • Update inventory + COGS                                │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  5. INVOICING                                                            │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Post sales invoice                                     │          │
│     │ • Apply commissions                                      │          │
│     │ • Process rebates / trade allowances                    │          │
│     │ • Customer payment (handled in AR)                      │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `SalesTable` | All sales orders | Orders |
| `SalesQuotationTable` | All quotations | Quotations |
| `SalesAgreement` | Sales agreements | Agreements |
| `CustTable` | All customers | Customers |
| `LeadTable` | Leads | Marketing |
| `OpportunityTable` | Opportunities | Marketing |
| `SalesAndMarketingParameters` | Sales and marketing parameters | Setup |
| `CommissionTrans` | Commission transactions | Commissions |
| `SalesOrderHoldCode` | Order hold codes | Setup |
| `RebateTable` | Rebate deals | Rebates |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Customers** must exist before sales orders can be created
2. **Released products** must exist and be sold-to eligible
3. **Commission groups** (sales, customer, item) must all be set up before commission calculation
4. **Discount groups** must be defined before trade agreements reference them
5. **Sales agreement classifications** must exist before creating sales agreements
6. **Order hold codes** must be configured before credit management can apply holds
7. **Delivery terms and modes** should be configured for shipping
8. **Rebate groups** must be set before rebate deals
9. **Sales posting profiles** must be configured in inventory posting

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Customer account not found" | Customer not created or wrong company | Create customer in correct legal entity |
| "No trade agreement found" | Price/discount agreement missing or expired | Create/extend trade agreement |
| "Order on hold" | Credit limit exceeded or manual hold | Review and release hold |
| "ATP date unavailable" | No available inventory or supply | Check inventory and planned supply |
| "Commission not calculated" | Missing commission group assignment | Assign all three commission groups |
| "Posting account not found" | Revenue/COGS posting not configured | Update inventory posting profiles |
| "Rebate calculation error" | Rebate deal configuration issue | Review rebate deal setup |
