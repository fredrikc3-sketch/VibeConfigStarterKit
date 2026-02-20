# Cloud & On-Premises Deployment Module - Knowledge Source

> This file is the central knowledge hub for **Cloud & On-Premises Deployment** within Dynamics 365 Finance & Operations Administration.

---


---


> **Microsoft Learn Reference:** [Cloud & On-Premises Deployment](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/deployment/choose-deployment-type)

## Module Overview

Dynamics 365 Finance & Operations supports both cloud-hosted and on-premises deployment options. Cloud deployment leverages Microsoft Azure infrastructure with automatic updates, scalability, and disaster recovery. On-premises deployment runs in a customer's own data center using Azure Service Fabric, for scenarios requiring data sovereignty or regulatory compliance.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Cloud Deployment** | Azure-hosted environments with Microsoft-managed infrastructure and updates |
| **On-Premises Deployment** | Self-hosted environments using Azure Service Fabric for data sovereignty needs |
| **Environment Provisioning** | Automate creation of development, sandbox, and production environments |
| **Update Management** | Manage service updates, quality updates, and hotfixes |
| **Data Management** | Import/export data across environments using the Data Management Framework |
| **Disaster Recovery** | Built-in high availability and disaster recovery for cloud deployments |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Deployment configuration is managed through Lifecycle Services (LCS) and environment provisioning, not through data migration entities.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Deployment-related business process areas:
- **Environment lifecycle management** (provisioning, deployment, updates)
- **Infrastructure management** (cloud vs. on-premises topology)
- **Service updates** (One Version, quality updates, proactive updates)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Deploy Dynamics 365 Finance and Operations apps** | https://learn.microsoft.com/en-us/training/paths/deploy-finance-operations-apps/ |
| Understand the deployment options | https://learn.microsoft.com/en-us/training/modules/deploy-dynamics-365-finance-operations/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Deployment overview | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/deployment/choose-deployment-type |
| Cloud deployment overview | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/deployment/cloud-deployment-overview |
| On-premises deployment | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/deployment/on-premises-deployment-landing-page |
| One Version service updates | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/oneversion-overview |
| Environment planning | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/organization-administration/environment-planning |
| Sandbox environments | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/deployment/sandbox-environments |
| Production environment deployment | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/deployment/deploy-production-environment |
| Database movement operations | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/database/dbmovement-operations |
| Service update availability | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/get-started/public-preview-releases |
| Continuous updates FAQ | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/faq-continuous-updates |

---

## Environment Types

| Environment | Purpose | Provisioned Via |
|-------------|---------|-----------------|
| **Development / Build** | Code development, unit testing | LCS / Azure DevOps |
| **Tier-1 (Dev/Test)** | Development and testing | LCS cloud-hosted or Microsoft-managed |
| **Tier-2+ (Sandbox)** | UAT, performance testing, training | LCS (Microsoft-managed) |
| **Production** | Live business operations | LCS (Microsoft-managed) |
| **On-Premises** | Local data center deployment | Local Business Data (LBD) |

---

## Cloud vs. On-Premises Comparison

| Feature | Cloud | On-Premises |
|---------|-------|-------------|
| **Hosting** | Microsoft Azure (managed) | Customer data center |
| **Updates** | Automatic (One Version) | Customer-managed |
| **LCS project type** | Implementation / cloud | On-premises implementation |
| **Database** | Azure SQL | SQL Server |
| **Availability** | Microsoft SLA | Customer-managed |
| **Cost model** | Subscription (SaaS) | License + infrastructure |
| **Extensibility** | Cloud-only features available | Subset of features |
| **Telemetry** | Full Microsoft telemetry | Limited |

---

## Deployment Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    DEPLOYMENT LIFECYCLE FLOW                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. ENVIRONMENT PLANNING                                                 │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Select deployment type (cloud / on-premises)           │          │
│     │ • Plan environment topology (dev, sandbox, prod)         │          │
│     │ • Estimate capacity and subscription requirements        │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  2. PROVISIONING                                                         │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Create LCS project                                     │          │
│     │ • Configure Azure connector (cloud)                      │          │
│     │ • Deploy sandbox environment(s)                          │          │
│     │ • Deploy production environment                          │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  3. CONFIGURATION & DATA MIGRATION                                       │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Apply configuration packages                           │          │
│     │ • Migrate master data via DMF                            │          │
│     │ • Deploy customizations (deployable packages)            │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  4. GO-LIVE & OPERATIONS                                                 │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Go-live readiness review (LCS)                         │          │
│     │ • Production cutover                                     │          │
│     │ • Monitor via LCS diagnostics & Azure Monitor            │          │
│     │ • Apply service updates on schedule                      │          │
│     └────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Configuration Areas

| Area | Tool | Purpose |
|------|------|---------|
| LCS project | Lifecycle Services portal | Environment management, deployments |
| Azure connector | LCS > Project settings | Link Azure subscription for cloud-hosted |
| Deployable packages | LCS > Asset library | Custom code and ISV packages |
| Database operations | LCS > Environment actions | Point-in-time restore, refresh, export |
| Service updates | LCS > Update settings | Pause windows, update schedule |
| Environment monitoring | LCS > Environment monitoring | Performance, batch jobs, SQL insights |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **LCS project** must be created and configured before any environment can be deployed
2. **Azure subscription** must be linked for cloud-hosted development environments
3. **Sandbox environments** should be fully tested before production deployment
4. **Go-live readiness** must pass LCS review before production can be used
5. **Service updates** must be applied within the Microsoft-defined cadence (pauses limited)
6. **Database refresh** from production to sandbox requires environment to be stopped
7. **Deployable packages** must be validated on sandbox before applying to production

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Environment provisioning failed" | Azure subscription quota or region issue | Check Azure quotas and region availability |
| "Package deployment failed" | Code compilation errors or dependency issues | Review package logs in LCS |
| "Database refresh timeout" | Large database or network issues | Retry or contact Microsoft support |
| "Service update blocked" | Customization incompatibility | Fix blocking issues, run regression tests |
| "Go-live review not passed" | Missing prerequisites | Complete LCS go-live checklist |
