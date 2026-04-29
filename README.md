<p align="center">
  <img src="Media/FinanceOperations_scalable.svg" alt="Dynamics 365 Finance & Operations" width="72">
</p>

<h1 align="center">Dynamics 365<br><sub>Finance & Operations</sub></h1>

<p align="center"><strong>Implementation Accelerator — Skills Edition</strong></p>

<p align="center">
An AI-driven workspace for configuring, deploying, and documenting Dynamics 365 Finance & Operations environments — built on the <strong>Anthropic Skills</strong> architecture and the official <strong>Dynamics 365 ERP MCP server</strong>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-2.2-blue" alt="Version 2.2">
  <img src="https://img.shields.io/badge/architecture-Skills%20%2B%20Sub--Agents-7c3aed" alt="Skills + sub-agents">
  <img src="https://img.shields.io/badge/skills-13-2563eb" alt="13 skills">
  <img src="https://img.shields.io/badge/layers-4-2563eb" alt="4 layers">
  <img src="https://img.shields.io/badge/modules-47-059669" alt="47 modules">
  <img src="https://img.shields.io/badge/DMF_templates-24-059669" alt="24 DMF templates">
</p>

---

## What this is

A structured, AI-readable knowledge base that turns D365 F&O implementations from consultant memory + scattered spreadsheets into a repeatable, self-improving process. Every capability lives in a **Skill** — a small `SKILL.md` with YAML frontmatter that the AI loads on demand.

## Why Skills?

Traditional copilot instruction files dump everything into the always-loaded base context. **Skills** use **progressive disclosure**: only each skill's `description` is permanently visible. The full body loads only when the task matches. The result:

- Smaller always-loaded context → faster, cheaper turns.
- Each capability evolves independently — no monolithic instruction file to grow forever.
- Industry-standard, model-agnostic format (Anthropic Skills).

## Architecture: 4-Layer Orchestration

The big change in v2.1 is **multi-layer orchestration with sub-agent delegation**. Per-module work — config building, deployment, validation — is dispatched to sub-agents that load only their own module's knowledge. The main agent's context stays small even on a project with 25+ modules.

**v2.2 council-driven hardening** layers on top:

- **Canonical JSON Schemas** in [`schemas/`](schemas/) for journal entries, DMF templates, run-state, dependency graph and the fan-out worker contract — enforced by `tools/validate_repo.py` and a CI quality gate.
- **Single-source-of-truth dependency graph** at [`Modules/dependency-graph.json`](Modules/dependency-graph.json). Skills derive waves from this file, no more hand-rolled wave lists.
- **Concurrent-write safety**: workers write per-module artefacts under `Documentation/_status/<phase>/<module>.json`; the orchestrator merges into shared MD files after each wave.
- **Resumable runs** via `Documentation/run-state.json` — environment fingerprint check prevents wrong-env disasters; `desiredStateHash` enables idempotent retries and partial-redeploy.
- **Sub-agent guards** on all worker descriptions plus an explicit dry-run mode in [`fo-mcp-server`](skills/fo-mcp-server/SKILL.md).
- **Smarter RL loop**: dedup hashes, supersede chains, prevention KPIs and project-id namespacing.

```
Layer 0  phase-orchestrator           classify request, check gates, pick phase
            │
Layer 1  phase skill                  d365-config-builder │ d365-deployment │ d365-validation-testing │ …
            │ identifies in-scope modules, builds dispatch table
Layer 2  module-fanout                spawns one sub-agent per module
            │ parallel within DMF ExecutionUnit, sequential across
Layer 3  worker skill (sub-agent)     module-config-worker │ module-deployment-worker │ module-validation-worker
            │ each loads ONLY its assigned module's knowledge
Layer 4  leaf skills                  fo-mcp-server │ reinforcement-learning │ d365-knowledge-routing
```

### Why not promote each module to a skill?

Tempting — but wrong. Skills are *capabilities*; modules are *reference knowledge*. Promoting all 47 modules to skills would push 47 always-loaded `description` blocks into every turn, even on tasks that touch zero modules. The optimal pattern is:

1. **`d365-knowledge-routing`** as the lookup index (already in place).
2. **Sub-agent fan-out** so each module's deep knowledge is loaded only in the sub-agent that needs it.

