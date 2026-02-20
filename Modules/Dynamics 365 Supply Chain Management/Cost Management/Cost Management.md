# Cost Management Module - Knowledge Source

> This file is the central knowledge hub for the **Cost Management** module within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Cost Management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/cost-management-home-page)

## Module Overview

The Cost Management module in Dynamics 365 Supply Chain Management manages inventory valuation and cost of goods manufactured (COGM). It supports standard costing, moving average, FIFO, LIFO, and weighted average costing methods. It handles BOM/formula cost calculations, cost variances, inventory close, and cost analysis reporting.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Costing Methods** | Support FIFO, LIFO, weighted average, standard cost, and moving average |
| **Standard Cost Setup** | Define and update standard costs for purchased and manufactured items |
| **BOM/Formula Calculations** | Calculate planned costs by rolling up material, labor, and overhead |
| **Cost Variance Analysis** | Analyze purchase price, production, and cost change variances |
| **Inventory Close** | Run inventory close to settle inventory transactions and adjust costs |
| **Costing Sheets** | Configure overhead cost allocation using costing sheet nodes |
| **Cost Groups** | Categorize costs for analysis and variance reporting |
| **Inventory Value Reports** | Report inventory valuation by item, dimension, or warehouse |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 420 - Costing (`420 - Costing.json`)

Cost management configuration entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Reconciliation parameters | CostReconciliationParametersEntity | Costing - Parameters | 30 |
| 10 | Calculation groups | CostCalculationGroupEntity | Costing - Setup | 30 |
| 10 | Cost groups | CostGroupEntity | Costing - Setup | 30 |
| 10 | Costing sheet node | CostSheetNodeEntity | Costing - Sheet | 30 |
| 10 | Costing sheet node absorption basis | CostSheetNodeAbsorptionBasisEntity | Costing - Sheet | 30 |
| 10 | Cost flow assumption policies | CostFlowAssumptionPolicyEntity | Costing - Policies | 30 |
| 20 | Cost group profit percentages | CostGroupProfitPercentageEntity | Costing - Setup | 40 |
| 20 | Costing sheet node calculation factors | CostSheetNodeCalculationFactorEntity | Costing - Sheet | 40 |
| 30 | Costing versions | CostingVersionEntity | Costing - Versions | 50 |

**DMF Load Order Notes:**
- **Seq 10** contains foundational costing setup — cost groups, calculation groups, costing sheet structure, flow assumption policies
- **Seq 20** contains dependent entities — profit percentages on cost groups and calculation factors on costing sheet nodes
- **Seq 30** contains costing versions — the master container for standard costs, planned costs, or cost conversions
- Cost groups must be loaded before profit percentages
- Costing sheet nodes must be loaded before absorption basis and calculation factors

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (cost groups, calculation groups, costing sheet, reconciliation parameters)
- **Level 40:** Dependent entities (profit percentages, calculation factors)
- **Level 50:** Costing versions (loaded last as they reference all other setup)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Cost Management** module.

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

### Plan to produce

