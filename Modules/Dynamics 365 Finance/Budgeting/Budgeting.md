# Budgeting Module - Knowledge Source

> This file is the central knowledge hub for the **Budgeting** module within Dynamics 365 Finance.

---


---


> **Microsoft Learn Reference:** [Budgeting](https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/budgeting-overview)

## Module Overview

The Budgeting module in Dynamics 365 Finance supports financial planning and budget control. It enables organizations to create budget plans, register budget entries, define budget models, and enforce budget control rules that prevent spending beyond approved limits. Budget planning supports workflow-based approval and what-if scenarios.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Budget Planning** | Create multi-scenario budget plans with workflow-based approvals |
| **Budget Register Entries** | Record and track budget amounts against ledger accounts and dimensions |
| **Budget Control** | Enforce spending limits by checking available budget before transactions post |
| **Budget Models** | Define budget models to organize and compare multiple budget versions |
| **Budget Transfer Rules** | Control budget transfers between accounts and dimensions |
| **Position Budgeting** | Plan and budget for workforce positions and compensation |
| **Budget Analysis** | Compare actuals vs. budget with variance analysis reports |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 160 - Budgeting (`160 - Budgeting.json`)

Budgeting configuration, budget control, and budget planning entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Budget code | BudgetTransactionCodeEntity | Budget - Setup | 30 |
| 10 | Budget control configuration activation | BudgetControlConfigurationActivationEntity | Budget Control | 30 |
| 10 | Budget control configuration | BudgetControlConfigurationEntity | Budget Control | 30 |
| 10 | Budget control cycle model | BudgetCycleEntity | Budget Control | 30 |
| 10 | Budget control dimension attribute value set | BudgetControlDimensionAttributeValueSetEntity | Budget Control | 30 |
| 10 | Budget control documents and journals | BudgetControlDocumentsAndJournalsEntity | Budget Control | 30 |
| 10 | Budget control group criteria | BudgetControlGroupCriteriaEntity | Budget Control | 30 |
| 10 | Budget control group | BudgetControlGroupEntity | Budget Control | 30 |
| 10 | Budget control message level | BudgetControlMessageLevelEntity | Budget Control | 30 |
| 10 | Budget control over budget permissions | BudgetControlOverBudgetPermissionsEntity | Budget Control | 30 |
| 10 | Budget control rules | BudgetControlRuleEntity | Budget Control | 30 |
| 10 | Budget dimensions | BudgetDimensionEntity | Budget - Setup | 30 |
| 10 | Budget model | BudgetModelEntity | Budget - Setup | 30 |
| 10 | Budget parameters | BudgetParametersEntity | Budget - Setup | 30 |
| 10 | Budget plan allocation schedule | BudgetPlanAllocationScheduleEntity | Budget Planning | 30 |
| 10 | Budget plan column | BudgetPlanColumnEntity | Budget Planning | 30 |
| 10 | Budget plan layout | BudgetPlanLayoutEntity | Budget Planning | 30 |
| 10 | Budget plan preparation | BudgetPlanPrepareEntity | Budget Planning | 30 |
| 10 | Budget plan priority | BudgetPlanPriorityEntity | Budget Planning | 30 |
| 10 | Budget plan process administration | BudgetPlanProcessAdministrationEntity | Budget Planning | 30 |
| 10 | Budget plan process | BudgetPlanProcessEntity | Budget Planning | 30 |
| 10 | Budget plan scenario | BudgetPlanScenarioEntity | Budget Planning | 30 |
| 10 | Budget plan stage rule | BudgetPlanStageRuleEntity | Budget Planning | 30 |
| 10 | Budget plan stage | BudgetPlanStageEntity | Budget Planning | 30 |
| 10 | Budget plan workflow stage | BudgetPlanWorkflowStageEntity | Budget Planning | 30 |
| 10 | Budget sub model | BudgetSubModelEntity | Budget - Setup | 40 |
| 10 | Budget transfer rules | BudgetTransferRulesEntity | Budget - Setup | 30 |
| 10 | Forecast position budget cost elements | ForecastPositionBudgetCostElementEntity | Budget Planning | 30 |
| 10 | Forecast positions | ForecastPositionEntity | Budget Planning | 30 |
| 10 | Period allocation categories | BudgetPeriodAllocationCategoryEntity | Budget Planning | 30 |
| 20 | Budget control configuration budget group | BudgetControlConfigBudgetGroupEntity | Budget Control | 40 |
| 20 | Budget control configuration dimension | BudgetControlConfigDimensionEntity | Budget Control | 40 |
| 20 | Budget plan allocation schedule lines | BudgetPlanAllocationScheduleLineEntity | Budget Planning | 40 |
| 20 | Budget plan layout columns | BudgetPlanLayoutColumnEntity | Budget Planning | 40 |
| 20 | Budget plan layout elements | BudgetPlanLayoutElementEntity | Budget Planning | 40 |
| 20 | Budget plan process stage rules | BudgetPlanProcessStageRuleEntity | Budget Planning | 40 |

