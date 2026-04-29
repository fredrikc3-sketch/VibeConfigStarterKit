---
name: financial-compliance-guard
description: NON-NEGOTIABLE compliance gate for any project that configures D365 Finance modules (General Ledger, AP, AR, Fixed Assets, Cash & Bank, Tax, Budgeting, Project Accounting, Expense). Captures the customer's applicable accounting and regulatory frameworks (US GAAP, IFRS, local GAAPs, SOX, ASC 606 / IFRS 15, ASC 842 / IFRS 16, SAF-T, GoBD, MTD-VAT, ESG/CSRD, etc.) at Phase 1.1, and validates the proposed AND deployed configuration against them at Phase 1.4 (config validation), Phase 1.5 (approval gate), and Phase 2.2 (E2E testing). If any check has `result = fail` and `severity = blocker`, the project STOPS — Phase 1.5 cannot pass and Phase 2.1 must not start. Produces `Documentation/compliance-validation.json` and `Documentation/compliance-validation.md`.
---

# Financial Compliance Guard

> **Cardinal rule (non-negotiable)**: Finance configuration that violates the customer's applicable accounting framework is a **defect**, not a preference. It must be caught before deployment, not in the audit.

## When to invoke

| Trigger | Phase | Output state |
|---|---|---|
| Requirements analysis identifies finance-module scope | 1.1 | Frameworks list populated, checks marked `deferred` |
| Config files for finance modules are built | 1.4 | All checks executed; failures must be remediated before 1.5 |
| Approval gate | 1.5 | Hard gate — `gateStatus` must be `open` to proceed |
| E2E validation | 2.2 | Re-run against deployed environment; deployed-state evidence captured |
| On user request | any | Audit-style re-run |

The skill is **always** invoked when ANY of these modules is in scope: General Ledger, Accounts Payable, Accounts Receivable, Fixed Assets, Cash & Bank, Tax, Budgeting, Project Accounting, Expense. The orchestrator must refuse to skip it.

## Inputs

- `Documentation/requirement-profile.md`, `requirement-matrix.json` — for stated frameworks
- `Documentation/config-{module}.md`, `parameter-settings.md` — proposed config
- `Modules/Dynamics 365 Finance/**/*.md` — module knowledge for compliance-relevant config rules
- DMF templates under `Modules/Dynamics 365 Finance/**/NNN - *.json` — entity values
- `Documentation/deployment-log.md` (Phase 2.2 only) — deployed evidence
- Customer-supplied auditor letters / SOX matrices in `Requirements/` (if any)

## Outputs

| Artefact | Location | Purpose |
|---|---|---|
| Compliance validation (machine) | `Documentation/compliance-validation.json` | Schema: `schemas/compliance-validation.schema.json` |
| Compliance validation (human)   | `Documentation/compliance-validation.md`   | Auditor-ready summary |
| Gate banner (when blocked)      | `Documentation/_status/<phase>/compliance-gate.md` | Surfaces blocker list to orchestrator |

---

## Step A — Capture frameworks (Phase 1.1)

For every legal entity in scope, ask explicitly (do **not** assume):

1. **Primary accounting framework**: US GAAP, IFRS, UK FRS 102, German HGB, French PCG, Japanese GAAP, Chinese ASBE, Norwegian NRS, Swedish K3, Indian Ind-AS, Brazilian CPC, etc.
2. **Whether dual-book (statutory + management) is required** — if yes, multi-book configuration is mandatory.
3. **Public-company status / SOX applicability** — if listed on US exchanges, SOX §404 internal-controls checks become mandatory.
4. **Revenue-recognition standard**: ASC 606 (US-GAAP) / IFRS 15.
5. **Lease accounting**: ASC 842 (US-GAAP) / IFRS 16.
6. **Tax / e-invoicing localizations**: SAF-T (Norway, Portugal, Poland, etc.), GoBD (Germany), MTD-VAT (UK), e-invoicing mandates (Italy SDI, France, Brazil, Mexico).
7. **ESG / sustainability disclosures**: EU CSRD, SEC climate rules.
8. **Industry overlays**: insurance (IFRS 17), banking (IFRS 9 / Basel), public sector (IPSAS).

