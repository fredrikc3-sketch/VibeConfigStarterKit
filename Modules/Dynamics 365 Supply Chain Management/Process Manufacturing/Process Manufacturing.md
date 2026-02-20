# Process Manufacturing Module - Knowledge Source

> This file is the central knowledge hub for the **Process Manufacturing** module within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Process Manufacturing](https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/production-process-overview)

## Module Overview

Process Manufacturing in Dynamics 365 Supply Chain Management supports formula-based and batch manufacturing industries (food, chemical, pharmaceutical). It uses formulas instead of BOMs, batch orders instead of production orders, and supports co-products, by-products, potency management, batch balancing, and catch weight items.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Formulas** | Define product recipes with ingredients, co-products, and by-products |
| **Batch Orders** | Create and manage batch production orders for process manufacturing |
| **Co-products & By-products** | Track multiple outputs from a single production batch |
| **Potency Management** | Manage ingredient concentration and adjust quantities based on potency |
| **Batch Balancing** | Adjust ingredient quantities based on active ingredient content |
| **Catch Weight** | Handle items sold by nominal quantity but weighed at receipt/shipment |
| **Shelf Life Tracking** | Manage best-before, expiration, and shelf advice dates for batches |
| **Consolidated Batch Orders** | Consolidate multiple demand signals into a single batch production |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 412 - Process Manufacturing (`412 - Process manufacturing.json`)

Process manufacturing configuration entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Bulk item conversions | BulkItemConversionEntity | Process Mfg - Setup | 30 |
| 10 | Batch attributes | PdsBatchAttributeEntity | Process Mfg - Batch | 30 |
| 10 | Item batch attribute groups | PdsItemBatchAttributeGroupEntity | Process Mfg - Batch | 30 |
| 10 | Item batch attribute group assignments | PdsItemBatchAttributeGroupAssignmentEntity | Process Mfg - Batch | 40 |
| 10 | Formula substitution groups | FormulaSubstitutionGroupEntity | Process Mfg - Formula | 30 |
| 10 | Product specific batch attributes | PdsProductSpecificBatchAttributeEntity | Process Mfg - Batch | 40 |
| 20 | Formula headers | FormulaHeaderEntity | Process Mfg - Formula | 40 |
| 20 | Formula versions V2 | FormulaVersionV2Entity | Process Mfg - Formula | 40 |
| 20 | Formula lines V2 | FormulaLineV2Entity | Process Mfg - Formula | 50 |
| 20 | Formula by-products V2 | FormulaByProductV2Entity | Process Mfg - Formula | 50 |
| 20 | Formula co-products V2 | FormulaCoProductV2Entity | Process Mfg - Formula | 50 |
| 20 | Formula version document attachments | FormulaVersionDocumentAttachmentEntity | Process Mfg - Formula | 50 |
| 30 | Formula line consumption intervals | FormulaLineConsumptionIntervalEntity | Process Mfg - Formula | 60 |

**DMF Load Order Notes:**
- **Seq 10** contains foundational setup — batch attributes, attribute groups, substitution groups, bulk item conversions
- **Seq 20** contains formula definition — headers, versions, lines, by-products, co-products (the equivalent of BOMs for process manufacturing)
- **Seq 30** contains consumption interval details — depends on formula lines
- Batch attributes must be loaded before attribute groups and product-specific assignments
- Formula headers and versions must exist before formula lines and by-products

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (batch attributes, substitution groups, bulk conversions)
- **Level 40:** Dependent entities (attribute group assignments, product-specific attributes, formula headers/versions)
- **Level 50:** Formula detail entities (lines, by-products, co-products, attachments)
- **Level 60:** Consumption intervals (loaded last)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Process Manufacturing** module.

### Plan to produce

