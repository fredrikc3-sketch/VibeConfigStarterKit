# Leave & Absence Management Module - Knowledge Source

> This file is the central knowledge hub for **Leave & Absence Management** within Dynamics 365 Human Resources.

---


---


> **Microsoft Learn Reference:** [Leave & Absence Management](https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-leave-and-absence-overview)

## Module Overview

Leave & Absence Management in Dynamics 365 Human Resources tracks employee time-off including vacation, sick leave, family leave, and custom leave types. It supports accrual plans, leave requests with workflow approval, leave balances, calendar integration, and compliance with regional leave regulations.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Leave Plans** | Define leave types and accrual policies (vacation, sick, PTO, etc.) |
| **Leave Requests** | Employee self-service leave requests with manager approval workflow |
| **Accrual Processing** | Calculate leave accruals based on tenure, employment date, or custom rules |
| **Leave Balances** | View real-time leave balances and usage by employee |
| **Leave Calendar** | Visual calendar showing team absences for planning |
| **Buy & Sell Leave** | Allow employees to buy additional leave or sell unused days |
| **Compliance** | Support regional leave regulations and statutory requirements |
| **Leave Suspension** | Suspend accruals during leave of absence or other situations |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Leave and absence configuration uses dedicated setup forms within Human Resources.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Leave & Absence-related business process areas:
- **Leave types** (vacation, sick, FMLA, personal)
- **Leave plans** (accrual rules and entitlements)
- **Leave requests** (employee submission and approval)
- **Leave calendar** (team absence visibility)
- **Buy and sell leave** (policy-based leave transactions)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure leave and absence in Dynamics 365 Human Resources** | https://learn.microsoft.com/en-us/training/modules/configure-leave-absence-dyn365-hr/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Leave and absence overview | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-leave-and-absence-overview |
| Leave and absence types | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-leave-and-absence-types |
| Leave and absence plans | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-leave-and-absence-plans |
| Leave and absence accrual | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-leave-and-absence-accrue |
| Leave and absence parameters | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-leave-and-absence-parameters |
| Buy and sell leave policies | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-leave-and-absence-buy-sell |
| Leave calendar | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-employee-self-service-calendar |
| Leave request workflow | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-leave-and-absence-workflow |
| Leave of absence (FMLA) | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-leave-and-absence-manage-leave-of-absence |
| Working time calendars | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-leave-and-absence-working-time-calendar |
| Suspend leave (carry forward) | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-leave-and-absence-suspend-leave |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Leave and absence parameters | Human resources > Setup > Leave and absence parameters | Module-level settings |
| Working time calendars | Organization administration > Working time calendars | Work day definitions |
| Workers | Human resources > Workers | Eligible employees |
| Number sequences | (Within parameters) | Leave request numbers |

### Phase 2: Leave Types & Plans

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Leave types | Leave and absence > Links > Leave types | Vacation, sick, personal, FMLA |
| Reason codes | Leave and absence > Links > Reason codes | Leave request reasons |
| Leave plans | Leave and absence > Links > Leave and absence plans | Accrual rules per type |
| Accrual schedules | (Within leave plan) > Accrual schedule | Frequency (monthly, biweekly, etc.) |
| Tier rules | (Within leave plan) > Tiers | Accrual by seniority |
| Plan rules | (Within leave plan) > Rules | Carry forward, minimum balance |

### Phase 3: Enrollment & Policies

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Enroll workers | Leave and absence > Links > Enroll workers | Assign plans to workers |
| Accrue leave | Leave and absence > Links > Accrue leave balances | Run accrual process |
| Buy and sell leave policies | Leave and absence > Links > Buy and sell leave policies | Allow leave purchase/sell |
| Leave of absence configuration | Leave and absence > Links > Leave of absence | FMLA and extended leave |
| Workflow configuration | System administration > Workflow > Leave request | Approval flow |

### Phase 4: Ongoing Operations

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Leave requests (employee) | Employee self service > Leave requests | Submit time-off requests |
| Leave approval (manager) | Manager self service > My team > Leave requests | Approve/reject requests |
| Leave calendar | Leave and absence > Calendar | Team absence visibility |
| Adjust balances | Leave and absence > Workers > (worker) > Adjust balance | Manual correction |

---

## Leave & Absence Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    LEAVE & ABSENCE FLOW                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  SETUP                                                                   │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ Leave Types → Leave Plans → Accrual Rules → Enrollment   │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  ACCRUAL PROCESSING                                                      │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Scheduled accrual (batch job)                          │             │
│  │ • Balance accumulation per plan                          │             │
│  │ • Carry forward at year-end (per rules)                  │             │
│  │ • Expiration of unused leave                             │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  LEAVE REQUESTS                                                          │
│  ┌────────────────────────────────────────────────────────┐             │
│  │                                                          │             │
│  │  Employee             Manager               HR            │             │
│  │  ┌─────────┐         ┌──────────┐         ┌───────┐     │             │
│  │  │ Submit   │ ──────▶ │ Approve / │ ──────▶ │ Track │     │             │
│  │  │ Request  │         │ Reject    │         │       │     │             │
│  │  └─────────┘         └──────────┘         └───────┘     │             │
│  │                                                          │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  PAYROLL & CALENDAR                                                      │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Leave balances reflected in payroll                     │             │
│  │ • Team calendar shows absences                            │             │
│  │ • Compliance reporting (FMLA tracking)                    │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `HcmLeaveAbsenceWorkspace` | Leave and absence | Workspace |
| `HcmLeaveType` | Leave types | Setup |
| `HcmLeavePlan` | Leave and absence plans | Setup |
| `HcmLeaveAccrue` | Accrue leave balances | Processing |
| `HcmLeaveRequest` | Leave requests | Transactions |
| `HcmLeaveCalendar` | Leave calendar | Views |
| `HcmLeaveBuySell` | Buy and sell leave | Policies |
| `HcmLeaveAbsenceParameters` | Leave and absence parameters | Setup |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Parameters** must be configured before creating leave types
2. **Leave types** must exist before creating leave plans
3. **Leave plans** with accrual rules must be defined before worker enrollment
4. **Workers must be enrolled** in plans before accrual processing
5. **Accrual processing** must be run (batch job) to generate balances
6. **Workflow** must be activated for leave request approval
7. **Working time calendar** must be assigned to workers for accurate day calculation

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Insufficient balance" | Accrual not run or balance depleted | Run accrual or check balance |
| "Leave request pending" | No workflow or manager not assigned | Configure workflow and reporting line |
| "Accrual not processing" | Worker not enrolled in plan | Enroll worker in leave plan |
| "Incorrect days calculated" | Working time calendar missing | Assign working time calendar |
| "Carry forward not applied" | Plan rules not configured | Set carry forward rules in plan |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Leave & Absence Management** module.

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

