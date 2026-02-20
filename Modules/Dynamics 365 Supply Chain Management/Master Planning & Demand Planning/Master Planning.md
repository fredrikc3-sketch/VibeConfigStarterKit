# Master Planning Module - Knowledge Source

> This file is the central knowledge hub for the **Master Planning & Demand Planning** module within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Master Planning & Demand Planning](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-planning-home-page)

## Module Overview

The Master Planning module (Planning Optimization) in Dynamics 365 Supply Chain Management automates supply planning by calculating net requirements and generating planned orders for purchasing, production, and transfer. Demand Planning integrates with Azure Machine Learning for AI-powered demand forecasting using historical data and external signals.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Planning Optimization** | Cloud-based MRP engine for fast, scalable supply planning calculations |
| **Net Requirements** | Calculate supply needs based on demand, on-hand, and planned orders |
| **Planned Orders** | Generate planned purchase, production, and transfer orders automatically |
| **Demand Forecasting** | Use AI/ML models to predict future demand from historical patterns |
| **Safety Stock** | Calculate and maintain safety stock levels to buffer demand variability |
| **Coverage Groups & Rules** | Define planning parameters by item or item group |
| **Action & Futures Messages** | Get recommendations to expedite, postpone, or adjust planned orders |
| **Intercompany Planning** | Plan supply across legal entities in an intercompany chain |
| **Finite Capacity Planning** | Consider resource constraints when scheduling planned orders |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 430 - Master Planning (`430 - Master planning.json`)

Master planning configuration entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Forecast models | ForecastModelEntity | Planning - Setup | 30 |
| 10 | Forecast sub models | ForecastSubModelEntity | Planning - Setup | 30 |
| 10 | Working time templates | WorkingTimeTemplateEntity | Planning - Calendars | 30 |
| 10 | Calendars | CalendarEntity | Planning - Calendars | 30 |
| 10 | Period templates | PeriodTemplateEntity | Planning - Setup | 30 |
| 10 | Period template lines | PeriodTemplateLineEntity | Planning - Setup | 40 |
| 10 | Time transactions | TimeTransactionEntity | Planning - Calendars | 30 |
| 20 | Master plans | MasterPlanEntity | Planning - Plans | 40 |
| 20 | Forecast plans | ForecastPlanEntity | Planning - Plans | 40 |
| 30 | Master planning parameters | MasterPlanningParametersEntity | Planning - Parameters | 50 |
| 30 | Item coverage groups | ItemCoverageGroupEntity | Planning - Coverage | 50 |

**DMF Load Order Notes:**
- **Seq 10** contains foundational setup — forecast models, working time templates, calendars, period templates
- **Seq 20** contains the master plan and forecast plan definitions — depend on forecast models and calendars
- **Seq 30** contains planning parameters and item coverage groups — loaded last
- Forecast models must exist before sub-models can reference them
- Working time templates must be loaded before calendars that use them
- Period template headers must be loaded before period template lines

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (forecast models, calendars, working time templates, period templates)
- **Level 40:** Plan definitions, period template lines
- **Level 50:** Module parameters, item coverage groups (loaded last)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Master Planning & Demand Planning** module.

### Forecast to plan

*73 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze business performance | 3 | — |
| Conduct sales and operations planning | 24 | [Learn more](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/forecast-to-plan-manage-intercompany-forecast) |
| Develop business strategy | 22 | — |
| Execute sales and operations | 24 | — |

### Plan to produce

