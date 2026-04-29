---
name: d365-documentation
description: Use after Phase 2 validation passes to generate the two final HTML deliverables — `Documentation/html/rollout-report.html` (full project narrative) and `Documentation/html/environment-config.html` (visual environment reference). Both are single-file HTML documents with embedded CSS/JS, professional styling, and interactive elements (collapsible sections, diagrams, tables). This is Phase 3 of the implementation lifecycle. Pull data exclusively from Phase 1 and Phase 2 artefacts — never invent.
---

# Documentation Generation (Phase 3)

> Single-file HTML, embedded CSS/JS, **no external runtime dependencies**.

## Inputs (read-only — never invent)
- `Documentation/requirement-profile.md`, `requirement-matrix.json`
- `Documentation/config-{module}.md`, `parameter-settings.md`
- `Documentation/rollout-plan.md`, `e2e-test-plan.md`, `test-scenarios.json`
- `Documentation/validation-report.md`, `gap-resolutions.md`
- `Documentation/deployment-log.md`, `e2e-test-results.md`
- `ChallengeJournal/challenge_journal.json`
- Module `.md` knowledge files (for environment-config visualisation)

## Outputs
| File | Purpose |
|---|---|
| `Documentation/html/rollout-report.html` | Full project narrative |
| `Documentation/html/environment-config.html` | Visual environment reference |

---

## Step 3.1 — `rollout-report.html`

Sections (in order):
1. **Project overview** — scope, modules, timeline (from requirement profile).
2. **Requirements** — categorised matrix (Standard / Migration / Parameter / Workflow / Integration / Gap / Clarification).
3. **Configuration design** — per-module summaries with key DMF templates and parameter settings.
4. **Deployment** — module-by-module log + tool counts (data / form / action).
5. **Testing** — every E2E scenario with pass/fail per step.
6. **Challenges & resolutions** — pulled from `challenge_journal.json`.
7. **Appendices** — links to source artefacts, glossary, contact list.

Styling:
- Embedded CSS: clean type, generous whitespace, sticky TOC, collapsible sections.
- Charts (inline SVG): module count, test pass rate, deployment-tool mix.
- All assets inline — works offline.

## Step 3.2 — `environment-config.html`

Sections:
1. **Org hierarchy** — legal entities → operating units → departments (D3 tree or inline SVG).
2. **Chart of accounts** — main accounts grouped, dimensions, posting profiles.
3. **Module cards** — one card per deployed sub-module: status, key parameters, key entities, tool mix.
4. **Integration map** — OData endpoints, dual-write tables, custom APIs (`api_find_actions` results).
5. **Security roles** — roles in scope and what they grant.

Styling:
- Visual-first; minimise prose.
- Card grid with status badges (✅ ⚠️ ❌).
- Expandable detail per card.

## Quality gate (both files)
- [ ] Every figure traces to a Phase 1 / Phase 2 artefact.
- [ ] Open in a vanilla browser with no network — must render fully.
- [ ] No `<script src="…">` referencing external URLs.
- [ ] Print stylesheet works.
