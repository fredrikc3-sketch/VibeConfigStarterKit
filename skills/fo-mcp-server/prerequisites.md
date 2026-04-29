# Dynamics 365 ERP MCP Server — Environment Prerequisites

Source: <https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp>

## Environment requirements

| Requirement | Detail |
|-------------|--------|
| **F&O version** | ≥ 10.0.47 |
| **Feature flag** | Enable **"Dynamics 365 ERP Model Context Protocol server"** in Feature Management. |
| **Environment tier** | Tier 2 or above, **or** a Unified Developer Environment. **Cloud Hosted Environments (CHE) are not supported.** |
| **Allowed MCP clients** | Add your agent platform to the **Allowed MCP Clients** form. By default, only Microsoft Copilot Studio and Visual Studio Code are allowed. |

## Allowed clients (defaults)

| Platform | Client ID |
|----------|-----------|
| Microsoft Copilot Studio | `7ab7862c-4c57-491e-8a45-d52a7e023983` |
| Visual Studio Code | `aebc6443-996d-45c2-90f0-388ff96faa56` |

To add another platform:
1. Register the app in Microsoft Entra ID.
2. Add its client ID to the **Allowed MCP clients** form with **Allowed = true**.

## Licensing summary

Two cost components:
1. **Orchestration cost (LLM)** — billed by the agent client.
2. **MCP server execution cost** — `0.1 Copilot Credits` per tool call for non–Copilot Studio clients. Bundled into the Agent Action rate when used from Copilot Studio.

### Premium licenses exempt from MCP execution billing (non–Copilot Studio agents only)
- Dynamics 365 Finance Premium
- Dynamics 365 Supply Chain Management Premium

Copilot Studio agents continue to bill at the fixed Agent Action rate even with these premium licenses.

### Agent identity licensing
The agent's identity does **not** need a Dynamics 365 user license. Human users interacting with chat-based agents still need their own license.

## Static-server retirement

The legacy "static" MCP server (13 fixed tools, Dataverse-connector-based) is retired in calendar year **2026**. Available today on F&O ≥ 10.0.2263.17 — migrate to the dynamic server before retirement.
