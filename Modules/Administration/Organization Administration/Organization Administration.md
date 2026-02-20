# Organization Administration Module - Knowledge Source

> This file is the central knowledge hub for the **Organization Administration** module within Dynamics 365 Finance & Operations.

---


---


> **Microsoft Learn Reference:** [Organization Administration](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/organization-administration/organization-administration-home-page)

## Module Overview

The Organization Administration module is the foundational configuration module for Dynamics 365 Finance & Operations. It manages legal entities, operating units, organization hierarchies, global address book, number sequences, currencies, units of measure, and system-wide settings. All other modules depend on the structures defined here.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Legal Entity Management** | Define and configure legal entities (companies) that form the organizational backbone |
| **Organization Hierarchies** | Create hierarchies for reporting, centralized payments, and organizational structure |
| **Global Address Book** | Manage shared address book for parties (customers, vendors, contacts) across legal entities |
| **Number Sequences** | Configure automatic number generation for documents, records, and transactions |
| **Currency & Exchange Rates** | Set up currencies, exchange rate types, and currency pair rates |
| **Units of Measure** | Define units and unit conversions used across the system |
| **Workflow Configuration** | Design and manage approval workflows for business processes |
| **Address Setup** | Configure address formats, countries/regions, states, cities, and postal codes |
| **Fiscal Calendars** | Define fiscal calendars, years, and periods used throughout the system |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template files define the data entities required for migrating and configuring this module:

#### 010 - System Setup (`010 - System Setup.json`)

Organization and system configuration entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Address format lines | LogisticsAddressFormatLineEntity | System - Address | 30 |
| 10 | Address format | LogisticsAddressFormatEntity | System - Address | 30 |
| 10 | Address parameters | LogisticsAddressParametersEntity | System - Address | 30 |
| 10 | Countries / Regions | LogisticsAddressCountryRegionEntity | System - Address | 30 |
| 10 | County | LogisticsAddressCountyEntity | System - Address | 30 |
| 10 | Cities | LogisticsAddressCityEntity | System - Address | 30 |
| 10 | Districts | LogisticsAddressDistrictEntity | System - Address | 30 |
| 10 | State / Province | LogisticsAddressStateEntity | System - Address | 30 |
| 10 | Zip / Postal codes | LogisticsAddressZipCodeEntity | System - Address | 30 |
| 10 | Currencies | CurrencyEntity | System - Currency | 30 |
| 10 | Currency exchange rate type | ExchangeRateTypeEntity | System - Currency | 30 |
| 10 | Currency pair exchange rates | ExchangeRateCurrencyPairEntity | System - Currency | 40 |
| 10 | Financial Calendar | FiscalCalendarEntity | System - Calendar | 30 |
| 10 | Financial Calendar Year | FiscalCalendarYearEntity | System - Calendar | 35 |
| 10 | Financial Calendar Period | FiscalCalendarPeriodEntity | System - Calendar | 40 |
| 10 | Global Address Book | DirPartyEntity | System - Address | 30 |
| 10 | Legal entities | LegalEntityEntity | System - Organization | 10 |
| 10 | Operating units | OMOperatingUnitEntity | System - Organization | 20 |
| 10 | Organization hierarchy - published | OMOrganizationHierarchyPublishedEntity | System - Organization | 30 |
| 10 | Organization hierarchy purposes | OMHierarchyPurposeEntity | System - Organization | 20 |
| 10 | Organization hierarchy type | OMHierarchyTypeEntity | System - Organization | 20 |
| 10 | Language | LanguageEntity | | 30 |
| 10 | Party contacts V3 | DirPartyContactEntity | System - Address | 40 |
| 10 | Party postal addresses V2 | DirPartyPostalAddressEntity | System - Address | 40 |
| 10 | System Users | SystemUserEntity | System - Security | 30 |
| 10 | User information | UserInfoEntity | System - Security | 30 |
| 15 | Security roles | SecurityRoleEntity | System - Security | 30 |
| 15 | Security user role associations | SecurityUserRoleAssociationEntity | System - Security | 40 |
| 20 | Units | UnitEntity | System - Units | 30 |
| 20 | Unit conversions | UnitConversionEntity | System - Units | 40 |
| 30 | Number sequences | NumberSequenceEntity | System - Number Sequences | 50 |

