# Asset Management Module - Knowledge Source

> This file is the central knowledge hub for **Asset Management** within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Asset Management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/index)

## Module Overview

The Asset Management module in Dynamics 365 Supply Chain Management provides enterprise asset management (EAM) for maintaining and servicing physical assets and equipment. It supports work orders, preventive maintenance scheduling, asset lifecycle tracking, fault management, and integration with production and warehouse modules.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Asset Registry** | Maintain a comprehensive registry of physical assets with hierarchies and attributes |
| **Work Orders** | Create, schedule, and manage maintenance work orders with job types |
| **Preventive Maintenance** | Schedule recurring maintenance based on time, counter, or condition triggers |
| **Maintenance Plans** | Define maintenance plans and rounds for systematic asset care |
| **Fault Management** | Record and analyze asset faults, symptoms, and causes for root cause analysis |
| **Asset Lifecycle States** | Track asset states from installation through decommissioning |
| **Resource Scheduling** | Assign maintenance workers and tools to work orders |
| **Asset KPIs** | Monitor asset performance with KPIs like MTBF and MTTR |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Asset management uses dedicated maintenance scheduling, work order, and asset hierarchy forms.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Asset Management-related business process areas:
- **Functional locations** (physical locations where assets operate)
- **Assets** (equipment, machinery, buildings)
- **Maintenance plans** (preventive maintenance schedules)
- **Work orders** (corrective and preventive maintenance execution)
- **Work order lifecycle** (states from created → completed)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure Asset Management in Dynamics 365 Supply Chain Management** | https://learn.microsoft.com/en-us/training/modules/configure-asset-management-dyn365-supply-chain-mgmt/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Asset management overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/index |
| Functional locations | https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/functional-locations/introduction-to-functional-locations |
| Assets overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/objects/introduction-to-objects |
| Asset types | https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/setup-for-objects/object-types |
| Maintenance plans | https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/preventive-and-reactive-maintenance/maintenance-plans |
| Work orders | https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/work-orders/introduction-to-work-orders |
| Work order lifecycle states | https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/setup-for-work-orders/work-order-lifecycle-states |
| Maintenance requests | https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/manage-maintenance-requests/maintenance-request-overview |
| Maintenance workers and groups | https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/setup-for-work-orders/maintenance-worker-groups |
| Asset BOM (bill of materials) | https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/objects/object-bom |
| Integration with Fixed Assets | https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/integration-to-fixed-assets/fixed-asset-integration |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Asset management parameters | Asset management > Setup > Asset management parameters | Module settings |
| Workers (maintenance) | Human resources > Workers | Maintenance technicians |
| Warehouses | Inventory management > Setup > Inventory breakdown > Warehouses | Spare parts inventory |

### Phase 2: Type & Location Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Functional location types | Asset management > Setup > Functional locations > Functional location types | Location classifications |
| Functional location lifecycle states | Asset management > Setup > Functional locations > Lifecycle states | Active, inactive, demolished |
| Functional locations | Asset management > Functional locations > All functional locations | Physical location hierarchy |
| Asset types | Asset management > Setup > Assets > Asset types | Equipment classification |
| Asset lifecycle states | Asset management > Setup > Assets > Lifecycle states | Created, active, scrapped |

### Phase 3: Asset Configuration

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Assets | Asset management > Assets > All assets | Create asset records |
| Asset attributes | (Within asset type or asset) | Custom attributes |
| Asset BOM | (Within asset) > BOM | Spare parts list |
| Counters / meters | Asset management > Setup > Asset types > Counters | Usage meters (hours, km) |
| Asset criticality | Asset management > Setup > Assets > Criticality | Priority classification |

### Phase 4: Maintenance Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Maintenance job types | Asset management > Setup > Work orders > Maintenance job types | Repair, inspection, lubrication |
| Maintenance workers | Asset management > Setup > Workers > Maintenance workers | Assign worker capabilities |
| Maintenance worker groups | Asset management > Setup > Workers > Maintenance worker groups | Crew/team definitions |
| Maintenance plans | Asset management > Setup > Preventive maintenance > Maintenance plans | Scheduled PM intervals |
| Maintenance rounds | Asset management > Setup > Preventive maintenance > Maintenance rounds | Group maintenance tasks |

