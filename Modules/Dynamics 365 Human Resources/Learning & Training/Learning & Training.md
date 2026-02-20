# Learning & Training Module - Knowledge Source

> This file is the central knowledge hub for **Learning & Training** within Dynamics 365 Human Resources.

---


---


> **Microsoft Learn Reference:** [Learning & Training](https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-course-overview)

## Module Overview

Learning & Training in Dynamics 365 Human Resources manages employee training courses, certifications, and learning programs. It integrates with Learning Management Systems (LMS) via APIs to track course enrollment, completion, and compliance training requirements.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Course Management** | Create and manage training courses with schedules and locations |
| **Course Enrollment** | Enroll employees in courses individually or in bulk |
| **Certification Tracking** | Track employee certifications and renewal requirements |
| **Training Compliance** | Ensure mandatory training completion for regulatory compliance |
| **LMS Integration** | Integrate with external learning management systems via APIs |
| **Skills Development** | Link courses to skill development and competency gaps |
| **Training Reports** | Report on course completion rates and training effectiveness |
| **Instructor Management** | Manage instructors, rooms, and training resources |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Learning and training configuration uses dedicated course management forms.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Learning & Training-related business process areas:
- **Course management** (create and manage training courses)
- **Course enrollment** (register participants)
- **Instructor management** (assign instructors)
- **Training compliance** (mandatory training tracking)
- **Certificates and skills** (competency tracking)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Create training courses in Dynamics 365 Human Resources** | https://learn.microsoft.com/en-us/training/modules/create-training-courses-dyn365-hr/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Courses overview | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-course-overview |
| Set up training courses | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-learning-courses |
| Questionnaires | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-learning-questionnaires |
| Skills and certificates | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-develop-skills |
| Competencies | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-develop-performance-competencies |
| Job and position skills | https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-develop-skills#jobs-and-positions |

---

## 3-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Workers | Human resources > Workers | Participants |
| Locations / rooms | Organization administration > Locations | Training venues |
| Skill types | Human resources > Setup > Competencies > Skill types | Skill categorization |

### Phase 2: Course Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Course types | Human resources > Learning > Course types | Categorize courses (safety, soft skills, etc.) |
| Course groups | Human resources > Learning > Course groups | Group courses for reporting |
| Course locations | Human resources > Learning > Locations | Training rooms / venues |
| Instructors | Human resources > Learning > Instructors | Assign qualified instructors |
| Courses | Human resources > Learning > Courses | Define courses (description, dates, capacity) |
| Course sessions | (Within course) > Sessions | Schedule specific sessions |

### Phase 3: Enrollment & Tracking

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Open for registration | (Within course) | Enable enrollment |
| Register participants | (Within course) > Participants | Enroll workers |
| Course completion | (Within course) > Status | Mark completion status |
| Skills update | (Automatic or manual) | Update worker skill profile |
| Certificates | Human resources > Workers > (worker) > Certificates | Issue completion certificates |

---

## Learning & Training Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    LEARNING & TRAINING FLOW                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  COURSE SETUP                                                            │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Define course type and group                           │             │
│  │ • Set dates, location, instructor                        │             │
│  │ • Set minimum/maximum participants                       │             │
│  │ • Define agenda and sessions                             │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  ENROLLMENT                                                              │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Open registration                                      │             │
│  │ • HR assigns mandatory attendees                         │             │
│  │ • Employees self-enroll (via ESS)                        │             │
│  │ • Waitlist management                                    │             │
│  └────────────────────────────────────────────────────────┘             │
│                              │                                           │
│                              ▼                                           │
│  DELIVERY                                                                │
│  ┌────────────────────────────────────────────────────────────┐         │
│  │ Classroom  │  Virtual (Teams/Zoom)  │  E-Learning (LMS)     │         │
│  └────────────────────────────────────────────────────────────┘         │
│                              │                                           │
│                              ▼                                           │
│  COMPLETION & CERTIFICATION                                              │
│  ┌────────────────────────────────────────────────────────┐             │
│  │ • Mark attendance and completion                         │             │
│  │ • Update skills / competency records                     │             │
│  │ • Issue certificates (with expiry)                       │             │
│  │ • Questionnaires / assessments                           │             │
│  └────────────────────────────────────────────────────────┘             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `HRMCourseTable` | Courses | Learning |
| `HRMCourseType` | Course types | Setup |
| `HRMCourseGroup` | Course groups | Setup |
| `HRMCourseInstructor` | Instructors | Setup |
| `HRMCourseLocation` | Course locations | Setup |
| `HcmSkill` | Skills | Competencies |
| `HcmCertificate` | Certificates | Competencies |
| `KMQuestionnaireStatistics` | Questionnaires | Assessment |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Course types and groups** must be defined before creating courses
2. **Locations and instructors** must exist before assigning to courses
3. **Course must be in "Open" status** for enrollment
4. **Maximum participants** controls enrollment capacity
5. **Skills** must be defined before they can be updated on completion
6. **Certificates with expiry dates** need renewal tracking processes

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Course is full" | Maximum capacity reached | Increase capacity or add session |
| "Registration closed" | Course not in Open status | Change course status to Open |
| "Instructor conflict" | Instructor scheduled for another course | Reassign instructor |
| "Certificate expired" | Renewal not completed | Re-enroll in refresher course |
| "Skill not updated" | Completion not recorded | Mark course participation as complete |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Learning & Training** module.

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

