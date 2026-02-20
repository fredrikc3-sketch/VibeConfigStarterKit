# Project Accounting Module - Knowledge Source

> This file is the central knowledge hub for the **Project Accounting & Invoicing** module within Dynamics 365 Project Operations / Finance.

---


---


> **Microsoft Learn Reference:** [Project Accounting & Invoicing](https://learn.microsoft.com/en-us/dynamics365/project-operations/project-accounting/project-accounting-overview)

## Module Overview

Project Accounting & Invoicing in Dynamics 365 Project Operations handles the financial aspects of projects including project cost posting, revenue recognition, WIP management, project invoicing (time & material and fixed-price), and integration with Dynamics 365 Finance for general ledger posting and financial reporting.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Project Invoicing** | Generate invoices based on time & material or fixed-price milestones |
| **Revenue Recognition** | Recognize revenue using percentage of completion or completed contract |
| **WIP Management** | Calculate and post work-in-progress to the general ledger |
| **Cost Posting** | Post project costs from actuals to the general ledger |
| **Funding Sources** | Manage multiple funding sources per contract with limits and allocation |
| **Invoice Proposals** | Create and review invoice proposals before customer billing |
| **Credit Notes** | Process credit notes for invoice corrections and adjustments |
| **Financial Integration** | Integrate with D365 Finance GL for consolidated financial reporting |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 650 - Project Accounting (`650 - Project accounting.json`)

Project management and accounting configuration entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Category groups | ProjCategoryGroupEntity | Project - Categories | 30 |
| 10 | Cost template | ProjCostTemplateEntity | Project - Setup | 30 |
| 10 | Forecast models | ForecastModelEntity | Project - Setup | 30 |
| 10 | Indirect cost component | ProjIndirectCostComponentEntity | Project - Setup | 30 |
| 10 | Indirect cost component group | ProjIndirectCostComponentGroupEntity | Project - Setup | 30 |
| 10 | Journal names | ProjJournalNameEntity | Project - Setup | 30 |
| 10 | Line properties | ProjLinePropertyEntity | Project - Setup | 30 |
| 10 | Period types | ProjPeriodTypeEntity | Project - Setup | 30 |
| 10 | Project categories | ProjCategoryEntity | Project - Categories | 30 |
| 10 | Project contract | ProjContractEntity | Project - Contracts | 30 |
| 10 | Project groups | ProjGroupEntity | Project - Setup | 30 |
| 10 | Project parameters | ProjParametersEntity | Project - Parameters | 30 |
| 10 | Project stages | ProjStageEntity | Project - Setup | 30 |
| 10 | Resource roles | ResourceRoleEntity | Project - Resources | 30 |
| 10 | Resource role price | ResourceRolePriceEntity | Project - Resources | 30 |
| 10 | Timesheet weekly periods | TsTimesheetWeeklyPeriodEntity | Project - Timesheet | 30 |
| 10 | Validation connection types | ProjValConnectionTypeEntity | Project - Validation | 30 |
| 10 | Validation groups | ProjValGroupEntity | Project - Validation | 30 |
| 10 | WBS templates | ProjWBSTemplateEntity | Project - Templates | 30 |
| 20 | Funding rules | ProjFundingRuleEntity | Project - Contracts | 40 |
| 20 | Funding sources | ProjFundingSourceEntity | Project - Contracts | 40 |
| 20 | Intercompany parameters | ProjIntercompanyParametersEntity | Project - Setup | 40 |
| 20 | Ledger posting definitions | ProjLedgerPostingDefinitionEntity | Project - Posting | 40 |
| 20 | Project contract billing rules | ProjContractBillingRuleEntity | Project - Contracts | 40 |
| 20 | Project contract line items | ProjContractLineItemEntity | Project - Contracts | 40 |
| 20 | Projects | ProjProjectEntity | Project - Master | 40 |
| 20 | Project stage rules | ProjStageRuleEntity | Project - Setup | 40 |
| 20 | Validation group assignments | ProjValGroupAssignmentEntity | Project - Validation | 40 |
| 30 | Customer retention terms | ProjCustomerRetentionTermEntity | Project - Billing | 50 |
| 30 | Vendor retention terms | ProjVendorRetentionTermEntity | Project - Billing | 50 |
| 30 | WBS draft | ProjWBSDraftEntity | Project - Planning | 50 |
| 30 | WBS estimates | ProjWBSEstimateEntity | Project - Planning | 50 |

**DMF Load Order Notes:**
- **Seq 10** contains all foundational project setup — categories, groups, parameters, contracts, forecast models, validation groups, line properties
- **Seq 20** contains dependent entities — projects, funding sources/rules, posting definitions, intercompany setup, billing rules
- **Seq 30** contains advanced entities — retention terms, WBS drafts, WBS estimates
- Project contracts must exist before funding sources, billing rules, and contract line items
- Project groups and categories must exist before projects
- Project stages must exist before stage rules

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (categories, groups, parameters, contracts, stages, roles)
- **Level 40:** Dependent entities (projects, funding, posting definitions, validation assignments)
- **Level 50:** Advanced entities (retention terms, WBS structure)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Project Accounting & Invoicing** module.

### Project to profit

*131 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze project performance | 14 | — |
| Develop project strategy | 6 | — |
| Manage project contracts | 18 | — |
| Manage project delivery | 42 | — |
| Manage project financials | 25 | — |
| Plan projects | 26 | — |

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Category groups | `ProjCategoryGroupEntity` | `ProjCategoryGroups` | auto-exact |
| Forecast models | `ForecastModelEntity` | `ForecastModels` | verified |
| Journal names | `ProjJournalNameEntity` | `ProjectJournalNames` | verified |
| Project categories | `ProjCategoryEntity` | `ProjectCategoryEntities` | verified |
| Project contract | `ProjContractEntity` | `ProjectContracts` | verified |
| Project groups | `ProjGroupEntity` | `ProjectGroups` | verified |
| Project parameters | `ProjParametersEntity` | `ProjectParameterV2` | verified |
| WBS templates | `ProjWBSTemplateEntity` | `ProjWBSTemplateTasks` | verified |
| Ledger posting definitions | `ProjLedgerPostingDefinitionEntity` | `ProjectLedgerPostingDefinitions` | verified |
| Project contract line items | `ProjContractLineItemEntity` | `ProjectContractLines` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Cost template | `ProjCostTemplateEntity` |
| Indirect cost component | `ProjIndirectCostComponentEntity` |
| Indirect cost component group | `ProjIndirectCostComponentGroupEntity` |
| Line properties | `ProjLinePropertyEntity` |
| Period types | `ProjPeriodTypeEntity` |
| Project stages | `ProjStageEntity` |
| Resource roles | `ResourceRoleEntity` |
| Resource role price | `ResourceRolePriceEntity` |
| Timesheet weekly periods | `TsTimesheetWeeklyPeriodEntity` |
| Validation connection types | `ProjValConnectionTypeEntity` |
| Validation groups | `ProjValGroupEntity` |
| Funding rules | `ProjFundingRuleEntity` |
| Funding sources | `ProjFundingSourceEntity` |
| Intercompany parameters | `ProjIntercompanyParametersEntity` |
| Project contract billing rules | `ProjContractBillingRuleEntity` |
| Projects | `ProjProjectEntity` |
| Project stage rules | `ProjStageRuleEntity` |
| Validation group assignments | `ProjValGroupAssignmentEntity` |
| Customer retention terms | `ProjCustomerRetentionTermEntity` |
| Vendor retention terms | `ProjVendorRetentionTermEntity` |
| WBS draft | `ProjWBSDraftEntity` |
| WBS estimates | `ProjWBSEstimateEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Project Accounting:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Project Accounting-related business process areas:
- **Project to Profit** (end-to-end project lifecycle)
- **Project setup and planning** (contracts, WBS, estimates)
- **Time and expense recording** (timesheets, expense journals)
- **Project invoicing** (invoice proposals, billing rules, retention)
- **Revenue recognition** (estimates, WIP, revenue recognition)
- **Project cost control** (cost tracking, budget analysis)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure Project Operations in Dynamics 365** | https://learn.microsoft.com/en-us/training/paths/configure-project-operations-finance/ |
| Configure project management and accounting | https://learn.microsoft.com/en-us/training/modules/get-started-project-management-accounting-dyn365-finance/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Project management and accounting overview | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/overview-project-management-accounting |
| Configure project management and accounting | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/configure-project-management-accounting |
| Project categories | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/project-categories-templates |
| Project contracts | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/project-contracts |
| Funding sources | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/project-funding |
| Project groups | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/project-groups |
| Project stages | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/project-stages |
| Project invoicing | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/project-invoicing |
| Project estimates | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/project-estimates-templates |
| Project timesheets | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/project-timesheets |
| Work breakdown structures | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/work-breakdown-structures |
| Project budget management | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/project-budgets |
| Intercompany invoicing | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/intercompany-invoicing |
| Project posting profiles | https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-pma/project-ledger-posting |

---

## 6-Phase Configuration Sequence

### Phase 1: Prerequisites (GL & Organization)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Main accounts | General ledger > Chart of accounts > Accounts > Main accounts | Project-related GL accounts (WIP, accrued revenue, cost) |
| Financial dimensions | General ledger > Chart of accounts > Dimensions | Project dimension |
| Fiscal calendars | General ledger > Calendars > Fiscal calendars | Project period calendars |
| Number sequences | Organization administration > Number sequences | Project, contract, invoice numbering |
| Workers | Human resources > Workers > Workers | Project team members |

### Phase 2: Category & Group Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| ProjCategoryGroup | Project management and accounting > Setup > Categories > Category groups | Category classification |
| ProjCategory | Project management and accounting > Setup > Categories > Project categories | Transaction category definitions |
| ProjGroup | Project management and accounting > Setup > Posting > Project groups | Project type grouping (Time & material, Fixed-price, etc.) |
| ProjLineProperty | Project management and accounting > Setup > Posting > Line properties | Chargeable/Non-chargeable classification |
| ProjStage | Project management and accounting > Setup > Project stages | Project lifecycle stages |

### Phase 3: Contract & Billing Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| ProjContract | Project management and accounting > Project contracts > Project contracts | Contract definitions |
| ProjFundingSource | (Within contract) | Customer/grant funding sources |
| ProjFundingRule | (Within contract) | Funding allocation rules |
| ProjContractBillingRule | (Within contract) | Billing schedule/milestones |
| ProjContractLineItem | (Within contract) | Contract line detail |
| ProjCostTemplate | Project management and accounting > Setup > Costs > Cost templates | Cost completion method |

### Phase 4: Posting & Validation Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| ProjLedgerPostingDefinition | Project management and accounting > Setup > Posting > Ledger posting setup | GL posting rules per transaction type |
| ProjValGroup | Project management and accounting > Setup > Validation > Validation groups | Category/worker/project validation |
| ProjValGroupAssignment | (Within validation group) | Validation assignments |
| ProjJournalName | Project management and accounting > Setup > Journals > Journal names | Project journal types |
| ForecastModel | Project management and accounting > Setup > Forecasting > Forecast models | Forecast model hierarchy |

### Phase 5: Parameters & Resource Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| ProjParameters | Project management and accounting > Setup > Project management and accounting parameters | Module parameters |
| ResourceRole | Project management and accounting > Setup > Resources > Resource roles | Role-based pricing |
| ResourceRolePrice | Project management and accounting > Setup > Resources > Resource role prices | Role/category rate tables |
| TsTimesheetWeeklyPeriod | Project management and accounting > Setup > Timesheets > Timesheet periods | Timesheet period setup |
| ProjIntercompanyParameters | Project management and accounting > Setup > Intercompany > Intercompany parameters | Cross-company project billing |

### Phase 6: Projects & WBS

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| ProjTable | Project management and accounting > Projects > All projects | Project master records |
| ProjWBSTemplate | Project management and accounting > Setup > Projects > Work breakdown structure templates | WBS templates |
| ProjWBSDraft | (Within project) | Project WBS structure |
| ProjWBSEstimate | (Within project WBS) | Task-level estimates |
| ProjCustomerRetentionTerm | Project management and accounting > Setup > Retention > Customer retention terms | Retention schedules |
| ProjVendorRetentionTerm | Project management and accounting > Setup > Retention > Vendor retention terms | Subcontractor retention |

---

## Project Lifecycle Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       PROJECT LIFECYCLE FLOW                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. CONTRACT & PROJECT CREATION                                          │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Create project contract (customer, funding sources)    │          │
│     │ • Define billing rules (T&M, fixed-price, milestones)   │          │
│     │ • Create project (linked to contract)                    │          │
│     │ • Build WBS (tasks, resources, schedule)                 │          │
│     │ • Create project budget                                  │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  2. COST RECORDING                                                       │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Timesheet entry (hours by project/task)                │          │
│     │ • Expense journal posting                                │          │
│     │ • Item consumption                                       │          │
│     │ • Vendor invoices charged to project                     │          │
│     │ • Fee journal entries                                    │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  3. REVENUE RECOGNITION                                                  │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Run Estimate process (WIP & accrued revenue)           │          │
│     │ • Post estimates to ledger                               │          │
│     │ • Fixed-price: percentage of completion method            │          │
│     │ • T&M: post as incurred                                  │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  4. INVOICING                                                            │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Create invoice proposals                               │          │
│     │ • Review and adjust billing lines                        │          │
│     │ • Apply retention terms                                  │          │
│     │ • Post project invoices                                  │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  5. PROJECT CLOSE                                                        │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Eliminate WIP and accrued revenue                      │          │
│     │ • Final invoicing and retention release                  │          │
│     │ • Project completion analysis                            │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Project Types

| Type | Revenue Recognition | Billing Method | Use Case |
|------|--------------------|----------------|----------|
| **Time and material** | On posting | Actual cost + markup | Consulting, support services |
| **Fixed-price** | Percentage of completion | Milestone-based | Construction, implementation |
| **Investment** | No revenue | No billing | Internal projects, R&D |
| **Cost project** | No revenue | No billing | Internal cost tracking |
| **Time project** | No revenue | No billing | Time tracking only |
| **Internal** | No revenue | No billing | Internal initiatives |

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `ProjParameters` | Project management and accounting parameters | Setup |
| `ProjCategory` | Project categories | Setup |
| `ProjGroup` | Project groups | Setup |
| `ProjContract` | Project contracts | Contracts |
| `ProjTable` | All projects | Projects |
| `ProjJournalTable` | Project journals | Journals |
| `TsTimesheetEntry` | My timesheets | Timesheets |
| `ProjInvoiceProposalList` | Invoice proposals | Invoicing |
| `ProjEstimate` | Estimates | Revenue |
| `ProjWIPAccount` | WIP | Revenue |
| `ProjLedgerPostingSetup` | Ledger posting setup | Posting |
| `ProjValGroup` | Validation groups | Validation |
| `ProjStage` | Project stages | Setup |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **GL accounts** must exist for WIP, accrued revenue, cost, and revenue accounts
2. **Project categories** must be configured before project transactions can be posted
3. **Project groups** determine the posting behavior — must exist before creating projects
4. **Project contracts** must exist before projects can be associated to them
5. **Funding sources** must be added to contracts before billing can occur
6. **Posting definitions** must be configured before project transactions post to GL
7. **Timesheet periods** must be generated before timesheets can be entered
8. **Line properties** (chargeable/non-chargeable) must exist before transaction posting

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Category not valid for project" | Validation group restricts category | Add category to validation group |
| "Posting profile not found" | Ledger posting definition missing | Configure ledger posting setup |
| "Funding limit exceeded" | Contract funding source limit reached | Increase funding limit or add funding source |
| "Estimate process failed" | Project group or parameters misconfigured | Review project group estimate settings |
| "Timesheet period not found" | Period not generated for date range | Generate timesheet periods |
| "WIP account not configured" | Missing GL account in posting setup | Add WIP account to ledger posting definitions |
