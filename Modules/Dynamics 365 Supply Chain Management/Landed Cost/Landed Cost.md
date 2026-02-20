# Landed Cost Module - Knowledge Source

> This file is the central knowledge hub for **Landed Cost** within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Landed Cost](https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/landed-cost-overview)

## Module Overview

The Landed Cost module in Dynamics 365 Supply Chain Management helps organizations accurately calculate the total cost of imported goods by tracking all costs associated with bringing products from origin to destination. It manages voyages, shipping containers, cost estimation, duty/tariff, freight, and customs for international procurement.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Voyage Management** | Create and track voyages from origin to destination with multi-leg support |
| **Cost Estimation** | Estimate total landed costs before goods arrive at the warehouse |
| **Auto-Cost Rules** | Define automatic cost rules for freight, duty, insurance, and handling |
| **Shipping Containers** | Track costs at the container or folio level for precise costing |
| **Goods in Transit** | Record goods in transit before physical receipt at the warehouse |
| **Cost Type Management** | Categorize costs as freight, duty, insurance, or customs charges |
| **Vendor Invoice Reconciliation** | Match actual vendor invoices against estimated voyage costs |
| **Multi-Currency Support** | Handle costs in multiple currencies with conversion at receipt |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Landed cost configuration uses dedicated voyage and cost management forms.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Landed Cost-related business process areas:
- **Voyages** (shipment tracking from origin to destination)
- **Cost estimation** (freight, duties, insurance, customs)
- **Goods in transit** (in-transit inventory tracking)
- **Auto costs** (automatic cost rules)
- **Cost reconciliation** (estimated vs. actual cost settlement)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Landed cost module overview** | https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/landed-cost-overview |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Landed cost overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/landed-cost-overview |
| Landed cost parameters | https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/landed-cost-parameters |
| Voyage creation | https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/manage-voyages |
| Shipping containers | https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/shipping-container-setup |
| Auto costs | https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/auto-cost-setup |
| Costing parameters | https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/costing-parameters-setup |
| Goods in transit | https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/in-transit-processing |
| Vendor invoicing | https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/landed-cost-vendor-invoicing |
| Multi-leg journeys | https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/multi-leg-journey-setup |
| Cost type codes | https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/costing-parameters-setup#cost-type-codes |
| Over/under delivery | https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/over-under-tolerances |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Landed cost parameters | Landed cost > Setup > Landed cost parameters | Module settings |
| Vendors (shipping companies, customs brokers) | Accounts payable > Vendors | Cost service providers |
| Warehouses (in-transit, destination) | Inventory management > Setup > Warehouses | In-transit and receiving warehouses |
| Purchase order setup | Procurement > Setup | Standard PO configuration |

### Phase 2: Cost Configuration

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Cost type codes | Landed cost > Costing setup > Cost type codes | Freight, duty, insurance, etc. |
| Cost area assignments | (Within cost type codes) | Voyage, container, folio, line |
| Auto costs | Landed cost > Costing setup > Auto costs | Automatic cost estimation rules |
| Costing parameters | Landed cost > Costing setup > Costing parameters | Costing method settings |

### Phase 3: Shipping Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Shipping ports | Landed cost > Delivery setup > Ports | Origin and destination ports |
| Multi-leg journey templates | Landed cost > Delivery setup > Multi-leg journey | Leg definitions (port-to-port) |
| Shipping container types | Landed cost > Delivery setup > Shipping containers > Types | 20ft, 40ft, etc. |
| Folios | (Created within voyage) | Group lines for customs/costing |
| Goods-in-transit warehouse | (Within warehouse setup) | In-transit inventory location |

### Phase 4: Voyage Execution

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Create voyage | Landed cost > Voyages > All voyages > New | Create shipment record |
| Add purchase orders to voyage | (Within voyage) > Lines | Link POs to voyage |
| Tracking control | Landed cost > Tracking > Tracking control | Update voyage progress |
| Goods in transit receiving | (At destination) > Goods in transit orders | Receive in-transit inventory |

### Phase 5: Cost Reconciliation

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Vendor invoicing | (Against voyage costs) | Match actual invoices |
| Cost reconciliation | Landed cost > Inquiries > Cost reconciliation | Estimated vs. actual comparison |
| Over/under tolerance | Landed cost > Setup > Over/under tolerance | Variance thresholds |
| Post variances | (Within cost reconciliation) | Settle cost differences |

---

## Landed Cost Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       LANDED COST FLOW                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PURCHASE ORDER                                                          │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ PO confirmed with international vendor                    │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  VOYAGE CREATED                                                          │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ Voyage                                                    │             │
│  │ ├── Shipping Container(s)                                 │             │
│  │ │    └── Folio(s)                                         │             │
│  │ │         └── Lines (from PO)                             │             │
│  │ │                                                         │             │
│  │ ├── Auto Costs Applied:                                   │             │
│  │ │    Freight........$5,000                                │             │
│  │ │    Insurance......$  500                                │             │
│  │ │    Customs duty...$2,000                                │             │
│  │ │    Handling.......$  300                                │             │
│  │ │    ─────────────────────                                │             │
│  │ │    Est. Total.....$7,800                                │             │
│  │ │                                                         │             │
│  │ └── Journey: Shanghai → (sea) → LA Port → (truck) → WH   │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  IN TRANSIT                                                              │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Goods tracked in "in-transit" warehouse                 │             │
│  │ • Inventory visible but not available for allocation      │             │
│  │ • Voyage tracking updates (ETD, ETA, delays)              │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  RECEIVE & RECONCILE                                                     │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Receive goods-in-transit → destination warehouse        │             │
│  │ • Vendor invoices for each cost type                      │             │
│  │ • Reconcile: Estimated $7,800 vs. Actual $8,200           │             │
│  │ • Post variance ($400 over) per tolerance rules           │             │
│  │ • Final landed cost per unit calculated                   │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `ITMLandedCostParameters` | Landed cost parameters | Setup |
| `ITMVoyageTable` | Voyages | Voyages |
| `ITMAutoCost` | Auto costs | Costing Setup |
| `ITMCostTypeTable` | Cost type codes | Costing Setup |
| `ITMGoodsInTransit` | Goods in transit | Processing |
| `ITMPortTable` | Ports | Delivery Setup |
| `ITMMultiLegJourney` | Multi-leg journeys | Delivery Setup |
| `ITMShippingContainer` | Shipping containers | Delivery Setup |
| `ITMCostReconciliation` | Cost reconciliation | Inquiries |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Landed cost parameters** must be configured before any voyage creation
2. **Cost type codes** must be defined before auto costs
3. **Auto cost rules** should be set up to automatically estimate costs per voyage
4. **In-transit warehouse** must be configured for goods-in-transit processing
5. **Multi-leg journey templates** simplify voyage creation for standard routes
6. **Purchase orders** must be confirmed before adding to a voyage
7. **Goods-in-transit receiving** must be completed before final cost calculation

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No auto costs applied" | Auto cost rules not matching | Check auto cost conditions |
| "In-transit order not found" | Goods not shipped or voyage not updated | Update voyage status |
| "Cost variance exceeds tolerance" | Actual costs much higher than estimated | Adjust tolerance or investigate pricing |
| "Voyage not tracking" | Tracking control not updated | Update tracking milestones |
| "Duplicate cost on voyage" | Manual cost added when auto cost exists | Remove duplicate cost entry |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Landed Cost** module.

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

