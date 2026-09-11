---
title: "TM1 Query"
description: Read cube data from an IBM TM1 / Planning Analytics server by saved view or MDX, apply an optional point-of-view slice, and land the result as a table — cloud-direct over REST, with a preview before you save.
---

## Description

Reads data from an IBM **TM1 / Planning Analytics** cube over your [TM1 connection](/guides/connections/tm1/), either by running a saved **view** or by writing an **MDX** query. A point-of-view (POV) can pin additional dimension members beyond what the view or MDX already fixes. The returned cellset lands as a project table — schema-on-read, with dimension columns plus a `Value` measure column, created from the query's own axes.

This step appears in the step menu under **IBM TM1 / Planning Analytics**.

The step reaches TM1 **cloud-direct** over its REST API — there is no on-premises agent involved, and none available for this step yet.

## Configuration

### Source and Target

| Field | Required | Notes |
|---|---|---|
| TM1 Connection | Yes | The [TM1 connection](/guides/connections/tm1/) to read through. |
| Environment | Yes | The connection's environment. |
| Database | Yes | The TM1 database (instance) to query. Defaults to the connection's Default Database if one is set. |
| Cube | Yes | The TM1 cube to query. Discovered live from the connected database, or typed by hand. |
| Target Table | Yes | The project table the returned cellset lands in. |

### Slice

| Field | Required | Notes |
|---|---|---|
| Source Mode | Yes | `By View` (default) runs a saved TM1 view. `By MDX` runs a raw MDX query you write. |
| View | With By View | The saved TM1 cube view to run. Discovered live once a cube is chosen, or typed by hand. |
| MDX | With By MDX | The MDX query to run against the cube. |

### Point of View

Pin one member per dimension to bound the slice beyond what the view or MDX already fixes — useful for an incremental extract (see below). Add a dimension row, pick the dimension, and type the member. A member value can be a literal (`Jan-2026`) or a `{variable}` token resolved from the workflow's own variables at run time, the same substitution the MDX field itself gets. Leave the point of view empty for a plain view or MDX read. Applying a point of view alongside `By View` is not supported — use `By MDX` if you need one.

### Options

| Field | Default | Notes |
|---|---|---|
| Suppress Zero/Empty Cells | Off | Drops cells whose value is exactly numeric `0` **after** they've been fetched. It saves no bandwidth and, in a planning cube where a posted `0` is a real fact, discards it. Prefer suppressing zeros in the query itself — `NON EMPTY` in your MDX, or the saved view's own suppression setting — so TM1 never computes them in the first place. |
| Row Limit | Unlimited | Caps the number of returned cells. Leave blank for unlimited. A query that exceeds the limit fails rather than truncating silently — narrow the query or raise the limit. |

## Incremental Extracts

TM1 has no built-in change tracking, so there's no "give me only what changed since last time" call to make. The pattern instead is to **slice by period (or version)** on every run: pin `Period` in the point of view to a `{period}` workflow variable rather than a literal member name, so each run substitutes the run's own target period and pulls one period's worth of data instead of the whole cube. Combine this with a scheduled workflow and a variable that advances each run to build an incremental history one period at a time.

## Preview

Before saving, **Preview** runs the current slice against TM1 and shows the first rows and a cell count, capped to a small row limit independent of whatever Row Limit the step itself is configured with.

## When Value Lands as Text

A TM1 measure dimension routinely holds numeric elements (`Sales`, `Cost`) alongside String elements (`Comment`, `Status`) in the same dimension. A slice that spans both lands the `Value` column as text — a column has one physical type, and a single non-numeric cell in the slice is enough to decide it.

This is correct handling: setting the string cells to null would lose data, failing the query would block a legitimate cube, and splitting into two columns would make the schema depend on the data returned. What the step does instead is say so. It warns, naming the column, the scale, and the elements responsible, for example:

> Column Value landed as text: 3 of 4,812 cells are non-numeric (text or boolean), and a column can only have one type. The non-numeric cells come from element Comment. Exclude that element from the slice, or query it separately, to keep this column numeric.

**Preview** shows the same detail before you save, and the point-of-view member picker marks each element's TM1 type (Numeric, String, or Consolidated) so a String element is visible before you pin it. Pinning a String element in the point of view is not blocked — it is a legitimate way to read a text measure — but doing so lands the whole `Value` column as text, since the measure sits in the POV rather than on an axis; in that case the warning reports the counts without naming an element, because every member on the axes is equally non-numeric and none of them discriminates the slice.

To keep `Value` numeric, exclude the String element from the slice, or query the String and numeric measures separately.

## Capability Limits

| Limitation | What it means |
|---|---|
| Read-only | Reads cube data from TM1. No write-back, no TI process execution. |
| Cloud-direct only | No on-premises PlaidLink agent path for this step yet — the TM1 server needs a network path PlaidCloud can reach directly. |
| No change tracking | TM1 exposes no delta/changed-since API. Slice by period or version on every run instead (see Incremental Extracts above). |
| No dimension/hierarchy import | This step reads cube data. Importing TM1 dimension hierarchies as PlaidCloud dimensions is not available yet. |

## Related

- [Connect to TM1 (guide)](/guides/connections/tm1/) — create the connection and build a query.
- [TM1 Connector](/reference/connectors/rest/tm1/) — connection field reference.
- [IBM TM1 / Planning Analytics Steps](/reference/workflow-steps/ibm-planning-analytics/)
