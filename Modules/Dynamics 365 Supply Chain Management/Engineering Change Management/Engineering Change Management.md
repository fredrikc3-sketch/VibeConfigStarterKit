# Engineering Change Management Module - Knowledge Source

> This file is the central knowledge hub for **Engineering Change Management** within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Engineering Change Management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/engineering-change-management/product-engineering-overview)

## Module Overview

The Engineering Change Management module in Dynamics 365 Supply Chain Management enables structured management of product changes throughout the engineering lifecycle. It supports engineering companies, engineering versions, engineering change requests and orders, readiness policies, and product release workflows to manage changes from design through production.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Engineering Companies** | Use an engineering company to own product definitions before release to operating companies |
| **Engineering Change Requests** | Propose product changes through formal requests with impact analysis |
| **Engineering Change Orders** | Implement approved changes with controlled release to production |
| **Engineering Versions** | Track product versions with BOM and route version control |
| **Readiness Policies** | Define checklists that must be completed before product release |
| **Product Release Workflow** | Control when and how engineering products are released to legal entities |
| **Formula & BOM Changes** | Manage changes to product formulas and bills of materials through change orders |
| **Engineering Attributes** | Define engineering-specific attributes for products and variants |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Engineering change management uses dedicated product engineering forms and change order workflows.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Engineering Change Management-related business process areas:
- **Engineering products** (products owned by engineering organizations)
- **Engineering categories** (classification and attribute management)
- **Engineering change requests** (propose product changes)
- **Engineering change orders** (approve and execute changes)
- **Product versioning** (version lifecycle and readiness)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Engineering change management overview** | https://learn.microsoft.com/en-us/dynamics365/supply-chain/engineering-change-management/product-engineering-overview |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Engineering change management overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/engineering-change-management/product-engineering-overview |
| Engineering organizations | https://learn.microsoft.com/en-us/dynamics365/supply-chain/engineering-change-management/engineering-org-data-ownership-rules |
| Engineering products and versions | https://learn.microsoft.com/en-us/dynamics365/supply-chain/engineering-change-management/engineering-versions-product-category |
| Engineering categories | https://learn.microsoft.com/en-us/dynamics365/supply-chain/engineering-change-management/engineering-versions-product-category#engineering-categories |
| Engineering attributes | https://learn.microsoft.com/en-us/dynamics365/supply-chain/engineering-change-management/engineering-attributes-and-search |
| Engineering change requests | https://learn.microsoft.com/en-us/dynamics365/supply-chain/engineering-change-management/engineering-change-management |
| Engineering change orders | https://learn.microsoft.com/en-us/dynamics365/supply-chain/engineering-change-management/engineering-change-management#engineering-change-orders |
| Product readiness policies | https://learn.microsoft.com/en-us/dynamics365/supply-chain/engineering-change-management/product-readiness |
| Release product structures | https://learn.microsoft.com/en-us/dynamics365/supply-chain/engineering-change-management/release-product-structure |
| Formula changes (process manufacturing) | https://learn.microsoft.com/en-us/dynamics365/supply-chain/engineering-change-management/manage-formula-changes |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Engineering change management parameters | Engineering change management > Setup > Parameters | Module settings |
| Enable feature | Feature management > Engineering change management | Turn on feature |
| Legal entities | Organization administration > Organizations | Companies for release |

### Phase 2: Organization & Categories

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Engineering organizations | Engineering change management > Setup > Engineering organizations | Engineering ownership entity |
| Engineering categories | Engineering change management > Setup > Engineering categories | Product classification (versioning rules, attributes) |
| Readiness policies | Engineering change management > Setup > Product readiness policies | Checklist for release authorization |
| Engineering attributes | Engineering change management > Setup > Engineering attributes | Custom product attributes |

### Phase 3: Product & Version Management

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Engineering products | Engineering change management > Engineering products | Create engineering-controlled products |
| Product versions | (Within product) > Versions | Version records with effectivity dates |
| BOM/Route per version | (Within version) > BOM / Route | Version-specific bill of materials |
| Release product to companies | (Within product) > Release | Push to operational companies |