This keeps the orchestrator lean and parallelizes the work — large multi-module projects scale almost linearly with concurrency.

## The 13 skills

### Orchestration (Layers 0 & 2)
| Skill | Purpose |
|---|---|
| [`phase-orchestrator`](skills/phase-orchestrator/SKILL.md) | Classify any user request, check prerequisite gates, dispatch to the right phase skill |
| [`module-fanout`](skills/module-fanout/SKILL.md) | Pattern + contract for spawning per-module sub-agents (parallel within wave, sequential across) |

### Phase skills (Layer 1)
| Skill | Purpose |
|---|---|
| [`d365-requirements-analysis`](skills/d365-requirements-analysis/SKILL.md) | Phase 1.1 — ingest `Requirements/`, classify, build profile + matrix |
| [`d365-config-builder`](skills/d365-config-builder/SKILL.md) | Phase 1.2–1.5 — config files, rollout plan, test plan, approval gate. **Fans out to `module-config-worker`.** |
| [`d365-deployment`](skills/d365-deployment/SKILL.md) | Phase 2.1 — deploy via MCP. **Fans out to `module-deployment-worker`** in DMF dependency waves. |
| [`d365-validation-testing`](skills/d365-validation-testing/SKILL.md) | Phase 2.2 — E2E tests + fix loop. **Fans out to `module-validation-worker`.** |
| [`d365-documentation`](skills/d365-documentation/SKILL.md) | Phase 3 — single-file HTML deliverables |

### Worker skills (Layer 3 — run in sub-agents)
| Skill | Purpose |
|---|---|
| [`module-config-worker`](skills/module-config-worker/SKILL.md) | Build all config artefacts for ONE module |
| [`module-deployment-worker`](skills/module-deployment-worker/SKILL.md) | Deploy ONE module to F&O via MCP |
| [`module-validation-worker`](skills/module-validation-worker/SKILL.md) | Run a scenario slice for ONE module's process |

### Leaf skills (Layer 4)
| Skill | Purpose |
|---|---|
| [`d365-knowledge-routing`](skills/d365-knowledge-routing/SKILL.md) | Module → file path index, DMF load order, keyword router |
| [`fo-mcp-server`](skills/fo-mcp-server/SKILL.md) | Dynamics 365 ERP MCP server interaction. Built from the [official Microsoft Learn article](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp). |
| [`reinforcement-learning`](skills/reinforcement-learning/SKILL.md) | Challenge journal + knowledge feedback loop |

## The 3-phase lifecycle

```
PHASE 1 — Analysis & Preparation       PHASE 2 — Deployment            PHASE 3 — Documentation
─────────────────────────────────      ─────────────────────────       ─────────────────────────
1.1 Requirements analysis              2.1 MCP-driven deployment       3.1 rollout-report.html
1.2 Config building                    2.2 E2E validation + fix loop   3.2 environment-config.html
1.3 Rollout plan + E2E test plan
1.4 Validation
1.5 Approval gate
```

No phase begins until the previous one is complete.

## The new `fo-mcp-server` skill

The headline change in this edition. The skill teaches the agent to use the **Dynamics 365 ERP MCP server** — the new *dynamic* server that replaces the retiring legacy 13-tool static server.

It covers:
- The three tool categories — **data tools** (CRUD via OData / SQL), **form tools** (server-side form navigation), **action tools** (X++ `ICustomAPI` invocation).
- Tool selection hierarchy (data > form > action) and when each is mandatory.
- Naming conventions (plural entities, V2+ rules), no-deep-insert, enum syntax, internal-name-not-label rule.
- Prerequisites — F&O ≥ 10.0.47, feature flag, **Allowed MCP Clients** registration, Tier 2+ env.
- Licensing — `0.1 Copilot Credits` per tool call (waived for premium F&O / SCM licenses on non-Copilot-Studio clients).
- The `data_find_entities_sql` upgrade path (10.0.48+).

See [`skills/fo-mcp-server/`](skills/fo-mcp-server/) for `SKILL.md`, the full `tools-reference.md`, and `prerequisites.md`.

## Workspace layout

