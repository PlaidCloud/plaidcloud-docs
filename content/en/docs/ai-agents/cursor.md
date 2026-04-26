---
title: Cursor
slug: cursor
weight: 4.0
description: Configure Cursor IDE to call PlaidCloud's MCP tools through its built-in MCP support.
---

[Cursor](https://cursor.com) supports MCP servers through a `mcp.json` config file. The shape is the same as Claude Code's `.mcp.json`, so the same Bearer-token snippet works in both.

## Setup

1. Get a Bearer token by visiting `https://<your-tenant>.plaidcloud.org/mcp/setup/token` in a browser where you're signed into PlaidCloud.

2. Open Cursor's MCP config:
   - **Project-scoped**: create `.cursor/mcp.json` in your project root.
   - **User-scoped (all projects)**: create `~/.cursor/mcp.json` in your home directory.

3. Add the PlaidCloud server:

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "url": "https://<your-tenant>.plaidcloud.org/mcp/",
          "headers": {
            "Authorization": "Bearer eyJhbGc…"
          }
        }
      }
    }
    ```

4. Open Cursor's **Settings → MCP** to verify the server is connected. If it shows an error, see [Troubleshooting](../troubleshooting/).

## Using the tools

In Cursor's Composer or chat panel, you can prompt the agent in plain English ("describe the structure of project `Q4 Forecast`") and it will pick the appropriate `plaidcloud_*` tool. Tool calls and responses appear inline — review mutating operations before approving.

## Refreshing the token

When the token expires, reload `https://<your-tenant>.plaidcloud.org/mcp/setup/token` and paste the new value into `mcp.json`. Cursor picks up the change without a full restart — toggle the server off/on in **Settings → MCP** if needed.

## Multiple tenants

Repeat the entry under a different name:

```json
{
  "mcpServers": {
    "plaidcloud-prod": { "url": "https://prod.plaidcloud.org/mcp/", "headers": { "Authorization": "Bearer …" } },
    "plaidcloud-dev":  { "url": "https://dev.plaidcloud.org/mcp/",  "headers": { "Authorization": "Bearer …" } }
  }
}
```
