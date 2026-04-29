---
name: d365-documentation
description: Use after Phase 2 validation passes to generate the Phase 3 HTML deliverable suite under `Documentation/html/`. Produces seven single-file HTML documents — two narrative reports (`rollout-report.html`, `environment-config.html`) plus five interactive dashboards (`test-results.html`, `challenge-journal.html`, `process-catalogue.html`, `dependency-graph.html`, `run-state.html`). All seven are self-contained — embedded CSS/JS, no external network calls, professional styling, interactive elements (collapsible sections, search/filter, diagrams). Pull data exclusively from Phase 1 / Phase 2 artefacts and from the canonical JSON files under `Modules/`, `ChallengeJournal/`, `Documentation/` — never invent.
---

# Documentation Generation (Phase 3)

> Single-file HTML, embedded CSS/JS, **no external runtime dependencies**.

## Inputs (read-only — never invent)
- `Documentation/requirement-profile.md`, `requirement-matrix.json`
- `Documentation/config-{module}.md`, `parameter-settings.md`
- `Documentation/rollout-plan.md`, `e2e-test-plan.md`, `test-scenarios.json`
- `Documentation/validation-report.md`, `gap-resolutions.md`
- `Documentation/deployment-log.md`, `e2e-test-results.md`
- `Documentation/run-state.json`
- `Documentation/_status/<phase>/<module>.json` (per-worker status files)
- `ChallengeJournal/challenge_journal.json`
- `Modules/dependency-graph.json`
- `Business Process/ProcessCatalogue.json`, `ProcessCatalogue_flat.json`
- Module `.md` knowledge files (for environment-config visualisation)

## Outputs
| File | Purpose | Type |
|---|---|---|
| `Documentation/html/rollout-report.html` | Full project narrative | Narrative |
| `Documentation/html/environment-config.html` | Visual environment reference | Narrative |
| `Documentation/html/test-results.html` | E2E test results dashboard | Dashboard |
| `Documentation/html/challenge-journal.html` | Searchable journal browser + KPIs | Dashboard |
| `Documentation/html/process-catalogue.html` | APQC process catalogue explorer | Dashboard |
| `Documentation/html/dependency-graph.html` | Visual deployment-wave graph | Dashboard |
| `Documentation/html/run-state.html` | Live deployment progress view | Dashboard |
| `Documentation/html/index.html` | Landing page linking all seven deliverables | Index |

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

Styling: clean type, generous whitespace, sticky TOC, collapsible sections, inline SVG charts. All assets inline — works offline.

## Step 3.2 — `environment-config.html`

Sections:
1. **Org hierarchy** — legal entities → operating units → departments (inline SVG tree).
2. **Chart of accounts** — main accounts grouped, dimensions, posting profiles.
3. **Module cards** — one card per deployed sub-module: status, key parameters, key entities, tool mix.
4. **Integration map** — OData endpoints, dual-write tables, custom APIs (`api_find_actions` results).
5. **Security roles** — roles in scope and what they grant.

Styling: visual-first; card grid with status badges (✅ ⚠️ ❌); expandable detail per card.

---

## Step 3.3 — `test-results.html` (Dashboard)

Source: `Documentation/e2e-test-results.md`, `Documentation/test-scenarios.json`, per-module status files in `Documentation/_status/2.2/`.

Required UI:
- **KPI strip**: total scenarios, passed, failed, pending; pass-rate %; total step count.
- **Module filter** (multi-select chip bar) and **status filter** (✅ / ❌ / ⏸).
- **Free-text search** across scenario name and step text.
- **Scenario grid**: one row per scenario showing module, scenario id, status, step pass/fail mini-bar, journal links.
- **Drill-down**: clicking a row expands an accordion showing per-step expected vs actual + linked journal entries.
- **Charts** (inline SVG): pass-rate per module, failures by category, retry count distribution.

Embed all data as a JSON `<script type="application/json" id="data">` block; render with vanilla JS. No frameworks.

## Step 3.4 — `challenge-journal.html` (Dashboard)

