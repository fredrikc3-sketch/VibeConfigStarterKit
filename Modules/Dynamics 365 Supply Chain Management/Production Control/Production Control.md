# Production Control Module - Knowledge Source

> This file is the central knowledge hub for the **Production Control** module within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Production Control](https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/production-process-overview)

## Module Overview

The Production Control module in Dynamics 365 Supply Chain Management manages discrete and lean manufacturing operations. It handles production orders, bills of materials (BOMs), routes, operations scheduling, job scheduling, production floor execution, and integration with warehouse and inventory modules for material consumption and finished goods receipt.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Production Orders** | Create, estimate, schedule, release, start, and report finished production orders |
| **Bills of Materials (BOM)** | Define product structures with multi-level BOM support |
| **Routes & Operations** | Define manufacturing routes with operation sequences and resource requirements |
| **Operations Scheduling** | Schedule production at the operation level for capacity planning |
| **Job Scheduling** | Schedule individual jobs within operations for detailed shop floor planning |
| **Production Floor Execution** | Provide shop floor workers with a touch-friendly job execution interface |
| **Lean Manufacturing** | Support kanban-based pull manufacturing with production and transfer kanbans |
| **Subcontracting** | Manage outsourced operations with vendor-performed route operations |
| **Production Reporting** | Report production as finished, material consumption, and route operations |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 410 - Production Control (`410 - Production control.json`)

Production control configuration entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Working time templates | WorkingTimeTemplateEntity | Production - Calendars | 30 |
| 10 | Calendars | CalendarEntity | Production - Calendars | 30 |
| 10 | Working times | WorkingTimeEntity | Production - Calendars | 30 |
| 10 | Capabilities | ResourceCapabilityEntity | Production - Resources | 30 |
| 10 | Operations | OperationEntity | Production - Operations | 30 |
| 10 | Route groups | RouteGroupEntity | Production - Routes | 30 |
| 10 | Production journal names | ProdJournalNameEntity | Production - Journals | 30 |
| 10 | Time and attendance groups | TimeAttendanceGroupEntity | Production - T&A | 30 |
| 20 | Operations resources | OperationsResourceEntity | Production - Resources | 40 |
| 20 | Operations resource groups | OperationsResourceGroupEntity | Production - Resources | 40 |
| 20 | Operations resource capabilities | OperationsResourceCapabilityEntity | Production - Resources | 40 |
| 20 | Route headers | RouteHeaderEntity | Production - Routes | 40 |
| 20 | Route operations | RouteOperationEntity | Production - Routes | 40 |
| 20 | Route versions | RouteVersionEntity | Production - Routes | 40 |
| 20 | BOM headers | BOMHeaderEntity | Production - BOM | 40 |
| 20 | BOM lines | BOMLineEntity | Production - BOM | 40 |
| 20 | BOM versions | BOMVersionEntity | Production - BOM | 40 |
| 20 | Job card terminal configurations | JmgJobCardTerminalConfigEntity | Production - Shop Floor | 40 |
| 20 | Job card device configurations | JmgJobCardDeviceConfigEntity | Production - Shop Floor | 40 |
| 30 | Production control parameters | ProdParametersEntity | Production - Parameters | 50 |

