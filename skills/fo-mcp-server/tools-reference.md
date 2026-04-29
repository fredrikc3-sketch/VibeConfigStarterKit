# Dynamics 365 ERP MCP Server — Tool Catalogue

Source: <https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp>

## Data tools (7)

| Tool | Purpose |
|------|---------|
| `data_find_entity_type` | Find OData entity types. Returns multiple candidates — pick the right one before calling `data_get_entity_metadata`. |
| `data_get_entity_metadata` | Fetch the field schema for an entity. Required before any CRUD operation. |
| `data_create_entities` | Create records via OData. **Deep inserts not supported** — create parent then children separately. |
| `data_update_entities` | Update records via OData (PATCH semantics). |
| `data_delete_entities` | Delete records via OData. |
| `data_find_entities` | Read records via OData (`$filter`, `$select`, `$expand`, etc.). |
| `data_find_entities_sql` | Read records via SQL. Available from F&O **10.0.48**. Replaces `data_find_entities` for read scenarios — prefer it when available. |

## Form tools (12)

| Tool | Purpose |
|------|---------|
| `form_find_menu_item` | Locate a menu item by internal name (groups menu items by type automatically). |
| `form_open_menu_item` | Open a form by its menu item. |
| `form_close_form` | Close the current form. |
| `form_find_controls` | Locate controls on the active form (one search term per call — call repeatedly for multiple). |
| `form_set_control_values` | Set values on one or more controls. **Do not use** for lookup-driven controls — use `form_open_lookup` instead. |
| `form_open_lookup` | Open a lookup control to drive selection of a related record. |
| `form_click_control` | Click a control or sub-element (use `actionId` for sub-elements like menu sub-buttons). |
| `form_open_or_close_tab` | Toggle tab visibility on the active form. |
| `form_filter_form` | Apply a filter to the entire form. |
| `form_filter_grid` | Apply a filter to a grid. |
| `form_sort_grid_column` | Sort a grid by one of its columns. |
| `form_select_grid_row` | Select a specific row in a grid. |
| `form_save_form` | Save pending changes on the form. |

## Action tools (2)

| Tool | Purpose |
|------|---------|
| `api_find_actions` | List X++ classes (implementing `ICustomAPI`) that the agent's security role can invoke. |
| `api_invoke_action` | Invoke one of the discovered actions with parameters. |

## Notes

- All tools return a **view model filtered by the authenticated user's security role**. Hidden objects = role missing the privilege.
- The static (legacy) MCP server's 13 fixed tools are out of scope of this catalogue. Migrate off it before 2026.
