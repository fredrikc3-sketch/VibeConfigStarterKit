# US Payroll Module - Knowledge Source

> This file is the central knowledge hub for **US Payroll** within Dynamics 365 Human Resources.

---


---


> **Microsoft Learn Reference:** [US Payroll](https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-admin-integration-payroll-api-introduction)

## Module Overview

US Payroll in Dynamics 365 Human Resources provides payroll processing for US-based employees. It handles earnings, deductions, tax calculations, garnishments, and payroll integration. For advanced scenarios, it integrates with third-party payroll providers through the Payroll Integration API.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Earnings Processing** | Calculate regular, overtime, and special earnings |
| **Tax Calculations** | Compute federal, state, and local payroll taxes |
| **Deductions** | Process benefit deductions, garnishments, and voluntary deductions |
| **Payroll Integration API** | Integrate with third-party payroll providers for end-to-end processing |
| **Pay Statements** | Generate pay stubs with earnings, deductions, and tax details |
| **W-2 Processing** | Generate W-2 forms for annual tax reporting |
| **Garnishment Support** | Process court-ordered wage garnishments |
| **Retroactive Pay** | Calculate and process retroactive pay adjustments |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** US Payroll configuration uses dedicated payroll setup forms and requires the Payroll license key.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key US Payroll-related business process areas:
- **Earnings setup** (earning codes, earning statement generation)
- **Benefits and deductions** (pre-tax, post-tax, garnishments)
- **Tax setup** (federal, state, local tax authorities)
- **Pay cycle processing** (pay period generation, pay statements)
- **Payroll posting** (GL integration)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Set up payroll in Dynamics 365 Human Resources** | https://learn.microsoft.com/en-us/training/modules/set-up-payroll-dyn365-hr/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Payroll overview | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-admin-manage-payroll |
| Payroll FAQ | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-payroll-faq |
| Configure payroll positions | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-payroll-positions |
| Earning codes and earning code groups | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-payroll-earning-codes |
| Payroll parameters | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-payroll-parameters |
| Pay cycles and pay periods | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-payroll-pay-cycles |
| Benefits deducted from payroll | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-payroll-benefit-plans |
| Tax regions and tax codes | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-payroll-tax-codes |
| Generate pay statements | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-payroll-pay-statements |
| Purchase earnings statements | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-payroll-earning-statements |
| Payroll posting to General Ledger | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-payroll-posting |

---

## 5-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Payroll license key | System administration > License configuration > Payroll | Enable payroll features |
| Payroll parameters | Human resources > Setup > Payroll > Payroll parameters | Module-level settings |
| Workers with positions | Human resources > Workers / Positions | Payroll-eligible workers |
| General ledger integration | General ledger > Ledger setup | GL posting configuration |

### Phase 2: Pay Configuration

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Pay cycles | Human resources > Payroll > Pay cycles | Weekly, biweekly, monthly |
| Pay periods | (Within pay cycle) > Generate pay periods | Period calendar |
| Earning codes | Human resources > Payroll > Earning codes | Regular pay, overtime, bonus |
| Earning code groups | Human resources > Payroll > Earning code groups | Group for reporting |
| Pay groups | Human resources > Payroll > Pay groups | Group workers for processing |

### Phase 3: Tax Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Tax regions | Human resources > Payroll > Tax setup > Tax regions | Federal, state, local |
| Tax codes | Human resources > Payroll > Tax setup > Tax codes | Specific tax definitions |
| Worker tax regions | (Within worker) > Payroll > Tax regions | Assign tax jurisdictions |
| W-4 / tax withholding | (Within worker) > Payroll > Tax withholdings | Federal/state withholding elections |

### Phase 4: Benefits & Deductions

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Benefit deductions | (Within benefit plan) > Payroll mapping | Link benefits to payroll deductions |
| Garnishment types | Human resources > Payroll > Garnishments | Court-ordered withholdings |
| Garnishment setup | (Within worker) > Payroll > Garnishments | Worker-specific garnishments |
| Deduction priorities | Human resources > Payroll > Deduction priority | Processing order |

