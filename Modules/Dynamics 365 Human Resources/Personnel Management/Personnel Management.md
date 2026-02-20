# Personnel Management Module - Knowledge Source

> This file is the central knowledge hub for **Personnel Management** within Dynamics 365 Human Resources.

---


---


> **Microsoft Learn Reference:** [Personnel Management](https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-personnel-departments-jobs-positions)

## Module Overview

Personnel Management in Dynamics 365 Human Resources manages the core employee lifecycle including worker records, positions, departments, job classifications, employment history, and worker onboarding/offboarding. It forms the foundation for all other HR modules.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Worker Management** | Create and maintain worker records with personal and employment details |
| **Position Management** | Define positions, reporting relationships, and position hierarchies |
| **Department Management** | Create and manage organizational departments |
| **Job Classification** | Define jobs, job types, job functions, and compensation structures |
| **Onboarding** | Manage new hire onboarding tasks and checklists |
| **Offboarding** | Process worker separations with exit procedures |
| **Worker History** | Track employment history, transfers, and status changes |
| **Loaned Equipment** | Track company equipment assigned to workers |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Personnel management uses dedicated worker and employment forms in Human Resources.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Personnel Management-related business process areas:
- **Worker lifecycle** (hire, transfer, terminate)
- **Employment records** (employment history, employment types)
- **Worker personal data** (demographics, addresses, contacts)
- **Compensation management** (fixed/variable compensation)
- **Task management** (onboarding/offboarding checklists)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Manage personnel in Dynamics 365 Human Resources** | https://learn.microsoft.com/en-us/training/paths/manage-personnel-dyn365-hr/ |
| Configure compensation | https://learn.microsoft.com/en-us/training/modules/configure-compensation-dyn365-hr/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Personnel management workspace | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-personnel-workspace |
| Workers overview | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-personnel-workers |
| Hire new workers | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-personnel-recruit |
| Worker personal information | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-personnel-manage-personal-info |
| Employment history | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-personnel-employment-history |
| Fixed compensation plans | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-compensation-fixed-plans |
| Variable compensation plans | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-compensation-variable-plans |
| Compensation process | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-compensation-process |
| Task management (checklists) | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-task-mgmt |
| Mass hire projects | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-personnel-mass-hire |
| Termination and offboarding | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-personnel-terminate-worker |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| HR parameters | Human resources > Setup > Human resources parameters | Module settings |
| Legal entities | Organization administration > Organizations > Legal entities | Employment companies |
| Departments | Human resources > Departments | Org structure |
| Jobs and positions | Human resources > Jobs / Positions | Role definitions |
| Number sequences | (Within HR parameters) | Personnel numbers |

### Phase 2: Compensation Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Compensation regions | Human resources > Compensation > Compensation regions | Geographic pay zones |
| Compensation levels | Human resources > Compensation > Compensation levels | Grade/band structure |
| Compensation grids | Human resources > Compensation > Compensation grids | Pay ranges per level |
| Fixed compensation plans | Human resources > Compensation > Fixed plans | Salary structure |
| Variable compensation plans | Human resources > Compensation > Variable plans | Bonus/incentive plans |
| Eligibility rules | (Within compensation plan) > Eligibility | Comp plan eligibility |

### Phase 3: Worker Lifecycle - Hire

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Create worker | Human resources > Workers > New worker | New hire record |
| Employment details | (Within worker) > Employment | Employment type, dates |
| Position assignment | (Within worker) > Position | Assign to position |
| Fixed compensation enrollment | (Within worker) > Compensation > Fixed plan | Set base pay |
| Onboarding checklist | (Within worker) > Task management | Onboarding tasks |

### Phase 4: Worker Lifecycle - Maintain

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Transfer worker | (Within worker) > Employment > Transfer | Department/position change |
| Compensation change | Human resources > Compensation > Process events | Merit, promotion adjustments |
| Personal information updates | (Within worker or ESS) | Address, contact, dependents |
| Mass hire | Human resources > Workers > Mass hire projects | Bulk hiring |
| Loaned workers | Human resources > Workers > Loaned workers | Inter-company lending |

