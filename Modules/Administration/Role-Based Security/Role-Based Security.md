# Role-Based Security Module - Knowledge Source

> This file is the central knowledge hub for **Role-Based Security** within Dynamics 365 Finance & Operations Administration.

---


---


> **Microsoft Learn Reference:** [Role-Based Security](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/role-based-security)

## Module Overview

The Role-Based Security framework in Dynamics 365 Finance & Operations controls access to the system through security roles, duties, and privileges. It aligns with organizational job functions to ensure users have access only to the functionality required for their roles. Security can be configured at the organization, legal entity, and record level.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Security Roles** | Assign predefined or custom roles that group duties and privileges |
| **Duties & Privileges** | Define granular access rights organized by business responsibilities |
| **Segregation of Duties** | Enforce separation of conflicting tasks to prevent fraud |
| **Security Diagnostics** | Run diagnostics to identify and resolve security configuration issues |
| **User Management** | Create, manage, and assign roles to system users |
| **Data Security Policies** | Restrict access to data based on legal entity, organization, or custom criteria |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Security roles, duties, and privileges are managed through the Security configuration form and can be exported/imported via security role packages.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Security-related business process areas:
- **Security administration** (role assignment, user management)
- **Segregation of duties** (conflict detection, enforcement)
- **Data security** (extensible data security policies)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure security in Dynamics 365 Finance and Operations** | https://learn.microsoft.com/en-us/training/modules/configure-security-dynamics-365-finance-operations/ |
| Implement security | https://learn.microsoft.com/en-us/training/paths/implement-finance-operations/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Role-based security overview | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/role-based-security |
| Security architecture | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/security-architecture |
| Security roles | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/assign-users-security-roles |
| Duties and privileges | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/duties-privileges |
| Segregation of duties | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/segregation-of-duties |
| Extensible data security | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/extensible-data-security-policies |
| Security diagnostic tool | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/security-reports |
| Create new security roles | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/create-new-security-role |
| B2B authentication | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/b2b-guest-user |
| Batch job security | https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/batch-security |

---

## Security Model Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  ROLE-BASED SECURITY ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  USER                                                                    │
│    │                                                                     │
│    ├── SECURITY ROLE (e.g., "Accounts Payable Clerk")                    │
│    │     │                                                               │
│    │     ├── DUTY (e.g., "Maintain vendor invoices")                     │
│    │     │     │                                                         │
│    │     │     ├── PRIVILEGE (e.g., "Post vendor invoice")               │
│    │     │     │     │                                                   │
│    │     │     │     └── PERMISSIONS (Entry points + access level)       │
│    │     │     │           • Menu items (Display / Action / Output)      │
│    │     │     │           • Service operations                         │
│    │     │     │           • Web content                                │
│    │     │     │           • Table permissions (CRUD)                   │
│    │     │     │                                                         │
│    │     │     └── PRIVILEGE (e.g., "View vendor invoice")               │
│    │     │                                                               │
│    │     ├── DUTY (e.g., "Inquire into vendor master")                   │
│    │     │                                                               │
│    │     └── Direct PRIVILEGES (rarely used)                             │
│    │                                                                     │
│    ├── SECURITY ROLE (additional roles)                                  │
│    │                                                                     │
│    └── ORGANIZATION CONSTRAINTS                                          │
│          • Legal entity restrictions                                     │
│          • Operating unit restrictions                                   │
│                                                                          │
│  ACCESS LEVELS: No Access | Read | Update | Create | Delete | Grant      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 4-Phase Configuration Sequence

### Phase 1: User & Azure AD Setup

| Task | Location | Purpose |
|------|----------|---------|
| Azure AD users | Azure portal / Entra ID | Create/sync user accounts |
| Import users | System administration > Users > Users | Import from Azure AD |
| Assign licenses | Microsoft 365 Admin Center | Assign D365 F&O licenses |

### Phase 2: Security Role Definition

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Review standard roles | System administration > Security > Security roles | Evaluate out-of-box roles |
| Create custom roles | System administration > Security > Security roles > Create | Organization-specific roles |
| Add duties to roles | (Within security role) | Assign business function duties |
| Add privileges to duties | (Within duty) | Assign specific entry point access |
| Exclusion rules | (Within security role) | Remove specific access from inherited duties |

### Phase 3: Role Assignment

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Assign roles to users | System administration > Users > Users > Assign roles | User-to-role mapping |
| Set organization constraints | (Within role assignment) | Restrict by legal entity / operating unit |
| Role-based data security | System administration > Security > Extensible data security | Row-level data filtering |

### Phase 4: Segregation of Duties & Audit

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Define SoD rules | System administration > Security > Segregation of duties > Segregation of duties rules | Conflicting duty pairs |
| Verify SoD compliance | System administration > Security > Segregation of duties > Verify compliance | Detect violations |
| Security reports | System administration > Security > Security roles > Role to user assignments | Audit role assignments |

---

## Standard Security Roles (Common)

| Role | Description | Module |
|------|-------------|--------|
| System administrator | Full system access | All |
| Accounts payable clerk | AP invoice/payment processing | Finance |
| Accounts payable manager | AP supervision and setup | Finance |
| Accounts receivable clerk | AR invoice/payment processing | Finance |
| Accounting manager | GL and financial management | Finance |
| Purchasing agent | PO creation and management | Procurement |
| Sales representative | Sales order management | Sales |
| Warehouse worker | Warehouse operations | WMS |
| Production manager | Production order management | Production |
| HR manager | Human resources management | HR |

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `SysSecRoles` | Security roles | Security |
| `SysSecDuties` | Duties | Security |
| `SysSecPrivileges` | Privileges | Security |
| `SysSecUserRole` | Assign users to roles | Security |
| `SysSecSegregationOfDuties` | Segregation of duties rules | Security |
| `SysSecSoDConflicts` | Segregation of duties conflicts | Security |
| `SysSecExtensibleDataSecurity` | Extensible data security policies | Security |
| `SysSecUserPermissions` | User permissions | Security |
| `SystemUser` | Users | Administration |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Azure AD users** must exist before they can be imported into D365
2. **D365 licenses** must be assigned before users can sign in
3. **Security roles** must be defined before they can be assigned to users
4. **Duties** should be understood before creating custom roles
5. **Segregation of duties rules** should be defined before mass role assignment
6. **Organization constraints** should be applied during role assignment for multi-entity environments
7. **Security role changes** take effect on next user sign-in

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Access denied" | User missing required security role | Assign appropriate role |
| "SoD conflict detected" | User assigned conflicting roles | Resolve by removing one role or getting exemption |
| "User cannot access legal entity" | Missing organization constraint | Add legal entity to role assignment |
| "Menu item not visible" | Missing privilege for menu item entry point | Add privilege to duty/role |
| "Cannot create record" | Read-only access level | Elevate permission to Create level |
| "Batch job access denied" | Missing batch job privileges | Add batch processing duties |
