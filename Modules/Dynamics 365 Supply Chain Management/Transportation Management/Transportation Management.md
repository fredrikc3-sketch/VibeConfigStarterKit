# Transportation Management Module - Knowledge Source

> This file is the central knowledge hub for the **Transportation Management** module within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Transportation Management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/transportation-management-overview)

## Module Overview

The Transportation Management module in Dynamics 365 Supply Chain Management manages outbound and inbound transportation logistics. It supports carrier management, rate shopping, route planning, load building, freight reconciliation, and integration with warehouse management for shipping operations.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Carrier Management** | Set up shipping carriers, services, and rating profiles |
| **Rate & Route Engine** | Calculate freight rates and optimize routes for cost efficiency |
| **Load Building** | Consolidate shipments into loads for efficient transportation |
| **Freight Reconciliation** | Match carrier invoices against calculated freight charges |
| **Appointment Scheduling** | Schedule dock appointments for inbound and outbound loads |
| **Transportation Modes** | Support multiple transport modes (truck, rail, ocean, air, parcel) |
| **Bill of Lading** | Generate bills of lading and other shipping documents |
| **In-Transit Planning** | Track shipments and manage in-transit visibility |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 405 - Transportation Management (`405 - Transportation management.json`)

Transportation management configuration entities. This is one of the largest DMF templates with approximately 93 entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Transportation modes | TransportationModeEntity | TMS - Setup | 30 |
| 10 | Transportation methods | TransportationMethodEntity | TMS - Setup | 30 |
| 10 | Shipping carriers | ShippingCarrierEntity | TMS - Carriers | 30 |
| 10 | Shipping carrier services | ShippingCarrierServiceEntity | TMS - Carriers | 30 |
| 10 | Shipping carrier groups | ShippingCarrierGroupEntity | TMS - Carriers | 30 |
| 10 | Hub types | TMSHubTypeEntity | TMS - Hubs | 30 |
| 10 | Hubs | TMSHubEntity | TMS - Hubs | 30 |
| 10 | Freight bill types | FreightBillTypeEntity | TMS - Billing | 30 |
| 10 | Load templates | LoadTemplateEntity | TMS - Load | 30 |
| 10 | Accessorial charge groups | AccessorialChargeGroupEntity | TMS - Charges | 30 |
| 10 | Rate master headers | RateMasterHeaderEntity | TMS - Rating | 30 |
| 20 | Rate engines | RateEngineEntity | TMS - Rating | 40 |
| 20 | Rate bases | RateBaseEntity | TMS - Rating | 40 |
| 20 | Rate breaks | RateBreakEntity | TMS - Rating | 40 |
| 20 | Route plans | RoutePlanEntity | TMS - Routes | 40 |
| 20 | Route segments | RouteSegmentEntity | TMS - Routes | 40 |
| 20 | Carrier service assignments | CarrierServiceAssignmentEntity | TMS - Carriers | 40 |
| 20 | Accessorial charges | AccessorialChargeEntity | TMS - Charges | 40 |
| 20 | Freight bill matching | FreightBillMatchingEntity | TMS - Billing | 40 |
| 20 | Rating metadata | RatingMetadataEntity | TMS - Rating | 40 |
| 30 | Transportation management parameters | TMSParametersEntity | TMS - Parameters | 50 |

