---
title: "TM1 Query (Agent)"
description: Read a cube slice from an on-premises IBM TM1 / Planning Analytics server that the cloud cannot reach directly — the same view/MDX/point-of-view query as TM1 Query, dispatched through an installed PlaidLink agent.
---

## Description

The on-premises twin of [TM1 Query](/reference/workflow-steps/ibm-planning-analytics/tm1-query/): the same read — a saved **view** or an **MDX** query against a TM1 cube, with an optional point-of-view (POV) slice, landed as a project table — dispatched through an installed [PlaidLink agent](/reference/cli/plaidlink/) on your network instead of called cloud-direct. Use this step, instead of TM1 Query, when the TM1 server is only reachable from inside your own network.

This step appears in the step menu under **IBM TM1 / Planning Analytics**.

## What's Different From TM1 Query

| | TM1 Query | TM1 Query (Agent) |
|---|---|---|
| Transport | Cloud-direct over REST | Dispatched to a PlaidLink agent on your network |
| Configuration fields | — | Identical, plus a required **Agent** |
| Cube / View discovery | Live, from the connected database | Not available — type the names by hand |
| Preview before saving | Yes | Not available |

Everything else — the connection, the database, the view/MDX choice, the point-of-view slice, Suppress Zero/Empty Cells, Row Limit, and the incremental-extract pattern by period — works exactly as described on the [TM1 Query](/reference/workflow-steps/ibm-planning-analytics/tm1-query/) page. Only the differences below are specific to this step.

## Configuration

### Source and Target

| Field | Required | Notes |
|---|---|---|
| Agent | Yes | The PlaidLink agent to dispatch this read to. Its build must include the TM1 handler (see [Requirements](#requirements) below). |
| TM1 Connection | Yes | The [TM1 connection](/guides/connections/tm1/) to read through. The connection picker is not filtered by the selected agent — share the connection with the agent separately (see below). |
| Environment | Yes | The connection's environment. |
| Database | Yes | The TM1 database (instance) to query. |
| Cube | Yes | The TM1 cube to query. Typed by hand — there is no live discovery on this step. |
| Target Table | Yes | The project table the returned cellset lands in. |

### Slice and Options

Same fields as [TM1 Query](/reference/workflow-steps/ibm-planning-analytics/tm1-query/#slice) — Source Mode (By View / By MDX), View, MDX, Point of View, Suppress Zero/Empty Cells, and Row Limit — all typed entry rather than discovered, and all validated when the step runs rather than in a preview.

## No Agent-Mediated Discovery

TM1 Query's Cube, View, and Dimension pickers query the connected server live while you're editing the step. That live discovery does not exist for this step: an agent is only reachable during a run, not while a form is open in your browser. Cube, view, and MDX are typed entry, and an unrecognized name fails the run with a clear error rather than failing silently. For the same reason there is no **Preview** button — a preview would have to reach TM1, which only the agent can do.

## Requirements

Reading an on-premises TM1 server needs:

- **An installed PlaidLink agent** on a machine with network access to the TM1 server. See [Install PlaidLink](/reference/cli/plaidlink/install/).
- **A build of that agent that includes the TM1 handler.** PlaidCloud checks the agent's advertised capabilities before dispatching; an agent whose build predates this capability cannot serve the request. **PlaidLink does not auto-update** — an existing agent must be manually rebuilt/reinstalled to pick up TM1 support. See [Upgrade PlaidLink](/reference/cli/plaidlink/upgrade/).
- **The TM1 connection shared with that agent**, in addition to whatever member/group access it already has — grant it from the connection's `Actions > Agents` list. See [Security Model](/guides/connections/create-connection/#security-model).

## Related

- [TM1 Query](/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — the cloud-direct twin this step mirrors.
- [TM1 Dimension Read](/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — load a TM1 hierarchy into a PlaidCloud dimension, cloud-direct.
- [Connect to TM1 (guide)](/guides/connections/tm1/) — create the connection.
- [TM1 Connector](/reference/connectors/rest/tm1/) — connection field reference, including the on-prem agent path.
- [PlaidLink](/reference/cli/plaidlink/) — installing and upgrading agents.
- [IBM TM1 / Planning Analytics Steps](/reference/workflow-steps/ibm-planning-analytics/)