*123 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze production operations | 14 | — |
| Control production quality | 30 | — |
| Develop production strategies | 16 | — |
| Plan production operations | 26 | — |
| Run production operations | 37 | — |

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

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Formula versions V2 | `FormulaVersionV2Entity` | `FormulaVersionsV2` | verified |
| Formula lines V2 | `FormulaLineV2Entity` | `FormulaLinesV2` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Bulk item conversions | `BulkItemConversionEntity` |
| Batch attributes | `PdsBatchAttributeEntity` |
| Item batch attribute groups | `PdsItemBatchAttributeGroupEntity` |
| Item batch attribute group assignments | `PdsItemBatchAttributeGroupAssignmentEntity` |
| Formula substitution groups | `FormulaSubstitutionGroupEntity` |
| Product specific batch attributes | `PdsProductSpecificBatchAttributeEntity` |
| Formula headers | `FormulaHeaderEntity` |
| Formula by-products V2 | `FormulaByProductV2Entity` |
| Formula co-products V2 | `FormulaCoProductV2Entity` |
| Formula version document attachments | `FormulaVersionDocumentAttachmentEntity` |
| Formula line consumption intervals | `FormulaLineConsumptionIntervalEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Process Manufacturing:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Process Manufacturing-related business process areas:
- **Plan to Produce** (formula management, batch order production)
- **Batch order processing** (batch order creation, scheduling, execution)
- **Quality management** (batch attribute testing, shelf life management)
- **Potency management** (concentration-based purchasing/production)
- **Co-product and by-product management**

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and use process manufacturing in Dynamics 365 Supply Chain Management** | https://learn.microsoft.com/en-us/training/paths/configure-use-process-manufacturing-dyn365-supply-chain-mgmt/ |
| Get started with process manufacturing | https://learn.microsoft.com/en-us/training/modules/get-started-process-manufacturing-dyn365-supply-chain-mgmt/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Process manufacturing overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/process-manufacturing-overview |
| Formulas and formula versions | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/formulas-and-formula-versions |
| Batch attributes | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/batch-attributes |
| Co-products and by-products | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/co-products-by-products |
| Batch orders | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/batch-order-lifecycle |
| Potency | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/batch-attribute-potency |
| Shelf life | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/shelf-life |
| Formula substitutions | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/formula-substitutions |
| Consolidation and packing of batch orders | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/consolidate-batch-orders |
| Catch weight processing | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/catch-weight-processing |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites (Inventory & Production)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Released products | Product information management > Products > Released products | Formula items with production type = Formula |
| Production groups | Production control > Setup > Production > Production groups | Posting group for batch orders |
| Routes / Operations | Production control > Setup > Routes | Processing routes for formulas |
| Units of measure | Organization administration > Setup > Units | Measurement and conversion units |
| Batch number groups | Inventory management > Setup > Inventory > Batch number groups | Batch number generation |

### Phase 2: Batch Attribute Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| PdsBatchAttribute | Inventory management > Setup > Batch > Batch attributes | Attribute definitions (potency, viscosity, etc.) |
| PdsItemBatchAttributeGroup | Inventory management > Setup > Batch > Batch attribute groups | Attribute group definitions |
| PdsItemBatchAttributeGroupAssignment | (Within released product) | Assign attribute groups to products |
| PdsProductSpecificBatchAttribute | (Within released product) | Product-specific attribute targets/tolerances |

### Phase 3: Formula Definition

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| FormulaHeader | Product information management > Bills of materials and formulas > Formulas | Formula master records |
| FormulaVersion | (Within formula) | Formula version activation |
| FormulaLine | (Within formula) | Ingredient lines |
| FormulaByProduct | (Within formula) | By-product outputs |
| FormulaCoProduct | (Within formula) | Co-product outputs |
| FormulaSubstitutionGroup | Production control > Setup > Formulas > Substitution groups | Ingredient substitution rules |
| BulkItemConversion | Inventory management > Setup > Batch > Bulk item conversion | Bulk to packed conversion |

### Phase 4: Batch Order Execution

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| ProdTable (Batch) | Production control > Production orders > All production orders | Batch order creation |
| ProdParmSchedule | (Within batch order) | Scheduling parameters |
| ProdRoute | (Within batch order) | Batch processing route |

---

## Process Manufacturing vs. Discrete Manufacturing

| Feature | Process Manufacturing | Discrete Manufacturing |
|---------|----------------------|----------------------|
| **Recipe structure** | Formula | BOM |
| **Order type** | Batch order | Production order |
| **Output** | Co-products + by-products | Single finished good |
| **Measurements** | Variable (weight, volume, concentration) | Fixed (each, units) |
| **Batch attributes** | Yes (potency, quality) | No |
| **Scalability** | Formula scales with batch size | BOM fixed quantities |
| **Shelf life** | Common (expiration dates) | Less common |

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `PdsBatchAttributes` | Batch attributes | Setup |
| `PdsBatchAttributeGroups` | Batch attribute groups | Setup |
| `FormulaDesigner` | Formula designer | Formulas |
| `FormulaVersions` | Formula versions | Formulas |
| `ProdBatchOrders` | Batch orders | Production |
| `FormulaSubstitutionGroups` | Substitution groups | Setup |
| `BulkItemConversion` | Bulk item conversion | Setup |
| `ProdParmScheduleBatch` | Schedule batch orders | Production |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Released products** must have production type = Formula for process manufacturing items
2. **Batch attributes** must exist before attribute groups and product-specific assignments
3. **Formula headers** must be created before versions, lines, and co/by-products
4. **Formula versions** must be activated before batch orders can use them
5. **Routes/operations** must be configured for formula processing steps
6. **Co-product cost allocation** must be set if co-products share production costs
7. **Potency attributes** must be configured for concentration-based purchasing

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No active formula version" | Formula version not activated | Activate formula version for date range |
| "Batch attribute not found" | Attribute not defined or not assigned | Create batch attribute and assign to product |
| "Co-product cost allocation error" | Missing cost allocation method | Configure co-product cost allocation |
| "Formula scalability error" | Ingredient not set as scalable | Check scalable flag on formula line |
| "Batch number generation failed" | Batch number group not assigned | Assign batch number group to product |
