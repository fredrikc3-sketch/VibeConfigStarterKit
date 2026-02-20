# Quality Management Module - Knowledge Source

> This file is the central knowledge hub for the **Quality Management** module within Dynamics 365 Supply Chain Management.

---


---


> **Microsoft Learn Reference:** [Quality Management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-management-processes)

## Module Overview

The Quality Management module in Dynamics 365 Supply Chain Management enables organizations to manage product quality through quality orders, quality associations, test groups, and nonconformance management. It supports automatic quality order generation triggered by inventory events and integration with quarantine management.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Quality Orders** | Create and process quality inspection orders with test results |
| **Quality Associations** | Automatically trigger quality orders based on inventory events (receipt, production, etc.) |
| **Test Groups & Instruments** | Define tests, acceptable quality levels, and testing procedures |
| **Nonconformance Management** | Track, investigate, and resolve quality issues with corrective actions |
| **Quarantine Orders** | Isolate inventory for inspection before releasing to stock |
| **Quality Item Sampling** | Define sampling plans for statistical quality control |
| **Certificate of Analysis** | Generate certificates documenting quality test results |
| **Corrective Actions** | Plan and track corrective and preventive actions for quality issues |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

The following DMF template file defines the data entities required for migrating and configuring this module:

#### 395 - Quality Management (`395 - Quality management.json`)

Quality management configuration entities.

| Seq | Entity Name | Target Entity | Category | Level |
|-----|-------------|---------------|----------|-------|
| 10 | Diagnostic types | QualityDiagnosticTypeEntity | Quality - Setup | 30 |
| 10 | Item quality groups | QualityItemQualityGroupEntity | Quality - Groups | 30 |
| 10 | Item sampling | QualityItemSamplingEntity | Quality - Sampling | 30 |
| 10 | Nonconformance charge types | QualityNonConformanceChargeTypeEntity | Quality - Nonconformance | 30 |
| 10 | Nonconformance operation categories | QualityNonConformanceOperationCategoryEntity | Quality - Nonconformance | 30 |
| 10 | Quality groups | QualityGroupEntity | Quality - Groups | 30 |
| 10 | Quality problem types | QualityProblemTypeEntity | Quality - Problems | 30 |
| 10 | Quality test instruments | QualityTestInstrumentEntity | Quality - Testing | 30 |
| 10 | Quality test variables | QualityTestVariableEntity | Quality - Testing | 30 |
| 10 | Quality test variable outcomes | QualityTestVariableOutcomeEntity | Quality - Testing | 30 |
| 10 | Quality tests | QualityTestEntity | Quality - Testing | 30 |
| 10 | Quarantine zones | QualityQuarantineZoneEntity | Quality - Quarantine | 30 |
| 20 | Test groups | QualityTestGroupEntity | Quality - Testing | 40 |
| 20 | Test group assignments | QualityTestGroupAssignmentEntity | Quality - Testing | 40 |
| 30 | Quality order creation policies V2 | QualityOrderCreationPolicyV2Entity | Quality - Policies | 50 |

**DMF Load Order Notes:**
- **Seq 10** contains foundational quality setup — diagnostic types, quality groups, sampling methods, test instruments, test variables, nonconformance types, quarantine zones
- **Seq 20** contains test group definitions and their assignments — depends on tests, variables, and instruments
- **Seq 30** contains quality order creation policies (quality associations) — depends on test groups and quality groups
- Quality tests must exist before test groups
- Test variables and outcomes must exist before tests referencing them
- Test groups must exist before quality order creation policies

**Level (LevelInExecutionUnit) Priority Guide:**
- **Level 30:** Core setup entities (tests, instruments, variables, diagnostic types, quality groups, quarantine zones)
- **Level 40:** Test groups and assignments (group tests into reusable sets)
- **Level 50:** Quality order creation policies (automated quality order triggers)


---

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Quality Management** module.

### Inventory to deliver

*179 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze warehouse operations | 14 | — |
| Maintain inventory levels | 37 | — |
| Manage freight and transportation | 9 | — |
| Manage inventory quality | 50 | — |
| Manage warehouse operations | 23 | — |
| Process inbound goods | 22 | — |
| Process outbound goods | 24 | — |

### Plan to produce

*123 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze production operations | 14 | — |
| Control production quality | 30 | — |
| Develop production strategies | 16 | — |
| Plan production operations | 26 | — |
| Run production operations | 37 | — |

### Source to pay

