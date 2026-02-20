# Product Information Management Module - Knowledge Source

> This file is the central knowledge hub for the **Product Information Management** module within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Product Information Management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information)

## Module Overview

The Product Information Management module in Dynamics 365 Supply Chain Management provides centralized product master data management. It supports product creation, product variants (using dimensions like size, color, style, configuration), product categories, product attributes, translation, and release of products across legal entities.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Product Masters** | Define shared product definitions with core attributes like name, type, and category |
| **Product Variants** | Create product variants using size, color, style, and configuration dimensions |
| **Product Categories** | Organize products into hierarchical category structures |
| **Product Attributes** | Define custom attributes for enhanced product classification and search |
| **Product Release** | Release products from shared definitions to specific legal entities |
| **Product Translation** | Maintain product descriptions in multiple languages |
| **Product Lifecycle States** | Control product availability and behavior through lifecycle states |
| **Product Relationships** | Define cross-sell, up-sell, and substitute product relationships |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 310 - Product Information Management (`310 - Product information management.json`)

Product information management configuration and master data entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Product attributes | EcoResProductAttributeEntity | PIM - Attributes | 30 |
| 10 | Product attribute groups | EcoResProductAttributeGroupEntity | PIM - Attributes | 30 |
| 10 | Product attribute translations | EcoResProductAttributeTranslationEntity | PIM - Attributes | 30 |
| 10 | Product dimension groups | EcoResProductDimensionGroupEntity | PIM - Dimensions | 30 |
| 10 | Storage dimension groups | EcoResStorageDimensionGroupEntity | PIM - Dimensions | 30 |
| 10 | Tracking dimension groups | EcoResTrackingDimensionGroupEntity | PIM - Dimensions | 30 |
| 10 | Color groups | EcoResProductColorGroupEntity | PIM - Variants | 30 |
| 10 | Color group lines | EcoResProductColorGroupLineEntity | PIM - Variants | 30 |
| 10 | Size groups | EcoResProductSizeGroupEntity | PIM - Variants | 30 |
| 10 | Size group lines | EcoResProductSizeGroupLineEntity | PIM - Variants | 30 |
| 10 | Style groups | EcoResProductStyleGroupEntity | PIM - Variants | 30 |
| 10 | Style group lines | EcoResProductStyleGroupLineEntity | PIM - Variants | 30 |
| 10 | Product lifecycle states | EcoResProductLifecycleStateEntity | PIM - Lifecycle | 30 |
| 10 | Reservation hierarchies | WHSReservationHierarchyEntity | PIM - WHS | 30 |
| 10 | Reduction keys | ReductionKeyEntity | PIM - Planning | 30 |
| 10 | Catch weight item conversions | CatchWeightItemConversionEntity | PIM - Catch Weight | 30 |
| 20 | Products V2 | EcoResProductV2Entity | PIM - Products | 40 |
| 20 | Product masters | EcoResProductMasterEntity | PIM - Products | 40 |
| 20 | Product master colors | EcoResProductMasterColorEntity | PIM - Variants | 40 |
| 20 | Product master sizes | EcoResProductMasterSizeEntity | PIM - Variants | 40 |
| 20 | Product master styles | EcoResProductMasterStyleEntity | PIM - Variants | 40 |
| 30 | Released products V2 | EcoResReleasedProductV2Entity | PIM - Released | 50 |
| 30 | Released product variants | EcoResReleasedProductVariantEntity | PIM - Released | 50 |
| 40 | Item coverage | ReqItemCoverageEntity | PIM - Planning | 60 |
| 40 | Item barcodes | InventItemBarcodesEntity | PIM - Barcodes | 60 |
| 40 | Item batches | InventBatchEntity | PIM - Batch | 60 |
| 40 | Item serial numbers | InventSerialNumberEntity | PIM - Serial | 60 |
| 40 | Product default order settings | InventProductDefaultOrderSettingsEntity | PIM - Order Settings | 60 |
| 40 | Catch weight policies | CatchWeightItemPolicyEntity | PIM - Catch Weight | 60 |