### Phase 5: Worker Lifecycle - Terminate

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Terminate worker | (Within worker) > Terminate | End employment |
| Offboarding checklist | (Within worker) > Task management | Offboarding tasks |
| Final compensation | (Payroll processing) | Final pay calculation |
| Benefits termination | (Automatic via life event) | End benefit elections |

---

## Worker Lifecycle Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     WORKER LIFECYCLE FLOW                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────┐    ┌────────────┐    ┌──────────────┐    ┌─────────────┐│
│  │  RECRUIT  │ →  │   HIRE      │ →  │  ONBOARD      │ →  │  PRODUCTIVE  ││
│  │           │    │             │    │               │    │             ││
│  │ • Job     │    │ • Create    │    │ • Checklist   │    │ • Day-to-day││
│  │   posting │    │   worker    │    │ • IT setup    │    │   work      ││
│  │ • Screen  │    │ • Position  │    │ • Benefits    │    │ • Goals     ││
│  │ • Offer   │    │ • Comp plan │    │   enrollment  │    │ • Training  ││
│  └──────────┘    └────────────┘    └──────────────┘    └──────┬──────┘│
│                                                                │       │
│                              ┌──────────────────────────────────┘       │
│                              ▼                                          │
│  ┌──────────────────────────────────────────────────────────────┐      │
│  │                    EMPLOYMENT EVENTS                           │      │
│  │  ┌─────────┐  ┌───────────┐  ┌──────────┐  ┌─────────────┐  │      │
│  │  │ Transfer │  │ Promotion  │  │Comp Change│  │ Leave of    │  │      │
│  │  │ (dept,   │  │ (position  │  │ (merit,   │  │ Absence     │  │      │
│  │  │  legal   │  │  change)   │  │  market)  │  │ (FMLA, etc.)│  │      │
│  │  │  entity) │  │            │  │           │  │             │  │      │
│  │  └─────────┘  └───────────┘  └──────────┘  └─────────────┘  │      │
│  └──────────────────────────────────────────────────────────────┘      │
│                              │                                          │
│                              ▼                                          │
│  ┌──────────────┐    ┌──────────────┐                                  │
│  │  TERMINATE    │ →  │  OFFBOARD     │                                  │
│  │               │    │               │                                  │
│  │ • End date    │    │ • Checklist   │                                  │
│  │ • Reason code │    │ • Final pay   │                                  │
│  │ • Position    │    │ • Benefits    │                                  │
│  │   vacated     │    │   termination │                                  │
│  └──────────────┘    └──────────────┘                                  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `HcmPersonnelWorkspace` | Personnel management | Workspace |
| `HcmWorkerListPage` | Workers | Workers |
| `HcmWorkerNewWorker` | Hire new worker | Workers |
| `HcmCompFixedEmpl` | Fixed compensation | Compensation |
| `HcmCompVarEmpl` | Variable compensation | Compensation |
| `HcmCompProcess` | Compensation process events | Compensation |
| `HcmTaskManagement` | Task management | Checklists |
| `HcmMassHireProject` | Mass hire projects | Workers |
| `HcmWorkerTerminate` | Terminate worker | Workers |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Legal entity and department** must exist before hiring
2. **Jobs and positions** must be created before worker-position assignment
3. **Compensation plans** must be configured before enrolling workers
4. **Compensation grids** must have appropriate ranges for the compensation level
5. **Position must be active** to assign a worker
6. **Onboarding checklists** should be configured before first hire arrives
7. **Termination** triggers benefits life event processing automatically

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Position already occupied" | Overlapping assignments | End current assignment first |
| "Compensation out of range" | Pay exceeds grid min/max | Adjust grid or request exception |
| "Worker number duplicate" | Number sequence conflict | Reset number sequence |
| "Cannot terminate" | Active leave or pending transactions | Complete leave and transactions first |
| "Onboarding tasks not created" | Checklist template not assigned | Configure task management template |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Personnel Management** module.

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

