# Omnichannel Fulfillment Module - Knowledge Source

> This file is the central knowledge hub for **Omnichannel Fulfillment** within Dynamics 365 Commerce.

---


---


> **Microsoft Learn Reference:** [Omnichannel Fulfillment](https://learn.microsoft.com/en-us/dynamics365/commerce/dom)

## Module Overview

Omnichannel Fulfillment in Dynamics 365 Commerce enables unified order fulfillment across channels including buy-online-pickup-in-store (BOPIS), ship-from-store, curbside pickup, and distributed order management. It leverages intelligent order routing to fulfill from the optimal location based on inventory, proximity, and cost.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Distributed Order Management** | Optimize order fulfillment routing across channels and warehouses |
| **Buy Online Pickup In Store** | Enable BOPIS and curbside pickup scenarios |
| **Ship from Store** | Fulfill online orders from retail store inventory |
| **Order Fulfillment Workspace** | Provide store associates a streamlined fulfillment experience |
| **Real-time Inventory** | Share inventory availability across all fulfillment locations |
| **Split Shipments** | Automatically split orders across fulfillment locations |
| **Returns Processing** | Handle cross-channel returns and exchanges |
| **Fulfillment Rules** | Define fulfillment priorities, cost optimization, and service levels |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Fulfillment configuration is managed through Commerce headquarters and store setup.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Omnichannel Fulfillment-related business process areas:
- **Distributed order management (DOM)** (intelligent order routing)
- **Order fulfillment** (ship-from-store, BOPIS, curbside pickup)
- **Inventory visibility** (real-time cross-channel inventory)
- **Returns management** (cross-channel returns)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Work with order fulfillment in Dynamics 365 Commerce** | https://learn.microsoft.com/en-us/training/modules/work-order-fulfillment-dyn365-commerce/ |
| Configure omnichannel in Commerce | https://learn.microsoft.com/en-us/training/paths/configure-work-omnichannel-prequisites-commerce/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Distributed order management (DOM) | https://learn.microsoft.com/en-us/dynamics365/commerce/dom |
| Order fulfillment in store | https://learn.microsoft.com/en-us/dynamics365/commerce/order-fulfillment-overview |
| Buy online, pick up in store (BOPIS) | https://learn.microsoft.com/en-us/dynamics365/commerce/cpe-bopis |
| Customer orders overview | https://learn.microsoft.com/en-us/dynamics365/commerce/customer-orders-overview |
| Ship-from-store | https://learn.microsoft.com/en-us/dynamics365/commerce/ship-from-store |
| Inventory lookup in POS | https://learn.microsoft.com/en-us/dynamics365/commerce/pos-inventory-lookup-operation |
| Returns and exchanges | https://learn.microsoft.com/en-us/dynamics365/commerce/pos-returns |
| Inventory availability calculation | https://learn.microsoft.com/en-us/dynamics365/commerce/calculated-inventory-retail-channels |
| Order notification emails | https://learn.microsoft.com/en-us/dynamics365/commerce/set-up-order-notification |
| Fulfillment groups | https://learn.microsoft.com/en-us/dynamics365/commerce/order-fulfillment-overview#fulfillment-groups |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Commerce channels (stores, online) | Retail and Commerce > Channels | Active channels for fulfillment |
| Warehouses per store | (Within store definition) | Inventory fulfillment location |
| Modes of delivery | Commerce > Setup > Modes of delivery | Shipping, BOPIS, curbside |
| Delivery charges | Commerce > Setup > Charges > Auto charges | Shipping cost calculation |

### Phase 2: Fulfillment Configuration

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Fulfillment groups | Retail and Commerce > Distributed order management > Fulfillment groups | Group stores for fulfillment |
| DOM profiles | Retail and Commerce > Distributed order management > DOM profiles | Fulfillment optimization rules |
| DOM rules | (Within DOM profile) | Cost, distance, priority rules |
| Fulfillment plans | Retail and Commerce > Distributed order management > Fulfillment plans | Fulfillment plan definitions |

### Phase 3: Channel Fulfillment Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Store fulfillment | (Within store) > Fulfillment settings | Enable ship-from-store |
| BOPIS settings | (Within store) > Pickup settings | Buy online pick up in store |
| POS operations | Retail and Commerce > Channel setup > POS > Button grids | Add fulfillment operations to POS |
| Inventory visibility | (Within channel) > Inventory settings | Cross-channel inventory view |

### Phase 4: Returns & Post-Sales

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Return policies | Retail and Commerce > Returns > Return policies | Cross-channel return rules |
| Return reason codes | Retail and Commerce > Returns > Return reason codes | Reason classification |
| Exchanges/refunds | (Within POS or call center) | Exchange or refund workflow |

---

## Omnichannel Fulfillment Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   OMNICHANNEL FULFILLMENT FLOW                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ORDER SOURCES                                                           │
│  ┌──────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐                   │
│  │ POS   │  │ E-Commerce│  │Call Center│  │ Mobile   │                   │
│  └───┬───┘  └─────┬─────┘  └─────┬─────┘  └─────┬────┘                   │
│      │            │              │              │                         │
│      └────────────┴──────────────┴──────────────┘                        │
│                              │                                           │
│                              ▼                                           │
│  DISTRIBUTED ORDER MANAGEMENT (DOM)                                      │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Evaluate fulfillment rules (cost, distance, priority)  │             │
│  │ • Check inventory across all locations                    │             │
│  │ • Route order to optimal fulfillment location             │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│              ┌───────────────┼───────────────┐                           │
│              ▼               ▼               ▼                           │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                    │
│  │ SHIP FROM     │ │ SHIP FROM     │ │ PICK UP       │                    │
│  │ WAREHOUSE     │ │ STORE         │ │ IN STORE      │                    │
│  │               │ │               │ │ (BOPIS)       │                    │
│  │ • WMS pick    │ │ • Store pick  │ │ • Store pick  │                    │
│  │ • Pack & ship │ │ • Pack & ship │ │ • Customer    │                    │
│  │               │ │               │ │   pickup      │                    │
│  └──────────────┘ └──────────────┘ └──────────────┘                    │
│                                                                          │
│  POST-SALE                                                               │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Cross-channel returns (buy online, return in store)     │             │
│  │ • Exchanges and refunds                                   │             │
│  │ • Order tracking and notifications                        │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `DOMAuto` | Distributed order management | Fulfillment |
| `DOMProfile` | DOM profiles | Setup |
| `DOMFulfillmentGroup` | Fulfillment groups | Setup |
| `RetailStoreOrderFulfillment` | Store order fulfillment | Operations |
| `RetailAllCustomerOrders` | Customer orders | Orders |
| `RetailReturns` | Returns | Post-Sale |
| `RetailInventoryAvailability` | Inventory availability | Inventory |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Channels and warehouses** must be fully configured before fulfillment setup
2. **Modes of delivery** must include BOPIS and ship options
3. **Fulfillment groups** must be defined before DOM profiles
4. **DOM profiles and rules** must be activated before automatic routing works
5. **POS button grids** must include fulfillment operations for store associates
6. **Distribution schedule** must be run after configuration changes
7. **Inventory visibility** must be enabled for cross-channel inventory checks

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No fulfillment location found" | DOM rules too restrictive or no inventory | Relax rules or check stock |
| "BOPIS not available" | Store not enabled for pickup | Enable pickup in store settings |
| "Ship-from-store failed" | Store fulfillment not configured | Enable fulfillment for the store |
| "Inventory not visible" | Distribution schedule not run | Run distribution schedule |
| "Return rejected" | Return policy not configured for channel | Configure cross-channel return policy |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Omnichannel Fulfillment** module.

### Order to cash

*73 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze sales performance | 1 | — |
| Develop sales policies | 15 | — |
| Manage accounts receivable | 20 | — |
| Manage credit and collections | 2 | — |
| Manage sales orders | 35 | — |

### Inventory to deliver

*1 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Manage warehouse operations | 1 | — |

