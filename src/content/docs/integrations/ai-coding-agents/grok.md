---
title: Grok
description: Connect xAI's Grok to PlaidCloud's MCP server through its custom connectors.
sidebar:
  order: 8
---

[Grok](https://grok.com) supports MCP servers through custom connectors, configured at grok.com.

## Setup

1. Go to [grok.com/connectors](https://grok.com/connectors) and click **New Connector → Custom**.
2. Paste the MCP server URL: `https://<your-workspace>.plaid.cloud/mcp`.
3. Complete sign-in when Grok redirects you to PlaidCloud. You'll see an **Application Access Request** page naming the requesting application and the redirect URI it will send credentials to — check both match Grok before approving.

## Company Plans

Business and Enterprise workspaces route connector setup through a team admin: a workspace admin provisions the connector at grok.com/connectors, after which members connect their own account to it.

## Refreshing Access

If Grok reports the connection needs reauthorization, repeat the sign-in step — the connector keeps its URL, so you don't need to re-add it from scratch.
