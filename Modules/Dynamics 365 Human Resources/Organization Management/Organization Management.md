# Organization Management Module - Knowledge Source

> This file is the central knowledge hub for **Organization Management** within Dynamics 365 Human Resources.

---


---


> **Microsoft Learn Reference:** [Organization Management](https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-personnel-departments-jobs-positions)

## Module Overview

Organization Management in Dynamics 365 Human Resources manages the organizational structure including departments, teams, reporting relationships, and job architecture. It provides workforce analytics and planning capabilities for headcount forecasting and organizational design.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Organization Design** | Design and visualize organizational structures |
| **Department Hierarchies** | Create departmental reporting hierarchies |
| **Workforce Planning** | Plan headcount and forecast workforce needs |
| **Reporting Relationships** | Define manager-employee and matrix reporting structures |
| **Team Management** | Create and manage cross-functional teams |
| **Job Architecture** | Define job frameworks, levels, and career paths |
| **Organization Charts** | Visualize organizational charts from hierarchy data |
| **Analytics & Reporting** | Use built-in workforce analytics for insights |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Organization structures are configured through Organization Administration and HR forms.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Organization Management-related business process areas:
- **Organization hierarchies** (reporting lines, cost center structures)
- **Departments** (organizational units)
- **Jobs and positions** (job catalog, position management)
- **Position hierarchy** (reporting relationships)
- **Headcount planning** (budgeted vs. filled positions)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure organizational structures in Dynamics 365 Human Resources** | https://learn.microsoft.com/en-us/training/modules/configure-organizational-structures-dyn365-hr/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Organization hierarchies | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-organization-hierarchy |
| Departments, jobs, and positions | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-personnel-departments-jobs-positions |
| Set up positions | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-personnel-set-up-positions |
| Set up jobs | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-personnel-set-up-jobs |
| Organization administration overview | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/organization-administration-home-page |
| Plan organizational hierarchy | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/plan-organizational-hierarchy |
| Create operating units | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/tasks/create-operating-unit |
| Number sequences | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/number-sequence-overview |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Legal entities | Organization administration > Organizations > Legal entities | Company definitions |
| Organization hierarchy purposes | Organization administration > Organizations > Organization hierarchy purposes | Purpose types (reporting, budget, etc.) |
| Global address book | Organization administration > Global address book | Party records |

### Phase 2: Organizational Units

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Departments | Human resources > Departments | Organizational departments |
| Cost centers | General ledger > Chart of accounts > Dimensions > Cost centers | Financial organizational units |
| Business units | Organization administration > Organizations > Business units | Business segments |
| Teams | Organization administration > Organizations > Teams | Cross-functional teams |

### Phase 3: Jobs & Positions

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Job functions | Human resources > Jobs > Job functions | Functional classification |
| Job types | Human resources > Jobs > Job types | Type classification |
| Jobs | Human resources > Jobs > Jobs | Job catalog (template) |
| Compensation regions | Human resources > Compensation > Regions | Geographic comp zones |
| Positions | Human resources > Positions > Positions | Specific role instances |
| Position assignments | (Within position) > Worker assignment | Assign workers to positions |

### Phase 4: Hierarchies & Reporting

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Organization hierarchies | Organization administration > Organizations > Organization hierarchies | Build hierarchy trees |
| Position hierarchy | Human resources > Positions > Position hierarchy | Manager-report structure |
| Publish hierarchy | (Within hierarchy) > Publish | Activate hierarchy |
| Headcount analysis | Human resources > Positions > Open positions | Budgeted vs. filled |

---

## Organization Structure Model

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   ORGANIZATION STRUCTURE MODEL                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  HIERARCHY PURPOSES                                                      │
│  ┌───────────────────────────────────────────────────────────┐          │
│  │ Reporting │ Budget Control │ Security │ Procurement │ HR    │          │
│  └───────────────────────────────────────────────────────────┘          │
│                                                                          │
│  LEGAL ENTITY                                                            │
│  └── Business Unit                                                       │
│       └── Department                                                     │
│            └── Cost Center                                               │
│                 └── Team                                                  │
│                                                                          │
│  JOB → POSITION MODEL                                                    │
│  ┌────────────────────────────────────────────────────────┐             │
│  │                                                          │             │
│  │  JOB (Template)                POSITION (Instance)       │             │
│  │  ┌──────────────────┐         ┌──────────────────┐      │             │
│  │  │ "Accountant"      │  ──▶   │ "Sr. Accountant   │      │             │
│  │  │  • Job function   │         │  - Finance Dept"  │      │             │
│  │  │  • Job type        │         │  • Department     │      │             │
│  │  │  • Compensation    │         │  • Reports to     │      │             │
│  │  │    zone            │         │  • Worker: J.Doe  │      │             │
│  │  │  • Skills required │         │  • Start/End date │      │             │
│  │  └──────────────────┘         └──────────────────┘      │             │
│  │                                                          │             │
│  │  One Job ──  many Positions                              │             │
│  │  One Position ── one Worker (at a time)                  │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
│  POSITION HIERARCHY (Reporting Lines)                                    │
│  ┌────────────────────────────────────────────────────────┐             │
│  │           CFO                                            │             │
│  │          /   \                                           │             │
│  │    Controller  Treasury Mgr                              │             │
│  │      / | \         |                                     │             │
│  │  AP Mgr AR Mgr GL Mgr  Cash Mgr                        │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `OMOrganizationHierarchies` | Organization hierarchies | Organizations |
| `HcmDepartment` | Departments | Organizations |
| `HcmJob` | Jobs | HR Setup |
| `HcmPosition` | Positions | HR Setup |
| `HcmPositionHierarchy` | Position hierarchy | HR Setup |
| `OMOperatingUnit` | Operating units | Organizations |
| `DirPartyTable` | Global address book | Setup |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Legal entities** must exist before departments and operating units
2. **Hierarchy purposes** must be defined before building hierarchies
3. **Jobs** (templates) must be created before positions
4. **Departments** must exist before positions can be assigned to them
5. **Positions** must exist before workers can be assigned
6. **Hierarchies must be published** to take effect
7. **Position hierarchy** drives manager self-service and approval workflows

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Position already filled" | Worker assignment overlap | End current assignment first |
| "Hierarchy not published" | Changes not activated | Publish the hierarchy |
| "No reporting line" | Position has no parent position | Assign reports-to position |
| "Department not in hierarchy" | Department not added to org hierarchy | Add to hierarchy and publish |
| "Job not found" | Job not created before position | Create job first, then position |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Organization Management** module.

### Hire to retire

*154 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze HR programs | 14 | — |
| Develop people strategy | 20 | — |
| Manage compensation and benefits | 29 | — |
| Manage performance and growth | 39 | — |
| Manage time and attendance | 6 | — |
| Manage workplace compliance | 16 | — |
| Offboard talent | 12 | — |
| Recruit and onboard talent | 18 | — |