```
ProcessBaseline/
├── .github/copilot-instructions.md    ← thin orchestrator (skills index + cardinal rules)
├── skills/                            ← 13 skills, 4 layers
│   ├── phase-orchestrator/            Layer 0
│   │   └── SKILL.md
│   ├── module-fanout/                 Layer 2
│   │   └── SKILL.md
│   ├── d365-requirements-analysis/
│   │   ├── SKILL.md
│   │   └── requirement-matrix.schema.json
│   ├── d365-config-builder/SKILL.md
│   ├── d365-deployment/SKILL.md
│   ├── d365-validation-testing/SKILL.md
│   ├── d365-documentation/SKILL.md    Layer 1 — phase skills
│   ├── module-config-worker/SKILL.md
│   ├── module-deployment-worker/SKILL.md
│   ├── module-validation-worker/SKILL.md   Layer 3 — sub-agent workers
│   ├── d365-knowledge-routing/SKILL.md
│   ├── fo-mcp-server/
│   │   ├── SKILL.md
│   │   ├── tools-reference.md
│   │   └── prerequisites.md
│   └── reinforcement-learning/
│       ├── SKILL.md
│       └── journal-entry.schema.json   Layer 4 — leaf skills
├── Modules/                            ← 47 module knowledge files + 24 DMF templates
│   ├── D365_Finance_Operations_Modules_Overview.md
│   ├── D365_Quick_Reference.md
│   ├── dmf_odata_mapping.json
│   ├── Administration/
│   ├── Dynamics 365 Finance/
│   ├── Dynamics 365 Supply Chain Management/
│   ├── Dynamics 365 Human Resources/
│   ├── Dynamics 365 Commerce/
│   └── Dynamics 365 Project Operations/
├── Business Process/                   ← 5,767-item APQC process catalogue
├── ChallengeJournal/                   ← running challenge + resolution log
├── Requirements/                       ← drop input requirement docs here
├── Documentation/                      ← all project output artefacts
└── SourceFiles/                        ← raw OData metadata + prompt templates
```

## Getting started

1. Open the workspace in your AI host (VS Code with Copilot, Claude Desktop, Claude Code, or any Skills-aware client).
2. Drop requirement documents into `Requirements/`.
3. Ask the agent to *"analyse the requirements"* → it auto-loads `d365-requirements-analysis` (and `d365-knowledge-routing` for module lookups).
4. Review the produced `Documentation/requirement-profile.md`, iterate.
5. *"Build the configuration files"* → `d365-config-builder` activates.
6. *"Deploy"* → `d365-deployment` + `fo-mcp-server` activate (after the Phase 1 approval gate).
7. *"Generate the rollout HTML"* → `d365-documentation` produces the final deliverables.

## Prerequisites

| Requirement | Detail |
|---|---|
| **AI host** | Any Skills-aware client (Claude, VS Code Copilot Chat with Skills, etc.) |
| **D365 F&O environment** | ≥ 10.0.47, Tier 2 or Unified Developer Environment, MCP feature flag enabled, agent client added to **Allowed MCP Clients** |
| **MCP server** | Dynamics 365 ERP MCP server registered in your host's MCP config |
| **Source documents** | Place requirement files in `Requirements/` |

See [`skills/fo-mcp-server/prerequisites.md`](skills/fo-mcp-server/prerequisites.md) for the full environment setup.

## Cardinal rules

- **Source files are authoritative.** Fix the source first, then re-deploy.
- **Document continuously.** Write as you go.
- **Follow processes start-to-finish.** No fragment testing.
- **Consult module knowledge first.** Module `.md` files before workarounds.
- **Feed back every discovery.** The Challenge Journal makes the system smarter.
- **Respect dependency order.** DMF template numbers (010 → 650) are non-negotiable.

---

<p align="center"><sub>Dynamics 365 Finance & Operations Implementation Accelerator · Version 2.2 (Skills + Sub-Agents + Schemas + CI)<br>Built from 13 skills across 4 layers, 47 module knowledge files, 24 DMF templates, 7 canonical schemas, and 5,767 business process items.<br>MCP guidance sourced from the <a href="https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp">official Microsoft Learn article</a>.</sub></p>
