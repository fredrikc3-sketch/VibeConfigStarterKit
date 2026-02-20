# Fixed Assets Management Module - Knowledge Source

> This file is the central knowledge hub for the **Fixed Assets Management** module within Dynamics 365 Finance.

---


---


> **Microsoft Learn Reference:** [Fixed Assets Management](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/fixed-assets)

## Module Overview

The Fixed Assets module in Dynamics 365 Finance manages the complete lifecycle of capital assets from acquisition through disposal. It supports multiple depreciation methods, value models, depreciation books, asset transfers between locations and dimensions, and integration with Accounts Payable for asset acquisition via purchase orders.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Asset Acquisition** | Acquire assets through purchase orders, free text invoices, or manual journals |
| **Depreciation** | Calculate depreciation using straight-line, declining balance, or custom methods |
| **Value Models & Depreciation Books** | Track asset values under multiple accounting standards simultaneously |
| **Asset Transfers** | Transfer assets between financial dimensions, locations, or legal entities |
| **Asset Disposal** | Process asset retirement through sale or scrap with gain/loss calculations |
| **Asset Leasing** | Manage right-of-use assets and lease liabilities under ASC 842/IFRS 16 |
| **Asset Maintenance** | Track maintenance costs and history against fixed assets |
| **Barcode Tracking** | Use barcodes for physical asset identification and counting |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 150 - Fixed Assets (`150 - Fixed assets.json`)

Fixed asset configuration and master data entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Fixed asset acquisition method | AssetAcquisitionMethodEntity | FA - Attributes | 30 |
| 10 | Fixed asset activity codes | AssetActivityCodeEntity | FA - Attributes | 30 |
| 10 | Fixed asset condition | AssetConditionEntity | FA - Attributes | 30 |
| 10 | Fixed asset locations | AssetLocationEntity | FA - Attributes | 30 |
| 10 | Fixed asset major type | AssetMajorTypeEntity | FA - Attributes | 30 |
| 10 | Fixed asset properties | AssetSortingEntity | FA - Attributes | 30 |
| 10 | Fixed asset property groups | AssetPropertyGroupEntity | FA - Attributes | 30 |
| 10 | Fixed asset provision types | AssetProvisionTypeEntity | FA - Attributes | 30 |
| 10 | Fixed asset consumption factors | AssetConsumptionFactorEntity | | 30 |
| 10 | Fixed asset consumption units | AssetConsumptionUnitEntity | | 30 |
| 10 | Fixed asset special depreciation allowance setup | AssetSpecialDepreciationAllowanceEntity | | 30 |
| 10 | Fixed asset depreciation profiles | AssetDepreciationProfileEntity | FA - Setup | 40 |
| 10 | Fixed asset inventory to fixed asset transfer journal names | AssetInventoryFixedAssetTransferJournalNameEntity | FA - Setup | 30 |
| 10 | Fixed asset groups | AssetGroupEntity | FA - Setup | 40 |
| 10 | Fixed asset posting profile disposal | AssetPostingProfileDisposalEntity | FA - Setup | 60 |
| 10 | Fixed asset book setup | AssetValueModelSetupEntity | | 50 |
| 10 | Fixed asset group/book special depreciation allowance | AssetGroupBookSpecialDepreciationAllowanceEntity | | 60 |
| 10 | Fixed assets | AssetFixedAssetEntity | | 150 |
| 15 | Fixed asset depreciation profile manual schedules | AssetDepreciationProfileManualScheduleEntity | FA - Setup | 40 |
| 20 | Fixed asset posting profile | AssetPostingProfileEntity | FA - Setup | 50 |
| 20 | Fixed asset book setup derived book | AssetValueModelSetupDerivedValueModelEntity | | 50 |
| 20 | Fixed asset group book setup | AssetGroupValueModelSetupEntity | | 50 |
| 30 | Fixed asset parameters | AssetParametersEntity | FA - Setup | 150 |
| 40 | Fixed asset proposal journal names | AssetParametersProposalJournalNamesEntity | | 150 |

