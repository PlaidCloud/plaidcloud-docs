---
title: Claude Code
slug: claude-code
weight: 2.0
description: Set up Claude Code (CLI, VSCode extension, JetBrains plugin) to call PlaidCloud's MCP tools using either OAuth or a static Bearer token.
---

[Claude Code](https://claude.com/claude-code) is Anthropic's coding agent. It ships as a CLI, a VSCode extension, and a JetBrains plugin — all three share the same MCP configuration.

## Option A — OAuth (recommended)

OAuth is the lowest-maintenance path. Claude Code's MCP bridge handles the browser redirect and refresh transparently.

1. From your project root, add the server. The CLI form:

    ```bash
    claude mcp add --transport http plaidcloud https://<your-workspace>.plaid.cloud/mcp/
    ```

    Or in `.mcp.json` at the project root:

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "type": "http",
          "url": "https://<your-workspace>.plaid.cloud/mcp/"
        }
      }
    }
    ```

2. Restart Claude Code. The first time you ask it to use a `plaidcloud_` tool, the bridge will pop up an authorization URL. Open it, sign in to PlaidCloud, approve the connection, and paste the callback URL Claude Code asked for. The token is cached locally and refreshed automatically.

3. Verify with `claude mcp list` (CLI) or `/mcp` (in-session). The server should show as connected.

{{< note >}}
The OAuth bridge state can occasionally get stuck on remote/SSH sessions where Claude Code can't reach `localhost` from your browser. If that happens, fall back to Option B.
{{< /note >}}

## Option B — Static Bearer token

When OAuth isn't practical (remote sessions, devcontainers, agent runtimes that don't survive browser redirects), use a Bearer token:

1. In a browser tab where you're signed into PlaidCloud, open:

    ```
    https://<your-workspace>.plaid.cloud/mcp/setup/token
    ```

    Click "Copy snippet."

2. Paste it into your project's `.mcp.json` under `mcpServers`:

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "type": "http",
          "url": "https://<your-workspace>.plaid.cloud/mcp/",
          "headers": {
            "Authorization": "Bearer eyJhbGc…"
          }
        }
      }
    }
    ```

    Or via the CLI:

    ```bash
    claude mcp add --transport http plaidcloud \
      https://<your-workspace>.plaid.cloud/mcp/ \
      -H "Authorization: Bearer eyJhbGc…"
    ```

3. Restart Claude Code. `claude mcp list` should show the server as connected.

When the token expires, reload the `/mcp/setup/token` URL and replace the `Authorization` value.

## Multi-tenant setup

You can configure multiple PlaidCloud tenants side-by-side — give each a distinct name:

```json
{
  "mcpServers": {
    "plaidcloud-prod":  { "type": "http", "url": "https://prod.plaid.cloud/mcp/" },
    "plaidcloud-dev":   { "type": "http", "url": "https://dev.plaid.cloud/mcp/"  }
  }
}
```

When you ask Claude Code to do something, name the tenant in your prompt ("in the dev tenant, find projects whose name starts with `Q4`") so it picks the right server.

## Tips

- Run `mcp_introspect` early in a session so Claude Code understands the tool surface without re-reading the full manifest on every call.
- Mutating tools (`*_upsert`, `*_organize`, `*_run`) accept `dry_run=True` — useful when you're letting an agent script changes and want a plan to review first.
- For long-running operations (workflow runs, query exports), prefer the `*_track` / `*_status` tools over poll loops — they're the single source of truth and avoid flooding the agent's context.
