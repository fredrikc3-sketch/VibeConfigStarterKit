# Call Center Operations Module - Knowledge Source

> This file is the central knowledge hub for **Call Center Operations** within Dynamics 365 Commerce.

---


---


> **Microsoft Learn Reference:** [Call Center Operations](https://learn.microsoft.com/en-us/dynamics365/commerce/call-center-functionality)

## Module Overview

The Call Center channel in Dynamics 365 Commerce enables phone-based order taking with advanced features including directed selling, catalog management, customer service scripts, price overrides, continuity programs, and gift card management. Call center agents can access a 360-degree customer view for personalized service.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Phone Order Entry** | Process sales orders, returns, and exchanges via phone |
| **Directed Selling** | Prompt agents with up-sell, cross-sell, and script recommendations |
| **Catalog Management** | Associate orders with marketing catalogs for source tracking |
| **Price Overrides** | Allow authorized agents to override prices with approval workflows |
| **Payment Processing** | Handle payments including split payments, gift cards, and credit |
| **Continuity Programs** | Manage subscription/continuity order programs |
| **Order Holds** | Place and manage fraud holds and payment holds on orders |
| **Customer 360 View** | Access complete customer history, preferences, and loyalty information |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Call center configuration is managed through Commerce setup forms.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Call Center-related business process areas:
- **Order management** (phone order entry, order holds, order completion)
- **Customer service** (customer lookup, order status, returns/exchanges)
- **Catalog management** (call center catalogs, source codes)
- **Payment processing** (credit card, continuity programs)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Work with call center in Dynamics 365 Commerce** | https://learn.microsoft.com/en-us/training/modules/work-call-center-dyn365-commerce/ |
| Configure Dynamics 365 Commerce | https://learn.microsoft.com/en-us/training/paths/configure-work-omnichannel-prequisites-commerce/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Call center overview | https://learn.microsoft.com/en-us/dynamics365/commerce/call-center-functionality |
| Set up a call center channel | https://learn.microsoft.com/en-us/dynamics365/commerce/set-up-order-processing-options |
| Call center catalogs | https://learn.microsoft.com/en-us/dynamics365/commerce/call-center-catalogs |
| Call center order holds | https://learn.microsoft.com/en-us/dynamics365/commerce/work-with-order-holds |
| Call center payments | https://learn.microsoft.com/en-us/dynamics365/commerce/call-center-payment-methods |
| Continuity programs | https://learn.microsoft.com/en-us/dynamics365/commerce/set-up-continuity-program |
| Call center fraud rules | https://learn.microsoft.com/en-us/dynamics365/commerce/set-up-fraud-alerts |
| Direct delivery from call center | https://learn.microsoft.com/en-us/dynamics365/commerce/call-center-direct-delivery |
| Source code tracking | https://learn.microsoft.com/en-us/dynamics365/commerce/call-center-catalogs#source-codes |
| Upsell and cross-sell | https://learn.microsoft.com/en-us/dynamics365/commerce/call-center-functionality#upsell-cross-sell |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Commerce headquarters setup | Commerce > Headquarters setup | Base Commerce configuration |
| Customers | Accounts receivable > Customers | Customer master data |
| Products / released products | Product information management > Products | Sellable catalog items |
| Payment methods | Commerce > Payment setup > Payment methods | Credit card, check, etc. |
| Number sequences | Organization administration > Number sequences | Order numbers |

### Phase 2: Call Center Channel Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Create call center channel | Retail and Commerce > Channels > Call centers > All call centers | Channel definition |
| Assign users to channel | (Within call center) > Channel users | Map workers to call center |
| Configure order processing | (Within call center) > Order defaults | Default order settings |
| Set up payment methods | (Within call center) > Payment methods | Channel payment configuration |
| Configure fulfillment | (Within call center) > Fulfillment | Order fulfillment rules |

### Phase 3: Catalog & Order Configuration

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Create call center catalogs | Retail and Commerce > Catalogs and assortments > Catalogs | Product catalogs with source codes |
| Configure source codes | (Within catalog) > Source codes | Track marketing campaigns |
| Set up order holds | Retail and Commerce > Customers > Order holds | Hold rules and reasons |
| Configure fraud detection | (Within call center) > Fraud | Fraud alert rules |
| Set up continuity programs | Retail and Commerce > Continuity > Continuity schedules | Recurring order programs |

### Phase 4: Advanced Features

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Up-sell / cross-sell scripts | (Within call center) > Scripts | Customer interaction scripts |
| Configure order completion | (Within call center) > Order completion | Required fields for order completion |
| Set up direct delivery | (Within call center) > Order defaults | Drop ship configuration |
| Distribution schedule | Retail and Commerce > IT > Distribution schedule | Sync data to channels |

---

## Call Center Order Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CALL CENTER ORDER FLOW                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. CUSTOMER CONTACT                                                     │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Identify / create customer                             │          │
│     │ • View order history                                     │          │
│     │ • Apply source code (catalog/campaign tracking)          │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  2. ORDER ENTRY                                                          │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Add items from catalog                                 │          │
│     │ • Apply promotions / discounts                           │          │
│     │ • Up-sell / cross-sell prompts                           │          │
│     │ • Capture payment (credit card, gift card, etc.)         │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  3. ORDER COMPLETION                                                     │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Fraud check (automatic rules)                          │          │
│     │ • Order hold check (credit, payment, manual)             │          │
│     │ • Complete order → Submit                                │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  4. FULFILLMENT                                                          │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Pick / pack / ship from warehouse                     │          │
│     │ • Direct delivery from vendor (drop ship)                │          │
│     │ • Invoice and payment capture                            │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `MCRCallCenter` | Call centers | Channels |
| `MCRSalesOrder` | Call center sales order | Orders |
| `MCRCatalog` | Catalogs | Catalogs |
| `MCROrderHolds` | Order holds | Orders |
| `MCRFraudAlerts` | Fraud alerts | Security |
| `MCRContinuity` | Continuity schedules | Programs |
| `MCRSourceCodes` | Source codes | Tracking |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Call center channel** must be created before users can be assigned
2. **Users** must be assigned to the call center channel to create call center orders
3. **Payment methods** must be configured at the channel level
4. **Catalogs** must be published before source codes are active
5. **Fraud rules** should be configured before go-live to prevent fraudulent orders
6. **Distribution schedule** must be run after configuration changes

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "User not assigned to call center" | Worker not linked to channel | Add user to call center channel users |
| "Order on hold" | Fraud or credit hold triggered | Review and release hold |
| "Payment declined" | Credit card authorization failed | Retry or use alternative payment |
| "Catalog not available" | Catalog not published | Publish the catalog |
| "Source code invalid" | Expired or inactive source code | Verify source code date range |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Call Center Operations** module.

### Order to cash

*73 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze sales performance | 1 | — |
| Develop sales policies | 15 | — |
| Manage accounts receivable | 20 | — |
| Manage credit and collections | 2 | — |
| Manage sales orders | 35 | — |