**DMF Load Order Notes:**
- **Seq 10** contains all foundational organization, address, currency, calendar, and user entities — load first
- **Seq 15** contains security role definitions and role assignments — depends on users from Seq 10
- **Seq 20** contains units of measure and conversions — independent foundational data
- **Seq 30** contains number sequences — loaded after all module structures are in place

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 10:** Legal entities (loaded first — all other entities depend on them)
- **Level 20:** Operating units, hierarchy purposes and types
- **Level 30:** Lookup/attribute entities (addresses, currencies, calendars, users)
- **Level 35-40:** Dependent entities (calendar years, periods, party addresses, role assignments, unit conversions)
- **Level 50:** Number sequences (loaded last)

---

#### 022 - Workflow (`022 - Workflow.json`)

Workflow configuration and definition entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Workflow version | WorkflowVersionEntity | Workflow | 30 |
| 10 | Workflow version notification | WorkflowVersionNoteEntity | Workflow | 30 |
| 10 | Workflow element | WorkflowElementEntity | Workflow | 30 |
| 10 | Workflow element notification | WorkflowElementNoteEntity | Workflow | 30 |
| 10 | Workflow step | WorkflowStepEntity | Workflow | 30 |
| 10 | Workflow escalation path | WorkflowEscalationPathEntity | Workflow | 30 |
| 10 | Workflow escalation step | WorkflowEscalationStepEntity | Workflow | 30 |
| 10 | Workflow parallel branch | WorkflowParallelBranchEntity | Workflow | 30 |
| 10 | Workflow sub workflow | WorkflowSubWorkflowEntity | Workflow | 30 |
| 10 | Workflow sub workflow element | WorkflowSubWorkflowElementEntity | Workflow | 30 |
| 10 | Workflow version association | WorkflowVersionAssociationEntity | Workflow | 30 |
| 10 | Workflow version association element notification | WorkflowVersionAssociationElemNoteEntity | Workflow | 30 |
| 10 | Workflow expression | WorkflowExpressionEntity | Workflow | 30 |
| 10 | Workflow time span | WorkflowTimeSpanEntity | Workflow | 30 |
| 10 | Workflow table | WorkflowTableEntity | Workflow | 30 |
| 10 | Workflow parallel activity | WorkflowParallelActivityEntity | Workflow | 30 |
| 10 | Work item queue | WorkflowWorkItemQueueEntity | Workflow | 30 |
| 10 | Work item queue group | WorkflowWorkItemQueueGroupEntity | Workflow | 30 |
| 10 | Work item queue group assignment | WorkflowWorkItemQueueGroupAssignmentEntity | Workflow | 30 |
| 10 | Workflow message text | WorkflowMessageTextEntity | Workflow | 30 |
| 10 | Workflow line item | WorkflowLineItemWorkflowEntity | Workflow | 30 |
| 10 | Workflow tracking status | WorkflowTrackingStatusEntity | Workflow | 30 |
| 10 | Workflow tracking table | WorkflowTrackingTableEntity | Workflow | 30 |

**DMF Load Order Notes:**
- All workflow entities are at **Seq 10 / Level 30** — they form a flat dependency set
- Workflow configuration should be loaded after the core system setup (010) is complete
- Workflow elements, steps, escalation paths, and parallel activities define the workflow structure
- Work item queues define assignment routing for workflow tasks
- Workflow tracking entities capture runtime status data


