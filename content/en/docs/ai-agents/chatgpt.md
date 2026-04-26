---
title: ChatGPT
slug: chatgpt
weight: 7.0
description: Current state of MCP support in ChatGPT and recommended approaches for connecting ChatGPT to PlaidCloud.
---

ChatGPT's support for user-added MCP servers is still rolling out and varies by plan tier and surface. This page describes what works today.

## ChatGPT Pro / Plus / Team — Connectors

If your ChatGPT plan exposes the **Connectors** UI (Settings → Connectors), you can add PlaidCloud as a custom MCP connector:

1. Go to **Settings → Connectors → Add custom connector**.
2. Enter:
   - **Name**: `PlaidCloud`
   - **MCP server URL**: `https://<your-tenant>.plaidcloud.org/mcp/`
3. ChatGPT will redirect you to PlaidCloud for OAuth login. Approve the connection.
4. Toggle the connector on inside any conversation that should be able to use it.

{{< note >}}
The Connectors UI may not be visible on every account or every region. If you don't see "Add custom connector," your plan or workspace policy doesn't currently allow user-added MCP servers — use the workaround below.
{{< /note >}}

## ChatGPT Enterprise

Enterprise admins can pin MCP connectors at the workspace level through the admin console. Follow the same OAuth setup as above but expect a workspace approval step from your admin before the connector becomes usable.

## Workaround — Custom GPTs with REST Actions

If your account doesn't support custom MCP connectors, you can still drive PlaidCloud from ChatGPT through a **Custom GPT** that calls PlaidCloud's REST API as an OpenAPI Action:

1. PlaidCloud's REST surface is described by the OpenAPI document at `https://<your-tenant>.plaidcloud.org/openapi_rest.json`.
2. In ChatGPT, create a Custom GPT (Explore GPTs → Create) and under **Actions** import that URL (or paste the JSON).
3. Configure authentication as **OAuth** and point at PlaidCloud's Keycloak endpoints. Your PlaidCloud admin can supply the realm URLs and client ID.

This trades MCP's tool-name conventions for direct REST endpoints — slightly more verbose for the model to navigate, but functionally equivalent for the read/write operations PlaidCloud exposes.

## Why MCP isn't always available

OpenAI's MCP support continues to evolve and the available surfaces (Connectors UI, Actions schema, etc.) change between plan tiers and over time. If the official **Connectors** path is open on your account, prefer it — it has built-in OAuth refresh and a tool-call experience matching the rest of this section. Falling back to Custom GPT Actions is only necessary when MCP isn't yet exposed for your account.
