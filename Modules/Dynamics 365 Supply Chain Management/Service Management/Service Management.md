# Service Management Module - Knowledge Source

> This file is the central knowledge hub for **Service Management** within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Service Management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/service-management-home-page)

## Module Overview

The Service Management module in Dynamics 365 Supply Chain Management supports after-sales service operations including service agreements, service orders, repair management, and service level tracking. It enables organizations to manage service delivery for products sold to customers.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Service Agreements** | Define recurring service contracts with billing and renewal terms |
| **Service Orders** | Create and dispatch service orders for on-site or depot repair |
| **Repair Management** | Track repair processes from receipt through return to customer |
| **Service Objects** | Register customer-owned items for service tracking (serialized assets) |
| **Service Tasks** | Define standard service tasks for consistent service delivery |
| **Service Level Agreements** | Track SLA compliance for response time and resolution targets |
| **Dispatch Board** | Schedule and assign service technicians to service orders |
| **Service Subscriptions** | Manage recurring service billing through subscription invoicing |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Service management configuration uses dedicated service order, agreement, and object forms.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Service Management-related business process areas:
- **Service agreements** (recurring service contracts)
- **Service orders** (individual service work orders)
- **Service objects** (customer equipment under service)
- **Service tasks** (work to be performed)
- **Repair management** (RMA and repair tracking)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Service management overview** | https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/service-management-home-page |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Service management home page | https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/service-management-home-page |
| Service agreements | https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/service-agreements |
| Service orders | https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/service-orders |
| Service objects | https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/service-objects |
| Service BOM | https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/service-bom |
| Service tasks | https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/service-tasks |
| Dispatch board | https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/dispatch-board |
| Service level agreements (SLA) | https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/service-level-agreements |
| Repair management | https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/repair-management |
| Return item (RMA) | https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/return-items |
| Subscription groups | https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/subscription-groups |
| Service intervals | https://learn.microsoft.com/en-us/dynamics365/supply-chain/service-management/service-intervals |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Service management parameters | Service management > Setup > Service management parameters | Module settings |
| Customers | Accounts receivable > Customers | Service customers |
| Products | Product information management > Products | Service items and spare parts |
| Workers (service technicians) | Human resources > Workers | Field service staff |

### Phase 2: Service Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Service object groups | Service management > Setup > Service objects > Service object groups | Classify service objects |
| Service objects | Service management > Service objects | Customer equipment records |
| Service object relations | (Within service object) > Relations | Link objects to agreements |
| Service task relations | Service management > Setup > Service orders > Service tasks | Define work activities |
| Service BOM templates | (Within service object or agreement) | Spare parts list per object |

### Phase 3: Service Agreements

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Service agreement groups | Service management > Setup > Service agreements > Service agreement groups | Agreement classification |
| Service level agreements | Service management > Setup > Service level agreements | SLA definitions (response time) |
| Service agreements | Service management > Service agreements > Service agreements | Recurring service contracts |
| Agreement lines | (Within agreement) > Lines | Scheduled service visits |
| Service intervals | Service management > Setup > Service agreements > Service intervals | Frequency of service |
| Subscription groups | Service management > Setup > Service subscriptions > Subscription groups | Recurring billing groups |

### Phase 4: Service Order Execution

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Create service orders | Service management > Service orders > Service orders > New | One-time or agreement-generated |
| Dispatch board | Service management > Periodic > Dispatch board | Assign technicians/schedule |
| Service order lines | (Within service order) > Lines | Hours, items, expenses |
| Service order stages | (Within service order) > Stage | In progress → completed |
| Service BOM consumption | (Within service order) > Objects > BOM | Parts used |

### Phase 5: Repair & Returns

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Repair management | Service management > Periodic > Repair management | Track repair items |
| Condition codes | Service management > Setup > Return orders > Condition codes | Item condition on return |
| Return orders (RMA) | Service management > Return orders | Customer returns for repair |
| Disposition codes | Service management > Setup > Return orders > Disposition codes | Repair, replace, credit |

