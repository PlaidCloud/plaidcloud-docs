---
title: Getting Started
slug: getting-started
weight: 1.0
description: Overview of the PlaidCloud MCP server — what it exposes, authentication options, and the basics every AI agent client needs.
---

## What is the MCP server?

The [Model Context Protocol](https://modelcontextprotocol.io) is an open standard for letting AI agents talk to external tools and data. PlaidCloud runs an MCP server on every workspace that wraps the same core helpers the REST API uses — grouped by intent (`find`, `describe`, `upsert`, `run`, `organize`) so an agent can navigate the surface without loading 1,000+ low-level RPC method names.

The server lives at:

```
https://<your-workspace>.plaid.cloud/mcp/
```

Replace `<your-workspace>` with your workspace subdomain (whatever you use to log into the PlaidCloud UI).

## What it exposes

The catalog covers most of the day-to-day surface an agent needs:

- **Projects, workflows, steps** — find/describe/upsert/run/organize, including step-level rerun and version history.
- **Tables, views, queries** — schema introspection, query execution, exports, snapshots, branches.
- **Dimensions** — describe, find, upsert, version, manage nodes/aliases/properties.
- **Connections** — find/upsert/test connections to external systems.
- **Lakehouse** — branches, snapshots, optimize/vacuum operations.
- **Identity** — members, groups, sessions, distros.
- **Documents, dashboards, UDFs, editors, agents, publishes** — domain-specific tools.
- **Workflow logs and run tracking** — `workflow_logs`, `workflow_run_status`, `workflow_job_track`.

Every tool returns a uniform envelope `{ok, data, next_cursor?, total?}`; failures use `{ok: false, error: {code, retryable, message, hint?}}`. Mutations accept `dry_run=True` for plan-without-write validation.

For the live catalog, point your agent at the server and call `mcp_introspect` (no arguments) — that returns the current tool count, per-domain summaries, and parameter signatures. Use `mcp_recipes` for common multi-tool playbooks (paginating large lists, snapshot-then-modify, rerun a failed step, etc.).

## Authentication

PlaidCloud's MCP server accepts two authentication paths:

1. **OAuth 2.1 + PKCE via Dynamic Client Registration (DCR).** This is what Claude.ai's custom-connector UI uses, and it's also the default for Claude Code's MCP bridge. The client registers itself, redirects you to PlaidCloud's Keycloak login, and gets back a token transparently. You don't need to do anything other than pick "OAuth" in the client and approve the login.
2. **Static Bearer token in an `Authorization` header.** For agent runtimes that don't have a usable browser redirect or that want a long-lived token in a config file. PlaidCloud exposes a helper page to mint one for you (see below).

### Getting a static Bearer token

Open this URL in a browser tab where you're already signed into PlaidCloud:

```
https://<your-workspace>.plaid.cloud/mcp/setup/token
```

The page returns a JSON snippet ready to paste into your agent's MCP config. Each workspace has its own snippet.

The token's lifespan is governed by your Keycloak realm's access-token-lifespan policy (typically a few hours to a day). To refresh, reload the same URL — your browser session re-mints the token automatically.

{{< note >}}
This flow is intended for getting started and for clients that can't complete an OAuth redirect. For long-lived agent access in production — service accounts, CI runners, scheduled jobs — use OAuth where the client supports it. Personal Access Tokens are planned but not yet generally available.
{{< /note >}}

## Pick a client

The rest of this section walks through setup for specific AI agent clients:

- [Claude Code](../claude-code/) — Anthropic's coding agent (CLI, VSCode extension, JetBrains plugin).
- [Claude Desktop and Claude.ai](../claude-desktop/) — the consumer Claude app (desktop) and web (`claude.ai`) using "Custom Connectors."
- [Cursor](../cursor/) — the AI-native code editor.
- [GitHub Copilot](../copilot/) — Copilot agent mode in VSCode.
- [Google Gemini CLI](../gemini/) — `gemini-cli` and Gemini Code Assist.
- [ChatGPT](../chatgpt/) — current support status and recommended workaround.
- [Troubleshooting](../troubleshooting/) — common errors and how to fix them.
