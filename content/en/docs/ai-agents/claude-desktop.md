---
title: Claude Desktop and Claude.ai
slug: claude-desktop
weight: 3.0
description: Add PlaidCloud as a Custom Connector in Claude.ai (web) or Claude Desktop so the chat assistant can call MCP tools during conversations.
---

The consumer Claude app — both the web UI at [claude.ai](https://claude.ai) and the desktop app — supports MCP servers through its **Custom Connectors** feature. Setup is a one-time OAuth dance, after which the connection is associated with your Claude account and follows you across devices.

{{< note >}}
Custom Connectors are available on Claude Pro, Max, Team, and Enterprise plans. Team and Enterprise admins can pin connectors for everyone in the workspace.
{{< /note >}}

## Setup

1. In Claude (web or desktop), open **Settings → Connectors**.
2. Click **Add custom connector**.
3. Fill in:
   - **Name**: `PlaidCloud` (or `PlaidCloud (prod)`, `PlaidCloud (dev)` if you have multiple tenants).
   - **Server URL**: `https://<your-tenant>.plaidcloud.org/mcp/`
4. Click **Add**. Claude opens a browser tab to PlaidCloud's Keycloak login.
5. Sign in and approve the connection. You'll be redirected back to Claude with the connection saved.

The connector is now available in any conversation. Toggle it on (or off) using the connectors picker in the chat composer.

## Usage

Once enabled, you can ask Claude things like:

- "List the workflows in project `Q4 Forecast`."
- "Show me the last 10 failed runs for the `daily-load` workflow."
- "Run `mcp_recipes` and pick the right one for backfilling a step."

Claude will pick the appropriate MCP tool, call it, and incorporate the response into its reply. For mutating operations it will typically narrate what it's about to do — review carefully before approving.

## Multiple tenants

Add a separate connector for each tenant. Give them distinct names so Claude can tell them apart in conversation. Only the connectors you toggle on for a given chat are available — leaving production off by default and only enabling it when you're sure is a sensible safety habit.

## Refreshing access

Custom connectors store an OAuth refresh token, so re-authentication is rare. If you change your PlaidCloud password, get a new device, or your session is invalidated server-side, the connector may show "needs authentication." Click **Reconnect** in the connectors settings to redo the OAuth flow.

## Disconnecting

Settings → Connectors → click the connector → **Remove**. This deletes the OAuth tokens stored with your Claude account. The PlaidCloud-side session is independent — log out of PlaidCloud separately if you want to invalidate the underlying Keycloak session.
