# Product Configuration Models Module - Knowledge Source

> This file is the central knowledge hub for the **Product Configuration Models** module within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Product Configuration Models](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/build-product-configuration-model)

## Module Overview

The Product Configuration module in Dynamics 365 Supply Chain Management enables constraint-based product configuration. It allows organizations to define configurable product models with attributes, components, subcomponents, and constraints that dynamically determine the product's BOM and route based on customer-selected options.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Configuration Models** | Build interactive product configurators using attributes and constraints |
| **Constraint Rules** | Define expression-based and table-based constraints for valid configurations |
| **Attribute Types** | Create attributes (integer, decimal, text, boolean, enum) for product options |
| **BOM & Route Generation** | Dynamically generate BOMs and routes based on configuration selections |
| **Configuration Templates** | Save common configurations as templates for reuse |
| **Solver Strategy** | Use the constraint solver engine to validate configurations in real time |
| **Sales Integration** | Configure products directly from sales quotations and sales orders |
| **Pricing Rules** | Define configuration-based pricing adjustments and surcharges |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 418 - Product Configuration Models (`418 - Product configuration models.json`)

Product configuration model entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Product configuration models V2 | PCProductConfigurationModelV2Entity | Config Models - Models | 30 |
| 20 | Product configuration model versions | PCProductConfigurationModelVersionEntity | Config Models - Versions | 40 |
| 30 | Constraint-based product configuration model parameters | PCConstraintBasedProductConfigModelParametersEntity | Config Models - Parameters | 50 |

