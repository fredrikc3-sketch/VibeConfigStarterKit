---
name: fo-mcp-server
description: Use when interacting with a Dynamics 365 Finance & Operations environment through the Dynamics 365 ERP MCP server — i.e. whenever a `data_*`, `form_*`, or `api_*` MCP tool call is planned. Covers tool selection hierarchy, naming conventions, OData/SQL querying, form navigation, action invocation, prerequisites (feature flag, allowed clients, version requirements), and the dynamic-vs-static server distinction. Read BEFORE the first tool call of any deployment, validation, or data-exploration task.
---

# Dynamics 365 ERP MCP Server — Interaction Skill

Authoritative rules for working with the **Dynamics 365 ERP MCP server** (the new *dynamic* server). Built from the official Microsoft Learn guidance: <https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp>.

> **Static vs Dynamic**: The legacy "static" Dynamics 365 ERP MCP server (13 fixed tools, Dataverse-connector-based) is **retired in 2026**. All guidance below targets the **dynamic** server. If you encounter the static server, migrate.

For a deeper drill-down see `tools-reference.md` (full tool catalogue) and `prerequisites.md` (environment + licensing setup).

---

## 1 · Role

Act as an **autonomous data-entry agent**. Each task is a workflow — execute one step at a time, reflect on the result of every tool call, and continue until the objective is met or an unrecoverable error blocks progress.

---

## 2 · The Three Tool Categories

| Category | Prefix | Purpose |
|----------|--------|---------|
| **Data tools** | `data_*` | Standard CRUD against data entities (OData / SQL). Most efficient for bulk operations. |
| **Form tools** | `form_*` | Navigate server-side form view models — exactly what a user would do in the client, but through APIs. |
| **Action tools** | `api_*` | Find and invoke X++ classes that implement `ICustomAPI` (custom business logic exposed as AI tools). |

Tool names appear bare (e.g. `data_find_entity_type`). Some hosts namespace them (e.g. `mcp_finance_opera_data_find_entity_type`); use whichever form the host exposes.

---

## 3 · Tool Selection Hierarchy (MANDATORY)

```
Priority 1 — DATA TOOLS
  → All standard CRUD against entities
  → Fastest, fewest tool calls, bulk-capable
  → Required first attempt for any create/read/update/delete

Priority 2 — FORM TOOLS
  → Use only when:
    a) data tools cannot do it (no entity, calculated field, action button), OR
    b) the user explicitly requests UI-style interaction

Priority 3 — ACTION TOOLS
  → Activate / Publish / Generate / Post and other X++ business logic
  → Anything exposed via ICustomAPI (visible in CustomApiTable form)
```

**Never** use form tools for plain CRUD if a data entity exists. Add module-level guidance in agent instructions when the agent picks the wrong tier.

---

## 4 · Data Tool Rules

### Pre-flight (always)
1. `data_find_entity_type` — confirm the entity exists. The tool returns multiple top hits; pick the right one yourself.
2. `data_get_entity_metadata` — fetch field schema. **Required** before `data_create_entities`, `data_update_entities`, `data_delete_entities`, `data_find_entities`, `data_find_entities_sql`.

### Querying
- **OData path**: `data_find_entities` (legacy, still supported).
- **SQL path**: `data_find_entities_sql` — replaces `data_find_entities` from F&O **10.0.48** onward. Prefer SQL when available.
- **25-row response cap** — if a result is exactly 25 rows, treat it as truncated and apply a tighter filter.

### Naming
| Rule | Example correct | Example wrong |
|------|-----------------|---------------|
| Entity sets are **plural** | `SalesOrderHeaders` | `SalesOrderHeader` |
| V2+ entities — plural goes **before** the V suffix | `SalesOrderHeadersV2` | `SalesOrderHeaderV2s` |

### Operation rules
- **No deep insert** — create parent, then children, in separate calls.
- **Enum filter syntax**: `$filter=Style has Namespace.Pattern'Yellow'`.
- **Enum value setting**: same `Namespace.Pattern'Value'` form on writes.
- Always verify writes by re-reading the affected records.

---

## 5 · Form Tool Rules

Use **internal names**, never display labels — for menu items, controls, tabs, and grid columns.

### Standard create flow
```
form_find_menu_item    → Locate menu item by internal name
form_open_menu_item    → Open the form
form_click_control     → Click "New"
form_set_control_values → Set fields (skip lookup-driven fields)
form_open_lookup       → For each lookup-driven field, then select
form_save_form         → Persist
```

### Update / inquiry flow
```
form_filter_form / form_filter_grid → Narrow rows
form_select_grid_row                → Select target row
form_set_control_values             → Apply changes
form_save_form                      → Persist
```

### Other rules
- Never ask the user for menu item *type* — `form_find_menu_item` groups types automatically.
- Skip optional parameters when no value is supplied.
- Date filter literal: `(lessThanDate(x:int))` is valid for grid date columns.
- 25-row cap also applies to `form_*` responses returning grid state.

