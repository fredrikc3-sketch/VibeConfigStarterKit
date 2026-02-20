# Inventory Management Module - Knowledge Source

> This file is the central knowledge hub for the **Inventory Management** module within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Inventory Management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-home-page)

## Module Overview

The Inventory Management module in Dynamics 365 Supply Chain Management manages stock levels, item tracking, inventory valuation, and inventory transactions. It supports batch and serial number tracking, quarantine management, inventory journals, inventory visibility, and on-hand inventory analysis across warehouses and sites.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Item Master Management** | Define items with storage, tracking, and planning dimensions |
| **Inventory Journals** | Process movement, adjustment, transfer, counting, and BOM journals |
| **Batch & Serial Tracking** | Track inventory by batch numbers, serial numbers, or both |
| **Quarantine Management** | Quarantine received or in-process items pending quality inspection |
| **Inventory Visibility** | Real-time inventory visibility across channels and systems |
| **Inventory Aging** | Analyze inventory age and identify slow-moving or obsolete stock |
| **Inventory On-hand** | View and filter current on-hand inventory across dimensions |
| **Consignment Inventory** | Manage vendor-owned inventory stored at your locations |
| **Inventory Blocking** | Block inventory from transactions for quality or other holds |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 300 - Inventory (`300 - Inventory.json`)

Inventory management configuration and master data entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | BOM journal names | InventJournalNameBOMEntity | Inventory - Journals | 30 |
| 10 | Counting journal names | InventJournalNameCountEntity | Inventory - Journals | 30 |
| 10 | Counting groups | InventCountingGroupEntity | Inventory - Setup | 30 |
| 10 | Inventory adjustment journal names | InventJournalNameAdjustmentEntity | Inventory - Journals | 30 |
| 10 | Inventory movement journal names | InventJournalNameMovementEntity | Inventory - Journals | 30 |
| 10 | Inventory transfer journal names | InventJournalNameTransferEntity | Inventory - Journals | 30 |
| 10 | Item arrival journal names | InventJournalNameItemArrivalEntity | Inventory - Journals | 30 |
| 10 | Item groups | InventItemGroupEntity | Inventory - Groups | 30 |
| 10 | Item model groups | InventModelGroupEntity | Inventory - Groups | 30 |
| 10 | Inventory status | InventInventoryStatusEntity | Inventory - Setup | 30 |
| 10 | Packing material allocation | InventPackingMaterialEntity | Inventory - Setup | 30 |
| 10 | Packing material groups | InventPackingMaterialGroupEntity | Inventory - Setup | 30 |
| 10 | Product categories | EcoResProductCategoryEntity | Inventory - Categories | 30 |
| 10 | Product category hierarchies | EcoResProductCategoryHierarchyEntity | Inventory - Categories | 30 |
| 10 | Product groups | InventProductGroupEntity | Inventory - Groups | 30 |
| 10 | Production input journal names | InventJournalNameProductionInputEntity | Inventory - Journals | 30 |
| 10 | Sites | InventSiteEntity | Inventory - Locations | 30 |
| 10 | Tag counting journal names | InventJournalNameTagCountEntity | Inventory - Journals | 30 |
| 10 | Tracking number groups | InventTrackingNumberGroupEntity | Inventory - Tracking | 30 |
| 10 | Inventory dimensions parameters | InventDimensionsParametersEntity | Inventory - Setup | 30 |
| 10 | Customer price groups | CustPriceGroupEntity | Inventory - Pricing | 30 |
| 10 | Vendor price groups | VendPriceGroupEntity | Inventory - Pricing | 30 |
| 20 | Warehouses | InventWarehouseEntity | Inventory - Locations | 40 |
| 20 | Warehouse locations | InventLocationEntity | Inventory - Locations | 40 |
| 20 | Warehouse aisles | InventAisleEntity | Inventory - Locations | 40 |
| 20 | Warehouse zones | InventZoneEntity | Inventory - Locations | 40 |
| 20 | Ledger posting definitions - Inventory | InventPostingInventoryEntity | Inventory - Posting | 40 |
| 20 | Ledger posting definitions - Procurement | InventPostingProcurementEntity | Inventory - Posting | 40 |
| 20 | Ledger posting definitions - Production | InventPostingProductionEntity | Inventory - Posting | 40 |
| 20 | Ledger posting definitions - Sales | InventPostingSalesEntity | Inventory - Posting | 40 |
| 20 | Ledger posting definitions - Standard cost variance | InventPostingStdCostVarianceEntity | Inventory - Posting | 40 |
| 30 | Inventory parameters | InventParametersEntity | Inventory - Parameters | 50 |
| 30 | BOM parameters | BOMParametersEntity | Inventory - Parameters | 50 |
| 30 | Product parameters | ProductParametersEntity | Inventory - Parameters | 50 |

