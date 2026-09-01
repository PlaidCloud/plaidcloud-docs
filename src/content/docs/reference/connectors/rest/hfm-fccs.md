---
title: HFM / FCCS Connector
description: Set up an Oracle FCCS (Financial Consolidation and Close, EPM Cloud) connection in PlaidCloud to self-serve an ad-hoc data slice with a point-of-view picker, with optional caching and a scheduled recurring load.
sidebar:
  order: 1
---

Connect PlaidCloud to Oracle **FCCS** — Financial Consolidation and Close, part of Oracle EPM Cloud — so a finance user can self-serve a data slice without filing a ticket with the HFM team. The [HFM/FCCS: Read Data (Ad-hoc)](/reference/workflow-steps/oracle-epm/hfm-fccs-read/) step feels like a live query, but under the hood it is an asynchronous request → poll → fetch against FCCS's data-export job API.

The connection kind appears in the connection picker as **REST - HFM/FCCS**.

:::caution[No live tenant validation]
This connector is built to Oracle's documented EPM Cloud REST API and has **not yet been validated against a live FCCS instance**. Some endpoint details are pending live validation. Verify a small, tightly scoped point of view against a non-production application before relying on it.
:::

## API Documentation

The connector uses Oracle EPM Cloud's [REST API](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/index.html) — the application metadata endpoints (to discover dimensions and members) and the data-export job endpoints (to request, poll, and fetch a grid).

## How Authentication Works

The connection uses **HTTP Basic authentication with a service account** on a classic EPM Cloud pod — there is no OAuth or token flow (OCI / Gen 2 bearer-token pods are out of scope). When an **Identity Domain** is set, PlaidCloud composes the login as `identitydomain.username` (the domain, a dot, then the username); if you leave Identity Domain blank, or your username already contains a dot, the username is sent as-is. Point the connection at a dedicated integration service account with read access to the applications and point-of-view slices your self-serve users will pull.

## Configuration

| Field | Required | Description |
|---|---|---|
| Name | Yes | Display name for this connection. |
| EPM Cloud URL | Yes | Your EPM Cloud pod/service URL, e.g. `https://planning-test-yourdomain.epm.us2.oraclecloud.com`. |
| Identity Domain | No | Your EPM Cloud identity domain. When set, PlaidCloud prefixes it to the username as `identitydomain.username` at login. |
| Username | Yes | The integration service account's username. |
| Password | Yes | The service account's password. Stored encrypted. |
| Default Application | No | A default FCCS application to prefill in the step's point-of-view picker. Each step can override it. |

## What You Can Do With the Connection

- **Self-serve an ad-hoc slice.** Build a point of view (POV) — Application plus the FCCS dimensions — in the step form, hit Run, and a result table lands automatically. See [HFM/FCCS: Read Data (Ad-hoc)](/reference/workflow-steps/oracle-epm/hfm-fccs-read/).
- **Skip the ticket.** The slice runs under the connection's service account, so a finance user pulls the data themselves rather than waiting on an HFM administrator.
- **Cache repeated pulls.** The same POV and as-of served again returns the already-landed copy instantly instead of re-hitting FCCS.
- **Govern who sees which entities.** The landed table is **row-level-security-ready**: an administrator can declare Row Access on the `Entity` column so self-serve users only see the entities they are entitled to. This is governed under admin control, not automatic — see the step reference.
- **Schedule a recurring load.** Enable **Bound target** to promote an ad-hoc slice to a persistent table that grows additively and merges rather than overwrites, so the same step placed in a scheduled workflow becomes a nightly recurring load.

## Metadata Discovery

On supported FCCS pods, the step form discovers each dimension's member list live from the application metadata once you pick a connection and an application, so the POV picker offers real members to choose from (it re-discovers whenever either changes). On older pods that don't expose the metadata endpoint, discovery returns nothing and the picker falls back to manual entry — you type member names by hand, and a saved point of view always round-trips. The pull works the same either way.

## Known Limitations

| Limitation | What it means |
|---|---|
| No live tenant validation | Built to Oracle's documented EPM Cloud REST API but not yet exercised against a live FCCS pod. A few endpoint details are pending live validation. Verify a tightly scoped POV against a non-production application first. |
| Read-only | The connector extracts data from FCCS. It does not write consolidation data, run consolidations, or post back. |
| Scope the entity dimension | An un-scoped extract (no `Entity` selection) can lock the FCCS application for a long time while the export job runs. Keep the entity selection bounded. |
| Manual members on older pods | Where a pod does not expose the metadata endpoint, member lists don't auto-populate — enter member names by hand. |
| Row-level security is admin-governed, not automatic | The landed table can be governed with Row Access, but an administrator must publish, declare the `Entity` column, approve the first governed write, and reconcile. Until they do, the table is not filtered. |

## Related

- [Extract from HFM / FCCS (guide)](/guides/connections/hfm-fccs/) — create the connection, build a POV, run it, cache, govern, and schedule.
- [HFM/FCCS: Read Data (Ad-hoc)](/reference/workflow-steps/oracle-epm/hfm-fccs-read/) — the step field reference.
- [Managing Security Groups and Assignments](/administration/access/managing-security-groups-and-assignments/) — how Row Access governs the landed table.
- [Create and Manage a Connection](/guides/connections/create-connection/)
