---
title: TM1 Connector
description: Connect PlaidCloud to an IBM TM1 / Planning Analytics server over its REST API — native Basic auth or CAM namespace auth — cloud-direct, or through an on-premises PlaidLink agent for a server the cloud cannot reach directly.
sidebar:
  order: 1
---

Connect PlaidCloud to an IBM **TM1 / Planning Analytics** server over its published OData v4 REST API — no JVM bridge, no PAOlap driver. Read cube data with [TM1 Query](/reference/workflow-steps/ibm-planning-analytics/tm1-query/) or a TM1 dimension hierarchy with [TM1 Dimension Read](/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/), both cloud-direct; for a TM1 server only reachable from inside your own network, [TM1 Query (Agent)](/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) dispatches the same read through an installed PlaidLink agent instead.

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

This connector is read-only. It reads cube data and dimension hierarchies out of TM1; it does not write, post, or run TI processes back into TM1.

## What You Can Do With the Connection

- **Read cube data by saved view or MDX.** The [TM1 Query](/reference/workflow-steps/ibm-planning-analytics/tm1-query/) step runs a named cube view or a raw MDX query, applies an optional point-of-view slice, and lands the result as a table.
- **Load a TM1 hierarchy as a PlaidCloud dimension.** The [TM1 Dimension Read](/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) step reads a dimension's elements, parent/child edges, and attributes, and builds a PlaidCloud dimension from them.
- **Slice by period for an incremental extract.** TM1 has no built-in change tracking, so a workflow that only needs new data narrows the query by period or version — see the step reference for the pattern.
- **Discover cubes, views, and dimensions live**, cloud-direct. The step form's Cube, View, and Dimension pickers query the connected server directly, so you pick real names instead of typing them blind.
- **Read a TM1 server the cloud cannot reach, through an on-premises agent.** See [Reading TM1 Behind a Firewall](#reading-tm1-behind-a-firewall) below.

## Reading TM1 Behind a Firewall

A TM1 server that is only reachable from inside your own network — no public endpoint, no allowlisted IP, no VPN into PlaidCloud — is reached through an installed **PlaidLink agent** instead of cloud-direct. The [TM1 Query (Agent)](/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) workflow step runs the same view/MDX/point-of-view query as TM1 Query, but dispatches it to the agent, which reaches TM1 on your network and returns the result.

This path requires:

- **An installed PlaidLink agent** on a machine with network access to the TM1 server. See [Install PlaidLink](/reference/cli/plaidlink/install/).
- **A build of that agent that includes the TM1 handler.** PlaidCloud checks an agent's advertised capabilities before dispatching a query to it, so an older agent build cannot serve TM1 requests until it's rebuilt and reinstalled — PlaidLink does not auto-update. See [Upgrade PlaidLink](/reference/cli/plaidlink/upgrade/).
- **This TM1 connection shared with that agent**, in addition to whatever member/group access it already has, from the connection's `Actions > Agents` list. See [Security Model](/guides/connections/create-connection/#security-model).

TM1 Query (Agent) has no live discovery — an agent is only reachable during a run, not while the step's form is open — so cube, view, and MDX are typed by hand and validated when the step runs. TM1 Dimension Read is cloud-direct only; it has no on-premises path yet.

## Known Limitations

| Limitation | What it means |
|---|---|
| Read-only | No write-back, no TI process execution. |
| On-prem reach is query-only | The on-premises PlaidLink agent path covers cube reads (TM1 Query (Agent)). TM1 Dimension Read has no on-premises path yet — it needs a network path PlaidCloud can reach directly. |
| Dimension read is single-hierarchy, single-parent | A TM1 hierarchy with an element under more than one parent cannot be loaded as a PlaidCloud dimension, and a consolidation weight's magnitude (0.5, 2.0) is not representable — only its sign. See [TM1 Dimension Read](/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/#what-this-step-cannot-represent). |
| No PAaaS bearer auth | Only Native (Basic) and CAM authentication are supported. |

## Related

- [Connect to TM1 (guide)](/guides/connections/tm1/) — create the connection and build a query.
- [TM1 Query](/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — cube reads, cloud-direct.
- [TM1 Query (Agent)](/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — cube reads through an on-premises agent.
- [TM1 Dimension Read](/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — load a TM1 hierarchy as a PlaidCloud dimension.
- [Create and Manage a Connection](/guides/connections/create-connection/)