**DMF Load Order Notes:**
- **Seq 10** contains foundational inventory setup — item groups, model groups, sites, journal names, tracking groups, categories, pricing groups
- **Seq 20** contains dependent entities — warehouses (depend on sites), locations/aisles/zones (depend on warehouses), all ledger posting definitions
- **Seq 30** contains module parameters — inventory, BOM, and product parameters loaded last
- Sites must be loaded before warehouses
- Item groups and model groups must exist before released products
- All posting definitions must be in place before transactions can post

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (groups, sites, journal names, categories, tracking)
- **Level 40:** Dependent entities (warehouses, locations, posting definitions)
- **Level 50:** Module parameters (loaded last)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Inventory Management** module.

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

### Design to retire

*176 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze product performance | 7 | — |
| Develop product strategy | 44 | — |
| Introduce products | 62 | — |
| Manage active products | 53 | — |
| Retire products | 10 | — |

### Order to cash

*97 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze sales performance | 13 | — |
| Develop sales policies | 12 | — |
| Manage accounts receivable | 11 | — |
| Manage sales orders | 61 | — |

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Counting groups | `InventCountingGroupEntity` | `InventoryCountingGroups` | verified |
| Product categories | `EcoResProductCategoryEntity` | `ProductCategories` | verified |
| Product category hierarchies | `EcoResProductCategoryHierarchyEntity` | `ProductCategoryHierarchies` | verified |
| Sites | `InventSiteEntity` | `InventorySites` | manual-unverified |
| Warehouses | `InventWarehouseEntity` | `Warehouses` | verified |
| Warehouse locations | `InventLocationEntity` | `Warehouses` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| BOM journal names | `InventJournalNameBOMEntity` |
| Counting journal names | `InventJournalNameCountEntity` |
| Inventory adjustment journal names | `InventJournalNameAdjustmentEntity` |
| Inventory movement journal names | `InventJournalNameMovementEntity` |
| Inventory transfer journal names | `InventJournalNameTransferEntity` |
| Item arrival journal names | `InventJournalNameItemArrivalEntity` |
| Item groups | `InventItemGroupEntity` |
| Item model groups | `InventModelGroupEntity` |
| Inventory status | `InventInventoryStatusEntity` |
| Packing material allocation | `InventPackingMaterialEntity` |
| Packing material groups | `InventPackingMaterialGroupEntity` |
| Product groups | `InventProductGroupEntity` |
| Production input journal names | `InventJournalNameProductionInputEntity` |
| Tag counting journal names | `InventJournalNameTagCountEntity` |
| Tracking number groups | `InventTrackingNumberGroupEntity` |
| Inventory dimensions parameters | `InventDimensionsParametersEntity` |
| Customer price groups | `CustPriceGroupEntity` |
| Vendor price groups | `VendPriceGroupEntity` |
| Warehouse aisles | `InventAisleEntity` |
| Warehouse zones | `InventZoneEntity` |
| Ledger posting definitions - Inventory | `InventPostingInventoryEntity` |
| Ledger posting definitions - Procurement | `InventPostingProcurementEntity` |
| Ledger posting definitions - Production | `InventPostingProductionEntity` |
| Ledger posting definitions - Sales | `InventPostingSalesEntity` |
| Ledger posting definitions - Standard cost variance | `InventPostingStdCostVarianceEntity` |
| Inventory parameters | `InventParametersEntity` |
| BOM parameters | `BOMParametersEntity` |
| Product parameters | `ProductParametersEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Inventory Management:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Inventory Management-related business process areas:
- **Inventory to Deliver** (receipt, storage, counting, movement, transfer)
- **Inventory counting** (cycle counting, tag counting, physical counting)
- **Inventory adjustments** (quantity and value adjustments)
- **Inventory close** (period-end settlement and reconciliation)
- **Quality management** (quality orders, quarantine)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and manage inventory in Dynamics 365 Supply Chain Management** | https://learn.microsoft.com/en-us/training/paths/configure-manage-inventory-dyn365-supply-chain-mgmt/ |
| Configure inventory management | https://learn.microsoft.com/en-us/training/modules/configure-inventory-management-dyn365-supply-chain-mgmt/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Inventory management overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-home-page |
| Item model groups | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/item-model-groups |
| Inventory journals | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-journals |
| Inventory counting | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-tag-counting |
| Inventory statuses | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-statuses |
| Inventory on-hand list | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-on-hand-list |
| Inventory visibility | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility |
| Warehouse setup | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/warehouse-configuration |
| Inventory posting profiles | https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/inventory-posting |
| Tracking number groups | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/tracking-number-groups |
| Sites and warehouses | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-locations |
| Inventory dimensions | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-dimensions |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites (GL & Organization)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Main accounts | General ledger > Chart of accounts > Accounts > Main accounts | Inventory, COGS, variance accounts |
| Financial dimensions | General ledger > Chart of accounts > Dimensions | Site, warehouse dimensions |
| Number sequences | Organization administration > Number sequences | Journal, transaction numbering |
| Units of measure | Organization administration > Setup > Units > Units | Measurement units |

### Phase 2: Inventory Groups & Classification

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| InventItemGroup | Inventory management > Setup > Inventory > Item groups | Item financial grouping |
| InventModelGroup | Inventory management > Setup > Inventory > Item model groups | Inventory valuation method |
| InventCountingGroup | Inventory management > Setup > Inventory > Counting groups | Counting frequency |
| InventInventoryStatus | Inventory management > Setup > Inventory > Inventory statuses | Status-based blocking/availability |
| InventTrackingNumberGroup | Inventory management > Setup > Inventory > Tracking number groups | Serial/batch auto-generation |
| EcoResProductCategoryHierarchy | Product information management > Setup > Categories and attributes > Category hierarchies | Category classification |

### Phase 3: Sites, Warehouses & Locations

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| InventSite | Inventory management > Setup > Inventory breakdown > Sites | Physical site definitions |
| InventWarehouse | Inventory management > Setup > Inventory breakdown > Warehouses | Warehouse definitions |
| InventLocation | Inventory management > Setup > Inventory breakdown > Locations | Bin/location setup (non-WMS) |
| InventAisle | (Within warehouse setup) | Aisle definitions |
| InventZone | (Within warehouse setup) | Zone definitions |

### Phase 4: Journal Names & Posting Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| InventJournalName | Inventory management > Setup > Journal names > Inventory | All journal type definitions |
| InventPosting - Inventory | Inventory management > Setup > Posting > Posting | Physical/financial inventory accounts |
| InventPosting - Procurement | Inventory management > Setup > Posting > Posting | Purchase-related accounts |
| InventPosting - Production | Inventory management > Setup > Posting > Posting | Production-related accounts |
| InventPosting - Sales | Inventory management > Setup > Posting > Posting | Sales-related accounts (COGS, revenue) |
| InventPosting - StdCostVariance | Inventory management > Setup > Posting > Posting | Standard cost variance accounts |

### Phase 5: Parameters

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| InventParameters | Inventory management > Setup > Inventory and warehouse management parameters | Module parameters |
| BOMParameters | Inventory management > Setup > Bills of materials > BOM parameters | BOM-specific parameters |
| ProductParameters | Product information management > Setup > Product information management parameters | Product-specific parameters |

---

## Inventory Journal Types

| Journal Type | Purpose | Menu Path |
|-------------|---------|-----------|
| **Movement** | Increase/decrease inventory with GL offset | Inventory management > Journal entries > Items > Movement |
| **Adjustment** | Adjust inventory quantity/value | Inventory management > Journal entries > Items > Inventory adjustment |
| **Transfer** | Move inventory between locations/warehouses | Inventory management > Journal entries > Items > Transfer |
| **Counting** | Physical inventory count reconciliation | Inventory management > Journal entries > Items > Counting |
| **Tag counting** | Tag-based physical count | Inventory management > Journal entries > Items > Tag counting |
| **BOM** | BOM component consumption/picking | Inventory management > Journal entries > Items > Bills of materials |
| **Item arrival** | Register received items | Inventory management > Journal entries > Items > Item arrival |
| **Production input** | Production consumption reporting | Inventory management > Journal entries > Items > Production input |

---

## Inventory Posting Profile Design

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   INVENTORY POSTING PROFILE DESIGN                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  INVENTORY (Physical & Financial)                                        │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Inventory receipt        → Debit Inventory (BS)        │             │
│  │ • Inventory issue          → Credit Inventory (BS)       │             │
│  │ • Inventory profit (adj)   → Credit P&L                  │             │
│  │ • Inventory loss (adj)     → Debit P&L                   │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
│  PROCUREMENT                                                             │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Purchase expenditure (uninvoiced)  → Debit Clearing    │             │
│  │ • Purchase expenditure (invoiced)    → Debit Expense     │             │
│  │ • Purchase accrual                   → Credit Accrual    │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
│  SALES                                                                   │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Cost of goods sold       → Debit COGS (P&L)           │             │
│  │ • Revenue                  → Credit Revenue (P&L)        │             │
│  │ • Packing slip revenue     → Credit Deferred Revenue     │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
│  PRODUCTION                                                              │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • WIP issue                → Debit WIP                   │             │
│  │ • WIP receipt              → Credit WIP                  │             │
│  │ • Report as finished       → Debit Finished goods        │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `InventParameters` | Inventory and warehouse management parameters | Setup |
| `InventItemGroup` | Item groups | Setup |
| `InventModelGroup` | Item model groups | Setup |
| `InventSite` | Sites | Locations |
| `InventWarehouse` | Warehouses | Locations |
| `InventLocation` | Locations | Locations |
| `InventJournalMovement` | Movement journal | Journals |
| `InventJournalCounting` | Counting journal | Journals |
| `InventJournalTransfer` | Transfer journal | Journals |
| `InventPosting` | Posting | Posting |
| `InventOnHand` | On-hand inventory | Inquiry |
| `InventClosing` | Inventory close | Period Close |
| `InventCountingGroup` | Counting groups | Setup |
| `InventStatus` | Inventory statuses | Setup |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Sites** must exist before warehouses can be created
2. **Warehouses** must exist before locations, and before products reference them
3. **Item groups** determine financial posting — must exist before released products
4. **Item model groups** define inventory valuation method — must be assigned to products
5. **Inventory posting profiles** must cover all transaction types before any inventory transactions
6. **Journal names** must be created before inventory journals can be used
7. **Counting groups** must be assigned to products for cycle counting
8. **Units of measure** must be defined before products
9. **Inventory parameters** should be configured after all setup entities

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Posting account not found" | Missing inventory posting definition | Configure posting for item group / transaction type |
| "Site is required" | Mandatory site dimension not specified | Ensure site is set on transaction |
| "Warehouse not found" | Warehouse not created or wrong company | Create warehouse in correct legal entity |
| "Item model group not assigned" | Released product missing model group | Assign model group on released product |
| "Journal name not found" | Journal type not configured | Create journal name for the type |
| "Inventory close error" | Transactions prevent settlement | Resolve open transactions before close |
