# Employee Self Service Module - Knowledge Source

> This file is the central knowledge hub for **Employee Self Service** within Dynamics 365 Human Resources.

---


---


> **Microsoft Learn Reference:** [Employee Self Service](https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-employee-self-service-workspace)

## Module Overview

Employee Self Service (ESS) in Dynamics 365 Human Resources provides employees a self-service portal to manage their personal information, view pay statements, request leave, enroll in benefits, update emergency contacts, and access company information without requiring HR department involvement.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Personal Information** | View and update personal details, addresses, and emergency contacts |
| **Leave Requests** | Submit, track, and manage time-off requests |
| **Benefits Enrollment** | Enroll in available benefit plans during open enrollment or life events |
| **Pay Statements** | View pay stubs and compensation history |
| **Tax Information** | Update tax withholding forms and view tax documents |
| **Skills & Certifications** | Maintain personal skills, education, and certification records |
| **Company Information** | Access company policies, announcements, and directories |
| **Task Management** | Complete assigned onboarding and compliance tasks |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Employee Self Service is a workspace/portal configuration, not a data-heavy setup.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Employee Self Service-related business process areas:
- **Personal information management** (address, contacts, bank accounts)
- **Benefits enrollment** (self-service plan selection)
- **Leave requests** (time-off requests and balances)
- **Performance reviews** (goal setting, self-assessment)
- **Learning & training enrollment** (course sign-up)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure employee and manager self service** | https://learn.microsoft.com/en-us/training/modules/configure-employee-manager-self-service-dyn365-hr/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Employee self service overview | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-employee-self-service-overview |
| Manager self service overview | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-employee-manager-self-service-overview |
| Employee self service workspace | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-employee-self-service-workspace |
| Personal information management | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-employee-self-service-manage-personal-info |
| Buy and sell leave | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-employee-self-service-buy-sell-leave |
| Restrict editing of personal info | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-employee-self-service-restrict-editing |
| Custom links in self service | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-employee-self-service-custom-links |

---

## 3-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Security roles assigned | System administration > Security > Assign users to roles | ESS/MSS role assignment |
| Worker records | Human resources > Workers | All employees must have records |
| Benefits plans configured | Benefits management > Plans | For benefits enrollment |
| Leave plans configured | Leave and absence > Leave plans | For leave requests |

### Phase 2: Workspace Configuration

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Employee self service parameters | Human resources > Setup > Human resources parameters > Employee self service | Feature toggles |
| Personal info editable fields | (Within HR parameters) > Restrict personal info editing | Control which fields employees can edit |
| Custom links | (Within HR parameters) > Custom links | Add links to ESS workspace |
| Document types | Document management > Document types | Attach certifications, documents |
| Workflow for changes | System administration > Workflow | Approval for address/bank changes |

### Phase 3: Manager Self Service

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Manager workspace configuration | Human resources > Setup > Human resources parameters > Manager self service | Manager view settings |
| Team performance visibility | (Within HR parameters) | Goals and reviews access |
| Pending approvals | (Via manager workspace) | Leave, expense, other approvals |

---

## Employee & Manager Self Service Features

```
┌─────────────────────────────────────────────────────────────────────────┐
│              EMPLOYEE & MANAGER SELF SERVICE                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  EMPLOYEE SELF SERVICE (ESS)                                             │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ Personal Information                                      │             │
│  │  • Address, phone, email changes                          │             │
│  │  • Emergency contacts                                     │             │
│  │  • Bank accounts (direct deposit)                         │             │
│  │  • Tax withholding (W-4)                                  │             │
│  │                                                           │             │
│  │ Benefits                                                  │             │
│  │  • View current elections                                 │             │
│  │  • Open enrollment selection                              │             │
│  │  • Life event changes                                     │             │
│  │                                                           │             │
│  │ Time & Leave                                              │             │
│  │  • Submit leave requests                                  │             │
│  │  • View leave balances                                    │             │
│  │  • Buy/sell leave                                         │             │
│  │                                                           │             │
│  │ Performance                                               │             │
│  │  • View/update goals                                      │             │
│  │  • Complete self-assessment                               │             │
│  │                                                           │             │
│  │ Learning                                                  │             │
│  │  • Enroll in courses                                      │             │
│  │  • View training history                                  │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
│  MANAGER SELF SERVICE (MSS)                                              │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ Team Overview                                             │             │
│  │  • Direct reports list                                    │             │
│  │  • Organization chart                                     │             │
│  │                                                           │             │
│  │ Approvals                                                 │             │
│  │  • Leave requests                                         │             │
│  │  • Expense reports                                        │             │
│  │  • Personal info changes                                  │             │
│  │                                                           │             │
│  │ Team Performance                                          │             │
│  │  • Review team goals                                      │             │
│  │  • Complete manager reviews                               │             │
│  │  • Compensation recommendations                           │             │
│  │                                                           │             │
│  │ HR Actions                                                │             │
│  │  • Position changes                                       │             │
│  │  • Transfer requests                                      │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `HcmEmployeeSelfService` | Employee self service | Workspace |
| `HcmManagerSelfService` | Manager self service | Workspace |
| `HcmPersonalInfo` | Personal information | ESS |
| `HcmBenefitEnrollment` | Benefits enrollment | ESS |
| `HcmLeaveRequest` | Leave requests | ESS |
| `HcmPerformanceGoals` | Goals | Performance |
| `HRMParameters` | Human resources parameters | Setup |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Security roles** (Employee/Manager) must be assigned for workspace access
2. **HR parameters** must configure self-service features before employees can use them
3. **Benefits and leave plans** must be configured before self-service enrollment works
4. **Workflow approvals** should be set up for sensitive changes (bank account, address)
5. **Restrict personal info editing** settings should be reviewed for compliance
6. **Manager hierarchy** must be correct for manager self service to show correct reports

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No workspace access" | ESS security role not assigned | Assign Employee self service role |
| "Cannot edit field" | Field restricted in HR parameters | Update restriction settings |
| "Leave request rejected" | No leave balance or manager not assigned | Check balance and reporting line |
| "Benefits not visible" | Not in enrollment period or not eligible | Verify enrollment window and eligibility |
| "Manager sees no reports" | Organization hierarchy incorrect | Fix reporting line in position hierarchy |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Employee Self Service** module.

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

