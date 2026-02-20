# Analytics & KPI Tracking Module - Knowledge Source

> This file is the central knowledge hub for **Analytics & KPI Tracking** within Dynamics 365 Project Operations.

---


---


> **Microsoft Learn Reference:** [Analytics & KPI Tracking](https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/project-management-overview)

## Module Overview

Analytics & KPI Tracking in Dynamics 365 Project Operations provides project performance dashboards, utilization analytics, profitability analysis, and Power BI integration for data-driven decision making. It enables project managers and executives to monitor KPIs across project portfolios.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Project Dashboards** | Real-time dashboards showing project health, cost, and schedule status |
| **Utilization Analytics** | Analyze resource utilization rates across the organization |
| **Profitability Analysis** | Compare actual vs. planned margin at project and portfolio levels |
| **Power BI Reports** | Built-in and custom Power BI reports for project analytics |
| **Cost Variance Analysis** | Track variances between estimated and actual project costs |
| **Schedule Performance** | Monitor schedule variance and forecast completion dates |
| **Portfolio Overview** | Aggregate view of all projects for executive decision making |
| **Custom Metrics** | Define and track custom KPIs for organizational needs |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Analytics and KPIs are delivered through built-in dashboards, Power BI integration, and Dataverse reporting.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Analytics & KPI-related business process areas:
- **Project dashboards** (project manager and executive views)
- **Resource utilization** (billable vs. non-billable hours)
- **Financial performance** (revenue, margin, EAC analysis)
- **Power BI content packs** (project analytics, practice management)
- **Dataverse reporting** (custom reports and views)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Work with Dynamics 365 Project Operations analytics** | https://learn.microsoft.com/en-us/training/modules/project-operations-analytics/ |
| Project Operations overview | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-operations-overview |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Project Operations dashboards | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/project-dashboard |
| Resource utilization overview | https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/resource-utilization-overview |
| Practice manager dashboard | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/practice-manager-overview |
| Project cost tracking | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/project-cost-tracking |
| Project status and cost consumption | https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/project-tracking-overview |
| Financial estimates and actuals | https://learn.microsoft.com/en-us/dynamics365/project-operations/actuals/actuals-overview |
| Power BI integration | https://learn.microsoft.com/en-us/dynamics365/project-operations/environment/resource-powerbI |

---

## Key Performance Indicators (KPIs)

| KPI | Formula | Target |
|-----|---------|--------|
| **Resource Utilization** | Billable hours / Available hours × 100 | 65-80% |
| **Billing Realization** | Billed revenue / Total billable value × 100 | >90% |
| **Project Margin** | (Revenue − Cost) / Revenue × 100 | Per target by project type |
| **Estimate at Completion (EAC)** | Actual cost + Estimate to complete | ≤ Original budget |
| **Schedule Variance** | Planned completion − Forecast completion | ≤ 0 days |
| **Cost Performance Index (CPI)** | Earned value / Actual cost | ≥ 1.0 |
| **Schedule Performance Index (SPI)** | Earned value / Planned value | ≥ 1.0 |
| **Backlog** | Unrecognized contracted revenue | Healthy pipeline |
| **Revenue Recognition Rate** | Recognized revenue / Total contract value | Per completion schedule |
| **Write-off Rate** | Written off amount / Total billable | < 5% |

---

## Analytics Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   ANALYTICS & KPI ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  DATA SOURCES                                                            │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ Time Entries │ Expense │ Materials │ Invoices │ Actuals  │             │
│  └───────┬──────┴────┬────┴─────┬─────┴────┬─────┴────┬───┘             │
│          │           │          │          │          │                   │
│          └───────────┴──────────┴──────────┴──────────┘                  │
│                              │                                           │
│                              ▼                                           │
│  ACTUALS ENGINE (Dataverse)                                              │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Cost actuals                                           │             │
│  │ • Unbilled sales actuals                                 │             │
│  │ • Billed sales actuals                                   │             │
│  │ • Inter-organizational actuals                           │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│              ┌───────────────┼───────────────┐                           │
│              ▼               ▼               ▼                           │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐                │
│  │ BUILT-IN      │ │ POWER BI     │ │ CUSTOM REPORTS    │                │
│  │ DASHBOARDS    │ │ CONTENT      │ │ (Dataverse views)  │                │
│  │               │ │              │ │                    │                │
│  │ • Project     │ │ • Practice   │ │ • Ad-hoc queries   │                │
│  │   tracking    │ │   management │ │ • Excel Online     │                │
│  │ • Resource    │ │ • Resource   │ │ • SSRS reports     │                │
│  │   utilization │ │   utilization│ │   (F&O integrated) │                │
│  │ • Cost        │ │ • Financial  │ │                    │                │
│  │   consumption │ │   overview   │ │                    │                │
│  └──────────────┘ └──────────────┘ └──────────────────┘                │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Built-in Dashboards

| Dashboard | Audience | Key Metrics |
|-----------|----------|-------------|
| **Project Dashboard** | Project Manager | Cost tracking, schedule, EAC, burn rate |
| **Practice Manager** | PMO / Director | Portfolio view, utilization, revenue |
| **Resource Utilization** | Resource Manager | Availability, utilization %, capacity |
| **Cost Tracking** | Finance / PM | Budget vs. actual, CPI, variances |
| **Financial Estimates** | Finance | Revenue recognition, WIP, backlog |

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `ProjectDashboard` | Project dashboard | Views |
| `PracticeManagerOverview` | Practice manager | Views |
| `ResourceUtilization` | Resource utilization | Views |
| `ProjectCostTracking` | Cost tracking | Views |
| `ActualsListPage` | Actuals | Data |
| `PowerBIReports` | Power BI reports | Reporting |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Actuals** are generated from approved time, expense, and material entries
2. **Cost rates and bill rates** must be configured for accurate financial KPIs
3. **Project budgets** must be set for meaningful variance analysis
4. **Resource calendars** must be accurate for utilization calculations
5. **Power BI** requires Dataverse connection and appropriate security roles
6. **Approved transactions** drive all analytics — unapproved entries are excluded

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Utilization shows 0%" | Resource calendar or time entries missing | Verify calendar and approved time |
| "EAC incorrect" | Estimate to complete not updated | Refresh remaining estimates |
| "Revenue mismatch" | Actuals not generated from approvals | Approve pending time/expense entries |
| "Power BI dashboard empty" | Dataverse connection not configured | Set up Power BI connection |
| "Cost not matching GL" | Actuals vs. subledger timing | Reconcile actuals with GL postings |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Analytics & KPI Tracking** module.

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