If the customer cannot answer authoritatively, escalate to the engagement partner / customer's CFO — **do not guess**. Mark unanswered items as `result: deferred` with a `remediation` requesting written sign-off.

## Step B — Run the non-negotiable check matrix

Every check below is mandatory whenever its triggering framework is selected. Each check populates one row in `checks[]`.

### B.1 Chart of Accounts & GL structure
| Check id | Title | Framework(s) | Pass criteria |
|---|---|---|---|
| FC-0010 | Account categories cover statutory P&L + Balance Sheet | All | Every main account is mapped to a statutory category that supports the framework's primary statements |
| FC-0011 | Reporting currency configured per legal entity | All | Each entity has the correct functional/reporting currency; FX revaluation method matches framework (e.g., temporal vs current rate) |
| FC-0012 | Multi-book configured if dual-GAAP required | IFRS + local-GAAP duals; SOX | "Ledger" + alternative book set up; posting layers defined |
| FC-0013 | Segments / financial dimensions support statutory reporting | All | Required dimensions (department, cost center, project, etc.) flagged on statutory accounts |

### B.2 Fiscal calendar & period close
| FC-0020 | Fiscal calendar matches statutory year | All | Periods, year-end, and adjusting periods configured |
| FC-0021 | Period-close locks prevent retroactive posting | SOX, GoBD, SAF-T | Closed periods are non-editable; on-hold/permanently-closed states used |
| FC-0022 | Audit trail preserved for all posted transactions | SOX, GoBD, all | "Allow voucher edit" disabled on production; voucher numbering is gap-less and immutable |

### B.3 Posting profiles & revenue recognition
| FC-0030 | Posting profiles trace each transaction class to GAAP-correct account | All | AP/AR/inventory/payroll posting profiles reviewed line by line |
| FC-0031 | Revenue recognition rules implement ASC 606 / IFRS 15 five-step model | ASC-606, IFRS-15 | Performance obligations, transaction price allocation, recognition timing all configured |
| FC-0032 | Deferred revenue / contract liability accounts segregated | ASC-606, IFRS-15 | Distinct accounts; reconciliation report scheduled |
| FC-0033 | Lease accounting capitalises right-of-use assets and liability | ASC-842, IFRS-16 | Asset Leasing module enabled; lease classification rules set; transition method documented |

### B.4 Inventory valuation
| FC-0040 | Inventory method permitted by framework | All | **LIFO is forbidden under IFRS** — must be FIFO / Weighted Average. US GAAP allows LIFO but requires LIFO reserve disclosure |
| FC-0041 | Cost rollups reflect framework-required cost components | IFRS, US-GAAP | Standard vs actual costing chosen; variance accounts mapped |

### B.5 Fixed assets & depreciation
| FC-0050 | Depreciation methods allowed by framework | IFRS, US-GAAP, local | Component depreciation under IFRS; matched useful lives; impairment posting profile configured |
| FC-0051 | Multiple depreciation books for tax vs book vs IFRS | dual-GAAP | "Depreciation books" set up with framework labels |

### B.6 Tax & statutory reporting
| FC-0060 | Sales tax / VAT codes match jurisdiction rules | TAX-LOCALIZATION, EU-VAT | Tax codes, jurisdictions, item sales tax groups complete |
| FC-0061 | E-invoicing / SAF-T / GoBD digital export configured | SAF-T, GoBD, MTD-VAT, country-specific | Required electronic message providers enabled; test export reconciles |
| FC-0062 | Withholding tax codes set up where applicable | local | WHT profiles tied to vendors; reporting layouts configured |

### B.7 Internal controls (SOX)
| FC-0070 | Segregation of duties enforced | SOX | SoD rules imported and conflicts resolved or compensated |
| FC-0071 | Workflow approvals on payment / journal posting above threshold | SOX, internal-controls | Workflow rules configured; approval thresholds match policy |
| FC-0072 | Audit log retention meets statutory minimum | SOX, GoBD (10 yr DE), local | Database log + DMF audit log retained for the required period |

