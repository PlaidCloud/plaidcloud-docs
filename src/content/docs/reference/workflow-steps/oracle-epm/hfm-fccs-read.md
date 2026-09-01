---
title: "HFM/FCCS: Read Data (Ad-hoc)"
description: Self-serve a data slice from Oracle FCCS by building a point of view in the step form — the returned grid lands automatically as a table, repeat pulls are cached, the Entity column is row-level-security-ready, and an optional bound target turns it into a scheduled recurring load.
---

## Description

Reads an ad-hoc data slice from Oracle **FCCS** (Financial Consolidation and Close, EPM Cloud) over your [HFM/FCCS connection](/guides/connections/hfm-fccs/), by **point of view (POV)** rather than by writing a query. A finance user picks an application, builds a POV from the FCCS dimensions, and runs the step; the returned grid lands automatically as a project table (schema-on-read — the table is created from the grid's columns). It feels like a live query, but under the hood the step submits an export job to FCCS, **polls** it to completion, then fetches and lands the result — so a long-running slice doesn't block, and it needs no ticket to the HFM team.

This step appears in the step menu under **Oracle EPM (HFM/FCCS)**.

:::note[Scope the entity dimension]
Keep the **Entity** selection bounded — an un-scoped extract can lock the FCCS application for a long time while the export job runs.
:::

## Configuration

### Source and Target

| Field | Required | Notes |
|---|---|---|
| HFM/FCCS Connection | Yes | The [HFM/FCCS connection](/guides/connections/hfm-fccs/) to read through. |
| Environment | Yes | The connection's environment. |
| Application | Yes | The FCCS application to read from. Defaults to the connection's Default Application if one is set. Picking the application drives live member discovery for the POV. |
| Target Table | Yes | The project table the returned grid lands in. |

### Point of View

Build the slice from the FCCS dimensions. On supported pods the member lists auto-populate from live metadata discovery once a connection and application are chosen; on older pods you type member names manually.

| Dimension | Required | Notes |
|---|---|---|
| Scenario | Yes | |
| Year | Yes | |
| Period | Yes | |
| Entity | Bounded | Must name a bounded slice — the form rejects an empty selection, "all", or a selection wider than 500 members. Keep it scoped so the export doesn't lock the application. |
| Account | No | |
| Custom1–Custom4 | No | The application's custom dimensions. |
| ICP | No | Intercompany. |
| View | No | |
| Value | No | |

An unset optional dimension applies no filter on that axis (FCCS's default member is used).

### Bound Target

Off by default — each run lands an ad-hoc slice that overwrites the target table.

| Field | Notes |
|---|---|
| Bound target (scheduled recurring load) | When checked, the target becomes a **persistent** table: the step merges into it with a keyset upsert instead of overwriting, and the schema grows additively when a later grid brings new columns (a new column raises a warning, never a failure). Placing the step in a scheduled workflow then gives a recurring load that accumulates rather than wipes. |
| Key Columns | Enabled only with Bound target on. Comma-separated columns that form the merge key (for example `Entity, Account`). **Leave it empty** to use the POV dimension columns present in the landed grid as the merge key. |

## How It Works

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 130" role="img" aria-label="The step submits an export job to FCCS, polls it to completion, fetches the grid, and lands it as a table; a repeat point of view is served from the cached table instead." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="hf-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="58" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Submit job</text>
<rect x="150" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="198" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Poll</text>
<rect x="290" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="338" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Fetch grid</text>
<rect x="430" y="46" width="120" height="40" rx="7" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" /><text x="490" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Land table</text>
<path d="M106 66 L150 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M246 66 L290 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M386 66 L430 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<text x="198" y="34" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">while running…</text>
<rect x="590" y="46" width="120" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="650" y="64" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">Repeat POV</text><text x="650" y="78" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">served from cache</text>
<path d="M550 82 C570 100 630 100 650 88" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="4 3" marker-end="url(#hf-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">A run submits an export job, polls it, fetches the grid, and lands a table. The same point of view requested again is served from the already-landed copy.</figcaption>
</figure>

While the job runs, the step shows a polling status. When it lands, the table is created from the grid's columns — no schema to define up front.

## Caching

The same POV requested again is **served from the already-landed table**, instantly, instead of re-submitting the export to FCCS. A run is keyed by application, target table, point of view, and an **as-of** tag (default `latest`); a repeat that resolves to an already-landed slice reports that the table was left in place rather than re-writing it. Change the as-of tag when you want to force a fresh extract of the same POV.

## Row-Level Security

The landed grid's entity axis is normalized to a column named exactly **`Entity`**, so the table is **row-level-security-ready** — an administrator can govern it with [Row Access](/administration/access/managing-security-groups-and-assignments/) so self-serve users only see the entities they're entitled to.

This is **governed under admin control, not automatic**. Because the extract runs under the connection's service account, PlaidCloud will not let the step declare its own security. An administrator follows the standard Row Access workflow:

1. **Publish** the landed table for reporting.
2. **Declare** the `Entity` column as a governing attribute (default deny).
3. **Approve** the first governed write.
4. **Reconcile** so grants take effect.

Until an administrator does this, the table is not filtered. See [Managing Security Groups and Assignments](/administration/access/managing-security-groups-and-assignments/).

## Capability Limits

| Limitation | What it means |
|---|---|
| Read-only | Extracts a slice from FCCS. It does not write consolidation data, run consolidations, or post back. |
| Bounded entity required | The form rejects an empty, "all", or wider-than-500-member entity selection, and a single aggregate member can still expand server side — keep the slice scoped. |
| Manual members on older pods | Where a pod doesn't expose the metadata endpoint, member lists don't auto-populate; enter member names by hand. |
| Row-level security is admin-governed | The `Entity` column is RLS-ready, but an administrator must publish, declare, approve the first write, and reconcile before the table is filtered. |

## Related

- [Extract from HFM / FCCS (guide)](/guides/connections/hfm-fccs/) — the full walkthrough.
- [HFM / FCCS Connector](/reference/connectors/rest/hfm-fccs/) — connection field reference.
- [Oracle EPM (HFM / FCCS) Steps](/reference/workflow-steps/oracle-epm/)
- [Managing Security Groups and Assignments](/administration/access/managing-security-groups-and-assignments/)