### Phase 4: Change Management

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Engineering change requests | Engineering change management > Change requests | Propose a product change |
| Engineering change orders | Engineering change management > Change orders | Formal change execution |
| Change order workflow | System administration > Workflow > Engineering change order | Approval configuration |
| Impact assessment | (Within change order) > Impact | Evaluate affected BOMs and orders |
| Execute change | (Within change order) > Release | Push changes to operational data |

---

## Engineering Change Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  ENGINEERING CHANGE MANAGEMENT FLOW                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ENGINEERING PRODUCT LIFECYCLE                                           │
│  ┌────────────────────────────────────────────────────────┐             │
│  │                                                          │             │
│  │  Create Product → Version 1 (V1)                         │             │
│  │  ├── BOM v1.0                                            │             │
│  │  ├── Route v1.0                                          │             │
│  │  ├── Engineering attributes                              │             │
│  │  └── Readiness check → Release to companies              │             │
│  │                                                          │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  CHANGE REQUEST                                                          │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Anyone can propose a change                             │             │
│  │ • Describes problem and proposed solution                 │             │
│  │ • Reviewed by engineering team                            │             │
│  │ • Approved → creates Change Order                         │             │
│  │ • Rejected → documented and closed                        │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  CHANGE ORDER                                                            │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Formal engineering change                               │             │
│  │ • Version increment (V1 → V2)                             │             │
│  │ • ┌────────────────────────────┐                         │             │
│  │   │ Impact Analysis:            │                         │             │
│  │   │ • Affected BOMs             │                         │             │
│  │   │ • Open purchase orders      │                         │             │
│  │   │ • Open production orders    │                         │             │
│  │   │ • On-hand inventory          │                         │             │
│  │   └────────────────────────────┘                         │             │
│  │ • Workflow approval                                       │             │
│  │ • Execute: Create V2, update BOM/Route                    │             │
│  │ • Release V2 to operational companies                     │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  EFFECTIVITY                                                             │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ V1: Effective  01/01/2024 – 03/31/2024                    │             │
│  │ V2: Effective  04/01/2024 – (open)                        │             │
│  │ Production/procurement uses version by effectivity date   │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `EngChgProductsV2` | Engineering products | Products |
| `EngChgCaseTable` | Change requests | Changes |
| `EngChgChangeOrder` | Change orders | Changes |
| `EngChgCategory` | Engineering categories | Setup |
| `EngChgOrganization` | Engineering organizations | Setup |
| `EngChgReadinessPolicy` | Product readiness policies | Setup |
| `EngChgAttributes` | Engineering attributes | Setup |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Feature** must be enabled in Feature Management
2. **Engineering organizations** must be created before engineering categories
3. **Engineering categories** define versioning and attribute rules — must exist before products
4. **Readiness policies** must be configured for product release authorization
5. **Change request** typically precedes a change order (but change orders can be created directly)
6. **Change order workflow** must be activated for approval enforcement
7. **Impact analysis** should be reviewed before executing changes

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Product not released" | Readiness checks not passed | Complete readiness checklist |
| "Version conflict" | Multiple open versions | Close or merge version changes |
| "BOM not updated" | Change order not executed | Execute change order |
| "Effectivity gap" | Version date ranges have gaps | Adjust version effectivity dates |
| "Change order rejected" | Workflow rejected by approver | Revise and resubmit |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Engineering Change Management** module.

### Design to retire

*176 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze product performance | 7 | — |
| Develop product strategy | 44 | — |
| Introduce products | 62 | — |
| Manage active products | 53 | — |
| Retire products | 10 | — |

### Plan to produce

*123 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze production operations | 14 | — |
| Control production quality | 30 | — |
| Develop production strategies | 16 | — |
| Plan production operations | 26 | — |
| Run production operations | 37 | — |

