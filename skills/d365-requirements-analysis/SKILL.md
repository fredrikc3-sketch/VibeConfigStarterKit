---
name: d365-requirements-analysis
description: Use at the start of a new D365 F&O project, or when requirements change, to ingest raw requirement documents from the `Requirements/` folder, classify each requirement (Standard Config, Data Migration, Parameter Setting, Workflow, Integration, Gap, Clarification), map every requirement to the correct module/entity/feature, and produce `Documentation/requirement-profile.md` and `Documentation/requirement-matrix.json`. This is Phase 1 Step 1.1 of the implementation lifecycle.
---

# Requirements Analysis (Phase 1.1)

> **Cardinal rule**: Think first, write continuously. No deployment happens until Phase 1 is complete and approved.

## Inputs
- All files in `Requirements/` (Word, PDF, Excel, text — anything readable).
- Module knowledge files (use the `d365-knowledge-routing` skill to find paths).
- `Modules/dmf_odata_mapping.json` (entity mapping).
- `Business Process/ProcessCatalogue.json` (5,767-item APQC tree).

## Outputs
| Artefact | Location | Format |
|---|---|---|
| Requirement Profile | `Documentation/requirement-profile.md` | Markdown |
| Requirement Matrix | `Documentation/requirement-matrix.json` | JSON (see schema) |
| Gap Analysis | embedded in profile | Markdown table |

Schema reference: [`requirement-matrix.schema.json`](./requirement-matrix.schema.json).

## Procedure

### 1. Ingest
Read **every** file in `Requirements/`. Extract every functional requirement, constraint, and assumption. Identify the business processes being described.

### 2. Map to D365 capabilities
For each requirement:
- Which module(s) can fulfil it? (use keyword router in `d365-knowledge-routing`)
- Which specific entity, parameter, or feature?
- Standard config, data migration, or genuine gap?

### 3. Classify
| Category | Meaning | Action |
|---|---|---|
| ✅ **Standard Config** | Out-of-box D365 capability | Map to module phase + entity |
| 📦 **Data Migration** | Requires data load | Map to DMF template + entity |
| ⚙️ **Parameter Setting** | Form-driven toggle/value | Map to form + field |
| 🔄 **Workflow / Process** | Workflow or business rule | Map to workflow type + conditions |
| 🔌 **Integration** | External connection | Map to OData / dual-write / API |
| ⚠️ **Gap** | No standard capability | Document gap + proposed approach |
| ❓ **Clarification** | Ambiguous | Flag for user input |

### 4. Build the requirement profile
`Documentation/requirement-profile.md` structure:
1. Executive summary — scope, modules, timelines.
2. Requirement matrix — `ID | Description | Category | Module | Entity | Status`.
3. Gap analysis — gaps + proposed solutions.
4. Assumptions & constraints.
5. Open questions for the client.

## Continuous-documentation rule
After every mapping decision, update `requirement-profile.md` immediately. **Never batch.**

## Hand-off
When complete, signal that Phase 1 Step 1.2 (config building) can begin — invoke the `d365-config-builder` skill.