**DMF Load Order Notes:**
- **Seq 10** contains all foundational budget setup — codes, models, parameters, dimensions, budget control config, budget plan definitions
- **Seq 20** contains dependent entities — budget control dimension assignments, budget plan layout details, process stage rules
- Budget models must be loaded before sub-models
- Budget plan stages and scenarios must exist before process definitions
- Budget control configuration must be loaded before activation

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (codes, models, parameters, dimensions, stages, scenarios, rules)
- **Level 40:** Dependent entities (sub-models, layout columns/elements, configuration groups)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Budgeting** module.

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

### Forecast to plan

*28 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze business performance | 9 | — |
| Conduct sales and operations planning | 6 | — |
| Develop business strategy | 12 | — |
| Execute sales and operations | 1 | — |

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Budget code | `BudgetTransactionCodeEntity` | `BudgetTransactionCodes` | manual-unverified |
| Budget control configuration activation | `BudgetControlConfigurationActivationEntity` | `BudgetControlConfigurationActivations` | verified |
| Budget control configuration | `BudgetControlConfigurationEntity` | `BudgetControlConfigurations` | verified |
| Budget control cycle model | `BudgetCycleEntity` | `BudgetCycles` | verified |
| Budget control documents and journals | `BudgetControlDocumentsAndJournalsEntity` | `BudgetControlDocumentsAndJournals` | auto-exact |
| Budget control group criteria | `BudgetControlGroupCriteriaEntity` | `BudgetControlGroupCriteria` | auto-exact |
| Budget control group | `BudgetControlGroupEntity` | `BudgetControlGroups` | auto-exact |
| Budget control message level | `BudgetControlMessageLevelEntity` | `BudgetControlMessageLevels` | auto-exact |
| Budget control over budget permissions | `BudgetControlOverBudgetPermissionsEntity` | `BudgetControlOverBudgetPermissions` | auto-exact |
| Budget control rules | `BudgetControlRuleEntity` | `BudgetControlRules` | auto-exact |
| Budget dimensions | `BudgetDimensionEntity` | `BudgetDimensions` | auto-exact |
| Budget model | `BudgetModelEntity` | `BudgetModels` | verified |
| Budget parameters | `BudgetParametersEntity` | `BudgetParameters` | verified |
| Budget plan allocation schedule | `BudgetPlanAllocationScheduleEntity` | `BudgetPlanAllocationSchedules` | auto-exact |
| Budget plan column | `BudgetPlanColumnEntity` | `BudgetPlanColumns` | verified |
| Budget plan layout | `BudgetPlanLayoutEntity` | `BudgetPlanLayouts` | verified |
| Budget plan priority | `BudgetPlanPriorityEntity` | `BudgetPlanPriorities` | verified |
| Budget plan process administration | `BudgetPlanProcessAdministrationEntity` | `BudgetPlanProcessAdministrations` | auto-exact |
| Budget plan process | `BudgetPlanProcessEntity` | `BudgetPlanProcesses` | verified |
| Budget plan scenario | `BudgetPlanScenarioEntity` | `BudgetPlanScenarios` | verified |
| Budget plan stage rule | `BudgetPlanStageRuleEntity` | `BudgetPlanStageRules` | auto-exact |
| Budget plan stage | `BudgetPlanStageEntity` | `BudgetPlanStages` | auto-exact |
| Budget plan workflow stage | `BudgetPlanWorkflowStageEntity` | `BudgetPlanWorkflowStages` | verified |
| Budget sub model | `BudgetSubModelEntity` | `BudgetSubModels` | auto-exact |
| Forecast position budget cost elements | `ForecastPositionBudgetCostElementEntity` | `ForecastPositionCostElements` | verified |
| Budget control configuration dimension | `BudgetControlConfigDimensionEntity` | `BudgetControlDimensionAttributes` | verified |
| Budget plan allocation schedule lines | `BudgetPlanAllocationScheduleLineEntity` | `BudgetPlanAllocationSchedules` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Budget control dimension attribute value set | `BudgetControlDimensionAttributeValueSetEntity` |
| Budget plan preparation | `BudgetPlanPrepareEntity` |
| Budget transfer rules | `BudgetTransferRulesEntity` |
| Forecast positions | `ForecastPositionEntity` |
| Period allocation categories | `BudgetPeriodAllocationCategoryEntity` |
| Budget control configuration budget group | `BudgetControlConfigBudgetGroupEntity` |
| Budget plan layout columns | `BudgetPlanLayoutColumnEntity` |
| Budget plan layout elements | `BudgetPlanLayoutElementEntity` |
| Budget plan process stage rules | `BudgetPlanProcessStageRuleEntity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Budgeting:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Budgeting-related business process areas:
- **Record to Report** (budget creation, budget register entries)
- **Budget planning** (collaborative budget preparation, workflow-based approval)
- **Budget control** (real-time budget checking on transactions)
- **Budget register entries** (original budget, transfers, revisions)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and use basic budgeting and budget control** | https://learn.microsoft.com/en-us/training/paths/configure-use-budgeting-dyn365-finance/ |
| Configure basic budgeting components | https://learn.microsoft.com/en-us/training/modules/configure-basic-budgeting-dyn365-finance/ |
| Configure budget control | https://learn.microsoft.com/en-us/training/modules/configure-budget-control-dyn365-finance/ |
| Configure and use budget planning | https://learn.microsoft.com/en-us/training/modules/configure-use-budget-planning-dyn365-finance/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Budgeting home page | https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/budgeting-overview |
| Budget planning overview and configuration | https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/budget-planning-overview-configuration |
| Budget control overview and configuration | https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/budget-control-overview-configuration |
| Budget planning data allocation | https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/budget-planning-data-allocation |
| Budget planning templates for Excel | https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/budget-planning-excel-templates |
| Position budgeting | https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/position-budgeting |
| Budget funds available | https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/budget-funds-available |
| Create budget register entries | https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/tasks/create-budget-register-entries |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites (GL & Organization)

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Fiscal calendars | General ledger > Calendars > Fiscal calendars | Budget cycle time spans |
| Financial dimensions | General ledger > Chart of accounts > Dimensions > Financial dimensions | Budget dimensions |
| Main accounts | General ledger > Chart of accounts > Accounts > Main accounts | Budget-relevant accounts |
| Organization hierarchy | Organization administration > Organizations > Organization hierarchies | Budget planning hierarchy |

### Phase 2: Basic Budget Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| BudgetParameters | Budgeting > Setup > Basic budgeting > Budget parameters | Module parameters |
| BudgetModel | Budgeting > Setup > Basic budgeting > Budget models | Budget model definitions |
| BudgetSubModel | (Within budget model) | Sub-model hierarchy |
| BudgetDimension | Budgeting > Setup > Basic budgeting > Budget dimensions | Dimensions for budgeting |
| BudgetTransactionCode | Budgeting > Setup > Basic budgeting > Budget codes | Transaction type codes |
| BudgetTransferRules | Budgeting > Setup > Basic budgeting > Budget transfer rules | Transfer permission rules |
| BudgetCycle | Budgeting > Setup > Basic budgeting > Budget cycle time spans | Budget cycle definitions |

### Phase 3: Budget Control Configuration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| BudgetControlConfiguration | Budgeting > Setup > Budget control > Budget control configuration | Master control setup |
| BudgetControlDimension | (Within budget control config) | Control dimensions |
| BudgetControlGroup | (Within budget control config) | Budget group definitions |
| BudgetControlRule | (Within budget control config) | Control rules per dimension |
| BudgetControlDocumentsAndJournals | (Within budget control config) | Source documents subject to control |
| BudgetControlOverBudgetPermissions | (Within budget control config) | Over-budget user permissions |
| BudgetControlMessageLevel | (Within budget control config) | Warning vs. error messages |
| BudgetControlConfigActivation | (Within budget control config) | Activate budget control |

### Phase 4: Budget Planning Configuration

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| BudgetPlanScenario | Budgeting > Setup > Budget planning > Budget planning configuration > Scenarios | Plan data scenarios |
| BudgetPlanStage | Budgeting > Setup > Budget planning > Budget planning configuration > Stages | Workflow stages |
| BudgetPlanPriority | Budgeting > Setup > Budget planning > Budget planning configuration > Priorities | Plan prioritization |
| BudgetPlanColumn | Budgeting > Setup > Budget planning > Budget planning configuration > Columns | Layout column definitions |
| BudgetPlanLayout | Budgeting > Setup > Budget planning > Budget planning configuration > Layouts | Layout assembly |
| BudgetPlanAllocationSchedule | Budgeting > Setup > Budget planning > Budget planning configuration > Allocation schedules | Data allocation rules |
| BudgetPlanProcess | Budgeting > Setup > Budget planning > Budget planning process | Planning process definition |

### Phase 5: Budget Register Entries

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| BudgetRegisterEntry | Budgeting > Budget register entries | Original budget, transfers, revisions |
| BudgetPlanHeader | Budgeting > Budget plans | Budget plan documents |

---

## Budget Control Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      BUDGET CONTROL PROCESS FLOW                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. BUDGET CREATION                                                      │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Create budget register entries (Original budget)       │          │
│     │ • Import from Excel or budget plan                       │          │
│     │ • Transfer/revision entries                              │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  2. BUDGET CONTROL ACTIVATION                                            │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Define control dimensions                              │          │
│     │ • Set budget control rules (by dimension combination)    │          │
│     │ • Configure documents/journals for checking              │          │
│     │ • Set over-budget permissions                            │          │
│     │ • Activate budget control                                │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  3. REAL-TIME BUDGET CHECKING                                            │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • User creates source document (PO, requisition, etc.)  │          │
│     │ • System checks budget funds available                   │          │
│     │ • Warning or hard-stop based on configuration            │          │
│     │ • Budget reservation created if funds available           │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
│  4. BUDGET ANALYSIS                                                      │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Budget vs. actuals comparison                          │          │
│     │ • Budget control statistics                              │          │
│     │ • Budget funds available inquiry                         │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `BudgetParameters` | Budget parameters | Setup |
| `BudgetModel` | Budget models | Setup |
| `BudgetDimensions` | Budget dimensions | Setup |
| `BudgetTransactionCode` | Budget codes | Setup |
| `BudgetTransferRules` | Budget transfer rules | Setup |
| `BudgetControlConfiguration` | Budget control configuration | Budget Control |
| `BudgetPlanConfiguration` | Budget planning configuration | Budget Planning |
| `BudgetPlanProcess` | Budget planning process | Budget Planning |
| `BudgetRegisterEntries` | Budget register entries | Transactions |
| `BudgetPlans` | Budget plans | Budget Planning |
| `BudgetControlStatistics` | Budget control statistics | Inquiry |
| `BudgetFundsAvailable` | Budget funds available | Inquiry |
| `BudgetCycleTimeSpan` | Budget cycle time spans | Setup |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Fiscal calendars** must exist before defining budget cycle time spans
2. **Financial dimensions** must be configured before budget dimensions
3. **Budget models** must be created before budget register entries
4. **Budget codes** define the type of budget entry (original, transfer, revision)
5. **Budget control configuration** must be fully set up before activation
6. **Once activated**, budget control cannot be deactivated without losing tracking data
7. **Budget planning hierarchy** must be published before budget planning processes
8. **Budget plan scenarios and stages** must exist before creating budget plan processes
9. **Layouts** must be defined before they can be assigned to planning process stages

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Budget funds not available" | Transaction exceeds available budget | Increase budget via transfer/revision or override |
| "Budget control not active" | Budget control configuration not activated | Complete configuration and activate |
| "Budget model not found" | Model not created for budget cycle | Create budget model |
| "Budget dimension combination not valid" | Dimension values not in budget control | Review control dimension setup |
| "Budget register entry cannot be posted" | Missing budget code or period closed | Verify budget code and fiscal period |
