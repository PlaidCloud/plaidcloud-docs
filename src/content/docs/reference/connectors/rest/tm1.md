---
title: TM1 Connector
description: Connect PlaidCloud to an IBM TM1 / Planning Analytics server over its REST API — native Basic auth or CAM namespace auth, cloud-direct with no on-premises agent — to read cube data with the TM1 Query workflow step.
sidebar:
  order: 1
---

Connect PlaidCloud to an IBM **TM1 / Planning Analytics** server over its published OData v4 REST API. The connection reaches the server directly — no JVM bridge, no PAOlap driver — and feeds the [TM1 Query](/reference/workflow-steps/ibm-planning-analytics/tm1-query/) step's cube/view/dimension pickers and live cellset reads.

The connection kind appears in the connection picker as **IBM Planning Analytics (TM1)**.

## How Authentication Works

Two authentication modes, matching TM1's own REST login schemes:

- **Native** — HTTP Basic authentication with a TM1 username and password.
- **CAM** — IBM Cognos Access Manager single sign-on, scoped to a namespace. The request carries an `Authorization: CAMNamespace` header built from the username, password, and namespace together, distinct from plain Basic.

There is no PlanningAnalytics-as-a-Service (PAaaS) bearer-token login yet — only the two REST login schemes above.

## Configuration

| Field | Required | Description |
|---|---|---|
| Name | Yes | Display name for this connection. |
| Host | Yes | The TM1 REST API host, e.g. `https://tm1-prod.example.com:8010` or a PAaaS URL. |
| Default Database | No | A convenience prefill for a TM1 Query step's Database field. Each step can override it. |
| Authentication Mode | Yes | `Native` (TM1 user/password) or `CAM` (Cognos Access Manager SSO). Defaults to Native. |
| Username | Yes | The TM1 account to authenticate with. |
| Password | Yes | Stored encrypted. |
| CAM Namespace | Only with CAM | The Cognos Access Manager namespace to authenticate against. Unused in Native mode. |
| Verify SSL Certificate | No | On by default. Turn off only for a known self-signed certificate on a test server. |
| Timeout (seconds) | No | Defaults to 30. |

## Testing the Connection

**Test Connection** probes the server's `Configuration` singleton (`GET {host}/api/v1/Configuration`) — the cheapest authenticated call TM1 exposes, and one that needs no database or cube context. A successful test reports the server's **`ProductVersion`**, confirming both that the host is reachable and that the credentials authenticate.

## Read-Only

This connector is read-only. It reads cube data out of TM1; it does not write, post, or run TI processes back into TM1.

## What You Can Do With the Connection

- **Read cube data by saved view or MDX.** The [TM1 Query](/reference/workflow-steps/ibm-planning-analytics/tm1-query/) step runs a named cube view or a raw MDX query, applies an optional point-of-view slice, and lands the result as a table.
- **Slice by period for an incremental extract.** TM1 has no built-in change tracking, so a workflow that only needs new data narrows the query by period or version — see the step reference for the pattern.
- **Discover cubes, views, and dimensions live.** The step form's Cube, View, and Dimension pickers query the connected server directly, so you pick real names instead of typing them blind.

## Known Limitations

| Limitation | What it means |
|---|---|
| Read-only | No write-back, no TI process execution. |
| Cloud-direct only | PlaidCloud reaches the TM1 server directly over REST. There is no on-premises PlaidLink agent option for TM1 yet — the server needs a network path PlaidCloud can reach directly (a public endpoint, an allowlisted IP, or a VPN). |
| No dimension/hierarchy import | The connection reads cube data through the TM1 Query step. Importing TM1 dimension hierarchies as PlaidCloud dimensions is not available yet. |
| No PAaaS bearer auth | Only Native (Basic) and CAM authentication are supported. |

## Related

- [Connect to TM1 (guide)](/guides/connections/tm1/) — create the connection and build a query.
- [TM1 Query](/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — the step field reference.
- [Create and Manage a Connection](/guides/connections/create-connection/)