Source: `ChallengeJournal/challenge_journal.json` (schema `schemas/challenge-journal.schema.json`, v2.0).

Required UI:
- **KPI cards**: total entries, open, investigating, resolved, superseded; `_metadata.kpi.preventedRecurrences`; `_metadata.kpi.averageTimeToResolveMinutes`; recurrence rate (entries with `recurrenceCount > 1`).
- **Filters**: module, phase, category, severity, status, projectId.
- **Search**: matches across `symptom.operation`, `rootCause`, `resolution.summary`.
- **Entry list** (left) + **detail pane** (right). Detail pane shows full entry with collapsible sections, plus a **supersede chain ribbon** if `supersedes`/`supersededBy` are present.
- **Trend chart**: entries created per week (inline SVG).
- **"Most-prevented"** leaderboard: top N entries by `preventionEffective.preventedCount`.

## Step 3.5 — `process-catalogue.html` (Dashboard)

Source: `Business Process/ProcessCatalogue.json` (5,767 items, hierarchical) + `ProcessCatalogue_flat.json` for fast search.

Required UI:
- **Tree view** (lazy-rendered; collapse/expand by parent) with breadcrumb on the right.
- **Search** with debounce, highlighting matches in the tree.
- **APQC code overlay** — show APQC PCF id next to each leaf when available.
- **Module mapping badge** — for each process, show which D365 module(s) implement it (cross-ref module knowledge files).
- **"In-scope filter"** — toggles to only show processes that have a configured module.

Performance: must render the full 5,767-item tree without freezing — use virtual scrolling (intersection observer) for the visible window.

## Step 3.6 — `dependency-graph.html` (Dashboard)

Source: `Modules/dependency-graph.json`.

Required UI:
- **Wave swimlane** — vertical lanes for waves 1–10; modules as cards inside each lane.
- **Edges** between cards drawn as inline SVG curves following `dependsOn`.
- **Hover card** showing module name, DMF seq, dependsOn, executionMode, knowledge-file path.
- **Legend** for parallel vs serialized waves.
- **Critical-path highlight** — option to highlight the longest dependency chain.

## Step 3.7 — `run-state.html` (Dashboard)

Source: `Documentation/run-state.json` (schema `schemas/run-state.schema.json`).

Required UI:
- **Header**: project id, environment fingerprint, start time, last update, current wave.
- **Wave progress bar** for all waves, segmented by `complete | failed | skipped-idempotent | pending | in-progress`.
- **Module table**: each module's `desiredStateHash`, `deployedStateHash`, status, last attempt time, retry count.
- **Failure callouts** — banner for any `failed` module with its journal entry id linked to `challenge-journal.html`.
- **Resume hint** — if status indicates an interrupted run, show the explicit `python tools/...` (or skill invocation) needed to resume.

Note: this is a **snapshot** rendered at Phase 3. Live updates are out of scope; re-run the documentation skill to refresh.

## Step 3.8 — `index.html` (Landing page)

Single landing page under `Documentation/html/index.html` linking all seven deliverables with one-line descriptions, generation timestamp, and project id (if present).

---

## Quality gate (every file)
- [ ] Every figure traces to a Phase 1 / Phase 2 artefact (no invention).
- [ ] Open in a vanilla browser with no network — must render fully.
- [ ] No `<script src="…">` referencing external URLs; no `<link rel="stylesheet" href="http…">`.
- [ ] Embedded data uses `<script type="application/json">` blocks, not inline JS literals (keeps payload diffable).
- [ ] Print stylesheet works (for narrative reports).
- [ ] Single file ≤ 8 MB; if a dashboard exceeds this (e.g. process-catalogue), apply minification and JSON dedup.
- [ ] Accessibility: semantic HTML, focus styles, keyboard navigation for tree/list views, aria-labels on chart SVGs.

## Skip conditions
If the source artefact for a dashboard is missing or empty (e.g. no `e2e-test-results.md` because Phase 2 was skipped), generate a stub HTML with a clear "Source not available" message and a list of required inputs. Do NOT fail Phase 3 outright.