**DMF Load Order Notes:**
- **Seq 10** contains foundational setup — working time templates, calendars, capabilities, operations, route groups, journal names, time and attendance groups
- **Seq 20** contains dependent entities — resources (need capabilities), resource groups, routes (need operations & route groups), BOMs, and shop floor configurations
- **Seq 30** contains module parameters — loaded last
- Working time templates must exist before calendars; capabilities before resource assignments
- Operations and route groups must exist before routes
- BOM headers must exist before lines; route headers before operations/versions

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (calendars, capabilities, operations, route groups, journal names)
- **Level 40:** Dependent entities (resources, routes, BOMs, shop floor configurations)
- **Level 50:** Module parameters (loaded last)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Production Control** module.

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

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Calendars | `CalendarEntity` | `WorkCalendars` | verified |
| Operations | `OperationEntity` | `Operations` | verified |
| Operations resources | `OperationsResourceEntity` | `OperationsResources` | auto-exact |
| Operations resource groups | `OperationsResourceGroupEntity` | `OperationsResourceGroups` | manual-unverified |
| Route headers | `RouteHeaderEntity` | `RouteHeaders` | verified |
| Route operations | `RouteOperationEntity` | `RouteOperations` | verified |
| Route versions | `RouteVersionEntity` | `RouteVersions` | verified |
| Production control parameters | `ProdParametersEntity` | `ProdParameters` | manual-unverified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Working time templates | `WorkingTimeTemplateEntity` |
| Working times | `WorkingTimeEntity` |
| Capabilities | `ResourceCapabilityEntity` |
| Route groups | `RouteGroupEntity` |
| Production journal names | `ProdJournalNameEntity` |
| Time and attendance groups | `TimeAttendanceGroupEntity` |
| Operations resource capabilities | `OperationsResourceCapabilityEntity` |
| BOM headers | `BOMHeaderEntity` |
| BOM lines | `BOMLineEntity` |
| BOM versions | `BOMVersionEntity` |
| Job card terminal configurations | `JmgJobCardTerminalConfigEntity` |
| Job card device configurations | `JmgJobCardDeviceConfigEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Production Control:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Production Control-related business process areas:
- **Plan to Produce** (production execution, BOM management, routing)
- **Production order lifecycle** (create, estimate, schedule, release, start, report as finished, end)
- **Shop floor management** (job card, production feedback, time and attendance)
- **Lean manufacturing** (kanban, production flow)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and use discrete manufacturing in Dynamics 365 Supply Chain Management** | https://learn.microsoft.com/en-us/training/paths/configure-use-discrete-manufacturing-dyn365-supply-chain-mgmt/ |
| Get started with production control | https://learn.microsoft.com/en-us/training/modules/get-started-production-control-dyn365-supply-chain-mgmt/ |
| Configure lean manufacturing | https://learn.microsoft.com/en-us/training/modules/get-started-lean-manufacturing-dyn365-supply-chain-mgmt/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Production control overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/production-process-overview |
| Production order lifecycle | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/production-order-lifecycle |
| Bill of materials and formulas | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/bill-of-material-bom |
| Routes and operations | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/routes-operations |
| Operations resources | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/operations-resources |
| Job scheduling | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/job-scheduling |
| Operations scheduling | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/operations-scheduling |
| Production feedback | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/production-feedback |
| Production floor execution | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/production-floor-execution-use |
| Lean manufacturing | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/lean-manufacturing-overview |
| Kanban | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/kanban-overview |
| Resource capabilities | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/resource-capabilities |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Released products | Product information management > Products > Released products | Items to produce |
| Sites & warehouses | Inventory management > Setup > Inventory breakdown | Production locations |
| Units of measure | Organization administration > Setup > Units | Production UOM |
| Main accounts | General ledger > Chart of accounts | WIP, variance, production accounts |
| Production groups | Production control > Setup > Production > Production groups | Posting definitions |

### Phase 2: Calendar & Capacity Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| WorkingTimeTemplate | Organization administration > Setup > Calendars > Working time templates | Shift patterns |
| Calendar | Organization administration > Setup > Calendars > Calendars | Working calendars |
| WorkingTime | (Within calendar) | Calendar time entries |
| ResourceCapability | Production control > Setup > Resources > Resource capabilities | Capability definitions |

### Phase 3: Resource Configuration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| OperationsResource | Organization administration > Resources > Resources | Machine/labor resource definitions |
| OperationsResourceGroup | Organization administration > Resources > Resource groups | Resource grouping |
| OperationsResourceCapability | (Within resource) | Capability assignments |
| RouteGroup | Production control > Setup > Routes > Route groups | Costing and scheduling method per operation |

### Phase 4: BOM & Route Definition

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| Operation | Production control > Setup > Routes > Operations | Operation definitions |
| RouteHeader | Production control > Setup > Routes > Routes | Route master records |
| RouteOperation | (Within route) | Route operation steps |
| RouteVersion | (Within route) | Route version activation |
| BOMHeader | Product information management > Bills of materials and formulas > Bills of materials | BOM master records |
| BOMLine | (Within BOM) | Component lines |
| BOMVersion | (Within BOM) | BOM version activation |

### Phase 5: Shop Floor & Parameters

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| JmgJobCardTerminalConfig | Production control > Setup > Manufacturing execution > Configure job card for devices | Job card terminal setup |
| JmgJobCardDeviceConfig | Production control > Setup > Manufacturing execution > Configure job card for devices | Device registration |
| ProdJournalName | Production control > Setup > Production journal names | Picking list, route card, job card, RAF journals |
| ProdParameters | Production control > Setup > Production control parameters | Module parameters |

---

## Production Order Lifecycle

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PRODUCTION ORDER LIFECYCLE                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐          │
│  │ CREATED   │───▶│ ESTIMATED │───▶│ SCHEDULED│───▶│ RELEASED │          │
│  │           │    │           │    │           │    │           │          │
│  │ • BOM     │    │ • Material│    │ • Job     │    │ • Picking │          │
│  │   exploded│    │   cost    │    │   schedule│    │   list    │          │
│  │ • Route   │    │ • Resource│    │ • Ops     │    │   ready   │          │
│  │   attached│    │   cost    │    │   schedule│    │ • Shop    │          │
│  │           │    │ • WIP     │    │ • Gantt   │    │   floor   │          │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘          │
│                                                                          │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐                           │
│  │ STARTED   │───▶│ REPORTED  │───▶│ ENDED    │                           │
│  │           │    │ AS        │    │           │                           │
│  │ • Picking │    │ FINISHED  │    │ • Cost   │                           │
│  │   list    │    │           │    │   calc   │                           │
│  │   posted  │    │ • Output  │    │ • WIP    │                           │
│  │ • Route   │    │   to      │    │   settled│                           │
│  │   card    │    │   inventory│    │ • Variance│                          │
│  │   started │    │ • RAF     │    │   posted │                           │
│  └──────────┘    │   journal │    │ • Order  │                           │
│                   └──────────┘    │   closed │                           │
│                                   └──────────┘                           │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Production Journal Types

| Journal Type | Purpose | When Used |
|-------------|---------|-----------|
| **Picking list** | Material consumption | Start / during production |
| **Route card** | Time/resource reporting per operation | During production |
| **Job card** | Detailed job-level reporting | During production |
| **Report as finished** | Output reporting of finished goods | Completion |

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `ProdTable` | All production orders | Orders |
| `ProdTableSchedule` | Production scheduling | Scheduling |
| `ProdParmRelease` | Release production orders | Orders |
| `BOMTable` | Bills of materials | BOM |
| `RouteTable` | Routes | Routes |
| `OperationsResource` | Resources | Resources |
| `OperationsResourceGroup` | Resource groups | Resources |
| `ProdParameters` | Production control parameters | Setup |
| `ProdJournalName` | Production journal names | Setup |
| `JmgJobCardTerminal` | Job card terminal | Shop Floor |
| `ProdFloorExecution` | Production floor execution | Shop Floor |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Working time templates** must exist before calendars
2. **Calendars** must be assigned to resources, sites, and warehouses for scheduling
3. **Capabilities** must be defined before assigning to resources
4. **Operations** must exist before routes can reference them
5. **Route groups** must exist before route operations (define costing/scheduling method)
6. **BOM versions** must be activated for products at the correct site
7. **Route versions** must be activated for products at the correct site
8. **Production groups** must be assigned for inventory posting
9. **Production parameters** should be configured before first production order
10. **Job card terminal** configuration is required for shop floor execution

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No active BOM version" | BOM version not activated for site/date | Activate BOM version |
| "No active route version" | Route version not activated for site/date | Activate route version |
| "Resource not available" | Calendar not assigned or no capacity | Assign calendar to resource |
| "Scheduling conflict" | Insufficient capacity or overlapping jobs | Review Gantt chart, adjust capacity |
| "Picking list posting error" | Insufficient inventory or missing posting | Ensure stock availability and posting setup |
| "WIP account not configured" | Missing production posting profile | Add WIP accounts to posting setup |