*90 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze procurement and sourcing | 5 | — |
| Develop procurement and sourcing strategy | 27 | [Learn more](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/procurement-catalogs) |
| Manage accounts payable | 4 | — |
| Manage supplier relationships | 32 | — |
| Procure goods and services | 10 | — |
| Source and contract goods and services | 12 | — |

<!-- ODATA-REFERENCE-START -->

## OData Entity Reference

> **MCP Data Tools Reference** — The following table maps each DMF entity to its OData entity set name
> for use with the Finance & Operations MCP data tools (`data_find_entities`, `data_create_entities`, etc.).

### Entities with OData Endpoints

| Entity Name | DMF Target Entity | OData Entity Set | Match |
|-------------|-------------------|------------------|-------|
| Quality groups | `QualityGroupEntity` | `QualityTestGroups` | verified |
| Quality test variable outcomes | `QualityTestVariableOutcomeEntity` | `QualityTestVariableOutcomes` | verified |
| Test groups | `QualityTestGroupEntity` | `QualityTestGroups` | verified |
| Test group assignments | `QualityTestGroupAssignmentEntity` | `QualityGroupItemAssignments` | verified |

### Entities without OData Endpoints

These entities are available via DMF import/export only (no direct OData/MCP access):

| Entity Name | DMF Target Entity |
|-------------|-------------------|
| Diagnostic types | `QualityDiagnosticTypeEntity` |
| Item quality groups | `QualityItemQualityGroupEntity` |
| Item sampling | `QualityItemSamplingEntity` |
| Nonconformance charge types | `QualityNonConformanceChargeTypeEntity` |
| Nonconformance operation categories | `QualityNonConformanceOperationCategoryEntity` |
| Quality problem types | `QualityProblemTypeEntity` |
| Quality test instruments | `QualityTestInstrumentEntity` |
| Quality test variables | `QualityTestVariableEntity` |
| Quality tests | `QualityTestEntity` |
| Quarantine zones | `QualityQuarantineZoneEntity` |
| Quality order creation policies V2 | `QualityOrderCreationPolicyV2Entity` |

<!-- ODATA-REFERENCE-END -->
---

### Process Catalogue References

The global Process Catalogue contains business process definitions related to Quality Management:

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Quality Management-related business process areas:
- **Quality assurance** (incoming inspection, in-process testing, outgoing inspection)
- **Nonconformance management** (defect tracking, corrective actions)
- **Quarantine management** (quarantine orders, disposition)
- **Quality associations** (automated quality order creation)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Configure and use quality management in Dynamics 365 Supply Chain Management** | https://learn.microsoft.com/en-us/training/modules/configure-use-quality-management-dyn365-supply-chain-mgmt/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Quality management overview | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-management-overview |
| Quality orders | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-orders |
| Quality associations (quality order policies) | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-associations |
| Quality tests | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-tests |
| Test variables | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-test-variables |
| Test instruments | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-test-instruments |
| Quality groups | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-groups |
| Item sampling | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-item-sampling |
| Nonconformance management | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-nonconformance-overview |
| Quarantine orders | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quarantine-orders |
| Quality management for warehouse processes | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-management-for-warehouses-processes |
| Diagnostic types | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-diagnostic-types |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Released products | Product information management > Products > Released products | Items subject to quality testing |
| Warehouses | Inventory management > Setup > Inventory breakdown > Warehouses | Quality warehouse for quarantine |
| Vendors | Accounts payable > Vendors > All vendors | Vendor-specific quality associations |
| Sites | Inventory management > Setup > Inventory breakdown > Sites | Site-specific quality setup |

### Phase 2: Quality Test Setup

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| QualityTest | Inventory management > Setup > Quality control > Tests | Test definitions (quantitative/qualitative) |
| QualityTestInstrument | Inventory management > Setup > Quality control > Test instruments | Measurement instruments |
| QualityTestVariable | Inventory management > Setup > Quality control > Test variables | Qualitative variable definitions |
| QualityTestVariableOutcome | (Within test variable) | Pass/fail outcome values |
| QualityItemSampling | Inventory management > Setup > Quality control > Item sampling | Sampling quantity/percentage rules |
| QualityDiagnosticType | Inventory management > Setup > Quality control > Diagnostic types | Root cause classification |
| QualityProblemType | Inventory management > Setup > Quality control > Problem types | Problem classification |
| QualityQuarantineZone | Inventory management > Setup > Quality control > Quarantine zones | Physical quarantine locations |