---

## Service Management Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SERVICE MANAGEMENT FLOW                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  SERVICE AGREEMENT (Contract)                                            │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Customer: Contoso Ltd                                   │             │
│  │ • Objects: 5 × Industrial Printers                        │             │
│  │ • SLA: 4-hour response time                               │             │
│  │ • Interval: Monthly preventive maintenance                │             │
│  │ • Duration: 12 months                                     │             │
│  │ • Auto-generate service orders monthly                    │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│              ┌───────────────┼───────────────┐                           │
│              ▼                               ▼                           │
│  SCHEDULED SERVICE              BREAK-FIX / AD-HOC                      │
│  ┌──────────────────┐          ┌──────────────────┐                     │
│  │ Auto-generated    │          │ Manual service     │                     │
│  │ service order     │          │ order (customer    │                     │
│  │ (from agreement)  │          │ call / issue)      │                     │
│  └────────┬─────────┘          └────────┬─────────┘                     │
│           │                             │                                │
│           └─────────────┬───────────────┘                                │
│                         ▼                                                │
│  DISPATCH & EXECUTION                                                    │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Dispatch board: Assign technician + schedule            │             │
│  │ • Technician performs work                                │             │
│  │ • Record: Hours, parts consumed, notes                    │             │
│  │ • Update service BOM (if parts replaced)                  │             │
│  │ • Stage: Created → In Progress → Completed                │             │
│  └────────────────────────────────────────────────────────┘             │
│                         │                                                │
│              ┌──────────┼──────────┐                                     │
│              ▼                     ▼                                     │
│  INVOICING                 REPAIR / RETURN                               │
│  ┌──────────────┐         ┌───────────────────┐                         │
│  │ Invoice from  │         │ RMA created         │                         │
│  │ service order │         │ Item returned         │                         │
│  │ (T&M or       │         │ Repair tracked        │                         │
│  │  subscription)│         │ Disposition:          │                         │
│  └──────────────┘         │  Repair/Replace/Credit│                         │
│                           └───────────────────┘                         │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `SMAServiceAgreement` | Service agreements | Agreements |
| `SMAServiceOrderTable` | Service orders | Orders |
| `SMADispatchBoard` | Dispatch board | Scheduling |
| `SMAServiceObject` | Service objects | Objects |
| `SMAServiceBOM` | Service BOM | Objects |
| `SMASLATable` | Service level agreements | Setup |
| `SMARepairManagement` | Repair management | Periodic |
| `ReturnTable` | Return orders | Returns |
| `SMASubscription` | Service subscriptions | Billing |
| `SMAServiceManagementParameters` | Service management parameters | Setup |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Service management parameters** must be configured first
2. **Service objects** must be defined before they can be linked to agreements
3. **Service agreements** must exist before automatic service order generation
4. **Service intervals** control generation frequency — must be set on agreement lines
5. **Dispatch board** requires workers with correct competencies
6. **Service BOM** tracks parts history — objects must have BOM attached
7. **SLA** must be active before response time tracking applies

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Service order not generated" | Agreement line missing interval | Set service interval on agreement line |
| "SLA breach" | Response time exceeded | Review dispatch and scheduling |
| "Object not found" | Service object not created | Create and link service object |
| "Parts not available" | Spare parts not in stock | Procure or transfer inventory |
| "Return disposition missing" | Disposition code not configured | Set up disposition codes |
| "Cannot invoice" | Service order not completed | Complete service order stages first |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Service Management** module.

### Service to deliver

*43 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze service performance | 5 | — |
| Deliver services | 13 | — |
| Develop service strategy | 11 | — |
| Manage service work | 8 | — |
| Plan service work | 6 | — |

### Case to resolution

*50 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze case performance | 2 | — |
| Define customer and employee service operations | 8 | — |
| Establish a knowledge base | 4 | — |
| Intake cases | 11 | — |
| Manage and work on cases | 25 | — |