*123 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze production operations | 14 | — |
| Control production quality | 30 | — |
| Develop production strategies | 16 | — |
| Plan production operations | 26 | — |
| Run production operations | 37 | — |

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

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Forecast models | `ForecastModelEntity` | `ForecastModels` | verified |
| Calendars | `CalendarEntity` | `WorkCalendars` | verified |
| Item coverage groups | `ItemCoverageGroupEntity` | `ItemCoverageGroups` | manual-unverified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Forecast sub models | `ForecastSubModelEntity` |
| Working time templates | `WorkingTimeTemplateEntity` |
| Period templates | `PeriodTemplateEntity` |
| Period template lines | `PeriodTemplateLineEntity` |
| Time transactions | `TimeTransactionEntity` |
| Master plans | `MasterPlanEntity` |
| Forecast plans | `ForecastPlanEntity` |
| Master planning parameters | `MasterPlanningParametersEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Master Planning:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Master Planning-related business process areas:
- **Plan to Produce** (demand forecasting, supply planning, MRP)
- **Master scheduling** (planned orders generation, firming)
- **Demand forecasting** (statistical forecasting, demand planning)
- **Supply planning** (coverage rules, lead times, safety stock)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and use master planning in Dynamics 365 Supply Chain Management** | https://learn.microsoft.com/en-us/training/paths/configure-use-master-planning-dyn365-supply-chain-mgmt/ |
| Get started with master planning | https://learn.microsoft.com/en-us/training/modules/get-started-master-planning-dyn365-supply-chain-mgmt/ |
| Configure Planning Optimization | https://learn.microsoft.com/en-us/training/modules/planning-optimization-dyn365-supply-chain-mgmt/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Master planning home page | https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-planning-home-page |
| Planning Optimization overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planning-optimization-overview |
| Coverage settings | https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/coverage-settings |
| Item coverage groups | https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/coverage-settings |
| Safety stock | https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-replenishment |
| Master plans | https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans |
| Demand forecasting | https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/introduction-demand-forecasting |
| Planned orders | https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planned-orders |
| Action messages | https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages |
| Calendars and master planning | https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/supply-chain-calendars-master-planning |
| Net requirements and pegging | https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/net-requirements |
| Demand Driven MRP (DDMRP) | https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/ddmrp-overview |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Released products | Product information management > Products > Released products | Items to plan |
| Item model groups | Inventory management > Setup > Inventory > Item model groups | Valuation method |
| Default order settings | (Per released product) | Default order type, quantities, warehouses |
| Sites & warehouses | Inventory management > Setup > Inventory breakdown | Physical locations |
| Vendors | Accounts payable > Vendors > All vendors | Purchase lead times |

### Phase 2: Calendar & Capacity Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| WorkingTimeTemplate | Organization administration > Setup > Calendars > Working time templates | Working day/shift patterns |
| Calendar | Organization administration > Setup > Calendars > Calendars | Working calendars for resources/vendors |
| TimeTransaction | (Within calendar) | Working time entries |

### Phase 3: Forecast & Coverage Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| ForecastModel | Master planning > Setup > Demand forecasting > Forecast models | Forecast model hierarchy |
| ForecastSubModel | (Within forecast model) | Sub-model definitions |
| ItemCoverageGroup | Master planning > Setup > Coverage > Coverage groups | Planning policies per item group |
| PeriodTemplate | Master planning > Setup > Coverage > Period templates | Period fence definitions |
| PeriodTemplateLine | (Within period template) | Period boundary lines |

### Phase 4: Plan & Parameters

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| MasterPlan | Master planning > Setup > Plans > Master plans | Plan definitions |
| ForecastPlan | Master planning > Setup > Demand forecasting > Forecast plans | Forecast plan definitions |
| MasterPlanningParameters | Master planning > Setup > Master planning parameters | Module parameters |

---

## Master Planning Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     MASTER PLANNING PROCESS FLOW                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. DEMAND INPUT                                                         │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Sales orders                                           │          │
│     │ • Sales forecasts                                        │          │
│     │ • Safety stock requirements                              │          │
│     │ • Minimum/maximum inventory policies                     │          │
│     │ • Project requirements                                   │          │
│     │ • Transfer orders and intercompany demand                │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  2. PLANNING OPTIMIZATION RUN                                            │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Net requirements calculation                           │          │
│     │ • Explosion through BOM/formula                          │          │
│     │ • Lead time scheduling                                   │          │
│     │ • Calendar-based date calculation                        │          │
│     │ • Generate planned orders (purchase, production, transfer)│          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  3. REVIEW & ADJUST                                                      │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Review planned orders                                  │          │
│     │ • Evaluate action messages (advance, postpone, etc.)     │          │
│     │ • Adjust quantities and dates                            │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  4. FIRMING                                                              │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Firm planned purchase orders → Purchase orders         │          │
│     │ • Firm planned production orders → Production orders     │          │
│     │ • Firm planned transfer orders → Transfer orders         │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Coverage Group Settings

| Setting | Options | Description |
|---------|---------|-------------|
| **Coverage code** | Requirement, Period, Min/Max, Manual | How demand is satisfied |
| **Coverage time fence** | Days | Planning horizon |
| **Negative days** | Days | Allows use of existing receipts in the past |
| **Positive days** | Days | Allows future receipts to cover current demand |
| **Action message** | Yes/No | Generate recommendations |
| **Firming time fence** | Days | Auto-firming horizon |

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `ReqParameters` | Master planning parameters | Setup |
| `ReqPlanSched` | Master plans | Setup |
| `ReqCovGroup` | Coverage groups | Setup |
| `ReqPlannedOrders` | Planned orders | Planning |
| `ReqNetRequirements` | Net requirements | Inquiry |
| `ReqActionMessages` | Action messages | Planning |
| `ForecastModels` | Forecast models | Forecasting |
| `ReqDemandForecast` | Demand forecasts | Forecasting |
| `ReqItemCoverage` | Item coverage | Setup |
| `WorkCalendarTable` | Calendars | Setup |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Released products** must have default order settings before planning runs
2. **Item coverage groups** must be assigned to products for planning policies
3. **Calendars** must be assigned to sites/warehouses/vendors for date calculation
4. **Working time templates** must exist before calendars referencing them
5. **Master plan definition** must exist before running planning
6. **Planning Optimization** is the default engine — deprecated master planning requires explicit setup
7. **Coverage time fences** should be configured before first planning run

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No coverage group assigned" | Item missing coverage group | Assign coverage group to item |
| "Calendar not found" | Site/warehouse missing calendar | Assign working calendar |
| "Planning run failed" | Data inconsistency or missing setup | Check planning log for details |
| "Planned order quantity is zero" | Min/max not configured correctly | Review coverage group rules |
| "Lead time not defined" | Vendor or production lead time missing | Set lead times on item or vendor |