*123 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze production operations | 14 | — |
| Control production quality | 30 | — |
| Develop production strategies | 16 | — |
| Plan production operations | 26 | — |
| Run production operations | 37 | — |

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Cost groups | `CostGroupEntity` | `CostGroups` | verified |
| Cost flow assumption policies | `CostFlowAssumptionPolicyEntity` | `CostFlowAssumptionPolicies` | auto-exact |
| Costing versions | `CostingVersionEntity` | `CostingVersions` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Reconciliation parameters | `CostReconciliationParametersEntity` |
| Calculation groups | `CostCalculationGroupEntity` |
| Costing sheet node | `CostSheetNodeEntity` |
| Costing sheet node absorption basis | `CostSheetNodeAbsorptionBasisEntity` |
| Cost group profit percentages | `CostGroupProfitPercentageEntity` |
| Costing sheet node calculation factors | `CostSheetNodeCalculationFactorEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Cost Management:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Cost Management-related business process areas:
- **Inventory to Deliver** (inventory costing, cost of goods sold)
- **Standard cost management** (standard cost setup, cost roll-up, cost conversions)
- **Cost analysis** (inventory valuation, cost variance analysis)
- **Period close** (inventory close, inventory recalculation, adjustment)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and use cost accounting in Dynamics 365 Finance** | https://learn.microsoft.com/en-us/training/paths/configure-use-cost-accounting-dyn365-finance/ |
| Get started with cost management | https://learn.microsoft.com/en-us/training/modules/get-started-cost-management-dyn365-supply-chain-mgmt/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Cost management home page | https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/cost-management-home-page |
| Cost groups | https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/cost-groups |
| Costing sheets | https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/costing-sheets |
| Costing versions | https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/costing-versions |
| Standard cost update overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/standard-cost-conversion-overview |
| BOM calculation | https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/bom-calculations |
| Inventory close | https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/inventory-close |
| Inventory value reports | https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/inventory-value-report-storage |
| FIFO with physical value and marking | https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/fifo-physical-value-marking |
| Weighted average | https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/weighted-average-physical-value-marking |
| Moving average | https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/moving-average |
| Production variance analysis | https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/production-order-cost-analysis |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites (GL & Inventory)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Main accounts | General ledger > Chart of accounts > Accounts > Main accounts | Cost of goods, variance, and WIP accounts |
| Item model groups | Inventory management > Setup > Inventory > Item model groups | Inventory valuation method (FIFO, standard, etc.) |
| Inventory posting setup | Inventory management > Setup > Posting > Posting | Inventory-to-GL account mapping |
| Financial dimensions | General ledger > Chart of accounts > Dimensions | Cost center, site dimensions |

### Phase 2: Cost Group & Calculation Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| CostGroup | Cost management > Inventory accounting policies setup > Cost groups | Cost classification (material, labor, overhead) |
| CostCalculationGroup | Cost management > Predetermined cost policies setup > Calculation groups | BOM calculation parameters |
| CostGroupProfitPercentage | (Within cost group) | Profit markup percentages |
| CostReconciliationParameters | Cost management > Inventory accounting policies setup > Reconciliation parameters | Reconciliation settings |

### Phase 3: Costing Sheet Configuration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| CostSheetNode | Cost management > Inventory accounting policies setup > Costing sheet | Costing sheet hierarchy |
| CostSheetNodeAbsorptionBasis | (Within costing sheet node) | Overhead absorption basis |
| CostSheetNodeCalculationFactor | (Within costing sheet node) | Surcharge/rate calculation factors |
| CostFlowAssumptionPolicy | Cost management > Inventory accounting policies setup > Cost flow assumption policies | FIFO/LIFO policies |

### Phase 4: Costing Versions

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| CostingVersion | Cost management > Predetermined cost policies setup > Costing versions | Standard cost / planned cost containers |
| BOM Cost Price | (Within costing version) | Item cost records |

---

## Cost Management Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    COST MANAGEMENT PROCESS FLOW                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. COST SETUP                                                           │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Define cost groups (material, labor, overhead)         │          │
│     │ • Configure costing sheet (surcharges, rates)            │          │
│     │ • Create costing versions                                │          │
│     │ • Set item cost records (standard cost items)            │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  2. BOM/FORMULA COST ROLL-UP                                             │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Calculate BOM cost (explode through all levels)        │          │
│     │ • Apply overhead surcharges from costing sheet           │          │
│     │ • Review calculated cost vs. current active cost         │          │
│     │ • Activate pending costs                                 │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  3. TRANSACTION COSTING                                                  │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Purchase receipt: cost from PO price or standard cost  │          │
│     │ • Production: standard cost or actual cost               │          │
│     │ • Sales: COGS calculation based on costing method        │          │
│     │ • Transfer: cost carried at inventory valuation           │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  4. PERIOD CLOSE                                                         │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Run inventory close (settle issues to receipts)        │          │
│     │ • Post variance adjustments                              │          │
│     │ • Reconcile inventory subledger to GL                    │          │
│     │ • Review inventory value reports                         │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Inventory Valuation Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| **Standard cost** | Predetermined cost; variances posted separately | Manufacturing, high-volume |
| **FIFO** | First in, first out | General inventory |
| **LIFO** | Last in, first out | Specific industries |
| **Weighted average** | Average cost per period | Common for non-manufactured |
| **Moving average** | Running average cost | Real-time costing needs |
| **FIFO Date** | FIFO with date-based settlement | Date-sensitive costing |
| **LIFO Date** | LIFO with date-based settlement | Date-sensitive costing |

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `CostGroup` | Cost groups | Setup |
| `CostCalculationGroup` | Calculation groups | Setup |
| `CostSheetDesigner` | Costing sheet | Setup |
| `CostingVersion` | Costing versions | Setup |
| `InventClosing` | Inventory close | Period Close |
| `InventRecalculation` | Inventory recalculation | Period Close |
| `InventValueReport` | Inventory value reports | Reports |
| `BOMCalc` | BOM calculation | Calculations |
| `CostFlowAssumptionPolicy` | Cost flow assumption policies | Policies |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Item model groups** define the costing method — must be assigned to products
2. **Cost groups** must exist before they can be assigned to BOM lines and resources
3. **Costing sheet** must be configured before overhead calculations work in BOM cost roll-up
4. **Costing versions** must exist before item cost records can be entered
5. **Standard costs** must be activated in a costing version before they are used in transactions
6. **Inventory posting setup** must include all variance account types for standard cost items
7. **Inventory close** must be run periodically for FIFO/LIFO/weighted average costing methods

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No active cost found" | Standard cost not activated in costing version | Activate pending cost record |
| "Variance account not configured" | Missing GL account for variance type | Add variance accounts in posting setup |
| "BOM calculation error" | Missing cost for component or resource | Ensure all components have active costs |
| "Inventory close cannot run" | Open transactions or previous close not complete | Resolve pending transactions |
| "Cost group not assigned" | BOM line or resource missing cost group | Assign cost group to BOM/resource |
