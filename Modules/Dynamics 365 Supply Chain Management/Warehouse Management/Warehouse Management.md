# Warehouse Management Module - Knowledge Source

> This file is the central knowledge hub for the **Warehouse Management** module within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Warehouse Management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/warehouse-management-overview)

## Module Overview

The Warehouse Management module (WMS) in Dynamics 365 Supply Chain Management provides advanced warehouse operations including wave processing, work creation, location directives, mobile device-driven picking/putaway, container management, replenishment, and cycle counting. It supports complex warehouse layouts with zones, locations, and location profiles.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Wave Processing** | Group and process outbound shipments into waves for efficient picking |
| **Work Templates & Policies** | Define work creation rules for pick, put, count, and replenishment |
| **Location Directives** | Configure rules to determine optimal put and pick locations |
| **Mobile Device Operations** | Execute warehouse tasks via the Warehouse Management mobile app |
| **Containerization** | Pack items into containers with automated packing strategies |
| **Cycle Counting** | Perform perpetual inventory counts using plans and thresholds |
| **Replenishment** | Automatically replenish pick locations from bulk storage |
| **Cluster Picking** | Pick items for multiple orders simultaneously to improve efficiency |
| **Inbound/Outbound Operations** | Manage receiving, putaway, picking, packing, and shipping |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 400 - Warehouse Management (`400 - Warehouse management.json`)

Warehouse management configuration entities. This is the largest DMF template with approximately 112 entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Wave templates | WHSWaveTemplateEntity | WMS - Waves | 30 |
| 10 | Wave attributes | WHSWaveAttributeEntity | WMS - Waves | 30 |
| 10 | Wave process methods | WHSWaveProcessMethodEntity | WMS - Waves | 30 |
| 10 | Location profiles | WHSLocationProfileEntity | WMS - Locations | 30 |
| 10 | Location formats | WHSLocationFormatEntity | WMS - Locations | 30 |
| 10 | Location types | WHSLocationTypeEntity | WMS - Locations | 30 |
| 10 | Work classes | WHSWorkClassEntity | WMS - Work | 30 |
| 10 | Work pool | WHSWorkPoolEntity | WMS - Work | 30 |
| 10 | Container types | WHSContainerTypeEntity | WMS - Containers | 30 |
| 10 | Container groups | WHSContainerGroupEntity | WMS - Containers | 30 |
| 10 | Mobile device menu items | WHSMobileDeviceMenuItemEntity | WMS - Mobile | 30 |
| 10 | Mobile device menu | WHSMobileDeviceMenuEntity | WMS - Mobile | 30 |
| 10 | Cluster profiles | WHSClusterProfileEntity | WMS - Picking | 30 |
| 10 | Cycle counting plans | WHSCycleCountPlanEntity | WMS - Counting | 30 |
| 10 | Cycle counting thresholds | WHSCycleCountThresholdEntity | WMS - Counting | 30 |
| 10 | Document routing | WHSDocumentRoutingEntity | WMS - Documents | 30 |
| 20 | Work templates | WHSWorkTemplateEntity | WMS - Work | 40 |
| 20 | Work policies | WHSWorkPolicyEntity | WMS - Work | 40 |
| 20 | Location directives | WHSLocationDirectiveEntity | WMS - Locations | 40 |
| 20 | Wave template details | WHSWaveTemplateDetailEntity | WMS - Waves | 40 |
| 20 | Replenishment templates | WHSReplenishmentTemplateEntity | WMS - Replenishment | 40 |
| 20 | Mobile device users | WHSMobileDeviceUserEntity | WMS - Mobile | 40 |
| 30 | Warehouse management parameters | WHSParametersEntity | WMS - Parameters | 50 |

**DMF Load Order Notes:**
- **Seq 10** contains foundational setup — wave templates/attributes/methods, location profiles/formats/types, work classes/pools, container types/groups, mobile device menu items/menus, cluster profiles, cycle counting, document routing
- **Seq 20** contains dependent entities — work templates (need work classes), work policies, location directives (need location profiles), wave template details, replenishment templates, mobile device users
- **Seq 30** contains module parameters
- Location types and profiles must exist before location directives
- Work classes must exist before work templates reference them
- Wave template headers must exist before wave template details
- Mobile device menu items must exist before menus reference them

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (wave templates, location setup, work classes, containers, mobile device menus, counting, documents)
- **Level 40:** Dependent entities (work templates, location directives, work policies, replenishment, mobile users)
- **Level 50:** Module parameters (loaded last)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Warehouse Management** module.

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