### Phase 5: Payroll Processing

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Generate earnings | Human resources > Payroll > Process payroll > Generate earnings | Create earning statements |
| Calculate pay | Human resources > Payroll > Process payroll > Calculate pay | Compute gross/net pay |
| Generate pay statements | Human resources > Payroll > Process payroll > Generate pay statements | Create pay stubs |
| Post payroll | Human resources > Payroll > Process payroll > Post payroll | Journal to GL |
| Payment journal | Human resources > Payroll > Process payroll > Payment journal | Bank payment processing |

---

## US Payroll Processing Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    US PAYROLL PROCESSING FLOW                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PAY PERIOD OPEN                                                         │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ Pay cycle: Biweekly   Period: Jan 1-14                   │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  1. GENERATE EARNINGS                                                    │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Regular hours from position/salary                      │             │
│  │ • Overtime, shift differentials                           │             │
│  │ • Bonus, commission entries                               │             │
│  │ • Retroactive pay adjustments                             │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  2. CALCULATE PAY                                                        │
│  ┌────────────────────────────────────────────────────────┐             │
│  │                                                          │             │
│  │  Gross Pay                                               │             │
│  │  ─ Pre-tax deductions (401k, HSA, medical)               │             │
│  │  = Taxable wages                                         │             │
│  │  ─ Federal income tax                                    │             │
│  │  ─ State income tax                                      │             │
│  │  ─ Local tax                                             │             │
│  │  ─ FICA (Social Security + Medicare)                     │             │
│  │  ─ Post-tax deductions (Roth 401k, garnishments)         │             │
│  │  = NET PAY                                               │             │
│  │                                                          │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  3. GENERATE PAY STATEMENTS                                              │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Employee pay stubs (earnings, deductions, net pay)      │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  4. POST & PAY                                                           │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Post to General Ledger (salary expense, liabilities)    │             │
│  │ • Generate payment journal (direct deposit / checks)      │             │
│  │ • Employer tax deposits and filings                       │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `PayrollParameters` | Payroll parameters | Setup |
| `PayrollPayCycle` | Pay cycles | Setup |
| `PayrollEarningCode` | Earning codes | Setup |
| `PayrollTaxRegion` | Tax regions | Tax Setup |
| `PayrollTaxCode` | Tax codes | Tax Setup |
| `PayrollProcessPayroll` | Process payroll | Processing |
| `PayrollEarningStatement` | Earning statements | Statements |
| `PayrollPayStatement` | Pay statements | Statements |
| `PayrollGarnishment` | Garnishments | Deductions |
| `PayrollPostPayroll` | Post payroll | GL Integration |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Payroll license key** must be enabled before payroll menus appear
2. **Pay cycles and periods** must be generated before payroll processing
3. **Earning codes** must be set before generating earnings
4. **Tax regions and codes** must be configured before tax calculation
5. **Worker tax withholdings** (W-4) must be entered for proper tax calculation
6. **Benefits-to-payroll mapping** must be complete for deduction processing
7. **Deduction priority** determines the order deductions are taken (important for garnishments)
8. **Payroll must be posted** to GL before financial reporting reflects payroll

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Payroll features not visible" | License key not enabled | Enable payroll license key |
| "No earnings generated" | Worker not in pay group or position inactive | Check pay group and position status |
| "Tax calculation error" | Tax region/code missing for worker | Assign tax regions and withholdings |
| "Deduction exceeds net pay" | Mandatory deductions exceed earnings | Review deduction priority order |
| "GL posting imbalance" | Posting accounts not configured | Set up payroll posting accounts |
| "Garnishment priority conflict" | Federal/state garnishment ordering | Follow statutory priority rules |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **US Payroll** module.

### Hire to retire

*154 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze HR programs | 14 | — |
| Develop people strategy | 20 | — |
| Manage compensation and benefits | 29 | — |
| Manage performance and growth | 39 | — |
| Manage time and attendance | 6 | — |
| Manage workplace compliance | 16 | — |
| Offboard talent | 12 | — |
| Recruit and onboard talent | 18 | — |