### Phase 3: Test Groups & Quality Groups

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| QualityGroup | Inventory management > Setup > Quality control > Quality groups | Item quality classification |
| QualityItemQualityGroup | (Within item or quality group) | Assign items to quality groups |
| QualityTestGroup | Inventory management > Setup > Quality control > Test groups | Group of tests to apply together |
| QualityTestGroupAssignment | (Within test group) | Tests within the group, AQL, sequence |
| QualityNonConformanceChargeType | Inventory management > Setup > Quality control > Charges | Nonconformance cost types |
| QualityNonConformanceOperationCategory | Inventory management > Setup > Quality control > Operations | Corrective action categories |

### Phase 4: Quality Order Policies

| Table | Menu Path | Purpose |
|-------|-----------|---------|
| QualityOrderCreationPolicy (Quality associations) | Inventory management > Setup > Quality control > Quality associations | Automated quality order triggers |

---

## Quality Management Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   QUALITY MANAGEMENT PROCESS FLOW                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. QUALITY ASSOCIATION (Trigger)                                        │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ Event types:                                             │          │
│     │ • Purchase receipt    • Production start                 │          │
│     │ • Production finish   • Sales order pick                 │          │
│     │ • Quarantine release  • Inventory                        │          │
│     │                                                          │          │
│     │ → Automatically creates quality order based on policy    │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  2. QUALITY ORDER                                                        │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Item, quantity, test group assigned                    │          │
│     │ • Sampling rules determine test quantity                 │          │
│     │ • Validate quality order                                 │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│  3. TESTING                                                              │
│     ┌────────────────────────────────────────────────────────┐          │
│     │ • Record test results (quantitative values or           │          │
│     │   qualitative outcomes)                                  │          │
│     │ • Compare against acceptable quality levels (AQL)        │          │
│     │ • Pass / Fail determination                              │          │
│     └────────────────────────────────────────────────────────┘          │
│                              │                                           │
│                     ┌────────┴────────┐                                  │
│                     ▼                 ▼                                   │
│  4a. PASS                     4b. FAIL                                   │
│  ┌──────────────┐            ┌──────────────────────┐                   │
│  │ • Release     │            │ • Quarantine order    │                   │
│  │   inventory   │            │ • Nonconformance      │                   │
│  │ • Continue    │            │   report              │                   │
│  │   process     │            │ • Corrective actions  │                   │
│  └──────────────┘            │ • Vendor charge-back  │                   │
│                               └──────────────────────┘                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Quality Association Event Types

| Event | Reference Type | When Triggered |
|-------|---------------|----------------|
| **Purchase** | Before/After product receipt | Incoming goods inspection |
| **Sales** | Before/After packing slip | Outgoing goods inspection |
| **Production** | Before/After report as finished | In-process / final inspection |
| **Quarantine** | Before/After quarantine report as finished | Quarantine release testing |
| **Inventory** | Manual or batch attribute | Ad-hoc quality testing |

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `QualityOrders` | Quality orders | Quality |
| `QualityAssociations` | Quality associations | Setup |
| `QualityTests` | Tests | Setup |
| `QualityTestGroups` | Test groups | Setup |
| `QualityTestInstruments` | Test instruments | Setup |
| `QualityTestVariables` | Test variables | Setup |
| `QualityItemSampling` | Item sampling | Setup |
| `QualityNonConformanceTable` | Nonconformances | Nonconformance |
| `QuarantineOrder` | Quarantine orders | Quarantine |
| `QualityGroups` | Quality groups | Setup |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Quality tests** must be defined before test groups can reference them
2. **Test variables and outcomes** must exist for qualitative tests
3. **Test instruments** must exist for quantitative tests requiring instrument tracking
4. **Test groups** must be defined before quality associations (policies)
5. **Quality associations** define the trigger — must be configured before automated quality orders work
6. **Item sampling** rules must be set for each quality association
7. **Quarantine warehouse** must be configured for quarantine order processing
8. **Nonconformance charge types** and **operation categories** must exist for nonconformance reporting

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Quality order not created" | No quality association matching the event | Create quality association for event/item |
| "Test group not assigned" | Quality association missing test group | Assign test group to quality association |
| "Cannot validate quality order" | Test results not entered | Complete all test results |
| "Quarantine warehouse not configured" | Missing quarantine warehouse setup | Configure quarantine warehouse in inventory parameters |
| "Nonconformance cannot be approved" | Missing approval workflow or permissions | Configure nonconformance workflow |
| "AQL exceeded" | Test results outside acceptable range | Review quality levels and corrective actions |
