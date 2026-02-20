# Retail & Commerce Module - Knowledge Source

> This file is the central knowledge hub for the **Dynamics 365 Commerce / Retail** module (Multi-Channel Setup, Retail, E-Commerce, DTC).

---


---


> **Microsoft Learn Reference:** [Multi-Channel Setup (Retail & E-Commerce)](https://learn.microsoft.com/en-us/dynamics365/commerce/welcome)

## Module Overview

Dynamics 365 Commerce provides a unified multi-channel retail platform encompassing e-commerce, in-store (POS), and call center channels. The retail module manages product assortments, pricing, promotions, catalogs, loyalty programs, and the Commerce Scale Unit (CSU) that connects channels to the back office.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Channel Management** | Set up and manage online stores, retail stores, and call center channels |
| **Product Assortments** | Define which products are available in which channels |
| **Pricing & Promotions** | Configure price groups, discounts, and promotional campaigns |
| **Commerce Scale Unit** | Deploy CSU for resilient omnichannel operations |
| **E-Commerce Site Builder** | Build and manage online storefronts with page templates and modules |
| **Catalogs** | Create product catalogs for B2B and B2C commerce scenarios |
| **Loyalty Programs** | Design loyalty programs with earning and redemption rules |
| **Distributed Order Management** | Optimize order fulfillment across channels and locations |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 500 - Retail (`500 - Retail.json`)

Retail and Commerce configuration entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Bar code mask characters | RetailBarcodeMaskCharacterEntity | Retail - Setup | 30 |
| 10 | Bar code mask segments | RetailBarcodeMaskSegmentEntity | Retail - Setup | 30 |
| 10 | Bar code masks | RetailBarcodeMaskEntity | Retail - Setup | 30 |
| 10 | Bar code setup | RetailBarcodeSetupEntity | Retail - Setup | 30 |
| 10 | Cancellation charges | RetailCancellationChargeEntity | Retail - Setup | 30 |
| 10 | Card types | RetailCardTypeEntity | Retail - Payment | 30 |
| 10 | Catalog | EcoResCatalogEntity | Retail - Assortment | 30 |
| 10 | Category hierarchy | EcoResCategoryHierarchyEntity | Retail - Assortment | 30 |
| 10 | Customer attribute groups | CustAttrGroupEntity | Retail - Customer | 30 |
| 10 | Delivery charges groups | DlvChargeDeliveryGroupEntity | Retail - Fulfillment | 30 |
| 10 | Delivery modes | DlvDeliveryModeEntity | Retail - Fulfillment | 30 |
| 10 | Hardware profiles | RetailHardwareProfileEntity | Retail - POS | 30 |
| 10 | Info code groups | RetailInfoCodeGroupEntity | Retail - Info Codes | 30 |
| 10 | Info codes | RetailInfoCodeEntity | Retail - Info Codes | 30 |
| 10 | Info sub codes | RetailSubInfoCodeEntity | Retail - Info Codes | 30 |
| 10 | Loyalty programs | RetailLoyaltyProgramEntity | Retail - Loyalty | 30 |
| 10 | Loyalty reward points | RetailLoyaltyRewardPointEntity | Retail - Loyalty | 30 |
| 10 | Loyalty schemes | RetailLoyaltySchemeEntity | Retail - Loyalty | 30 |
| 10 | Loyalty tiers | RetailLoyaltyTierEntity | Retail - Loyalty | 30 |
| 10 | POS button grid buttons | RetailButtonGridButtonsEntity | Retail - POS | 30 |
| 10 | POS button grids | RetailButtonGridEntity | Retail - POS | 30 |
| 10 | POS functionality profiles | RetailFunctionalityProfileEntity | Retail - POS | 30 |
| 10 | POS permissions | RetailPOSPermissionGroupEntity | Retail - POS | 30 |
| 10 | POS receipt profiles lines | RetailReceiptProfileLineEntity | Retail - POS | 30 |
| 10 | POS receipt profiles | RetailReceiptProfileEntity | Retail - POS | 30 |
| 10 | POS screen layout zones | RetailScreenLayoutZoneEntity | Retail - POS | 30 |
| 10 | POS screen layouts | RetailScreenLayoutEntity | Retail - POS | 30 |
| 10 | POS visual profiles | RetailVisualProfileEntity | Retail - POS | 30 |
| 10 | Payment methods | RetailStorePaymentMethodEntity | Retail - Payment | 30 |
| 10 | Payment connector configuration | RetailPaymentConnectorConfigEntity | Retail - Payment | 30 |
| 10 | Periodic discounts | RetailPeriodicDiscountEntity | Retail - Pricing | 30 |
| 10 | Price groups | PriceGroupEntity | Retail - Pricing | 30 |
| 10 | Product filters | RetailProductFilterEntity | Retail - Assortment | 30 |
| 10 | Reason codes | RetailInfoCodeEntity | Retail - Setup | 30 |
| 10 | Retail channels | RetailChannelEntity | Retail - Channels | 30 |
| 10 | Retail devices | RetailDeviceEntity | Retail - POS | 30 |
| 10 | Retail registers | RetailTerminalEntity | Retail - POS | 30 |
| 10 | Sales tax override groups | RetailSalesTaxOverrideGroupEntity | Retail - Tax | 30 |
| 10 | Sales tax overrides | RetailSalesTaxOverrideEntity | Retail - Tax | 30 |
| 10 | Store address book | RetailStoreAddressBookEntity | Retail - Channels | 30 |
| 10 | Store locator groups | RetailStoreLocatorGroupEntity | Retail - Channels | 30 |
| 10 | Store sections | RetailStoreSectionEntity | Retail - Channels | 30 |
| 10 | Store shelves | RetailStoreShelfEntity | Retail - Channels | 30 |
| 20 | Assortments | RetailAssortmentEntity | Retail - Assortment | 40 |
| 20 | Catalog products | EcoResCatalogProductEntity | Retail - Assortment | 40 |
| 20 | Channel categories | RetailChannelCategoryEntity | Retail - Assortment | 40 |
| 20 | Channel navigation hierarchy | RetailChannelNavigationHierarchyEntity | Retail - Assortment | 40 |
| 20 | Loyalty reward point translations | RetailLoyaltyRewardPointTranslationEntity | Retail - Loyalty | 40 |
| 20 | Loyalty scheme channels | RetailLoyaltySchemeChannelEntity | Retail - Loyalty | 40 |
| 20 | Loyalty scheme products | RetailLoyaltySchemeProductEntity | Retail - Loyalty | 40 |
| 20 | Loyalty tier rules | RetailLoyaltyTierRuleEntity | Retail - Loyalty | 40 |
| 20 | POS register financial dimensions | RetailTerminalFinancialDimensionEntity | Retail - POS | 40 |
| 20 | Retail channel payment methods | RetailChannelPaymentMethodEntity | Retail - Payment | 40 |

**DMF Load Order Notes:**
- **Seq 10** contains all foundational retail setup — channels, POS profiles, payment methods, loyalty structures, info codes, pricing, assortments
- **Seq 20** contains dependent entities — assortment assignments, catalog products, loyalty scheme details, channel payment methods
- POS profiles (hardware, functionality, visual, receipt) must be loaded before registers and devices
- Channels must exist before channel-specific payment methods and assortments are assigned


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Multi-Channel Setup (Retail & E-Commerce)** module.

### Order to cash

*73 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze sales performance | 1 | — |
| Develop sales policies | 15 | — |
| Manage accounts receivable | 20 | — |
| Manage credit and collections | 2 | — |
| Manage sales orders | 35 | — |

### Design to retire

*37 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze product performance | 1 | — |
| Develop product strategy | 14 | — |
| Introduce products | 14 | — |
| Manage active products | 6 | — |
| Retire products | 2 | — |

### Concept to market

*13 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze marketing operations | 2 | — |
| Manage marketing campaigns | 10 | — |
| Prepare marketing campaigns | 1 | — |

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Bar code mask characters | `RetailBarcodeMaskCharacterEntity` | `RetailBarcodeMaskCharacters` | auto-exact |
| Bar code mask segments | `RetailBarcodeMaskSegmentEntity` | `RetailBarcodeMaskSegments` | auto-exact |
| Bar code masks | `RetailBarcodeMaskEntity` | `RetailBarcodeMasks` | auto-exact |
| Category hierarchy | `EcoResCategoryHierarchyEntity` | `ProductCategoryHierarchies` | verified |
| Delivery modes | `DlvDeliveryModeEntity` | `DeliveryModesV2` | verified |
| Hardware profiles | `RetailHardwareProfileEntity` | `RetailHardwareProfiles` | verified |
| Info code groups | `RetailInfoCodeGroupEntity` | `RetailInfocodeGroups` | auto-exact |
| Info codes | `RetailInfoCodeEntity` | `InfocodesV2` | manual-unverified |
| Loyalty reward points | `RetailLoyaltyRewardPointEntity` | `RetailLoyaltyRewardPoints` | auto-exact |
| Loyalty schemes | `RetailLoyaltySchemeEntity` | `RetailLoyaltySchemes` | auto-exact |
| Loyalty tiers | `RetailLoyaltyTierEntity` | `RetailLoyaltyTiers` | auto-exact |
| POS button grid buttons | `RetailButtonGridButtonsEntity` | `RetailButtonGridButtons` | auto-exact |
| POS button grids | `RetailButtonGridEntity` | `RetailButtonGrids` | auto-exact |
| POS functionality profiles | `RetailFunctionalityProfileEntity` | `RetailFunctionalityProfiles` | verified |
| POS permissions | `RetailPOSPermissionGroupEntity` | `RetailPosPermissionGroups` | auto-exact |
| Reason codes | `RetailInfoCodeEntity` | `InfocodesV2` | manual-unverified |
| Retail devices | `RetailDeviceEntity` | `RetailDevices` | auto-exact |
| Retail registers | `RetailTerminalEntity` | `RetailTerminals` | verified |
| Sales tax override groups | `RetailSalesTaxOverrideGroupEntity` | `RetailSalesTaxOverrideGroups` | auto-exact |
| Sales tax overrides | `RetailSalesTaxOverrideEntity` | `RetailSalesTaxOverrides` | auto-exact |
| Store address book | `RetailStoreAddressBookEntity` | `RetailStoreAddressBooks` | auto-exact |
| Store locator groups | `RetailStoreLocatorGroupEntity` | `RetailStoreLocatorGroups` | auto-exact |
| Store sections | `RetailStoreSectionEntity` | `RetailStoreSections` | auto-exact |
| Assortments | `RetailAssortmentEntity` | `RetailAssortments` | auto-exact |
| Loyalty reward point translations | `RetailLoyaltyRewardPointTranslationEntity` | `RetailLoyaltyRewardPointTranslations` | auto-exact |
| Loyalty scheme channels | `RetailLoyaltySchemeChannelEntity` | `RetailLoyaltySchemeChannels` | auto-exact |
| Loyalty scheme products | `RetailLoyaltySchemeProductEntity` | `RetailLoyaltySchemes` | verified |
| Loyalty tier rules | `RetailLoyaltyTierRuleEntity` | `RetailLoyaltyTierRules` | auto-exact |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Bar code setup | `RetailBarcodeSetupEntity` |
| Cancellation charges | `RetailCancellationChargeEntity` |
| Card types | `RetailCardTypeEntity` |
| Catalog | `EcoResCatalogEntity` |
| Customer attribute groups | `CustAttrGroupEntity` |
| Delivery charges groups | `DlvChargeDeliveryGroupEntity` |
| Info sub codes | `RetailSubInfoCodeEntity` |
| Loyalty programs | `RetailLoyaltyProgramEntity` |
| POS receipt profiles lines | `RetailReceiptProfileLineEntity` |
| POS receipt profiles | `RetailReceiptProfileEntity` |
| POS screen layout zones | `RetailScreenLayoutZoneEntity` |
| POS screen layouts | `RetailScreenLayoutEntity` |
| POS visual profiles | `RetailVisualProfileEntity` |
| Payment methods | `RetailStorePaymentMethodEntity` |
| Payment connector configuration | `RetailPaymentConnectorConfigEntity` |
| Periodic discounts | `RetailPeriodicDiscountEntity` |
| Price groups | `PriceGroupEntity` |
| Product filters | `RetailProductFilterEntity` |
| Retail channels | `RetailChannelEntity` |
| Store shelves | `RetailStoreShelfEntity` |
| Catalog products | `EcoResCatalogProductEntity` |
| Channel categories | `RetailChannelCategoryEntity` |
| Channel navigation hierarchy | `RetailChannelNavigationHierarchyEntity` |
| POS register financial dimensions | `RetailTerminalFinancialDimensionEntity` |
| Retail channel payment methods | `RetailChannelPaymentMethodEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Retail operations:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Retail-related business process areas:
- **Order to Cash** (retail sales, POS transactions, e-commerce orders)
- **Manage store operations** (POS setup, registers, shifts, cash management)
- **Manage loyalty programs** (loyalty schemes, tiers, rewards)
- **Manage assortments and catalogs** (product assortment, navigation hierarchies)
- **Manage pricing and discounts** (price groups, periodic discounts, promotions)
- **Manage fulfillment** (ship from store, pickup, delivery modes)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Get started with Dynamics 365 Commerce** | https://learn.microsoft.com/en-us/training/paths/get-started-commerce/ |
| Configure and work with omnichannel prerequisites in Dynamics 365 Commerce | https://learn.microsoft.com/en-us/training/paths/configure-work-omnichannel-prequisites-commerce/ |
| Configure point of sale | https://learn.microsoft.com/en-us/training/modules/configure-point-sale/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Commerce home page | https://learn.microsoft.com/en-us/dynamics365/commerce/welcome |
| Set up a retail channel | https://learn.microsoft.com/en-us/dynamics365/commerce/channel-setup-retail |
| Channel prerequisites | https://learn.microsoft.com/en-us/dynamics365/commerce/channels-prerequisites |
| Set up retail products | https://learn.microsoft.com/en-us/dynamics365/commerce/set-up-retail-products |
| POS screen layouts | https://learn.microsoft.com/en-us/dynamics365/commerce/pos-screen-layouts |
| Hardware station configuration | https://learn.microsoft.com/en-us/dynamics365/commerce/dev-itpro/retail-hardware-station-configuration-installation |
| Peripherals overview | https://learn.microsoft.com/en-us/dynamics365/commerce/retail-peripherals-overview |
| Set up loyalty programs | https://learn.microsoft.com/en-us/dynamics365/commerce/set-up-customer-loyalty-program |
| Info codes and info code groups | https://learn.microsoft.com/en-us/dynamics365/commerce/info-codes-retail |
| Pricing management | https://learn.microsoft.com/en-us/dynamics365/commerce/price-management |
| Discount types | https://learn.microsoft.com/en-us/dynamics365/commerce/retail-discounts-overview |
| Assortment management | https://learn.microsoft.com/en-us/dynamics365/commerce/assortments |
| Commerce catalogs | https://learn.microsoft.com/en-us/dynamics365/commerce/retail-catalogs |
| Payment methods | https://learn.microsoft.com/en-us/dynamics365/commerce/payment-methods |
| Commerce Data Exchange | https://learn.microsoft.com/en-us/dynamics365/commerce/dev-itpro/cdx-overview |

---

## 6-Phase Configuration Sequence

### Phase 1: Prerequisites (Organization & Products)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Legal entities | Organization administration > Organizations > Legal entities | Legal entity for retail operations |
| Warehouses | Inventory management > Setup > Inventory breakdown > Warehouses | Store warehouses |
| Product categories | Product information management > Products > Category hierarchies | Product categorization |
| Released products | Product information management > Products > Released products | Products available for sale |
| Currencies | General ledger > Currencies > Currencies | Transaction currencies |
| Sales tax groups | Tax > Indirect taxes > Sales tax > Sales tax groups | Tax calculation |

### Phase 2: Retail Channel Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| RetailChannel | Retail and Commerce > Channels > Stores > All stores | Store channel definition |
| RetailStoreAddressBook | (Within channel setup) | Customer address book assignment |
| RetailStoreSection | (Within channel setup) | Store floor sections |
| RetailStoreShelf | (Within channel setup) | Shelf/fixture layout |
| DlvDeliveryMode | Retail and Commerce > Channel setup > Delivery modes | Delivery methods |

### Phase 3: POS Configuration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| RetailFunctionalityProfile | Retail and Commerce > Channel setup > POS setup > POS profiles > Functionality profiles | POS feature configuration |
| RetailVisualProfile | Retail and Commerce > Channel setup > POS setup > POS profiles > Visual profiles | POS theme and appearance |
| RetailHardwareProfile | Retail and Commerce > Channel setup > POS setup > POS profiles > Hardware profiles | Peripheral device mapping |
| RetailReceiptProfile | Retail and Commerce > Channel setup > POS setup > POS profiles > Receipt profiles | Receipt formatting |
| RetailScreenLayout | Retail and Commerce > Channel setup > POS setup > POS > Screen layouts | POS screen design |
| RetailButtonGrid | Retail and Commerce > Channel setup > POS setup > POS > Button grids | Button layout |
| RetailTerminal | Retail and Commerce > Channel setup > POS setup > Registers | Register definition |
| RetailDevice | Retail and Commerce > Channel setup > POS setup > Devices | Device activation |

### Phase 4: Payment & Tax Configuration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| RetailCardType | Retail and Commerce > Channel setup > Payment methods > Card types | Card type definitions |
| RetailStorePaymentMethod | Retail and Commerce > Channel setup > Payment methods | Store payment methods |
| RetailChannelPaymentMethod | (Within channel setup) | Payment method per channel |
| RetailPaymentConnectorConfig | Retail and Commerce > Channel setup > Payment connectors | Payment gateway setup |
| RetailSalesTaxOverride | Retail and Commerce > Channel setup > Sales taxes > Tax overrides | Tax override rules |

### Phase 5: Pricing, Discounts & Loyalty

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| PriceGroup | Retail and Commerce > Pricing and discounts > Price groups | Price group definitions |
| RetailPeriodicDiscount | Retail and Commerce > Pricing and discounts > All discounts | Discount configuration |
| RetailLoyaltyProgram | Retail and Commerce > Customers > Loyalty > Loyalty programs | Loyalty program setup |
| RetailLoyaltyScheme | Retail and Commerce > Customers > Loyalty > Loyalty schemes | Earning/redemption rules |
| RetailLoyaltyTier | (Within loyalty program) | Tier definitions |
| RetailLoyaltyRewardPoint | Retail and Commerce > Customers > Loyalty > Loyalty reward points | Reward point types |

### Phase 6: Assortments, Catalogs & Info Codes

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| RetailAssortment | Retail and Commerce > Catalogs and assortments > Assortments | Product assortment to channel |
| EcoResCatalog | Retail and Commerce > Catalogs and assortments > Catalogs | Product catalog management |
| RetailChannelNavigationHierarchy | Retail and Commerce > Products and categories > Channel navigation hierarchies | Category navigation |
| RetailInfoCode | Retail and Commerce > Channel setup > Info codes | Info code prompts |
| RetailBarcodeMask | Retail and Commerce > Inventory management > Bar codes and labels > Bar code mask setup | Barcode formatting |

---

## Retail Channel Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     RETAIL CHANNEL ARCHITECTURE                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  HEADQUARTER (D365 Finance & Operations)                                 │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Channel management & configuration                     │             │
│  │ • Product & assortment management                        │             │
│  │ • Pricing & discount management                          │             │
│  │ • Loyalty program management                             │             │
│  │ • Distribution schedules (CDX)                           │             │
│  └────────────────────────────────────────────────────────┘             │
│              │                                                           │
│              ▼                                                           │
│  COMMERCE SCALE UNIT (CSU)                                               │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Real-time service (RTS) for HQ operations              │             │
│  │ • Channel database                                       │             │
│  │ • Commerce runtime (CRT)                                 │             │
│  │ • Headless commerce APIs                                 │             │
│  └────────────────────────────────────────────────────────┘             │
│              │                                                           │
│     ┌────────┼─────────────┐                                            │
│     ▼        ▼             ▼                                            │
│  STORE POS  E-COMMERCE   CALL CENTER                                    │
│  (MPOS/CPOS) (Storefront)  (HQ Client)                                 │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Distribution Schedule Jobs

| Job Number | Name | Purpose |
|------------|------|---------|
| 1010 | Staff | Workers, POS permissions |
| 1020 | Bar codes | Barcode masks and setups |
| 1040 | Products | Product and pricing data |
| 1050 | Loyalty | Loyalty programs, schemes, tiers |
| 1060 | Discounts | Periodic discounts and price adjustments |
| 1070 | Channel configuration | Channel, register, device, profiles |
| 1080 | Tax | Tax configuration and overrides |
| 1090 | Registers | Register and terminal data |
| 1100 | Payments | Payment methods and connectors |
| 1110 | Global | Global configuration |
| 1150 | Catalogs | Catalog and assortment data |
| 9999 | Full sync | Complete data synchronization |

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `RetailAllStores` | All stores | Channels |
| `RetailOnlineStores` | Online stores | Channels |
| `RetailCallCenterChannels` | Call centers | Channels |
| `RetailFunctionalityProfiles` | Functionality profiles | POS Profiles |
| `RetailVisualProfiles` | Visual profiles | POS Profiles |
| `RetailHardwareProfiles` | Hardware profiles | POS Profiles |
| `RetailReceiptProfiles` | Receipt profiles | POS Profiles |
| `RetailScreenLayouts` | Screen layouts | POS Setup |
| `RetailTerminals` | Registers | POS Setup |
| `RetailDevices` | Devices | POS Setup |
| `RetailLoyaltyPrograms` | Loyalty programs | Loyalty |
| `RetailLoyaltySchemes` | Loyalty schemes | Loyalty |
| `RetailPeriodicDiscounts` | All discounts | Pricing |
| `RetailPriceGroups` | Price groups | Pricing |
| `RetailAssortments` | Assortments | Products |
| `RetailCatalogs` | Catalogs | Products |
| `RetailInfoCodes` | Info codes | Setup |
| `RetailDistributionSchedule` | Distribution schedule | IT |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Legal entity and warehouse** must exist before creating a retail channel
2. **Products** must be released to legal entity before they can be added to assortments
3. **POS profiles** (functionality, visual, hardware, receipt) must be configured before registers
4. **Registers** must exist before devices can be activated
5. **Payment methods** must be configured at both HQ level and channel level
6. **Price groups** must be assigned to channels before pricing takes effect
7. **Assortments** must be published and distribution jobs run before products appear in POS
8. **Distribution schedule** jobs must be run after any configuration change to sync data to CSU

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Product not available in channel" | Assortment not published or CDX not run | Publish assortment, run 1040 + 1150 jobs |
| "Payment method not configured" | Channel-level payment method missing | Add payment method to channel setup |
| "Register not found" | Register not synced to channel database | Run 1090 distribution job |
| "Device activation failed" | Device not mapped to register | Map device to register, run 1070 |
| "Price not found" | Price group not assigned to channel | Assign price group to channel, run 1040 |
| "Tax calculation error" | Sales tax group missing on channel | Set sales tax group on channel record |
| "CDX sync failed" | Channel database connection issue | Check CSU deployment and connectivity |