**DMF Load Order Notes:**
- **Seq 10** contains all foundational attribute tables and setup data — load these first
- **Seq 15** contains manual depreciation schedules which depend on depreciation profiles (Seq 10)
- **Seq 20** contains posting profiles and derived book/group book setup — depends on books and groups from Seq 10
- **Seq 30** contains FA parameters — loaded after all structural setup is in place
- **Seq 40** contains proposal journal name references — loaded last as it references both parameters and journal names

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Lookup/attribute entities (loaded first within a sequence)
- **Level 40:** Setup entities (groups, depreciation profiles)
- **Level 50:** Book setup & posting profiles
- **Level 60:** Disposal profiles, special depreciation group/book assignments
- **Level 150:** Master records (fixed assets) and parameters (loaded last)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Fixed Assets Management** module.

### Acquire to dispose

*106 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Acquire assets | 26 | — |
| Analyze assets | 14 | — |
| Define asset strategy | 15 | — |
| Dispose of assets | 11 | — |
| Manage active assets | 38 | — |
| Perform asset maintenance | 2 | — |

### Record to report

*236 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze financial performance | 26 | — |
| Close financial periods | 41 | — |
| Define accounting policies | 82 | — |
| Manage budgets | 25 | — |
| Manage cash | 26 | — |
| Record financial transactions | 36 | — |

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Fixed asset activity codes | `AssetActivityCodeEntity` | `AssetActivityCodes` | auto-exact |
| Fixed asset condition | `AssetConditionEntity` | `AssetConditions` | auto-exact |
| Fixed asset locations | `AssetLocationEntity` | `AssetLocations` | auto-exact |
| Fixed asset major type | `AssetMajorTypeEntity` | `AssetMajorTypes` | auto-exact |
| Fixed asset properties | `AssetSortingEntity` | `AssetSortings` | auto-exact |
| Fixed asset property groups | `AssetPropertyGroupEntity` | `AssetPropertyGroups` | auto-exact |
| Fixed asset provision types | `AssetProvisionTypeEntity` | `AssetProvisionTypes` | auto-exact |
| Fixed asset consumption units | `AssetConsumptionUnitEntity` | `AssetConsumptionUnits` | auto-exact |
| Fixed asset special depreciation allowance setup | `AssetSpecialDepreciationAllowanceEntity` | `AssetSpecialDepreciationAllowances` | auto-exact |
| Fixed asset depreciation profiles | `AssetDepreciationProfileEntity` | `DepreciationProfiles` | verified |
| Fixed asset inventory to fixed asset transfer journal names | `AssetInventoryFixedAssetTransferJournalNameEntity` | `InventoryFixedAssetTransferJournalNames` | verified |
| Fixed asset groups | `AssetGroupEntity` | `FixedAssetGroups` | verified |
| Fixed asset posting profile disposal | `AssetPostingProfileDisposalEntity` | `FixedAssetPostingProfileDisposals` | verified |
| Fixed asset book setup | `AssetValueModelSetupEntity` | `ValueModelSetups` | verified |
| Fixed asset group/book special depreciation allowance | `AssetGroupBookSpecialDepreciationAllowanceEntity` | `FixedAssetGroupBookSpecialDepreciationAllowances` | verified |
| Fixed assets | `AssetFixedAssetEntity` | `FixedAssets` | verified |
| Fixed asset depreciation profile manual schedules | `AssetDepreciationProfileManualScheduleEntity` | `DepreciationProfileManualSchedules` | verified |
| Fixed asset posting profile | `AssetPostingProfileEntity` | `FixedAssetPostingProfiles` | verified |
| Fixed asset book setup derived book | `AssetValueModelSetupDerivedValueModelEntity` | `FixedAssetValueModelSetupDerivedValueModels` | verified |
| Fixed asset group book setup | `AssetGroupValueModelSetupEntity` | `FixedAssetGroupValueModelSetups` | verified |
| Fixed asset parameters | `AssetParametersEntity` | `AssetParameters` | auto-exact |
| Fixed asset proposal journal names | `AssetParametersProposalJournalNamesEntity` | `AssetParametersProposalJournalNames` | auto-exact |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Fixed asset acquisition method | `AssetAcquisitionMethodEntity` |
| Fixed asset consumption factors | `AssetConsumptionFactorEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Fixed Assets operations under the **Acquire to Dispose** end-to-end process:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (CSV):** `../../../Business Process/ProcessCatalogue.csv`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key FA-related business process areas in the catalogue:
- **Acquire to Dispose** (end-to-end process)
- Plan fixed assets (budgeting, planning with Business Performance Planning, Microsoft Project, Planner)
- Budget fixed assets (budget register, FA budget journal, budget planning)
- Record fixed asset acquisitions (FA journals, acquisition proposals, auto-acquire from PO)
- Maintain fixed assets (create, update, additions, reclassify, write-up/write-down, impairment)
- Depreciate fixed assets (depreciation proposals, mid-quarter conversion)
- Dispose of assets (scrap via FA journal, sale via FA journal, sale via free text invoice)
- Retire/decommission fixed assets
- Analyze assets (FA register, FA values, FA books, depreciation analysis, FA statements)
- Reconcile fixed asset subledger to GL

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and manage fixed assets** | https://learn.microsoft.com/en-us/training/paths/configure-manage-fixed-assets-dyn365-finance/ |
| Set up fixed assets | https://learn.microsoft.com/en-us/training/modules/set-up-fixed-assets-dyn365-finance/ |
| Manage fixed assets | https://learn.microsoft.com/en-us/training/modules/manage-fixed-assets-dyn365-finance/ |
| Configure and manage fixed asset depreciation | https://learn.microsoft.com/en-us/training/modules/configure-manage-fixed-assets-depreciation/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Fixed assets home page | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/fixed-assets |
| Set up fixed assets | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/set-up-fixed-assets |
| Fixed asset depreciation | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/fixed-asset-depreciation |
| Depreciation methods and conventions | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/depreciation-methods-conventions |
| Fixed asset posting profiles | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/tasks/set-up-fixed-asset-posting-profiles |
| Fixed asset groups | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/tasks/set-up-fixed-asset-groups |
| Value models | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/tasks/set-up-value-models |
| Depreciation books | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/tasks/set-up-depreciation-books |
| Dispose of a fixed asset as scrap | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/dispose-of-a-fixed-asset-as-scrap |
| Fixed asset roll forward report | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/fixed-asset-roll-forward-report |
| Reclassify fixed assets | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/reclassify-fixed-assets |
| Derived books | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/derived-books |
| Bonus depreciation | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/bonus-depreciation |
| Fixed asset integration | https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/fixed-asset-integration |

---

## 7-Phase Configuration Sequence

### Phase 1: Prerequisites (GL & Organization)

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| CompanyInfo | Organization administration > Organizations > Legal entities | Legal entity must exist |
| Ledger | General ledger > Ledger setup > Ledger | Ledger and CoA must be configured |
| MainAccount | General ledger > Chart of accounts > Accounts > Main accounts | FA-related GL accounts created |
| NumberSequenceTable | Organization administration > Number sequences | FA number sequences |

**⚠️ GL accounts required before FA setup:**
- Fixed asset acquisition accounts (balance sheet)
- Accumulated depreciation accounts (contra-asset)
- Depreciation expense accounts (P&L)
- Gain/loss on disposal accounts (P&L)
- Net book value accounts (if applicable)

### Phase 2: Fixed Asset Attributes

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| AssetAcquisitionMethod | Fixed assets > Setup > Acquisition methods | How assets are acquired |
| AssetActivityCode | Fixed assets > Setup > Activity codes | Activity tracking |
| AssetCondition | Fixed assets > Setup > Condition | Asset condition classification |
| AssetLocation | Fixed assets > Setup > Fixed asset locations | Physical locations |
| AssetMajorType | Fixed assets > Setup > Major types | Major type classification |
| AssetSorting | Fixed assets > Setup > Property | Sorting/property attributes |
| AssetPropertyGroup | Fixed assets > Setup > Property groups | Property group classification |
| AssetProvisionType | Fixed assets > Setup > Provision types | Provision classification |
| AssetConsumptionUnit | Fixed assets > Setup > Consumption units | Units for consumption depreciation |
| AssetConsumptionFactor | Fixed assets > Setup > Consumption factors | Consumption-based factors |

### Phase 3: Depreciation Configuration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| AssetDepreciationProfile | Fixed assets > Setup > Depreciation profiles | Depreciation method definition |
| AssetDepreciationProfileManualSchedule | (Within depreciation profile) | Manual depreciation schedules |
| AssetSpecialDepreciationAllowance | Fixed assets > Setup > Special depreciation allowance | Bonus/special depreciation rules |

### Phase 4: Books & Groups

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| AssetBook (Value Models) | Fixed assets > Setup > Books | Book/value model definition |
| AssetGroup | Fixed assets > Setup > Fixed asset groups | Asset group classification |
| AssetGroupBookSetup | Fixed assets > Setup > Fixed asset groups > Books | Default book settings per group |
| AssetGroupBookSpecialDepreciationAllowance | (Within group/book setup) | Special depreciation per group/book |
| AssetBookDerivedBook | Fixed assets > Setup > Books > Derived books | Automatic derived postings |

### Phase 5: Posting Profiles

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| AssetLedgerAccounts (Posting Profile) | Fixed assets > Setup > Fixed asset posting profiles | GL account mapping by transaction type |
| AssetPostingProfileDisposal | (Within posting profiles) | Disposal-specific GL mapping |

### Phase 6: Parameters & Journal Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| AssetParameters | Fixed assets > Setup > Fixed assets parameters | Module-level parameters |
| AssetParametersProposalJournalNames | (Within FA parameters) | Default journals for proposals |
| LedgerJournalName | General ledger > Journal setup > Journal names | FA journal types |

### Phase 7: Fixed Asset Master Records

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| AssetTable | Fixed assets > Fixed assets > Fixed assets | Fixed asset master records |
| AssetBook (per asset) | (Within fixed asset) | Books attached to each asset |
| AssetTrans | (Via journals/postings) | Asset transaction history |

---

## Fixed Asset Books (Value Models)

### Book Types & Purpose

| Book Type | Purpose | Posts to GL? | Use Case |
|-----------|---------|--------------|----------|
| **Value model** | Primary accounting book | Yes | Financial/statutory reporting |
| **Depreciation book** | Tax or alternative depreciation | No (optional) | Tax reporting, IFRS dual books |
| **Derived book** | Auto-mirrors transactions from primary | Yes/No (configurable) | Automate tax book from accounting book |

### Book Setup Key Fields

| Field | Description | Impact |
|-------|-------------|--------|
| **Depreciation profile** | Method used for depreciation | Determines how depreciation is calculated |
| **Service life** | Expected useful life in years/months | Drives depreciation amount |
| **Depreciation convention** | When depreciation starts (Half year, Mid month, Full month) | Affects first/last year depreciation |
| **Calendar** | Fiscal calendar for depreciation | Controls period assignment |
| **Posting layer** | Current, Operations, Tax | Determines posting layer in GL |
| **Derived books** | Linked books that auto-post | Reduces manual entry |

---

## Depreciation Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| **Straight line service life** | Equal amount each period over service life | Most common method |
| **Reducing balance** | Percentage of net book value each period | Accelerated depreciation |
| **Straight line life remaining** | Equal amount over remaining life | After adjustments or impairment |
| **Reducing balance 200%** | Double declining balance | US MACRS-like accelerated |
| **Reducing balance 175%** | 1.75x declining balance | Moderate acceleration |
| **Reducing balance 150%** | 1.5x declining balance | Mild acceleration |
| **Factor** | User-defined percentage per period | Custom schedules |
| **Consumption** | Based on usage quantity | Vehicles, machinery by hours/miles |
| **Manual** | User-specified amounts per period | Irregular depreciation |
| **Round down (Japan)** | Japanese rounding rules | Japan statutory |
| **Low value pool (Australia)** | Australian low-value pool rules | Australia statutory |

### Depreciation Conventions

| Convention | First Year Behavior | Last Year Behavior |
|------------|--------------------|--------------------|
| **Full month** | Full depreciation from placed-in-service month | Full month of disposal |
| **Mid month** | Half month in placed-in-service month | Half month of disposal |
| **Half year** | Half year regardless of acquisition date | Half year in disposal year |
| **Mid quarter** | Mid-point of acquisition quarter | Mid-point of disposal quarter |
| **None** | Pro-rata from exact date | Pro-rata to exact date |

---

## Fixed Asset Groups

Fixed asset groups control default values when creating new assets and determine posting profile behavior.

### Group Category Examples

| Group ID | Description | Typical Assets | Default Book |
|----------|-------------|----------------|--------------|
| LAND | Land | Real estate - land | No depreciation |
| BUILD | Buildings | Offices, warehouses, factories | 20-40 yr SL |
| MACH | Machinery & Equipment | Production equipment, tools | 5-15 yr SL/RB |
| VEHIC | Vehicles | Company cars, trucks, forklifts | 3-7 yr SL/RB |
| FURN | Furniture & Fixtures | Desks, chairs, shelving | 5-10 yr SL |
| COMP | Computer Equipment | Servers, laptops, monitors | 3-5 yr SL |
| SOFTWARE | Intangible - Software | Licenses, ERP systems | 3-5 yr SL |
| LHOLD | Leasehold Improvements | Tenant improvements | Lease term SL |
| CONSTR | Construction in Progress | Assets under construction | No depreciation (until transfer) |

### Group/Book Setup

Each fixed asset group can have default book configurations:

| Setting | Description |
|---------|-------------|
| **Book** | Which book applies to the group |
| **Depreciation profile** | Default depreciation method |
| **Service life** | Default useful life |
| **Depreciation convention** | Default convention |
| **Depreciation run date** | Default calculation basis |
| **Special depreciation allowance** | Bonus depreciation rules |

---

## Posting Profiles

### Transaction Types & GL Account Mapping

| Transaction Type | Debit Account | Credit Account | Description |
|-----------------|---------------|----------------|-------------|
| **Acquisition** | Fixed Asset (BS) | Bank/AP/Offset | Asset capitalization |
| **Acquisition adjustment** | Fixed Asset (BS) | Offset | Cost basis change |
| **Depreciation** | Depreciation Expense (P&L) | Accumulated Depreciation (BS) | Periodic depreciation |
| **Depreciation adjustment** | Depreciation Expense (P&L) | Accumulated Depreciation (BS) | Depreciation correction |
| **Disposal - sale** | Bank/AR (BS) | Fixed Asset (BS) | Proceeds from sale |
| **Disposal - scrap** | Accum. Depreciation (BS) / Loss (P&L) | Fixed Asset (BS) | Retire with no proceeds |
| **Net book value - gain** | — | Gain on Disposal (P&L) | Proceeds > NBV |
| **Net book value - loss** | Loss on Disposal (P&L) | — | Proceeds < NBV |
| **Write-up** | Fixed Asset (BS) | Write-up Gain (P&L) | Increase asset value |
| **Write-down** | Write-down Loss (P&L) | Accumulated Depreciation (BS) | Decrease asset value |
| **Transfer** | Fixed Asset (new) | Fixed Asset (old) | Reclassify between groups |
| **Bonus depreciation** | Depreciation Expense (P&L) | Accumulated Depreciation (BS) | Special allowance |

### Posting Profile Setup Levels

| Level | Description |
|-------|-------------|
| **Table** | Specific fixed asset group |
| **Group** | Fixed asset group |
| **All** | Default for all assets |

---

## Fixed Asset Lifecycle

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        FIXED ASSET LIFECYCLE                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. PLANNING & BUDGETING                                                     │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Capital expenditure budgeting                            │
│     │ • FA budget journals / Budget register entries             │
│     │ • Budget planning integration                              │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  2. ACQUISITION                                                              │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Create fixed asset record                                │
│     │ • Acquire via FA journal (manual)                          │
│     │ • Acquire via purchase order (automatic)                   │
│     │ • Acquire via free text invoice                            │
│     │ • Acquisition proposal (batch from PO receipts)           │
│     │ • Transfer from inventory                                  │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  3. IN-SERVICE OPERATIONS                                                    │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Run depreciation proposals (periodic)                    │
│     │ • Record additions / improvements                          │
│     │ • Write-up / Write-down adjustments                        │
│     │ • Impairment recording                                      │
│     │ • Reclassification (group/location changes)               │
│     │ • Transfer between legal entities                          │
│     │ • Financial dimension adjustments                          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  4. DISPOSAL                                                                 │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Disposal - Sale (via FA journal or free text invoice)   │
│     │ • Disposal - Scrap (via FA journal)                        │
│     │ • Calculate gain/loss on disposal                          │
│     │ • Post disposal transactions                               │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  5. REPORTING & RECONCILIATION                                               │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Fixed asset roll forward report                          │
│     │ • FA subledger to GL reconciliation                        │
│     │ • NBV analysis by book                                     │
│     │ • Depreciation projection                                  │
│     │ • Audit trail and transaction inquiry                      │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Acquisition Methods

| Method | Source | Auto-Create Asset? | Description |
|--------|--------|-------------------|-------------|
| **FA Journal** | Fixed assets > Journal entries > Fixed assets journal | No | Manual acquisition entry |
| **Purchase Order** | Accounts payable > Purchase orders | Yes (if configured) | Acquire on PO receipt or invoice |
| **Free Text Invoice (credit)** | Accounts receivable > Free text invoices | No | Offset to asset account |
| **Inventory Transfer** | Fixed assets > Journal entries > Inventory to fixed assets | No | Convert inventory to FA |
| **Acquisition Proposal** | Within FA journal > Proposals > Acquisition proposal | No | Batch-acquire PO receipts |
| **Project** | Project management > Journals | Yes (if configured) | Capitalize project costs |

---

## Journal Types for Fixed Assets

| Journal Type | Journal Name Type | Use Case | Menu Item Name |
|--------------|------------------|----------|----------------|
| **Fixed assets journal** | Fixed assets | Acquisitions, disposals, adjustments | `LedgerJournalTable5` |
| **FA depreciation journal** | Fixed assets | Depreciation proposal postings | `LedgerJournalTable5` |
| **Inventory to FA transfer** | Inventory to fixed asset transfer | Convert inventory items to assets | `AssetInventJournalTable` |
| **Fixed asset budget** | Fixed assets | FA budget entries | `LedgerJournalTable5` |

### Depreciation Proposal Process

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      DEPRECIATION PROPOSAL FLOW                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. Open FA Journal (Fixed assets > Journal entries > Fixed assets)      │
│  2. Select journal name with type = Fixed assets                         │
│  3. Click Proposals > Depreciation proposal                              │
│  4. Set parameters:                                                      │
│     • To date (depreciation run date)                                    │
│     • Book (value model)                                                 │
│     • Summarize depreciation (optional)                                  │
│     • Filter by asset group/asset (optional)                             │
│  5. System calculates depreciation for all eligible assets               │
│  6. Review journal lines                                                 │
│  7. Post journal                                                         │
│                                                                          │
│  ⚠️ Run monthly as part of period close checklist                        │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Disposal Process

### Disposal - Sale

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        DISPOSAL - SALE FLOW                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Option A: Via FA Journal                                                │
│  1. Create FA journal entry                                              │
│  2. Transaction type = Disposal - sale                                   │
│  3. Enter sale price (credit)                                            │
│  4. System calculates:                                                   │
│     • Reverses acquisition cost                                          │
│     • Reverses accumulated depreciation                                  │
│     • Posts gain or loss                                                 │
│                                                                          │
│  Option B: Via Free Text Invoice                                         │
│  1. Create free text invoice for customer                                │
│  2. Line references fixed asset                                          │
│  3. On invoice posting:                                                  │
│     • Records sale proceeds to AR                                        │
│     • Triggers disposal posting                                          │
│     • Calculates and posts gain/loss                                     │
│                                                                          │
│  Option C: Via AP Invoice (Trade-in)                                     │
│  1. Vendor invoice references asset disposal                             │
│  2. Posts disposal as part of AP transaction                             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Disposal - Scrap

| Step | Action | GL Effect |
|------|--------|-----------|
| 1 | Create FA journal | — |
| 2 | Transaction type: Disposal - scrap | — |
| 3 | Post | DR: Accumulated Depreciation (full) |
| | | DR: Loss on Disposal (if NBV > 0) |
| | | CR: Fixed Asset Cost (full) |

---

## Fixed Asset Integration with Other Modules

| Module | Integration Point | Direction |
|--------|-------------------|-----------|
| **General Ledger** | Posting profiles map FA transactions → GL accounts | FA → GL |
| **Accounts Payable** | PO receipt/invoice auto-creates asset acquisition | AP → FA |
| **Accounts Receivable** | Free text invoice triggers disposal | AR → FA |
| **Inventory Management** | Inventory-to-FA transfer journal | INV → FA |
| **Project Accounting** | Capitalize project costs as fixed assets | PROJ → FA |
| **Budgeting** | FA budget entries integrate with budget register | FA ↔ Budget |
| **Asset Leasing** | Right-of-use assets create FA records (IFRS 16/ASC 842) | Lease → FA |
| **Cost Accounting** | Depreciation allocated to cost centers | FA → CA |

---

## FY27 Environment - Key Menu Items

*Based on Dynamics 365 Finance standard navigation*

### Core Setup Forms

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `AssetParameters` | Fixed assets parameters | FA Setup |
| `AssetGroup` | Fixed asset groups | FA Setup |
| `AssetDepreciationProfile` | Depreciation profiles | FA Setup |
| `AssetBookTable` | Books | FA Setup |
| `AssetPosting` | Fixed asset posting profiles | FA Setup |
| `AssetLocation` | Fixed asset locations | FA Attributes |
| `AssetCondition` | Condition | FA Attributes |
| `AssetMajorType` | Major types | FA Attributes |
| `AssetAcquisitionMethod` | Acquisition methods | FA Attributes |

### Transactions & Journals

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `LedgerJournalTable5` | Fixed assets journal | FA Journals |
| `AssetTable` | Fixed assets | FA Master |
| `AssetInventJournalTable` | Inventory to fixed assets journal | FA Transfer |
| `AssetProposalDepreciation` | Depreciation proposal | FA Periodic |

### Reports & Inquiries

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `AssetBalancesPeriod` | Fixed asset balances | FA Reports |
| `AssetStatementReport` | Fixed asset statement | FA Reports |
| `AssetTransactionListing` | Transaction listing | FA Reports |
| `AssetRollForward` | Fixed asset roll forward | FA Reports |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **General Ledger** must be fully configured (CoA, dimensions, account structures) before FA setup
2. **GL accounts** for FA transactions must exist in chart of accounts
3. **FA attribute tables** (locations, conditions, major types) should be loaded before asset groups
4. **Depreciation profiles** must be created before books
5. **Books** must be created before group/book setup
6. **Fixed asset groups** must exist before group/book setup
7. **Posting profiles** must be configured before any FA transactions
8. **FA parameters** should be configured after posting profiles and books
9. **Journal names** (type: Fixed assets) must exist before creating FA journals
10. **Fixed asset master records** are loaded last, after all setup is complete

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Posting profile not set up for transaction type" | Missing GL account in FA posting profile | Configure posting profile for the specific transaction type and group |
| "Book is not set up for the fixed asset group" | Asset group missing book assignment | Add book to fixed asset group via Group/Book setup |
| "Depreciation profile not found" | Book references non-existent depreciation profile | Create the depreciation profile first, then assign to book |
| "Fixed asset has already been acquired" | Duplicate acquisition attempt | Check asset status - may need acquisition adjustment instead |
| "Cannot dispose asset with open transactions" | Pending unposted transactions exist | Post or reverse open journal lines |
| "Service life must be greater than zero" | Missing or zero service life on book | Set service life in group/book setup or asset book |
| "Period is not open" | GL fiscal period closed/on-hold | Open the period in Ledger calendar |
| "Disposal parameters not configured" | Missing disposal posting profile entries | Configure disposal accounts in posting profiles |

---

## Derived Books

### Purpose & Configuration

Derived books automatically create mirror transactions in a secondary book when transactions are posted to the primary book. This is commonly used:

- **Tax book** derived from accounting book — different depreciation for tax purposes
- **IFRS book** derived from statutory book — dual GAAP compliance
- **Statistical book** — replacement cost tracking without GL posting

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        DERIVED BOOK FLOW                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PRIMARY BOOK (Accounting)          DERIVED BOOK (Tax)                   │
│  ┌─────────────────────┐           ┌─────────────────────┐              │
│  │ Acquisition: $10,000│ ─────────▶│ Acquisition: $10,000│              │
│  │ Depr Method: SL 5yr │           │ Depr Method: MACRS  │              │
│  │ Posts to: Current   │           │ Posts to: Tax layer  │              │
│  └─────────────────────┘           └─────────────────────┘              │
│                                                                          │
│  Transaction in primary book automatically generates                     │
│  corresponding transaction in derived book.                              │
│                                                                          │
│  Supported derived transaction types:                                    │
│  • Acquisition / Acquisition adjustment                                  │
│  • Disposal - sale / Disposal - scrap                                    │
│  • Transfer                                                              │
│                                                                          │
│  ⚠️ Depreciation is NOT derived — run separately per book               │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Special Depreciation Allowance (Bonus Depreciation)

Bonus depreciation allows an additional percentage to be depreciated in the first year (or another specified period), on top of regular depreciation.

| Setting | Description |
|---------|-------------|
| **Allowance name** | Identifier for the special depreciation rule |
| **Percentage** | Additional depreciation percentage (e.g., 30%, 50%, 100%) |
| **Priority** | Order of application when multiple allowances exist |
| **Before/after regular depreciation** | Whether bonus applies before or after standard calc |

**US Example (Section 179 / Bonus):**
- 100% bonus depreciation for qualifying assets
- Applied in year of acquisition
- Reduces depreciable basis for subsequent years

---

## Asset Reclassification

Reclassification allows transferring an asset between fixed asset groups without physical disposal.

| Step | Action |
|------|--------|
| 1 | Navigate to: Fixed assets > Periodic tasks > Reclassification |
| 2 | Select source asset |
| 3 | Select target fixed asset group |
| 4 | Optionally assign new asset number |
| 5 | System transfers cost and accumulated depreciation |
| 6 | Posting profile changes based on new group |

---

## Data Migration Sequence

```
1. GL Prerequisites (Legal Entity, CoA, Accounts, Dimensions)
2. FA Attributes (Locations, Conditions, Major Types, Properties)
3. FA Depreciation Profiles
4. FA Special Depreciation Allowance Setup
5. FA Consumption Units & Factors
6. FA Books (Value Models)
7. FA Groups
8. FA Group/Book Setup
9. FA Book Derived Books
10. FA Group/Book Special Depreciation Allowance
11. FA Posting Profiles (Acquisition, Depreciation, Disposal)
12. FA Posting Profile Disposal
13. FA Parameters
14. FA Proposal Journal Names
15. FA Journal Names (in GL journal setup)
16. FA Master Records (Fixed Assets)
17. FA Asset Book Assignments (if not defaulted from group)
18. Opening Balances (Acquisition + Accumulated Depreciation journals)
```

---

## Opening Balance Migration

### Strategy for Go-Live

When migrating fixed assets from a legacy system, opening balances require careful handling:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    OPENING BALANCE MIGRATION FLOW                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Step 1: Import FA Master Records                                        │
│     • Asset number, description, group, book assignments                 │
│     • Service life, placed-in-service date                               │
│                                                                          │
│  Step 2: Post Acquisition Journal                                        │
│     • Transaction type: Acquisition                                      │
│     • Amount: Original acquisition cost                                  │
│     • Date: Original acquisition date OR migration cutover date          │
│                                                                          │
│  Step 3: Post Accumulated Depreciation                                   │
│     • Transaction type: Depreciation adjustment                          │
│     • Amount: Total accumulated depreciation from legacy                 │
│     • Date: Day before go-live OR last day of prior period               │
│                                                                          │
│  Step 4: Verify                                                          │
│     • NBV in D365 = NBV in legacy system                                 │
│     • Run FA roll forward report                                         │
│     • Reconcile FA subledger to GL trial balance                         │
│                                                                          │
│  ⚠️ Ensure depreciation convention matches legacy to avoid               │
│     future depreciation discrepancies                                    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Related Modules

| Module | Relationship |
|--------|--------------|
| **General Ledger** | FA transactions post to GL via posting profiles |
| **Accounts Payable** | Asset purchases via purchase orders |
| **Accounts Receivable** | Asset disposals via free text invoices |
| **Inventory Management** | Inventory-to-FA transfer for capitalization |
| **Project Accounting** | Capitalize project costs as fixed assets |
| **Budgeting** | FA budget journals and budget register integration |
| **Asset Leasing** | ROU assets from lease contracts (IFRS 16 / ASC 842) |
| **Tax** | Different depreciation for tax books vs. accounting |

---

## References

- [Fixed assets home page](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/fixed-assets)
- [Set up fixed assets](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/set-up-fixed-assets)
- [Fixed asset depreciation](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/fixed-asset-depreciation)
- [Depreciation methods and conventions](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/depreciation-methods-conventions)
- [Derived books](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/derived-books)
- [Bonus depreciation](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/bonus-depreciation)
- [Fixed asset integration](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/fixed-asset-integration)
- [Dispose of a fixed asset as scrap](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/dispose-of-a-fixed-asset-as-scrap)
- [Reclassify fixed assets](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/reclassify-fixed-assets)
- [Fixed asset roll forward report](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/fixed-asset-roll-forward-report)
- [Data management overview](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-entities-data-packages)

---
