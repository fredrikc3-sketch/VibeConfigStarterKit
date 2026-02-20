# Lifecycle Services (LCS) Module - Knowledge Source

> This file is the central knowledge hub for **Lifecycle Services (LCS)** within Dynamics 365 Finance & Operations Administration.

---


---


> **Microsoft Learn Reference:** [Lifecycle Services](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/lcs)

## Module Overview

Lifecycle Services (LCS) is a collaborative workspace that Microsoft, partners, and customers use to manage Dynamics 365 Finance & Operations projects. It provides tools for project management, environment provisioning, code deployment, issue tracking, and business process modeling. Note: LCS is being deprecated in favor of Power Platform admin center and Dynamics 365 Lifecycle services integration.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Project Management** | Manage implementation projects with timelines, milestones, and team collaboration |
| **Environment Management** | Provision, deploy, and manage sandbox and production environments |
| **Code Deployment** | Deploy application updates, hotfixes, and customizations to environments |
| **Business Process Modeler** | Model and document business processes with task recordings |
| **Issue Search & Support** | Search knowledge base and create support incidents |
| **Asset Library** | Store and manage project assets like data packages, process diagrams, and scripts |
| **System Diagnostics** | Monitor environment health and diagnose issues |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** LCS is a management portal, not configured through data entities.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key LCS-related business process areas:
- **Implementation project management** (methodology, task tracking)
- **Environment management** (provisioning, monitoring, operations)
- **Asset management** (packages, BPM libraries, data assets)
- **Issue tracking** (support incidents, diagnostic tools)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Work with Lifecycle Services for Dynamics 365 Finance and Operations** | https://learn.microsoft.com/en-us/training/paths/work-lifecycle-services-dynamics-365-finance-operations/ |
| Navigate Lifecycle Services | https://learn.microsoft.com/en-us/training/modules/navigate-lifecycle-services/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| LCS overview | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/lcs |
| LCS project types | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/project-types |
| Business process modeler (BPM) | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/bpm-overview |
| Asset library | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/asset-library |
| Environment monitoring | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/monitoring-diagnostics |
| Issue search | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/issue-search-lcs |
| Configuration manager | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/configuration-manager-lcs |
| Database movement | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/database/dbmovement-operations |
| Subscription estimator | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/subscription-estimator |
| Go-live for implementation projects | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/go-live-faq |

---

## LCS Key Features

| Feature | Description | Access Path |
|---------|-------------|-------------|
| **Project dashboard** | Overview of implementation project status | LCS > Project home |
| **Methodology** | Implementation phases and task tracking | LCS > Methodology |
| **Environments** | Deploy, manage, monitor environments | LCS > Cloud-hosted environments |
| **Asset library** | Store deployable packages, data packages, BPM | LCS > Asset library |
| **Business process modeler** | Document and analyze business processes | LCS > Business process modeler |
| **Issue search** | Search known issues and hotfixes | LCS > Issue search |
| **Subscription estimator** | Estimate hardware/capacity needs | LCS > Subscription estimator |
| **System diagnostics** | Automated health checks | LCS > System diagnostics |
| **Environment monitoring** | Performance, SQL, batch monitoring | LCS > Environment > Monitoring |
| **Database movement** | Refresh, export, import, point-in-time restore | LCS > Environment > Database |

---

## LCS Implementation Methodology Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   LCS IMPLEMENTATION METHODOLOGY                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐│
│  │ ANALYZE   │─▶│ DESIGN   │─▶│ DEVELOP  │─▶│ DEPLOY   │─▶│ OPERATE  ││
│  │           │  │           │  │           │  │           │  │           ││
│  │• Fit/gap  │  │• Solution │  │• Build    │  │• UAT      │  │• Go-live ││
│  │• Process  │  │  design   │  │• Configure│  │• Data     │  │• Support ││
│  │  review   │  │• Data     │  │• Integrate│  │  migration│  │• Updates ││
│  │• BPM      │  │  model    │  │• Test     │  │• Cutover  │  │• Monitor ││
│  │  library  │  │• Security │  │           │  │• Go-live  │  │           ││
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  └──────────┘│
│                                                                          │
│  Cross-cutting: Environment management, Issue tracking, Asset library    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Asset Library Categories

| Asset Type | Description | Use |
|-----------|-------------|-----|
| **Software deployable package** | Custom code packages | Deploy to environments |
| **Data package** | DMF data packages | Data migration |
| **BPM library** | Business process libraries | Process documentation |
| **GER configuration** | Electronic reporting formats | Regulatory reporting |
| **Process data package** | Test automation data | RSAT testing |
| **NuGet package** | Development dependencies | Build automation |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **LCS project** must be created before any environments or assets
2. **Azure AD tenant** must be associated with the LCS project
3. **Users** must be added to the LCS project with appropriate roles
4. **Subscription estimator** should be completed before production deployment
5. **Methodology phases** should be tracked to enable go-live readiness
6. **Asset library** packages must be uploaded before they can be deployed
7. **Sandbox validation** must complete before production package deployment

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Cannot deploy to production" | Go-live readiness not complete | Complete LCS go-live checklist |
| "Package validation failed" | Incompatible or corrupt package | Rebuild and re-upload package |
| "User not authorized" | Missing LCS project role | Add user role in LCS project settings |
| "Subscription estimator incomplete" | Missing transaction line data | Complete the subscription estimator |
| "Environment action blocked" | Another operation in progress | Wait for current operation to complete |
