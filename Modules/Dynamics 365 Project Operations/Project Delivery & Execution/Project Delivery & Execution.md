# Project Delivery & Execution Module - Knowledge Source

> This file is the central knowledge hub for **Project Delivery & Execution** within Dynamics 365 Project Operations.

---


---


> **Microsoft Learn Reference:** [Project Delivery & Execution](https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/project-management-overview)

## Module Overview

Project Delivery & Execution in Dynamics 365 Project Operations covers the day-to-day management of active projects including time entry, expense entry, material usage, progress tracking, and project status reporting. It provides the operational foundation for project-based work.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Time Entry** | Record time spent on project tasks with approval workflows |
| **Expense Entry** | Submit project-related expenses with receipt capture |
| **Material Usage** | Track material consumption against project tasks |
| **Progress Tracking** | Monitor task completion, effort remaining, and schedule variance |
| **Project Status** | Update and communicate project health to stakeholders |
| **Approval Workflows** | Route time, expense, and material entries through approval chains |
| **Actuals Processing** | Create project actuals from approved time, expense, and material entries |
| **Project Team Management** | Manage project team composition and role assignments |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Project delivery is managed through Dataverse-based project management forms and task boards.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Project Delivery & Execution-related business process areas:
- **Time entry** (daily/weekly time tracking)
- **Expense management** (expense reports for projects)
- **Material usage** (material consumption on projects)
- **Project approvals** (time, expense, material approval workflows)
- **Task management** (task progress tracking, % complete)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Manage project delivery in Dynamics 365 Project Operations** | https://learn.microsoft.com/en-us/training/paths/manage-project-delivery-project-operations/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Time entry overview | https://learn.microsoft.com/en-us/dynamics365/project-operations/time/time-entry-overview |
| Create time entries | https://learn.microsoft.com/en-us/dynamics365/project-operations/time/create-time-entries |
| Expense management overview | https://learn.microsoft.com/en-us/dynamics365/project-operations/expense/expense-overview |
| Material usage on projects | https://learn.microsoft.com/en-us/dynamics365/project-operations/material/material-usage-log |
| Approvals overview | https://learn.microsoft.com/en-us/dynamics365/project-operations/approvals/approvals-overview |
| Project tracking overview | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/project-tracking-overview |
| Update project task progress | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/update-project-task |
| Project stages and lifecycle | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/project-stages |
| Actuals overview | https://learn.microsoft.com/en-us/dynamics365/project-operations/actuals/actuals-overview |
| Subcontracting | https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/subcontracting/subcontracting-overview |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Project Operations deployment | (Dataverse + Finance integration) | Dual-write or integrated deployment |
| Organization units | Settings > Organization units | Practice or delivery units |
| Transaction categories | Settings > Transaction categories | Time, expense, material categories |
| Price lists | Settings > Price lists | Cost and bill rates |

### Phase 2: Time & Expense Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Time entry configuration | Settings > Project parameters > Time entry | Weekly/daily mode, dimension defaults |
| Expense categories | Settings > Transaction categories > Expense | Category definitions |
| Expense policies | Settings > Expense policies | Per diem, receipt rules |
| Material categories | Settings > Transaction categories > Material | Material types |
| Approval configuration | Settings > Approval sets | Approval flow rules |

### Phase 3: Project Execution

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Project creation | Projects > New project | Create project record |
| WBS / Task creation | (Within project) > Tasks | Build task hierarchy |
| Team member assignment | (Within project) > Team | Assign resources to tasks |
| Task progress update | (Within project) > Tasks > (task) | % complete, effort remaining |
| Time entries | Time entries > New | Log hours against project tasks |
| Expense entries | Expenses > New | Submit project expenses |

### Phase 4: Approvals & Actuals

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Submit for approval | (Within time/expense entry) > Submit | Send for manager review |
| Approve entries | Approvals > Pending approvals | Manager approves/rejects |
| Actuals generation | (Automatic on approval) | Creates cost and sales actuals |
| Recall entries | (Within submitted entry) > Recall | Recall for correction |

---

## Project Delivery Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  PROJECT DELIVERY & EXECUTION FLOW                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PROJECT KICKOFF                                                         │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Project created (from quote or contract)               │             │
│  │ • WBS / tasks defined                                    │             │
│  │ • Team members assigned                                  │             │
│  │ • Project stage: Active                                  │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  WEEKLY EXECUTION CYCLE                                                  │
│  ┌────────────────────────────────────────────────────────┐             │
│  │                                                          │             │
│  │  TEAM MEMBERS                                            │             │
│  │  ┌─────────────────────────────────────────────────┐    │             │
│  │  │ Mon─Fri: Record time entries (task + hours)       │    │             │
│  │  │          Submit expense reports (receipts)        │    │             │
│  │  │          Log material usage                       │    │             │
│  │  │ Weekly:  Submit all entries for approval          │    │             │
│  │  └──────────────────────┬──────────────────────────┘    │             │
│  │                         │                                │             │
│  │                         ▼                                │             │
│  │  PROJECT MANAGER                                         │             │
│  │  ┌─────────────────────────────────────────────────┐    │             │
│  │  │ • Review and approve/reject entries               │    │             │
│  │  │ • Update task % complete                          │    │             │
│  │  │ • Monitor cost tracking dashboard                 │    │             │
│  │  │ • Manage scope changes                            │    │             │
│  │  └──────────────────────┬──────────────────────────┘    │             │
│  │                         │                                │             │
│  │                         ▼                                │             │
│  │  ACTUALS GENERATED (Automatic)                           │             │
│  │  ┌───────────────────────────────────────────────────┐  │             │
│  │  │ Cost actual │ Unbilled sales actual │ Journal entry │  │             │
│  │  └───────────────────────────────────────────────────┘  │             │
│  │                                                          │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  INVOICING (→ see Project Accounting module)                             │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Create invoice from unbilled actuals                    │             │
│  │ • Confirm invoice → billed sales actuals                  │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `ProjectsListPage` | Projects | Projects |
| `TimeEntries` | Time entries | Execution |
| `ExpenseEntries` | Expenses | Execution |
| `MaterialUsageLog` | Material usage | Execution |
| `ApprovalsListPage` | Approvals | Review |
| `ActualsListPage` | Actuals | Data |
| `ProjectTasks` | Project tasks | Management |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Project must be in Active stage** before time/expense can be recorded
2. **Team members must be assigned** to the project to submit entries
3. **Transaction categories** must be configured for the entry type
4. **Price lists** must cover the transaction date for cost/sales calculation
5. **Approval** generates actuals — unapproved entries have no financial impact
6. **Actuals cannot be edited** — must recall and resubmit to correct
7. **Subcontract entries** require subcontract lines and vendor association

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Cannot submit time" | Project not active or user not team member | Activate project and add user to team |
| "No price found" | Price list missing for date/role/unit | Configure pricing dimensions |
| "Approval pending" | Entry not approved by PM | Follow up on approval |
| "Actual reversal needed" | Approved entry was incorrect | Recall, correct, and resubmit |
| "Task not assignable" | Task is summary/parent task | Assign to leaf-level tasks only |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Project Delivery & Execution** module.

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

