# Project Planning & Scheduling Module - Knowledge Source

> This file is the central knowledge hub for **Project Planning & Scheduling** within Dynamics 365 Project Operations.

---


---


> **Microsoft Learn Reference:** [Project Planning & Scheduling](https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/project-management-overview)

## Module Overview

Project Planning & Scheduling in Dynamics 365 Project Operations provides work breakdown structure (WBS) creation, task scheduling, resource assignment, effort estimation, and project timeline management. It uses the Microsoft Project scheduling engine for automatic scheduling.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Work Breakdown Structure** | Create hierarchical task structures with predecessor dependencies |
| **Task Scheduling** | Automatic and manual task scheduling with duration and effort tracking |
| **Resource Assignment** | Assign team members to tasks with effort distribution |
| **Project Templates** | Create reusable project templates from existing projects |
| **Effort Estimation** | Estimate effort in hours by task and resource role |
| **Critical Path** | Identify the critical path for project timeline optimization |
| **Project Calendar** | Define working and non-working time for scheduling accuracy |
| **Gantt Chart** | Visualize project schedules with interactive Gantt views |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Project planning uses the Dataverse-based scheduling engine (Project for the Web).

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Project Planning & Scheduling-related business process areas:
- **Work breakdown structure (WBS)** (task hierarchy, milestones)
- **Task scheduling** (auto-scheduling, manual scheduling)
- **Task dependencies** (finish-to-start links)
- **Resource assignment** (team members to tasks)
- **Effort estimation** (planned hours, cost estimates)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Plan projects in Dynamics 365 Project Operations** | https://learn.microsoft.com/en-us/training/modules/plan-projects-project-operations/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Project management overview | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/project-management-overview |
| Create a project | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/create-project |
| Work breakdown structure (WBS) | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/work-breakdown-structures |
| Task dependencies | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/task-dependencies |
| Project scheduling modes | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/scheduling-modes |
| Resource assignments | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/resource-assignments |
| Effort estimates | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/effort-estimates |
| Expense estimates | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/expense-estimates |
| Project schedule API | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/schedule-api-preview |
| Project templates | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/project-templates |
| Project calendar | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/project-calendar |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Organization units | Settings > Business management > Organization units | Company/practice units |
| Work hour templates | Settings > Work hour templates | Calendar definitions |
| Transaction categories | Settings > Transaction categories | Task categorization |
| Roles (bookable resource categories) | Settings > Bookable resource categories | Named roles for assignment |

### Phase 2: Project Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Project templates | Projects > Project templates | Reusable WBS templates |
| Create project | Projects > New | New project record |
| Assign project calendar | (Within project) > Calendar | Work hours for scheduling |
| Set scheduling mode | (Within project) > Scheduling mode | Auto-scheduled or manually scheduled |

### Phase 3: WBS Construction

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Create summary tasks | (Within project) > Tasks > Add task | Parent/container tasks |
| Create leaf tasks | (Within project) > Tasks > Add task | Work items |
| Set task duration/effort | (Within task) | Planned hours and dates |
| Define dependencies | (Within task) > Predecessors | Finish-to-start links |
| Set milestones | (Within task) > Milestone flag | Key delivery points |

### Phase 4: Resource Assignment & Estimation

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Assign team members | (Within project) > Team > Add | Generic or named resources |
| Assign resources to tasks | (Within task) > Resource | Link team member to task |
| Effort estimates | (Calculated from assignment) | Hours per resource per task |
| Cost estimates | (Calculated from rates) | Financial impact of plan |
| Expense estimates | (Within project) > Estimates > Expense | Non-labor cost estimates |

---

## WBS & Scheduling Model

```
┌─────────────────────────────────────────────────────────────────────────┐
│                 WBS & SCHEDULING MODEL                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PROJECT                                                                 │
│  └── Phase 1: Discovery (Summary Task)                                   │
│       ├── 1.1 Requirements Gathering ─── 40h ─── Consultant             │
│       ├── 1.2 Current State Analysis ──── 24h ─── Sr. Consultant        │
│       └── 1.3 Gap Analysis ─────────── 16h ─── Architect                │
│                                           │ (Finish-to-Start)            │
│  └── Phase 2: Design (Summary Task)       ▼                             │
│       ├── 2.1 Solution Design ─────── 60h ─── Architect                 │
│       ├── 2.2 Technical Design ────── 40h ─── Developer                 │
│       └── ★ 2.3 Design Sign-off ──── 0h ──── MILESTONE                 │
│                                           │ (Finish-to-Start)            │
│  └── Phase 3: Build (Summary Task)        ▼                             │
│       ├── 3.1 Configuration ──────── 80h ─── Consultant                 │
│       ├── 3.2 Customization ─────── 120h ─── Developer                  │
│       └── 3.3 Unit Testing ─────── 40h ─── Developer                   │
│                                                                          │
│  SCHEDULING ENGINE                                                       │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Auto-scheduled: Engine calculates dates from effort,    │             │
│  │   dependencies, and resource calendars                    │             │
│  │ • Fixed duration / Fixed effort / Fixed units              │             │
│  │ • Respects project calendar (working days, holidays)      │             │
│  │ • Dependency chains drive critical path                   │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
│  ESTIMATION                                                              │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ Effort (hours)  ×  Cost Rate  =  Planned Cost            │             │
│  │ Effort (hours)  ×  Bill Rate  =  Planned Revenue          │             │
│  │ + Expense estimates + Material estimates                  │             │
│  │ = Total Project Estimate                                  │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `ProjectsListPage` | Projects | Projects |
| `ProjectTemplates` | Project templates | Templates |
| `ProjectTasks` | Tasks | Planning |
| `ProjectTeam` | Team | Resources |
| `ProjectEstimates` | Estimates | Financial |
| `WorkHourTemplates` | Work hour templates | Setup |
| `BookableResourceCategories` | Resource roles | Setup |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Work hour templates** must be configured before project calendars reference them
2. **Project calendar** must be assigned before task scheduling works correctly
3. **Summary tasks** must be created before child (leaf) tasks
4. **Team members** must be added to the project before they can be assigned to tasks
5. **Task dependencies** drive the schedule — changes cascade through linked tasks
6. **Resource assignments** generate effort contours and cost/revenue estimates
7. **Project templates** can jumpstart WBS creation for recurring project types

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Task dates not calculating" | Scheduling mode set to Manual | Switch to Auto-scheduled |
| "Resource overallocated" | Resource assigned beyond capacity | Balance assignments or extend timeline |
| "Circular dependency" | Task depends on itself (directly or indirectly) | Remove circular predecessor link |
| "Effort not estimating" | No resource assigned to task | Assign team member to task |
| "Project template import failed" | Template incompatible | Recreate template from working project |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Project Planning & Scheduling** module.

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

