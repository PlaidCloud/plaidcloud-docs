---
title: Oracle Essbase Connector
description: Connect PlaidCloud to Oracle Essbase 21c or Oracle Analytics Cloud with a service account to run live MDX queries against Essbase cubes from a workflow.
sidebar:
  order: 2
---

## API Documentation

This connector talks to [Oracle Essbase's REST API](https://docs.oracle.com/en/database/other-databases/essbase/) — the same `grid/mdx`, application, database, and outline endpoints Oracle documents for Essbase 21c and Oracle Analytics Cloud (OAC).

## What It Connects To

Oracle Essbase **21c or later**, and Oracle Analytics Cloud (OAC) Essbase. These versions expose Essbase over a documented REST API, which is what PlaidCloud calls. Pre-REST on-premises Essbase releases are **not supported** — there is no legacy Java-API or grid-client path.

Once the connection exists, the [Essbase Query](/reference/workflow-steps/general/essbase-query/) step runs live MDX against a cube and lands the result grid in a table.

## How Authentication Works

The connection authenticates with a service-account username and password over HTTP Basic. That account's Essbase provisioning controls which applications and cubes it can see and query, so grant it read access to exactly the applications you intend to query and nothing more.

## Configuration

| Field | Type | Description |
|---|---|---|
| Name | Text | Display name for this connection. |
| Base URL | Text | The Essbase server origin, for example `https://your-host:9001`. Enter the origin only — no trailing `/essbase/...` path. |
| Default Application | Text *(optional)* | Pre-selects this application in the Essbase Query step form. |
| Username | Text | Service-account user for HTTP Basic authentication. |
| Password | Text | Service-account password. Stored encrypted. |
| Verify SSL | Toggle | On by default. Turn off only for a host with a self-signed or otherwise unverifiable certificate. |

## Testing the Connection

Use **Test Connection** in the connection editor. A successful test reaches the Essbase server, lists the applications the service account can see, and reports how many it found — confirming both the base URL and the credentials before you build a query.

## Related

- [Essbase Query](/reference/workflow-steps/general/essbase-query/) — run a live MDX query against a cube and land the result in a table.
- [Create and Manage a Connection](/guides/connections/create-connection/)
