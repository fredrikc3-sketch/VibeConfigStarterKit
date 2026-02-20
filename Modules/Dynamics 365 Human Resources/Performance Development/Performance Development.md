# Performance Development Module - Knowledge Source

> This file is the central knowledge hub for **Performance Development** within Dynamics 365 Human Resources.

---


---


> **Microsoft Learn Reference:** [Performance Development](https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-develop-performance-management-overview)

## Module Overview

Performance Development in Dynamics 365 Human Resources supports employee performance management through goal setting, performance reviews, competency mapping, and skills gap analysis. It helps organizations align individual goals with business objectives and support career development planning.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Goal Setting** | Define SMART goals aligned with organizational objectives |
| **Performance Reviews** | Conduct structured performance appraisals with rating models |
| **Competency Management** | Define and track worker competencies and skill levels |
| **Skills Gap Analysis** | Identify gaps between required and actual worker skills |
| **Development Plans** | Create individual development plans for career growth |
| **360-Degree Feedback** | Collect feedback from managers, peers, and direct reports |
| **Performance Journal** | Maintain ongoing performance notes and achievements |
| **Compensation Link** | Connect performance ratings to compensation decisions |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Performance management uses dedicated goal and review forms.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Performance Development-related business process areas:
- **Performance goals** (individual and team objectives)
- **Performance reviews** (annual/semi-annual review cycles)
- **Competency management** (skills assessment and development)
- **Performance journals** (ongoing note-taking and feedback)
- **Development plans** (career growth activities)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Manage performance in Dynamics 365 Human Resources** | https://learn.microsoft.com/en-us/training/modules/manage-performance-dyn365-hr/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Performance management | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-develop-performance-management-overview |
| Performance goals | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-develop-performance-goals |
| Performance reviews | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-develop-performance-reviews |
| Performance journal | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-develop-performance-journal |
| Competencies | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-develop-performance-competencies |
| Skills | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-develop-skills |

---

## 3-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Workers and positions | Human resources > Workers / Positions | Participants and hierarchy |
| Position hierarchy | Human resources > Positions > Position hierarchy | Manager-report relationships |
| Competency models | Human resources > Setup > Competencies | Skills, education, certificates |

### Phase 2: Goal & Review Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Goal types | Human resources > Performance > Goals > Goal types | Categorize objectives |
| Performance goals | Human resources > Performance > Goals | Create goal templates |
| Review templates | Human resources > Performance > Reviews > Review templates | Standardize review format |
| Review periods | Human resources > Performance > Reviews > Review periods | Annual, semi-annual cycles |
| Rating levels | Human resources > Performance > Reviews > Rating levels | Rating scale (1-5, etc.) |

### Phase 3: Execution & Tracking

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Assign goals to workers | (Within goals or ESS) | Individual goal assignment |
| Performance journal entries | (Via ESS or direct entry) | Ongoing notes and feedback |
| Create performance reviews | Human resources > Performance > Reviews | Initiate review process |
| Self-assessment | (Employee self service) | Employee self-rating |
| Manager review | (Manager self service) | Manager evaluation |
| Review sign-off | (Within review) > Complete | Finalize review cycle |

---

## Performance Management Cycle

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  PERFORMANCE MANAGEMENT CYCLE                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│                    ┌─────────────────┐                                   │
│                    │  GOAL SETTING    │                                   │
│                    │  (Start of year) │                                   │
│                    └────────┬────────┘                                   │
│                             │                                            │
│               ┌─────────────▼─────────────┐                             │
│               │   ONGOING FEEDBACK          │                             │
│               │   (Throughout year)          │                             │
│               │   • Performance journal      │                             │
│               │   • 1:1 discussions           │                             │
│               │   • Competency development   │                             │
│               └─────────────┬───────────────┘                             │
│                             │                                            │
│                    ┌────────▼────────┐                                   │
│                    │  MID-YEAR        │                                   │
│                    │  CHECK-IN        │                                   │
│                    │  (Optional)      │                                   │
│                    └────────┬────────┘                                   │
│                             │                                            │
│               ┌─────────────▼─────────────┐                             │
│               │   ANNUAL REVIEW             │                             │
│               │   ┌──────────────────┐      │                             │
│               │   │ 1. Self-assessment│      │                             │
│               │   │ 2. Manager review │      │                             │
│               │   │ 3. Rating         │      │                             │
│               │   │ 4. Sign-off       │      │                             │
│               │   └──────────────────┘      │                             │
│               └─────────────┬───────────────┘                             │
│                             │                                            │
│               ┌─────────────▼─────────────┐                             │
│               │   DEVELOPMENT PLANNING      │                             │
│               │   • Training enrollment      │                             │
│               │   • Skill gap closure         │                             │
│               │   • Career path planning     │                             │
│               └─────────────┬───────────────┘                             │
│                             │                                            │
│                    ┌────────▼────────┐                                   │
│                    │  COMPENSATION    │                                   │
│                    │  DECISIONS       │                                   │
│                    │  (Merit, bonus)  │                                   │
│                    └─────────────────┘                                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `HcmGoal` | Performance goals | Goals |
| `HcmGoalType` | Goal types | Setup |
| `HcmPerformanceReview` | Performance reviews | Reviews |
| `HcmReviewTemplate` | Review templates | Setup |
| `HcmReviewPeriod` | Review periods | Setup |
| `HcmPerformanceJournal` | Performance journal | Tracking |
| `HcmCompetency` | Competencies | Development |
| `HcmRatingLevel` | Rating levels | Setup |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Position hierarchy** must reflect correct manager relationships
2. **Competency models** should be defined before reviews reference them
3. **Goal types** must exist before goals can be created
4. **Review templates** must be configured before creating reviews
5. **Review periods** define the cycle timeline
6. **Rating levels** must be defined before managers can rate
7. **Goals should be set** before the review period begins

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "No goals assigned" | Goals not created for worker | Create and assign goals |
| "Review template missing" | Template not configured | Create review template |
| "Manager cannot access review" | Position hierarchy incorrect | Fix reporting relationship |
| "Rating not available" | Rating levels not defined | Configure rating levels |
| "Review period closed" | Outside active review period | Adjust review period dates |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Performance Development** module.

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