### B.8 Consolidation & intercompany
| FC-0080 | Intercompany eliminations configured | IFRS, US-GAAP, multi-entity | Elimination rules / consolidation account set up; intercompany matching enabled |
| FC-0081 | Foreign-currency translation method matches framework | IFRS 21, ASC 830 | Functional currency designated correctly; CTA account configured |

### B.9 Data retention & ESG
| FC-0090 | Data retention policy meets statutory minimum | local, GDPR | Retention rules documented; deletion workflow configured |
| FC-0091 | ESG / CSRD data points tagged on relevant accounts | EU-CSRD | Sustainability tags on energy, scope-1/2/3 GHG-related accounts; ESG reporting workspace enabled |

> **The list above is the minimum.** When new frameworks or clauses surface in customer discussions, add new `FC-NNNN` checks. The list is intentionally extensible — never delete a check just because a customer says it doesn't apply; instead mark `result: not-applicable` with a `rationale`.

## Step C — Determine result + severity per check

- `result = pass` when configuration evidence demonstrates compliance.
- `result = warn` when partial / interpretive (e.g., framework allows multiple methods and the chosen one is defensible but not best practice).
- `result = fail` and `severity = blocker` when the configuration violates a non-negotiable framework rule (e.g., LIFO under IFRS, missing audit trail under SOX, no e-invoicing where mandated).
- `result = not-applicable` only with a documented `rationale` from a qualified stakeholder.
- `result = deferred` when the customer has not provided enough information yet — escalate.

## Step D — Gate logic (non-negotiable)

```
if any check has result == "fail" AND severity == "blocker":
    summary.gateStatus = "blocked"
    write Documentation/_status/<phase>/compliance-gate.md
    surface ALL blocking checks to the user with framework clause and remediation
    BLOCK Phase 1.5 (approval gate cannot pass)
    BLOCK Phase 2.1 (deployment must not start)
    do NOT advance the orchestrator
else:
    summary.gateStatus = "open"
```

The gate is **only** waivable by a written sign-off from a qualified person (engagement controller, customer CFO, or external auditor). Waivers must populate `waivedBy` and `waivedAt` on the specific check; bulk waivers are forbidden.

## Step E — Auditor-ready markdown report

`Documentation/compliance-validation.md` skeleton:

```markdown
# Financial Compliance Validation — <date> — Phase <n>

**Frameworks in scope**: US GAAP, SOX, ASC 606, ASC 842, EU-VAT
**Gate status**: ✅ OPEN | 🚫 BLOCKED (3 failures)

## Executive summary
| Total checks | Passed | Warnings | Failures (blockers) |
|---|---|---|---|
| 41 | 36 | 2 | 3 |

## Blockers
| ID | Framework | Title | Clause | Remediation |
|---|---|---|---|---|
| FC-0040 | IFRS | LIFO not permitted | IAS 2 §25 | Switch valuation to FIFO or weighted average; re-run inventory close |
| ...

## Detail per check
... (one section per check with evidence links)

## Sign-off
- Prepared by: …
- Reviewed by (controller): …
- Approved by (CFO / auditor): …
```

## Cardinal rules
- **Compliance failures are defects, not preferences.** Never override on convenience.
- **Frameworks come from the customer, not the agent.** Capture explicitly; never assume.
- **Every check must trace to a framework clause** (`frameworkClause` field) — auditors will ask.
- **Source-of-truth for evidence is the source files**, not the live environment. If the env drifts, fix the source first.
- **Re-run at every phase boundary.** Phase 1.4, Phase 1.5, Phase 2.2, and on-demand post-go-live.
- **Log every blocker** as a Challenge Journal entry (`category: "compliance"`, `severity: blocker`) so patterns surface across projects.
- **Project-id namespacing applies.** Multi-tenant deployments must keep compliance reports per-project.

## Cross-references
- Schema: `schemas/compliance-validation.schema.json`
- Phase 1.1: `skills/d365-requirements-analysis/SKILL.md` (framework capture)
- Phase 1.4 / 1.5: `skills/d365-config-builder/SKILL.md` (validation + approval gate)
- Phase 2.2: `skills/d365-validation-testing/SKILL.md` (deployed-state re-validation)
- Reinforcement learning: `skills/reinforcement-learning/SKILL.md`
