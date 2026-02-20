# Point of Sale (Modern & Cloud POS) Module - Knowledge Source

> This file is the central knowledge hub for **Point of Sale (Modern & Cloud POS)** within Dynamics 365 Commerce.

---


---


> **Microsoft Learn Reference:** [Point of Sale (Modern & Cloud POS)](https://learn.microsoft.com/en-us/dynamics365/commerce/dev-itpro/retail-store-system-begin)

## Module Overview

Dynamics 365 Commerce Point of Sale (POS) is the in-store application used by retail associates for sales transactions, customer interactions, and store operations. It is available as Modern POS (Windows/Android) with offline capability and Cloud POS (browser-based). Store Commerce is the latest evolution, replacing MPOS.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Sales Transactions** | Process sales, returns, exchanges, and layaway transactions |
| **Customer Lookup** | Search, create, and manage customer records at the register |
| **Payment Processing** | Accept multiple payment methods including cards, cash, and gift cards |
| **Offline Operations** | Continue selling when connectivity is interrupted (Modern POS / Store Commerce) |
| **Inventory Lookup** | Check real-time inventory availability across locations |
| **Order Management** | Create, fulfill, and manage customer orders from the POS |
| **Task Management** | Manage daily store tasks and checklists |
| **Peripheral Support** | Integrate with receipt printers, barcode scanners, payment terminals, and cash drawers |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** POS configuration is managed through Commerce headquarters, POS functionality profiles, and hardware profiles.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key POS-related business process areas:
- **Store operations** (cash register, shift management, end-of-day)
- **Transaction processing** (sales, returns, exchanges, voids)
- **Payment processing** (cash, card, gift card, loyalty points)
- **Peripheral management** (receipt printers, barcode scanners, payment terminals)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and use Point of Sale in Dynamics 365 Commerce** | https://learn.microsoft.com/en-us/training/paths/configure-use-pos-commerce/ |
| Set up a POS| https://learn.microsoft.com/en-us/training/modules/set-up-pos-dyn365-commerce/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Modern POS overview | https://learn.microsoft.com/en-us/dynamics365/commerce/dev-itpro/retail-modern-pos-architecture |
| Cloud POS vs. Modern POS | https://learn.microsoft.com/en-us/dynamics365/commerce/mpos-or-cpos |
| POS application and device setup | https://learn.microsoft.com/en-us/dynamics365/commerce/pos-application-user-language-settings |
| Hardware station setup | https://learn.microsoft.com/en-us/dynamics365/commerce/retail-hardware-station-configuration-installation |
| POS screen layouts | https://learn.microsoft.com/en-us/dynamics365/commerce/pos-screen-layouts |
| POS button grids | https://learn.microsoft.com/en-us/dynamics365/commerce/pos-screen-layouts#button-grids |
| POS operations | https://learn.microsoft.com/en-us/dynamics365/commerce/pos-operations |
| POS permissions and functionality profiles | https://learn.microsoft.com/en-us/dynamics365/commerce/pos-permissions |
| Shift and cash drawer management | https://learn.microsoft.com/en-us/dynamics365/commerce/shift-drawer-management |
| Receipt templates | https://learn.microsoft.com/en-us/dynamics365/commerce/receipt-templates-printing |
| Offline POS functionality | https://learn.microsoft.com/en-us/dynamics365/commerce/pos-offline-functionality |
| POS hybrid app | https://learn.microsoft.com/en-us/dynamics365/commerce/dev-itpro/hybridapp |

---

## Modern POS vs. Cloud POS

| Feature | Modern POS (MPOS) | Cloud POS (CPOS) |
|---------|-------------------|-------------------|
| **Deployment** | Installed on device/PC | Browser-based |
| **Offline support** | Yes (local database) | No (requires connectivity) |
| **Hardware access** | Direct peripheral access | Via shared hardware station |
| **OS support** | Windows, Android, iOS | Any browser |
| **Best for** | Dedicated registers | Shared/popup terminals |
| **Store Commerce** | Successor to MPOS | Still available |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Retail store channel | Retail and Commerce > Channels > Stores | Store definition |
| Workers / staff | Human resources > Workers | POS operators |
| Address books | Organization administration > Global address book | Worker-store mapping |
| Number sequences | Organization administration > Number sequences | Transaction, receipt numbers |

### Phase 2: POS Profiles

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Functionality profiles | Retail and Commerce > Channel setup > POS setup > POS profiles > Functionality profiles | Feature toggles, behaviors |
| Visual profiles | Retail and Commerce > Channel setup > POS setup > POS profiles > Visual profiles | Theme, layout, images |
| Hardware profiles | Retail and Commerce > Channel setup > POS setup > POS profiles > Hardware profiles | Peripheral device mapping |
| Offline profiles | Retail and Commerce > Channel setup > POS setup > POS profiles > Offline profiles | Offline database settings |

### Phase 3: Register & Device Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Registers | Retail and Commerce > Channel setup > POS setup > Registers | Define POS register records |
| Devices | Retail and Commerce > Channel setup > POS setup > Devices | Physical device registration |
| Hardware stations | (Within store or register) | Shared/dedicated hardware stations |
| Screen layouts | Retail and Commerce > Channel setup > POS setup > POS > Screen layouts | POS UI layout design |
| Button grids | (Within screen layout) | Transaction screen buttons |

### Phase 4: Operations & Receipts

| Task | Menu Path | Purpose |
|------|-----------|---------|
| POS permissions | Retail and Commerce > Channel setup > POS setup > POS > Permission groups | Operation-level security |
| Receipt profiles | Retail and Commerce > Channel setup > POS setup > POS profiles > Receipt profiles | Receipt format assignment |
| Receipt templates | Retail and Commerce > Channel setup > POS setup > POS > Receipt formats | Receipt content design |
| Email receipts | (Within receipt profile) | Digital receipt configuration |

### Phase 5: Activation & Distribution

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Distribution schedule | Retail and Commerce > IT > Distribution schedule | Sync configuration to POS |
| Device activation | (On POS device) | Activate POS with server URL + device ID |
| POS deployment | (Store Commerce app / CPOS URL) | Install or navigate to POS |

---

## POS Transaction Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      POS TRANSACTION FLOW                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. SHIFT MANAGEMENT                                                     │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Open shift (declare starting amount)                   │          │
│     │ • Cash drawer assignment                                 │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  2. SALE TRANSACTION                                                     │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Scan / search items                                    │          │
│     │ • Apply discounts / promotions                           │          │
│     │ • Add customer (loyalty, customer order)                 │          │
│     │ • Quantity, price override (with permission)             │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  3. PAYMENT                                                              │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Cash / Card / Gift card / Loyalty points               │          │
│     │ • Split payment (multiple tenders)                       │          │
│     │ • Change calculation                                     │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  4. RECEIPT & COMPLETION                                                 │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Print / email receipt                                  │          │
│     │ • Transaction completed                                  │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  5. END OF DAY                                                           │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Tender declaration (count cash)                        │          │
│     │ • Close shift                                            │          │
│     │ • Bank drop / safe drop                                  │          │
│     │ • Statement posting (in headquarters)                    │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `RetailPOSRegisters` | Registers | POS Setup |
| `RetailPOSDevices` | Devices | POS Setup |
| `RetailFunctionalityProfile` | Functionality profiles | Profiles |
| `RetailVisualProfile` | Visual profiles | Profiles |
| `RetailHardwareProfile` | Hardware profiles | Profiles |
| `RetailScreenLayouts` | Screen layouts | UI |
| `RetailButtonGrids` | Button grids | UI |
| `RetailReceiptProfiles` | Receipt profiles | Receipts |
| `RetailPOSPermissionGroups` | Permission groups | Security |
| `RetailHardwareStation` | Hardware stations | Peripherals |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Store channel** must be created and configured before registers
2. **Functionality profiles** must be assigned to stores before POS activation
3. **Hardware profiles** must be configured before peripheral devices work
4. **Screen layouts** and **button grids** must be designed before POS is usable
5. **Workers** must be linked to stores for POS sign-in
6. **Distribution schedule** must be run to push all configuration to POS
7. **Device activation** requires server URL, device ID, and register mapping
8. **Offline profiles** must be configured for MPOS offline capability

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Device activation failed" | Wrong device ID or server URL | Verify activation parameters |
| "Cannot open shift" | Previous shift not closed | Close pending shift |
| "Peripheral not responding" | Hardware station not connected | Check hardware station status |
| "Payment terminal error" | Payment connector misconfigured | Verify payment connector settings |
| "Offline database sync failed" | Offline profile not configured | Configure offline profile |
| "Operation not permitted" | Missing POS permission | Update permission group |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Point of Sale (Modern & Cloud POS)** module.

### Order to cash

*73 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze sales performance | 1 | — |
| Develop sales policies | 15 | — |
| Manage accounts receivable | 20 | — |
| Manage credit and collections | 2 | — |
| Manage sales orders | 35 | — |