**DMF Load Order Notes:**
- **Seq 10** contains foundational setup — dimension groups, variant groups (color/size/style), attributes, lifecycle states, reservation hierarchies, reduction keys
- **Seq 20** contains product definitions — products V2, product masters, and master dimension values (colors, sizes, styles)
- **Seq 30** contains released products and variants — depends on products, masters, and dimension groups
- **Seq 40** contains product-level settings — coverage, barcodes, batches, serial numbers, default order settings
- Dimension groups must exist before products referencing them
- Product masters must exist before variant dimension values can be assigned
- Products must be released before released product-level data can be set

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (dimension groups, variant groups, attributes, lifecycle states)
- **Level 40:** Product definitions (products, product masters, master dimensions)
- **Level 50:** Released products and variants
- **Level 60:** Product-level operational settings (coverage, barcodes, order settings)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Product Information Management** module.

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
| Product dimension groups | `EcoResProductDimensionGroupEntity` | `ProductDimensionGroups` | manual-unverified |
| Storage dimension groups | `EcoResStorageDimensionGroupEntity` | `ProductStorageDimensionGroups` | manual-unverified |
| Tracking dimension groups | `EcoResTrackingDimensionGroupEntity` | `ProductTrackingDimensionGroups` | manual-unverified |
| Color groups | `EcoResProductColorGroupEntity` | `ProductColorGroups` | verified |
| Color group lines | `EcoResProductColorGroupLineEntity` | `ProductColorGroupLines` | verified |
| Size groups | `EcoResProductSizeGroupEntity` | `ProductSizeGroups` | verified |
| Size group lines | `EcoResProductSizeGroupLineEntity` | `ProductSizeGroupLines` | verified |
| Style groups | `EcoResProductStyleGroupEntity` | `ProductStyleGroups` | verified |
| Style group lines | `EcoResProductStyleGroupLineEntity` | `ProductStyleGroupLines` | verified |
| Product lifecycle states | `EcoResProductLifecycleStateEntity` | `ProductLifecycleStates` | verified |
| Products V2 | `EcoResProductV2Entity` | `ReleasedProductsV2` | verified |
| Product masters | `EcoResProductMasterEntity` | `ProductMasters` | verified |
| Product master colors | `EcoResProductMasterColorEntity` | `ProductMasterColors` | verified |
| Product master sizes | `EcoResProductMasterSizeEntity` | `ProductMasterSizes` | verified |
| Product master styles | `EcoResProductMasterStyleEntity` | `ProductMasterStyles` | verified |
| Released products V2 | `EcoResReleasedProductV2Entity` | `ReleasedProductsV2` | verified |
| Released product variants | `EcoResReleasedProductVariantEntity` | `ProductNumberIdentifiedReleasedProductVariants` | verified |
| Item batches | `InventBatchEntity` | `ItemBatches` | verified |
| Product default order settings | `InventProductDefaultOrderSettingsEntity` | `ProductDefaultOrderSettingsV2` | manual-unverified |
| Catch weight policies | `CatchWeightItemPolicyEntity` | `CatchWeightItemHandlingPoliciesV2` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Product attributes | `EcoResProductAttributeEntity` |
| Product attribute groups | `EcoResProductAttributeGroupEntity` |
| Product attribute translations | `EcoResProductAttributeTranslationEntity` |
| Reservation hierarchies | `WHSReservationHierarchyEntity` |
| Reduction keys | `ReductionKeyEntity` |
| Catch weight item conversions | `CatchWeightItemConversionEntity` |
| Item coverage | `ReqItemCoverageEntity` |
| Item barcodes | `InventItemBarcodesEntity` |
| Item serial numbers | `InventSerialNumberEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Product Information Management:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key PIM-related business process areas:
- **Design to Retire** (product lifecycle management)
- **Product master data management** (product creation, variant generation)
- **Product release** (cross-company product distribution)
- **Category management** (product categorization and attributes)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and work with product information management** | https://learn.microsoft.com/en-us/training/paths/configure-work-product-information-management/ |
| Create and manage products | https://learn.microsoft.com/en-us/training/modules/create-manage-product-dyn365-supply-chain-mgmt/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Product information management overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information |
| Products, product masters, and product variants | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-identifiers |
| Product dimension groups | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-dimensions |
| Storage dimension groups | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/storage-dimensions |
| Tracking dimension groups | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/tracking-dimensions |
| Product lifecycle states | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-lifecycle |
| Product attributes | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-attributes-and-attribute-types |
| Product variants | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-variant-identification-nomenclature |
| Released products | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/tasks/release-product-product-master-legal-entities |
| Default order settings | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/default-order-settings |
| Catch weight processing | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/catch-weight-processing |
| Reservation hierarchies | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/flexible-warehouse-level-dimension-reservation |

---

## 5-Phase Configuration Sequence

### Phase 1: Dimension Groups

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| EcoResProductDimensionGroup | Product information management > Setup > Dimension and variant groups > Product dimension groups | Color, Size, Style, Configuration dimensions |
| EcoResStorageDimensionGroup | Product information management > Setup > Dimension and variant groups > Storage dimension groups | Site, Warehouse, Location, Inventory status |
| EcoResTrackingDimensionGroup | Product information management > Setup > Dimension and variant groups > Tracking dimension groups | Batch number, Serial number, Owner |
| WHSReservationHierarchy | Warehouse management > Setup > Warehouse > Reservation hierarchies | WMS reservation hierarchy |

### Phase 2: Variant Groups & Attributes

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| EcoResProductColorGroup | Product information management > Setup > Dimension and variant groups > Color groups | Color group definitions and lines |
| EcoResProductSizeGroup | Product information management > Setup > Dimension and variant groups > Size groups | Size group definitions and lines |
| EcoResProductStyleGroup | Product information management > Setup > Dimension and variant groups > Style groups | Style group definitions and lines |
| EcoResProductAttribute | Product information management > Setup > Categories and attributes > Product attributes | Attribute definitions |
| EcoResProductAttributeGroup | Product information management > Setup > Categories and attributes > Product attribute groups | Attribute groupings |
| EcoResProductLifecycleState | Product information management > Setup > Product lifecycle state | Active, deprecated, obsolete |

### Phase 3: Product Creation

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| EcoResProductV2 | Product information management > Products > Products | Distinct products (no variants) |
| EcoResProductMaster | Product information management > Products > Product masters | Products with variants |
| EcoResProductMasterColor | (Within product master) | Available colors for master |
| EcoResProductMasterSize | (Within product master) | Available sizes for master |
| EcoResProductMasterStyle | (Within product master) | Available styles for master |

### Phase 4: Product Release

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| EcoResReleasedProductV2 | Product information management > Products > Released products | Release to legal entities |
| EcoResReleasedProductVariant | (Within released product) | Release specific variants |

### Phase 5: Product-Level Settings

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| InventProductDefaultOrderSettings | (Within released product) | Default order type, MOQ, lead time |
| ReqItemCoverage | (Within released product > Plan) | Item-specific coverage rules |
| InventItemBarcodes | (Within released product) | Barcode assignments |
| InventBatch | (Within product) | Batch records |
| InventSerialNumber | (Within product) | Serial number records |

---

## Product Structure Hierarchy

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     PRODUCT STRUCTURE HIERARCHY                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  SHARED PRODUCT (Cross-Company)                                          │
│  ┌─────────────────────────────────────────────────────────┐            │
│  │                                                           │            │
│  │  ┌─────────────┐     ┌──────────────────────┐            │            │
│  │  │ DISTINCT     │     │ PRODUCT MASTER        │            │            │
│  │  │ PRODUCT      │     │                        │            │            │
│  │  │ (No variants)│     │ + Product Dimensions   │            │            │
│  │  │              │     │   - Color              │            │            │
│  │  │              │     │   - Size               │            │            │
│  │  │              │     │   - Style              │            │            │
│  │  │              │     │   - Configuration      │            │            │
│  │  │              │     │                        │            │            │
│  │  │              │     │ = Product Variants      │            │            │
│  │  └──────┬───────┘     └──────────┬─────────────┘            │            │
│  │         │                        │                          │            │
│  └─────────┼────────────────────────┼──────────────────────────┘            │
│            │                        │                                       │
│            ▼                        ▼                                       │
│  RELEASED PRODUCT (Per Legal Entity)                                       │
│  ┌─────────────────────────────────────────────────────────┐              │
│  │  + Item model group (inventory valuation)                 │              │
│  │  + Item group (financial posting)                         │              │
│  │  + Storage dimension group (site/warehouse/location)      │              │
│  │  + Tracking dimension group (batch/serial)                │              │
│  │  + Default order settings (order type, MOQ, warehouse)    │              │
│  │  + Coverage rules (planning)                              │              │
│  │  + BOM/Formula                                            │              │
│  │  + Route                                                  │              │
│  └─────────────────────────────────────────────────────────┘              │
│                                                                            │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `EcoResProductDetailsExtended` | Released products | Products |
| `EcoResProductMasterCreate` | Product masters | Products |
| `EcoResProductCreate` | Products | Products |
| `EcoResProductDimensionGroup` | Product dimension groups | Setup |
| `EcoResStorageDimensionGroup` | Storage dimension groups | Setup |
| `EcoResTrackingDimensionGroup` | Tracking dimension groups | Setup |
| `EcoResProductColorGroup` | Color groups | Variants |
| `EcoResProductSizeGroup` | Size groups | Variants |
| `EcoResProductStyleGroup` | Style groups | Variants |
| `EcoResProductAttributes` | Product attributes | Attributes |
| `EcoResProductLifecycleState` | Product lifecycle states | Lifecycle |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Dimension groups** (product, storage, tracking) must exist before products are created
2. **Variant groups** (color, size, style) must be defined before assigning to product masters
3. **Product masters** must have variant dimension values before variants can be generated
4. **Products must be released** to a legal entity before they can be used in transactions
5. **Item model group** must be assigned during product release (determines valuation method)
6. **Item group** must be assigned during product release (determines posting profile)
7. **Default order settings** should be configured per released product for planning
8. **Reservation hierarchies** must be assigned for WMS-enabled products
9. **Lifecycle states** can block products from transactions if set to inactive

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Dimension group required" | Product missing dimension group assignment | Assign all three dimension groups |
| "Product not released" | Product exists but not released to company | Release product to legal entity |
| "Variant does not exist" | Variant combination not generated | Generate variants from master dimensions |
| "No default order settings" | Released product missing defaults | Configure default order settings |
| "Item model group not assigned" | Missing on released product | Assign item model group |
| "Reservation hierarchy required" | WMS product missing hierarchy | Assign reservation hierarchy |