### Order to cash

*97 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze sales performance | 13 | — |
| Develop sales policies | 12 | — |
| Manage accounts receivable | 11 | — |
| Manage sales orders | 61 | — |

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
| Mobile device menu items | `WHSMobileDeviceMenuItemEntity` | `WHSMobileWorkMenuItems` | verified |
| Mobile device menu | `WHSMobileDeviceMenuEntity` | `WHSMobileWorkMenus` | verified |
| Replenishment templates | `WHSReplenishmentTemplateEntity` | `WarehouseReplenishmentTemplates` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Wave templates | `WHSWaveTemplateEntity` |
| Wave attributes | `WHSWaveAttributeEntity` |
| Wave process methods | `WHSWaveProcessMethodEntity` |
| Location profiles | `WHSLocationProfileEntity` |
| Location formats | `WHSLocationFormatEntity` |
| Location types | `WHSLocationTypeEntity` |
| Work classes | `WHSWorkClassEntity` |
| Work pool | `WHSWorkPoolEntity` |
| Container types | `WHSContainerTypeEntity` |
| Container groups | `WHSContainerGroupEntity` |
| Cluster profiles | `WHSClusterProfileEntity` |
| Cycle counting plans | `WHSCycleCountPlanEntity` |
| Cycle counting thresholds | `WHSCycleCountThresholdEntity` |
| Document routing | `WHSDocumentRoutingEntity` |
| Work templates | `WHSWorkTemplateEntity` |
| Work policies | `WHSWorkPolicyEntity` |
| Location directives | `WHSLocationDirectiveEntity` |
| Wave template details | `WHSWaveTemplateDetailEntity` |
| Mobile device users | `WHSMobileDeviceUserEntity` |
| Warehouse management parameters | `WHSParametersEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Warehouse Management:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Warehouse Management-related business process areas:
- **Inventory to Deliver** (receiving, put-away, picking, packing, shipping)
- **Warehouse operations** (wave processing, work execution, replenishment)
- **Inbound processing** (purchase receipt, cross-docking, quality inspection)
- **Outbound processing** (wave pick, cluster pick, packing, staging)
- **Inventory management** (cycle counting, movement, adjustments)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and use warehouse management in Dynamics 365 Supply Chain Management** | https://learn.microsoft.com/en-us/training/paths/configure-use-warehouse-management-dyn365-supply-chain-mgmt/ |
| Configure warehouse management | https://learn.microsoft.com/en-us/training/modules/configure-warehouse-management-dyn365-supply-chain-mgmt/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Warehouse management overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/warehouse-management-overview |
| Warehouse configuration | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/warehouse-configuration |
| Location directives | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/create-location-directive |
| Work templates | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/control-warehouse-location-directives |
| Wave processing | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wave-processing |
| Wave templates | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wave-templates |
| Mobile device setup | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/configure-mobile-devices-warehouse |
| Warehouse mobile app | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/install-configure-warehouse-management-app |
| Location profiles | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/location-profile |
| Cluster picking | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/set-up-cluster-picking |
| Replenishment | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/replenishment |
| Cycle counting | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting |
| Containerization | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wave-containerization |
| Cross-docking | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/planned-cross-docking |
| Reservation hierarchies | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/flexible-warehouse-level-dimension-reservation |

---

## 6-Phase Configuration Sequence

### Phase 1: Prerequisites (Sites & Inventory)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Sites | Inventory management > Setup > Inventory breakdown > Sites | Physical site definitions |
| Warehouses (WMS-enabled) | Warehouse management > Setup > Warehouse > Warehouses | Enable WMS on warehouse |
| Storage dimension groups | Product information management > Setup > Dimension and variant groups | Must include Location + License plate |
| Reservation hierarchies | Warehouse management > Setup > Warehouse > Reservation hierarchies | Control batch/serial reservation level |
| Units of measure | Organization administration > Setup > Units | Weight, volume, dimensions |

### Phase 2: Warehouse Layout

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| WHSLocationType | Warehouse management > Setup > Warehouse > Location types | Pick, bulk, staging, dock, etc. |
| WHSLocationFormat | Warehouse management > Setup > Warehouse > Location formats | Naming convention for locations |
| WHSLocationProfile | Warehouse management > Setup > Warehouse > Location profiles | Location behavior rules |
| Warehouse locations | (Within warehouse setup) | Physical location generation |
| Zones / Zone groups | Warehouse management > Setup > Warehouse > Zones | Logical area groupings |

### Phase 3: Work Configuration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| WHSWorkClass | Warehouse management > Setup > Work > Work classes | Work type classification |
| WHSWorkPool | Warehouse management > Setup > Work > Work pools | Work grouping for processing |
| WHSWorkTemplate | Warehouse management > Setup > Work > Work templates | Pick/put work structure definition |
| WHSWorkPolicy | Warehouse management > Setup > Work > Work policies | Work creation exceptions |
| WHSLocationDirective | Warehouse management > Setup > Location directives | Where to pick/put inventory |

### Phase 4: Wave & Processing

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| WHSWaveTemplate | Warehouse management > Setup > Waves > Wave templates | Wave processing steps |
| WHSWaveTemplateDetail | (Within wave template) | Process method sequence |
| WHSWaveAttribute | Warehouse management > Setup > Waves > Wave attributes | Wave grouping criteria |
| WHSReplenishmentTemplate | Warehouse management > Setup > Replenishment > Replenishment templates | Auto-replenishment rules |
| WHSContainerType | Warehouse management > Setup > Containers > Container types | Container dimensions/limits |
| WHSContainerGroup | Warehouse management > Setup > Containers > Container groups | Container grouping |
| WHSClusterProfile | Warehouse management > Setup > Mobile device > Cluster profiles | Cluster picking configuration |

### Phase 5: Mobile Device & Counting

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| WHSMobileDeviceMenuItem | Warehouse management > Setup > Mobile device > Mobile device menu items | Individual work operations |
| WHSMobileDeviceMenu | Warehouse management > Setup > Mobile device > Mobile device menu | Menu structure for app |
| WHSMobileDeviceUser | Warehouse management > Setup > Mobile device > Mobile device user accounts | Worker-to-user mapping |
| WHSCycleCountPlan | Warehouse management > Setup > Cycle counting > Cycle count plans | Recurring count schedules |
| WHSCycleCountThreshold | Warehouse management > Setup > Cycle counting > Cycle count thresholds | Minimum quantity triggers |
| WHSDocumentRouting | Warehouse management > Setup > Document routing | Label/document printing rules |

### Phase 6: Parameters

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| WHSParameters | Warehouse management > Setup > Warehouse management parameters | Module parameters |

---

## Warehouse Operations Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   WAREHOUSE OPERATIONS PROCESS FLOW                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────── INBOUND ───────────┐  ┌─────────── OUTBOUND ───────────┐ │
│  │                                │  │                                 │ │
│  │  1. RECEIVING                  │  │  1. WAVE PROCESSING             │ │
│  │  ┌──────────────────────┐     │  │  ┌───────────────────────┐     │ │
│  │  │ • PO/TO receipt        │     │  │  │ • Release SO/TO to      │     │ │
│  │  │ • License plate receipt│     │  │  │   warehouse              │     │ │
│  │  │ • Mixed LP receiving   │     │  │  │ • Create / process wave  │     │ │
│  │  │ • Cross-dock check     │     │  │  │ • Allocate inventory     │     │ │
│  │  └──────────────────────┘     │  │  │ • Create pick work       │     │ │
│  │             │                  │  │  └───────────────────────┘     │ │
│  │             ▼                  │  │             │                   │ │
│  │  2. PUT-AWAY                   │  │             ▼                   │ │
│  │  ┌──────────────────────┐     │  │  2. PICKING                     │ │
│  │  │ • Location directive   │     │  │  ┌───────────────────────┐     │ │
│  │  │   determines put loc   │     │  │  │ • Single order pick     │     │ │
│  │  │ • Work created:        │     │  │  │ • Cluster picking       │     │ │
│  │  │   Pick → Put           │     │  │  │ • Batch picking         │     │ │
│  │  │ • Execute on mobile    │     │  │  │ • Zone picking          │     │ │
│  │  └──────────────────────┘     │  │  │ • Execute on mobile     │     │ │
│  │             │                  │  │  └───────────────────────┘     │ │
│  │             ▼                  │  │             │                   │ │
│  │  3. QUALITY (Optional)         │  │             ▼                   │ │
│  │  ┌──────────────────────┐     │  │  3. PACKING                     │ │
│  │  │ • Quality order         │     │  │  ┌───────────────────────┐     │ │
│  │  │ • Quarantine            │     │  │  │ • Pack station          │     │ │
│  │  │ • Released to           │     │  │  │ • Containerization      │     │ │
│  │  │   available stock       │     │  │  │ • Label printing        │     │ │
│  │  └──────────────────────┘     │  │  └───────────────────────┘     │ │
│  │                                │  │             │                   │ │
│  └────────────────────────────────┘  │             ▼                   │ │
│                                      │  4. SHIPPING                    │ │
│  ┌─────── REPLENISHMENT ───────┐    │  ┌───────────────────────┐     │ │
│  │ • Demand replenishment       │    │  │ • Stage to dock         │     │ │
│  │ • Min/max replenishment      │    │  │ • Load confirmation     │     │ │
│  │ • Load demand replenishment  │    │  │ • Ship confirm          │     │ │
│  └──────────────────────────────┘    │  │ • BOL generation        │     │ │
│                                      │  └───────────────────────┘     │ │
│                                      └─────────────────────────────────┘ │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Core WMS Concepts

| Concept | Description | Configuration |
|---------|-------------|---------------|
| **Work Template** | Defines the work steps (pick/put pairs) | Per work order type and warehouse |
| **Location Directive** | Determines WHERE to pick/put | Per work order type, work type, warehouse |
| **Wave Template** | Groups & processes released orders | Per order type (sales, transfer, production) |
| **Mobile Device Menu Item** | Individual operations on the handheld | System-directed or user-directed work |
| **License Plate** | Container/pallet tracking unit | Generated or received from vendor |
| **Reservation Hierarchy** | Controls at which level batch/serial is reserved | Above or below location level |

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `WHSParameters` | Warehouse management parameters | Setup |
| `WHSWorkTemplate` | Work templates | Work |
| `WHSLocationDirective` | Location directives | Locations |
| `WHSWaveTemplate` | Wave templates | Waves |
| `WHSMobileDevMenu` | Mobile device menu | Mobile |
| `WHSMobileDevMenuItem` | Mobile device menu items | Mobile |
| `WHSLocationProfile` | Location profiles | Locations |
| `WHSReplenishmentTemplate` | Replenishment templates | Replenishment |
| `WHSCycleCountPlan` | Cycle count plans | Counting |
| `WHSClusterProfile` | Cluster profiles | Picking |
| `WHSContainerType` | Container types | Containers |
| `WHSAllWaves` | All waves | Waves |
| `WHSWork` | All work | Work |
| `WHSShipments` | All shipments | Shipping |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Warehouse must be WMS-enabled** — set "Use warehouse management processes" = Yes
2. **Storage dimension group** must include Location and License plate dimensions (active)
3. **Reservation hierarchies** must be assigned to released products for WMS warehouses
4. **Location types** must exist before location profiles
5. **Location formats** and **location profiles** must exist before generating warehouse locations
6. **Work classes** must exist before work templates reference them
7. **Work templates** must be configured per work order type before work can be created
8. **Location directives** must be set per work order type/work type for pick and put
9. **Wave templates** must be configured before order release creates waves
10. **Mobile device menu items** must exist before menus reference them
11. **Mobile device user accounts** must be mapped to worker records

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No work template found" | Missing work template for order type | Create work template for the work order type |
| "Location directive failed" | No directive matching the criteria | Add/adjust location directive with wider criteria |
| "Wave processing error" | Wave template misconfigured | Review wave process methods and sequence |
| "No available location" | All locations full or profile mismatch | Check location capacity and profile settings |
| "Reservation hierarchy mismatch" | Product hierarchy doesn't match warehouse | Re-assign reservation hierarchy to product |
| "Mobile device user not found" | Worker not mapped to user account | Create mobile device user mapping |
| "License plate not found" | LP hasn't been generated or received | Generate LP or check inbound receipt |
| "Work cannot be completed" | Location locked or inventory mismatch | Review location status and on-hand |