---

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Address format lines | `LogisticsAddressFormatLineEntity` | `AddressFormatLines` | verified |
| Address format | `LogisticsAddressFormatEntity` | `AddressFormats` | verified |
| Address parameters | `LogisticsAddressParametersEntity` | `AddressParameters` | verified |
| Countries / Regions | `LogisticsAddressCountryRegionEntity` | `AddressCountryRegions` | verified |
| County | `LogisticsAddressCountyEntity` | `AddressCounties` | verified |
| Cities | `LogisticsAddressCityEntity` | `AddressCities` | verified |
| Districts | `LogisticsAddressDistrictEntity` | `AddressDistricts` | verified |
| State / Province | `LogisticsAddressStateEntity` | `AddressStates` | verified |
| Zip / Postal codes | `LogisticsAddressZipCodeEntity` | `AddressPostalCodes` | verified |
| Currencies | `CurrencyEntity` | `Currencies` | auto-exact |
| Currency exchange rate type | `ExchangeRateTypeEntity` | `ExchangeRateTypes` | auto-exact |
| Currency pair exchange rates | `ExchangeRateCurrencyPairEntity` | `ExchangeRateCurrencyPairs` | auto-exact |
| Financial Calendar | `FiscalCalendarEntity` | `FiscalCalendars` | auto-exact |
| Financial Calendar Year | `FiscalCalendarYearEntity` | `FiscalCalendarYears` | auto-exact |
| Global Address Book | `DirPartyEntity` | `DirParties` | manual-unverified |
| Legal entities | `LegalEntityEntity` | `LegalEntities` | auto-exact |
| Operating units | `OMOperatingUnitEntity` | `OperatingUnits` | verified |
| Organization hierarchy - published | `OMOrganizationHierarchyPublishedEntity` | `OrganizationHierarchyPublishedV2` | verified |
| Organization hierarchy purposes | `OMHierarchyPurposeEntity` | `OrganizationHierarchyPurposes` | verified |
| Organization hierarchy type | `OMHierarchyTypeEntity` | `OrganizationHierarchyTypes` | verified |
| Language | `LanguageEntity` | `LanguageCodes` | verified |
| Party postal addresses V2 | `DirPartyPostalAddressEntity` | `PartyPostalAddresses` | manual-unverified |
| System Users | `SystemUserEntity` | `SystemUsers` | auto-exact |
| Security roles | `SecurityRoleEntity` | `SecurityRoles` | auto-exact |
| Security user role associations | `SecurityUserRoleAssociationEntity` | `SecurityUserRoleAssociations` | auto-exact |
| Units | `UnitEntity` | `UnitsOfMeasure` | verified |
| Unit conversions | `UnitConversionEntity` | `UnitOfMeasureConversions` | verified |
| Number sequences | `NumberSequenceEntity` | `NumberSequencesV2References` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Financial Calendar Period | `FiscalCalendarPeriodEntity` |
| Party contacts V3 | `DirPartyContactEntity` |
| User information | `UserInfoEntity` |
| Workflow version | `WorkflowVersionEntity` |
| Workflow version notification | `WorkflowVersionNoteEntity` |
| Workflow element | `WorkflowElementEntity` |
| Workflow element notification | `WorkflowElementNoteEntity` |
| Workflow step | `WorkflowStepEntity` |
| Workflow escalation path | `WorkflowEscalationPathEntity` |
| Workflow escalation step | `WorkflowEscalationStepEntity` |
| Workflow parallel branch | `WorkflowParallelBranchEntity` |
| Workflow sub workflow | `WorkflowSubWorkflowEntity` |
| Workflow sub workflow element | `WorkflowSubWorkflowElementEntity` |
| Workflow version association | `WorkflowVersionAssociationEntity` |
| Workflow version association element notification | `WorkflowVersionAssociationElemNoteEntity` |
| Workflow expression | `WorkflowExpressionEntity` |
| Workflow time span | `WorkflowTimeSpanEntity` |
| Workflow table | `WorkflowTableEntity` |
| Workflow parallel activity | `WorkflowParallelActivityEntity` |
| Work item queue | `WorkflowWorkItemQueueEntity` |
| Work item queue group | `WorkflowWorkItemQueueGroupEntity` |
| Work item queue group assignment | `WorkflowWorkItemQueueGroupAssignmentEntity` |
| Workflow message text | `WorkflowMessageTextEntity` |
| Workflow line item | `WorkflowLineItemWorkflowEntity` |
| Workflow tracking status | `WorkflowTrackingStatusEntity` |
| Workflow tracking table | `WorkflowTrackingTableEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Organization Administration:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Organization Administration-related business process areas:
- **Define the organizational structure** (legal entities, operating units, hierarchies)
- **Configure system settings** (number sequences, address setup, currencies)
- **Manage workflow** (workflow design, approval processes, escalation)
- **Manage security** (role-based security, duty segregation, user assignments)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Get started with Dynamics 365 Finance** | https://learn.microsoft.com/en-us/training/paths/get-started-finance-operations/ |
| Configure your organization in Finance and Operations | https://learn.microsoft.com/en-us/training/modules/configure-your-organization-finance-ops/ |
| Configure the workflow system | https://learn.microsoft.com/en-us/training/modules/configure-workflow/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Organization administration home page | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/organization-administration-home-page |
| Organizations and organizational hierarchies overview | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/organizations-organizational-hierarchies |
| Plan your organizational hierarchy | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/plan-organizational-hierarchy |
| Create a legal entity | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/create-legal-entity |
| Create an operating unit | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/create-operating-unit |
| Number sequences overview | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/number-sequence-overview |
| Set up number sequences using a wizard | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/set-up-number-sequences-wizard |
| Global address book overview | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/overview-global-address-book |
| Configure global address book | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/configure-global-address-book |
| Workflow system overview | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/overview-workflow-system |
| Workflow elements | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/workflow-elements |
| Create workflows | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/create-workflow |
| Configure workflow properties | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/configure-workflow-properties |
| Configure approval processes | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/configure-approval-process-workflow |
| Address setup | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/global-address-book-address-setup |
| Define the organizational structure | https://learn.microsoft.com/en-us/dynamics365/guidance/organizational-strategy/define-organizational-strategy |

---

## 5-Phase Configuration Sequence

### Phase 1: Legal Entities & Organization Structure

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| CompanyInfo | Organization administration > Organizations > Legal entities | Define legal entity (company) |
| OMOperatingUnit | Organization administration > Organizations > Operating units | Departments, cost centers, value streams |
| OMHierarchyType | Organization administration > Organizations > Organization hierarchy purposes | Hierarchy type definition |
| OMHierarchyPublished | Organization administration > Organizations > Organization hierarchies | Published hierarchy structure |

### Phase 2: Address & Localization Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| LogisticsAddressFormat | Organization administration > Global address book > Addresses > Address setup | Address format by country |
| LogisticsAddressCountryRegion | Organization administration > Global address book > Addresses > Address setup | Countries and regions |
| LogisticsAddressState | Organization administration > Global address book > Addresses > Address setup | States and provinces |
| LogisticsAddressCounty | Organization administration > Global address book > Addresses > Address setup | County definitions |
| LogisticsAddressCity | Organization administration > Global address book > Addresses > Address setup | City definitions |
| LogisticsAddressZipCode | Organization administration > Global address book > Addresses > Address setup | Postal codes |
| LogisticsAddressDistrict | Organization administration > Global address book > Addresses > Address setup | District definitions |
| DirPartyTable | Organization administration > Global address book > Global address book | Global address book entries |

### Phase 3: Currency & Calendar Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| Currency | General ledger > Currencies > Currencies | Currency code definitions |
| ExchangeRateType | General ledger > Currencies > Exchange rate types | Rate type classification |
| ExchangeRateCurrencyPair | General ledger > Currencies > Currency exchange rates | Exchange rate values |
| FiscalCalendar | General ledger > Calendars > Fiscal calendars | Fiscal calendar definition |
| FiscalCalendarYear | (Within fiscal calendar) | Fiscal year periods |
| FiscalCalendarPeriod | (Within fiscal calendar) | Fiscal period details |

### Phase 4: Users, Security & Number Sequences

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| SystemUser | System administration > Users > Users | System user accounts |
| UserInfo | System administration > Users > Users | User preferences and settings |
| SecurityRole | System administration > Security > Security roles | Role definitions |
| SecurityUserRoleAssociation | System administration > Security > Assign users to roles | User-to-role mapping |
| NumberSequenceTable | Organization administration > Number sequences > Number sequences | Number sequence definitions |

### Phase 5: Workflow Configuration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| WorkflowTable | (Various module > Setup > Workflows) | Workflow type registration |
| WorkflowVersion | (Within workflow editor) | Workflow version definitions |
| WorkflowElement | (Within workflow editor) | Approval/task elements |
| WorkflowStep | (Within workflow editor) | Workflow step assignments |
| WorkflowEscalationPath | (Within workflow editor) | Escalation routing |
| WorkItemQueue | Organization administration > Workflow > Work item queues | Queue-based work routing |

---

## Organization Structure Design

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ORGANIZATION STRUCTURE DESIGN                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  LEGAL ENTITIES (Companies)                                              │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Each legal entity = separate accounting entity         │             │
│  │ • Own chart of accounts, fiscal calendar, currency       │             │
│  │ • Mapped to tax registrations and regulatory reporting   │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
│  OPERATING UNITS                                                         │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Department — functional grouping (Sales, HR, Finance)  │             │
│  │ • Cost center — cost tracking unit                       │             │
│  │ • Value stream — lean manufacturing flow                 │             │
│  │ • Business unit — strategic business segment             │             │
│  │ • Retail channel — store or online channel               │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
│  ORGANIZATION HIERARCHIES                                                │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Centralized payments                                   │             │
│  │ • Financial reporting                                    │             │
│  │ • Budget planning                                        │             │
│  │ • Security                                               │             │
│  │ • Procurement                                            │             │
│  │ • Retail assortment                                      │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Workflow System Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        WORKFLOW PROCESS FLOW                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. USER SUBMITS DOCUMENT                                                │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Purchase requisition, expense report, journal, etc.    │          │
│     │ • System evaluates workflow conditions                   │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  2. WORKFLOW PROCESSING                                                  │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Manual tasks assigned to users/queues                  │          │
│     │ • Automated tasks execute system actions                 │          │
│     │ • Approval steps route for decision                      │          │
│     │ • Conditional decisions branch workflow                  │          │
│     │ • Parallel activities run simultaneously                 │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  3. ESCALATION                                                           │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Time-based escalation if no action taken               │          │
│     │ • Escalation paths route to next-level approver          │          │
│     │ • Auto-approve/reject options on timeout                 │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  4. COMPLETION                                                           │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Document status updated (Approved/Rejected)            │          │
│     │ • Notifications sent to originator                       │          │
│     │ • Downstream processes triggered                         │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `OMLegalEntities` | Legal entities | Organization |
| `OMOperatingUnits` | Operating units | Organization |
| `OMOrganizationHierarchies` | Organization hierarchies | Organization |
| `DirPartyTable` | Global address book | Address |
| `LogisticsAddressSetup` | Address setup | Address |
| `SystemCurrency` | Currencies | Currency |
| `ExchangeRateType` | Exchange rate types | Currency |
| `ExchangeRates` | Currency exchange rates | Currency |
| `NumberSequenceList` | Number sequences | Setup |
| `FiscalCalendar` | Fiscal calendars | Calendar |
| `SysUserManagement` | Users | Security |
| `SysSecurityRoles` | Security roles | Security |
| `WorkflowWorkItemQueue` | Work item queues | Workflow |
| `WorkflowStatus` | Workflow history | Workflow |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Legal entities** must be created first — all other configuration depends on company context
2. **Fiscal calendars** must exist before General Ledger setup
3. **Currencies** must be defined before any financial transaction configuration
4. **Exchange rate types** must exist before exchange rates can be entered
5. **Address formats** must be configured before postal addresses can be created
6. **Number sequences** must be set up before modules that require auto-numbering (AP, AR, GL, etc.)
7. **Organization hierarchies** must be published before they can be used by modules (budget planning, security, etc.)
8. **Users** must be imported before security role assignments
9. **Workflow** configuration requires the underlying module to be configured first (e.g., AP workflows need AP setup)

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Legal entity does not exist" | Company not created or not in data area | Create legal entity first |
| "Number sequence not found" | Number sequence not configured for reference | Set up number sequences via wizard or manual |
| "Currency code not found" | Currency not defined | Add currency in GL > Currencies |
| "Exchange rate not found for date" | Missing rate for currency pair / date | Add exchange rate for the specific date |
| "Fiscal calendar period not open" | Period status is On Hold or Closed | Open period in GL > Calendars |
| "Address format not valid" | Country/region missing address format | Configure address format lines |
| "Hierarchy not published" | Draft hierarchy cannot be used by modules | Publish the hierarchy with an effective date |