**DMF Load Order Notes:**
- **Seq 10** contains the product configuration model definitions (the constraint-based model structure)
- **Seq 20** contains model versions — depends on the model definitions
- **Seq 30** contains the module parameters for constraint-based configuration
- Product configuration models must exist before versions can reference them
- Product masters with configuration technology = Constraint-based must exist first

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Product configuration model definitions
- **Level 40:** Model versions
- **Level 50:** Module parameters (loaded last)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Product Configuration Models** module.

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

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Product configuration models V2 | `PCProductConfigurationModelV2Entity` |
| Product configuration model versions | `PCProductConfigurationModelVersionEntity` |
| Constraint-based product configuration model parameters | `PCConstraintBasedProductConfigModelParametersEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Product Configuration:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Product Configuration-related business process areas:
- **Product lifecycle management** (configurable product design)
- **Order to Cash** (configure-to-order sales process)
- **Plan to Produce** (configuration-driven BOMs and routes)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Set up product configuration in Dynamics 365 Supply Chain Management** | https://learn.microsoft.com/en-us/training/paths/set-up-product-configuration/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Product configuration models overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-configuration-models |
| Constraint-based configuration | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/constraint-based-product-configuration |
| Product configurator | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/build-product-configuration-model |
| Expression constraints | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/expression-constraints-table-constraints |
| System-defined and user-defined table constraints | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/system-defined-user-defined-table-constraints |
| Solver strategy | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/solver-strategy |
| Attribute-based pricing | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/attribute-based-product-configurator |
| Configuration rules | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/configuration-rules |
| Dimension-based configuration | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/dimension-based-product-configuration |

---

## 3-Phase Configuration Sequence

### Phase 1: Prerequisites (Product Master Setup)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Product masters | Product information management > Products > Product masters | Master product with configuration technology = Constraint-based |
| Product dimension groups | Product information management > Setup > Dimension and variant groups > Product dimension groups | Must include Configuration dimension |
| Attributes | Product information management > Setup > Categories and attributes > Attributes | Attribute definitions for model components |
| Attribute types | Product information management > Setup > Categories and attributes > Attribute types | Integer, text, boolean, decimal, enum |

### Phase 2: Configuration Model Design

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| PCProductConfigurationModel | Product information management > Products > Product configuration models | Model definition with components, attributes, constraints |
| Components | (Within model designer) | Sub-assemblies with their own attributes |
| Attribute assignments | (Within model designer) | Attributes assigned to components |
| Constraints | (Within model designer) | Expression or table constraints limiting valid combinations |
| BOM lines | (Within model designer) | Conditional BOM lines based on configuration |
| Route operations | (Within model designer) | Conditional route operations |

### Phase 3: Model Versions & Parameters

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| PCProductConfigurationModelVersion | (Within model) | Version activation for use in orders |
| PCConstraintBasedProductConfigModelParameters | Product information management > Setup > Product configuration model parameters | Solver and runtime configuration |

---

## Configuration Model Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  PRODUCT CONFIGURATION MODEL ARCHITECTURE                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PRODUCT MASTER (Configuration Technology = Constraint-Based)            │
│  ┌────────────────────────────────────────────────────────┐             │
│  │                                                          │             │
│  │   CONFIGURATION MODEL                                    │             │
│  │   ┌────────────────────────────────────────┐            │             │
│  │   │ Root Component                           │            │             │
│  │   │   ├── Attribute: Color (Enum)            │            │             │
│  │   │   ├── Attribute: Size (Decimal)          │            │             │
│  │   │   ├── Attribute: Material (Enum)         │            │             │
│  │   │   │                                      │            │             │
│  │   │   ├── Sub-Component A                    │            │             │
│  │   │   │   ├── Attribute: Width               │            │             │
│  │   │   │   └── Attribute: Height              │            │             │
│  │   │   │                                      │            │             │
│  │   │   ├── Sub-Component B (Optional)         │            │             │
│  │   │   │   └── Attribute: Finish              │            │             │
│  │   │   │                                      │            │             │
│  │   │   ├── Expression Constraints             │            │             │
│  │   │   │   └── "Width > 10 implies Material   │            │             │
│  │   │   │        = 'Steel'"                    │            │             │
│  │   │   │                                      │            │             │
│  │   │   ├── Conditional BOM Lines              │            │             │
│  │   │   │   └── Include part X if Color='Red'  │            │             │
│  │   │   │                                      │            │             │
│  │   │   └── Conditional Route Operations       │            │             │
│  │   │       └── Add painting if Color≠'Natural'│            │             │
│  │   └────────────────────────────────────────┘            │             │
│  │                                                          │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
│  RUNTIME: User selects attribute values → Solver validates →             │
│           BOM & Route generated → Order created                          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Configuration Technologies Comparison

| Feature | Constraint-Based | Dimension-Based | Predefined Variants |
|---------|-----------------|-----------------|---------------------|
| **Configurator UI** | Yes (runtime solver) | No | No |
| **Automatic BOM/Route** | Yes (conditional) | Yes (config groups) | Manual per variant |
| **Constraint validation** | Expression + table | Rules only | N/A |
| **Number of variants** | Unlimited (calculated) | Medium (finite) | Small (explicit) |
| **Use case** | Complex configurable products | Medium complexity | Simple products |

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `PCProductConfigurationModels` | Product configuration models | Models |
| `PCProductConfigurationModelDetails` | Model details | Models |
| `PCConstraintBasedParameters` | Product configuration model parameters | Setup |
| `EcoResProductMaster` | Product masters | Products |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Product masters** must be created with configuration technology = Constraint-based
2. **Product dimension groups** must include the Configuration dimension
3. **Attributes and attribute types** must be defined before they can be used in models
4. **Root component** of the model must be defined before sub-components
5. **Constraints** should be validated using the Test feature before model activation
6. **Model version** must be activated before it can be used on sales/production orders
7. **Solver strategy** should be set in parameters for performance optimization

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No active model version" | Model version not activated | Activate model version |
| "Constraint conflict" | Expression constraints mutually exclusive | Review and fix constraint logic |
| "Configuration cannot be completed" | Solver cannot find valid combination | Relax constraints or fix model design |
| "Product master not constraint-based" | Wrong configuration technology | Set configuration technology on product master |
| "BOM/Route not generated" | Conditional rules not matching | Review BOM/route conditions in model |