### Phase 5: Work Order Execution

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Work order lifecycle model | Asset management > Setup > Work orders > Lifecycle models | State flow configuration |
| Maintenance requests | Asset management > Maintenance requests | Corrective maintenance trigger |
| Work orders | Asset management > Work orders > All work orders | Execute maintenance work |
| Schedule maintenance | Asset management > Periodic > Preventive maintenance > Schedule maintenance plans | Generate PM work orders |

---

## Asset Management Lifecycle

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  ASSET MANAGEMENT LIFECYCLE                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ASSET SETUP                                                             │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ Functional Location ← Asset installed at location        │             │
│  │ Asset Type → Asset Record → BOM (spare parts)            │             │
│  │ Counters/meters attached                                 │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│              ┌───────────────┼───────────────┐                           │
│              ▼                               ▼                           │
│  PREVENTIVE MAINTENANCE             CORRECTIVE MAINTENANCE              │
│  ┌──────────────────┐              ┌──────────────────┐                 │
│  │ Maintenance Plan   │              │ Maintenance       │                 │
│  │ (Time/Counter)     │              │ Request            │                 │
│  │   │                │              │ (Breakdown/Issue)  │                 │
│  │   ▼                │              │   │                │                 │
│  │ Schedule batch →   │              │   ▼                │                 │
│  │ Generate Work      │              │ Create Work        │                 │
│  │ Orders             │              │ Order              │                 │
│  └────────┬───────────┘              └────────┬───────────┘                 │
│           │                                   │                          │
│           └───────────────┬───────────────────┘                          │
│                           ▼                                              │
│  WORK ORDER EXECUTION                                                    │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ Created → Scheduled → In Progress → Completed → Posted  │             │
│  │                                                          │             │
│  │ • Assign maintenance worker(s)                           │             │
│  │ • Consume spare parts (inventory)                        │             │
│  │ • Record hours and notes                                 │             │
│  │ • Update counter readings                                │             │
│  │ • Post costs to project / cost center                    │             │
│  └────────────────────────────────────────────────────────┘             │
│                           │                                              │
│                           ▼                                              │
│  ANALYSIS                                                                │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Asset fault analysis (failure codes)                     │             │
│  │ • KPIs: MTBF, MTTR, availability                         │             │
│  │ • Cost history per asset                                  │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `EntAssetObjectTable` | All assets | Assets |
| `EntAssetFunctionalLocation` | Functional locations | Locations |
| `EntAssetWorkOrder` | All work orders | Work Orders |
| `EntAssetMaintenanceRequest` | Maintenance requests | Requests |
| `EntAssetMaintenancePlan` | Maintenance plans | Preventive |
| `EntAssetMaintenanceRound` | Maintenance rounds | Preventive |
| `EntAssetObjectType` | Asset types | Setup |
| `EntAssetWorkerGroup` | Maintenance worker groups | Setup |
| `EntAssetParameters` | Asset management parameters | Setup |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Asset management parameters** must be configured first
2. **Functional location types** and **lifecycle states** before functional locations
3. **Asset types** before creating assets
4. **Assets** must be installed at functional locations for location-based reporting
5. **Maintenance job types** before maintenance plans and work orders
6. **Maintenance workers** must be configured before work order assignment
7. **Maintenance plans** must be scheduled (batch) to auto-generate work orders

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Asset lifecycle state invalid" | Wrong transition attempted | Check lifecycle model allowed transitions |
| "Work order cannot be scheduled" | No maintenance worker available | Assign qualified workers or adjust schedule |
| "Counter reading invalid" | Reading less than previous value | Verify counter entries chronologically |
| "PM work orders not generated" | Schedule batch not run | Run the schedule maintenance plans batch |
| "Spare part not available" | Inventory not in asset warehouse | Transfer or procure spare parts |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Asset Management** module.

### Acquire to dispose

*46 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Acquire assets | 14 | — |
| Analyze assets | 5 | — |
| Define asset strategy | 2 | — |
| Dispose of assets | 3 | — |
| Manage active assets | 2 | — |
| Perform asset maintenance | 20 | — |

### Service to deliver

*43 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze service performance | 5 | — |
| Deliver services | 13 | — |
| Develop service strategy | 11 | — |
| Manage service work | 8 | — |
| Plan service work | 6 | — |