**DMF Load Order Notes:**
- **Seq 10** contains foundational setup — transportation modes/methods, carriers/services/groups, hub types/hubs, freight bill types, load templates, accessorial charge groups, rate master headers
- **Seq 20** contains dependent entities — rate engines/bases/breaks (need rate masters), route plans/segments (need hubs), carrier service assignments, accessorial charges, freight bill matching
- **Seq 30** contains module parameters
- Transportation modes must exist before carriers reference them
- Carrier definitions must exist before services and service assignments
- Hub types must exist before hubs; hubs must exist before route segments
- Rate master headers must exist before rate bases and rate breaks

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (modes, methods, carriers, hubs, templates, rate masters)
- **Level 40:** Dependent entities (rate engines/bases/breaks, routes, carrier assignments, charges)
- **Level 50:** Module parameters (loaded last)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Transportation Management** module.

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
| Transportation modes | `TransportationModeEntity` | `TransportationModes` | verified |
| Transportation methods | `TransportationMethodEntity` | `TransportationMethods` | manual-unverified |
| Shipping carriers | `ShippingCarrierEntity` | `ShippingCarriers` | verified |
| Shipping carrier services | `ShippingCarrierServiceEntity` | `ShippingCarrierServices` | verified |
| Shipping carrier groups | `ShippingCarrierGroupEntity` | `ShippingCarrierGroups` | manual-unverified |
| Freight bill types | `FreightBillTypeEntity` | `FreightBillTypes` | manual-unverified |
| Load templates | `LoadTemplateEntity` | `LoadTemplates` | verified |
| Route plans | `RoutePlanEntity` | `TransportationRoutePlans` | verified |
| Transportation management parameters | `TMSParametersEntity` | `TransportationParameters` | manual-unverified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Hub types | `TMSHubTypeEntity` |
| Hubs | `TMSHubEntity` |
| Accessorial charge groups | `AccessorialChargeGroupEntity` |
| Rate master headers | `RateMasterHeaderEntity` |
| Rate engines | `RateEngineEntity` |
| Rate bases | `RateBaseEntity` |
| Rate breaks | `RateBreakEntity` |
| Route segments | `RouteSegmentEntity` |
| Carrier service assignments | `CarrierServiceAssignmentEntity` |
| Accessorial charges | `AccessorialChargeEntity` |
| Freight bill matching | `FreightBillMatchingEntity` |
| Rating metadata | `RatingMetadataEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Transportation Management:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Transportation Management-related business process areas:
- **Inventory to Deliver** (load planning, carrier selection, shipment execution)
- **Freight management** (rate shopping, freight reconciliation, freight billing)
- **Route planning** (route optimization, multi-stop planning)
- **Inbound/outbound transportation** (vendor shipments, customer shipments)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and use transportation management in Dynamics 365 Supply Chain Management** | https://learn.microsoft.com/en-us/training/paths/configure-use-transportation-management-dyn365-supply-chain-mgmt/ |
| Configure transportation management | https://learn.microsoft.com/en-us/training/modules/configure-transportation-management-dyn365-supply-chain-mgmt/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Transportation management overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/transportation-management-overview |
| Shipping carriers | https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/set-up-shipping-carriers |
| Transportation modes and methods | https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/transportation-management-modes-methods |
| Rate engines | https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/create-new-transportation-management-engine |
| Load building | https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/load-building-workbench |
| Route planning | https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/plan-freight-transportation-routes-multiple-stops |
| Freight reconciliation | https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/reconcile-freight-transportation-management |
| Accessorial charges | https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/set-up-accessorial-charges |
| Appointment scheduling | https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/appointment-scheduling |
| Hubs and hub consolidation | https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/set-up-hub-accessorial-charges |
| Small parcel shipping | https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/small-parcel-shipping |
| Transportation management engines | https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/transportation-management-engines |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites (Organization & Inventory)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Sites & warehouses | Inventory management > Setup > Inventory breakdown | Ship-from/ship-to locations |
| Customers | Accounts receivable > Customers > All customers | Delivery addresses |
| Vendors | Accounts payable > Vendors > All vendors | Carrier vendor accounts |
| Units of measure | Organization administration > Setup > Units | Weight, volume, distance |
| Main accounts | General ledger > Chart of accounts | Freight cost accounts |

### Phase 2: Transportation Foundation

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| TransportationMode | Transportation management > Setup > Carriers > Transportation mode | Modes (truck, rail, air, ocean) |
| TransportationMethod | Transportation management > Setup > Carriers > Transportation methods | Methods within modes |
| TMSHubType | Transportation management > Setup > General > Hub type | Hub classifications |
| TMSHub | Transportation management > Setup > General > Hubs | Physical hub/terminal locations |
| LoadTemplate | Transportation management > Setup > Load building > Load templates | Default load configurations |

### Phase 3: Carrier Configuration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| ShippingCarrier | Transportation management > Setup > Carriers > Shipping carriers | Carrier master records |
| ShippingCarrierService | (Within carrier) | Services offered by carrier |
| ShippingCarrierGroup | Transportation management > Setup > Carriers > Carrier groups | Carrier groupings |
| CarrierServiceAssignment | (Within carrier) | Service to carrier mapping |
| FreightBillType | Transportation management > Setup > Freight reconciliation > Freight bill types | Invoice classification |

### Phase 4: Rating & Routing

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| RateMasterHeader | Transportation management > Setup > Rating > Rate master | Rate master definitions |
| RateEngine | Transportation management > Setup > Engines > Rate engine | Rate calculation engines |
| RateBase | Transportation management > Setup > Rating > Rate base | Base rate definitions |
| RateBreak | (Within rate base) | Rate tier break points |
| RoutePlan | Transportation management > Setup > Routes > Route plan | Multi-stop route definitions |
| RouteSegment | (Within route plan) | Individual route legs |
| AccessorialChargeGroup | Transportation management > Setup > Accessorial charges > Accessorial charge groups | Charge group definitions |
| AccessorialCharge | Transportation management > Setup > Accessorial charges > Accessorial charges | Fuel surcharges, handling fees |

### Phase 5: Parameters & Integration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| TMSParameters | Transportation management > Setup > Transportation management parameters | Module parameters |
| FreightBillMatching | (Within freight reconciliation) | Auto-matching rules |
| RatingMetadata | Transportation management > Setup > Rating > Rating metadata | Rating configuration |

---

## Transportation Management Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                TRANSPORTATION MANAGEMENT PROCESS FLOW                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. LOAD PLANNING                                                        │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Create loads from sales orders / transfer orders       │          │
│     │ • Load building workbench (consolidate shipments)        │          │
│     │ • Apply load templates (weight/volume constraints)       │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  2. RATE SHOPPING & CARRIER SELECTION                                    │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Rate shopping across multiple carriers                 │          │
│     │ • Rate engine calculates freight cost per carrier         │          │
│     │ • Apply route guides for automated selection             │          │
│     │ • Select best carrier/service combination                │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  3. ROUTE PLANNING                                                       │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Define route segments (origin → hub → destination)     │          │
│     │ • Multi-stop planning                                    │          │
│     │ • Hub consolidation                                      │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  4. SHIPMENT EXECUTION                                                   │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Confirm shipment with carrier                          │          │
│     │ • Generate BOL / shipping documents                      │          │
│     │ • Appointment scheduling at docks                        │          │
│     │ • Track shipment in transit                              │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  5. FREIGHT RECONCILIATION                                               │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Receive freight bill from carrier                      │          │
│     │ • Auto-match to shipment (freight bill matching)         │          │
│     │ • Reconcile differences                                  │          │
│     │ • Approve and post freight cost                          │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `TMSLoadPlanning` | Load planning workbench | Planning |
| `TMSRateShopping` | Rate shopping | Rating |
| `TMSShipConfirm` | Shipment confirmation | Execution |
| `TMSFreightBillReconciliation` | Freight reconciliation | Billing |
| `TMSShippingCarrier` | Shipping carriers | Setup |
| `TMSRateMaster` | Rate master | Rating |
| `TMSRoutePlan` | Route plan | Routes |
| `TMSHubs` | Hubs | Setup |
| `TMSParameters` | Transportation management parameters | Setup |
| `TMSLoadBuildingWorkbench` | Load building workbench | Planning |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Transportation modes** must exist before carriers can reference them
2. **Carriers** must be created as vendor records in AP and then configured in TMS
3. **Hub types** must exist before hubs
4. **Hubs** must exist before route segments reference them
5. **Rate master headers** must exist before rate bases and breaks
6. **Rate engines** must be configured before rate shopping works
7. **Load templates** should be defined for load building to apply constraints
8. **Freight bill types** must be set up before freight reconciliation
9. **Route guides** automate carrier selection — configure after all carrier/rate setup

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No rate found" | Rate engine cannot calculate for origin/destination | Add rate base/breaks for the zone |
| "Carrier not available" | Carrier service not active or not configured | Activate carrier service |
| "Load exceeds template limits" | Weight/volume over template maximum | Adjust load template or split load |
| "Freight bill mismatch" | Carrier invoice doesn't match shipment | Review freight bill matching rules |
| "Hub not found on route" | Route segment references missing hub | Create hub definition |
| "Transportation mode required" | Mode not assigned to carrier | Assign transportation mode |
