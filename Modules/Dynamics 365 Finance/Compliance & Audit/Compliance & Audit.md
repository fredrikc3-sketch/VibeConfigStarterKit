# Compliance & Audit Module - Knowledge Source

> This file is the central knowledge hub for **Compliance & Audit** within Dynamics 365 Finance.

---


---


> **Microsoft Learn Reference:** [Compliance & Audit](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/general-electronic-reporting)

## Module Overview

Compliance & Audit capabilities in Dynamics 365 Finance support regulatory compliance, electronic reporting, audit trails, and financial controls. Electronic Reporting (ER) enables configurable generation of regulatory documents and reports. The Audit workbench provides tools for audit policy creation, case management, and document tracking.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Electronic Reporting** | Configure and generate regulatory reports, e-invoices, and payment files |
| **Audit Policies** | Define rules to identify transactions that violate business policies |
| **Audit Workbench** | Manage audit cases, track findings, and document remediation |
| **Audit Trail** | Track changes to master data and transactions with detailed logging |
| **Segregation of Duties** | Enforce separation of incompatible business responsibilities |
| **Regulatory Updates** | Receive automatic regulatory configuration updates for localized compliance |
| **Document Management** | Attach and manage supporting documentation for transactions |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Compliance and audit features are configured through General Ledger and System Administration forms.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Compliance & Audit-related business process areas:
- **Audit trail and audit workbench** (journal audit, transaction tracing)
- **Audit policy** (automated violation detection)
- **Electronic reporting** (regulatory reporting formats)
- **Financial period close** (control and compliance steps)
- **Database logging** (entity change tracking)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure auditing policies in Dynamics 365 Finance** | https://learn.microsoft.com/en-us/training/modules/configure-audit-policies-dyn365-finance/ |
| Perform financial close in Dynamics 365 Finance | https://learn.microsoft.com/en-us/training/paths/perform-financial-close-dyn365-finance/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Audit policy rules | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/audit-policy-rules |
| Audit policy violations and cases | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/audit-policy-violations-cases |
| Audit workbench | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/audit-workbench |
| Database logging | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/configure-manage-database-log |
| Electronic reporting overview | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/general-electronic-reporting |
| Financial period close workspace | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-period-close-workspace |
| Alert rules | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/get-started/create-alerts |
| Segregation of duties | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/tasks/set-up-segregation-of-duties |
| Reason codes for audit trails | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/reason-codes-for-financial-transactions |
| Legal entity compliance | https://learn.microsoft.com/en-us/dynamics365/finance/organization-administration/plan-organizational-hierarchy |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Security roles & duties | System administration > Security | Base role definitions |
| General ledger setup | General ledger > Ledger setup | Chart of accounts, fiscal calendar |
| Workflow configuration | System administration > Workflow | Approval workflows for controls |
| Number sequences | Organization administration > Number sequences | Case and audit policy numbers |

### Phase 2: Audit Trail & Database Logging

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Database logging setup | System administration > Database logging > Setup | Track entity-level changes |
| Database log cleanup | System administration > Database logging > Clean up | Manage log size |
| Reason codes | General ledger > Journal setup > Reason codes | Require reasons for changes |
| Journal audit trail | General ledger > Inquiries > Audit trail | View journal posting history |

### Phase 3: Audit Policies

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Audit policy | General ledger > Setup > Audit > Audit policy | Define policy framework |
| Audit policy rules | (Within audit policy) > Policy rules | Define violation conditions |
| Policy rule types | General ledger > Setup > Audit > Audit policy rule type | Custom rule type definitions |
| Schedule audit policy | (Within audit policy) > Schedule | Run policies on schedule |

### Phase 4: Compliance Monitoring

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Audit workbench | General ledger > Inquiries > Audit workbench | Review and investigate violations |
| Case management | Organization administration > Cases | Manage compliance cases |
| Segregation of duties | System administration > Security > Segregation of duties | Define SoD rules |
| SoD conflict resolution | System administration > Security > Segregation of duties > Conflicts | Resolve detected conflicts |
| Financial period close | General ledger > Period close > Financial period close workspace | Compliance checklist during close |

---

## Compliance & Audit Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    COMPLIANCE & AUDIT ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PREVENTIVE CONTROLS                                                     │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Segregation of Duties (SoD) — role conflict rules       │             │
│  │ • Workflow approvals — require authorization               │             │
│  │ • Security roles — restrict access to functions            │             │
│  │ • Reason codes — require justification for changes         │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  DETECTIVE CONTROLS                                                      │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Audit policies — scheduled rules scan for violations    │             │
│  │ • Database logging — track CUD operations on entities     │             │
│  │ • Alert rules — notify on condition changes               │             │
│  │ • Audit trail — journal and transaction history            │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  INVESTIGATION & RESOLUTION                                              │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Audit workbench — review violations                     │             │
│  │ • Case management — track compliance issues               │             │
│  │ • Financial period close — compliance checklist            │             │
│  │ • Electronic reporting — regulatory submissions           │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
│  REPORTING                                                               │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Electronic Reporting (ER) — regulatory format output    │             │
│  │ • Financial reports — trial balance, statements           │             │
│  │ • Audit file export — SAF-T, standard audit formats       │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `LedgerAuditTrail` | Audit trail | Inquiry |
| `AuditPolicyDocument` | Audit policies | Setup |
| `AuditWorkbench` | Audit workbench | Inquiry |
| `SysDataBaseLog` | Database logging | Administration |
| `SysSodSetup` | Segregation of duties | Security |
| `SysSodConflicts` | SoD conflicts | Security |
| `LedgerPeriodClose` | Financial period close | Period Close |
| `ERFormatDesigner` | Electronic reporting | Reporting |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Security roles** must be defined before SoD rules
2. **SoD rules** should be validated before go-live (run conflict check)
3. **Database logging** should be selectively enabled — excessive logging degrades performance
4. **Audit policies** need source documents to evaluate (e.g., expense reports, vendor invoices)
5. **Reason codes** must be configured before mandating reasons on transactions
6. **Electronic reporting configurations** must be imported from Global Repository before use
7. **Financial period close** checklists should be configured before first period close

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "SoD conflict detected" | User has conflicting duties | Resolve by adjusting role assignments |
| "Database log table full" | No cleanup schedule configured | Set up periodic log cleanup |
| "Audit policy returned no results" | Policy date range or scope incorrect | Verify policy schedule and scope |
| "ER configuration not found" | Configuration not imported | Import from Global Repository |
| "Reason code required" | Transaction attempted without reason | Enter reason code before posting |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Compliance & Audit** module.

### Record to report

*236 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze financial performance | 26 | — |
| Close financial periods | 41 | — |
| Define accounting policies | 82 | — |
| Manage budgets | 25 | — |
| Manage cash | 26 | — |
| Record financial transactions | 36 | — |

### Administer to operate

*2 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Administer system features | 2 | — |