### Form tool catalogue (12)
`form_click_control`, `form_close_form`, `form_filter_form`, `form_filter_grid`, `form_find_controls`, `form_find_menu_item`, `form_open_lookup`, `form_open_menu_item`, `form_open_or_close_tab`, `form_save_form`, `form_select_grid_row`, `form_set_control_values`, `form_sort_grid_column`.

---

## 6 · Action Tool Rules

```
api_find_actions   → Discover available ICustomAPI actions for current security role
api_invoke_action  → Execute a specific action with parameters
```

If the action you need is not exposed via API, fall back to clicking the equivalent button on the form.

---

## 7 · Dynamic Context & Security

The dynamic MCP server returns the **same view model** the client renders, filtered by the authenticated agent's security role:
- `data_find_entity_type` returns only entities the role can access.
- `form_find_menu_item` returns only menu items the role can open.
- `api_find_actions` returns only actions the role can invoke.

Forbidden calls fail at the server. Granting/restricting access is a **security-role** problem, not an MCP problem.

---

## 8 · Reasoning & Execution Protocol

### Before every tool call
1. State what you intend to do and why.
2. Check the relevant module's `.md` knowledge file for documented rules and discoveries.
3. Check `ChallengeJournal/challenge_journal.json` for prior failures of the same operation.

### After every tool call
1. Did it succeed? Did the response contain the expected shape?
2. Is the objective met? If not, what's the next step?
3. If it failed: capture the exact error verbatim, classify it, log it (see §10), and adjust.

### Non-negotiables
- **Never rely on general knowledge** for live data — always query the system.
- **Never substitute** on failure (e.g., reading existing records when asked to create new ones).
- **Never stop early** — continue until the goal is reached or the error is truly unrecoverable.
- **Think out loud** — narrate the plan and the verification at every step.

---

## 9 · Failure Handling

```
ON FAILURE:
  1. Read the module .md knowledge file FIRST
     — Critical Configuration Rules
     — Implementation Discoveries
  2. Capture the exact error message
  3. Classify:
     — Missing prerequisite     → deploy prerequisite, retry
     — Invalid value            → fix source data file, retry
     — Entity not found         → fall back to form tools
     — Permission denied        → check security role
     — Duplicate key            → switch from create to update
  4. Log to Challenge Journal (use the reinforcement-learning skill)
  5. Update source files if the fix changed deployed state
  6. Retry
```

---

## 10 · Dry-Run Mode

> Mandatory before the first live mutation of any new module on a new environment, and on demand whenever the user asks for a "dry run" or "plan only".

When the orchestrator (or user) sets `mode = dry-run`:

1. **Read-only tools execute normally** — `data_find_*`, `data_get_entity_metadata`, `form_find_menu_item`, `api_find_actions` all proceed.
2. **Mutating tools are NOT called.** Instead, the agent records the *planned* call to `Documentation/_status/<phase>/<module>.dry-run.jsonl` as one JSON line per intent:
   ```json
   {"step":12,"tool":"data_create_entities","entitySet":"LedgerJournalHeadersV2","payloadHash":"sha1:...","payloadSummary":"1 record, fields: JournalNum,JournalName"}
   ```
3. The agent narrates each planned mutation in the response: "Would POST 1 record to `LedgerJournalHeadersV2` with JournalNum=USMF-001."
4. After all planned calls are recorded, the agent asks the user to **approve** before re-running with `mode = live`.
5. In live mode, the agent reads the dry-run file and replays the calls in order — each successful live call appends `{...,"status":"executed"}` to the same file for audit.

Mutating tools that MUST be intercepted in dry-run: `data_create_entities`, `data_update_entities`, `data_delete_entities`, `form_click_control` (when control is Save/Post/Activate/Confirm), `form_save_form`, `api_invoke_action`.

---

## 11 · Quick-Reference Card

```
┌──────────────────────────────────────────────────────────────────┐
│  D365 ERP MCP — QUICK REFERENCE                                  │
│                                                                  │
│  CRUD / bulk         → DATA tools  (Priority 1)                  │
│  UI-only / actions   → FORM tools  (Priority 2)                  │
│  X++ business logic  → ACTION tools (Priority 3)                 │
│                                                                  │
│  Pre-flight: find_entity_type → get_entity_metadata              │
│  Names:      plural; HeadersV2 (not HeaderV2s)                   │
│  No deep insert. Parent first, then children.                    │
│  Enums:      Namespace.Pattern'Value'                            │
│  Forms:      internal NAMES, never labels                        │
│  Result cap: 25 rows → assume truncated, narrow filter           │
│  SQL:        data_find_entities_sql (10.0.48+) preferred         │
│                                                                  │
│  Prerequisites: feature flag ON, F&O ≥ 10.0.47, Tier 2+,         │
│                 client added to "Allowed MCP clients" list       │
└──────────────────────────────────────────────────────────────────┘
```

See `prerequisites.md` for environment setup and licensing details, `tools-reference.md` for the full tool catalogue.
