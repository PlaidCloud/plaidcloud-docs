---
title: Google Gemini CLI
description: Configure Google's gemini-cli to call PlaidCloud's MCP tools.
sidebar:
  order: 6
---

Google's [`gemini-cli`](https://github.com/google-gemini/gemini-cli) supports MCP servers through `~/.gemini/settings.json` (user-scoped) or `.gemini/settings.json` in a project root (project-scoped).

## Setup

1. Get a Bearer token by visiting `https://<your-workspace>.plaid.cloud/mcp/setup/token` in a browser where you're signed into PlaidCloud.

2. Edit `~/.gemini/settings.json` (create it if it doesn't exist):

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "httpUrl": "https://<your-workspace>.plaid.cloud/mcp",
          "headers": {
            "Authorization": "Bearer eyJhbGc…"
          }
        }
      }
    }
    ```

3. Restart `gemini`. Inside a session, run `/mcp` to verify the server is connected and list its tools.

## Usage

Prompt Gemini to use the PlaidCloud tools directly:

- "Use plaidcloud to list workflows in the `Sales Forecasting` project."
- "Describe the columns of the `customers` table and the most recent snapshot."

You can also call tools explicitly with the `/tools` command if you want to inspect a specific tool's input schema before invoking it.

## Refreshing the Token

When the token expires, reload `https://<your-workspace>.plaid.cloud/mcp/setup/token` and update the `Authorization` value in `settings.json`. Restart `gemini` to pick up the change.

## Gemini Code Assist (IDE)

Gemini Code Assist in VSCode/JetBrains accepts the same `mcpServers` config under its agent settings. The schema matches the CLI form — paste the same snippet under the IDE's MCP server settings panel.
