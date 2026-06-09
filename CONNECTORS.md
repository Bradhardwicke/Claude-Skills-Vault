---
title: Connectors
tags: [meta, connectors, integrations]
aliases: [Connector List, MCP Connectors]
---

# Connectors

This note resolves wikilinks from skill notes that reference `../../CONNECTORS` — a file that exists in each plugin's directory listing supported MCP connectors.

In the vault context, connector availability depends on what MCPs are connected in your Claude session. The skills that reference this file (Data, Design, Operations, Sales, Productivity) work standalone but are enhanced when relevant connectors are active.

## Connected in Brad's Setup

| Category | Connector | Notes |
|---|---|---|
| Productivity | Slack | Message search, posting |
| Productivity | Notion | Page read/write |
| Productivity | Linear | Issues, cycles |
| Productivity | Asana | Tasks, projects |
| Design | Figma | Design context, code connect |
| PM | Atlassian (Jira + Confluence) | Issues, docs |
| Sales | HubSpot | CRM |
| Data | BigQuery | SQL queries |
| Files | Desktop Commander | Local filesystem |

## How Skills Use Connectors

Skills that list connectors use them to supercharge their default behaviour. For example:
- `sales:call-prep` works standalone but is enhanced with CRM + calendar connectors
- `data:analyze` works with uploaded data but is enhanced with a live database connector
- `productivity:task-management` works with a local TASKS.md but is enhanced with Asana/Linear

When a connector is not available, skills fall back gracefully to manual input or file-based workflows.
