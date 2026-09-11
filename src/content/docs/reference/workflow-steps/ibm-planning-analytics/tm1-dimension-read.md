---
title: "TM1 Dimension Read"
description: Read an IBM TM1 / Planning Analytics hierarchy — elements, parent/child edges, and element attributes — into a PlaidCloud dimension, cloud-direct over REST.
---

## Description

Reads one hierarchy from an IBM **TM1 / Planning Analytics** dimension over your [TM1 connection](/guides/connections/tm1/) and loads it into a PlaidCloud dimension. The TM1 hierarchy's elements, parent/child edges, and element attributes are staged as parent/child rows in a table first, and the PlaidCloud dimension is built from that staged table — the same load PlaidCloud's own Dimension Load step performs, so a TM1 hierarchy lands exactly like a hand-built or any other externally-sourced one.

This step appears in the step menu under **IBM TM1 / Planning Analytics**.

The step reaches TM1 **cloud-direct** over its REST API — no on-premises agent is involved. See [TM1 Query (Agent)](/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) for the on-prem path.

## Configuration

### TM1 Source

| Field | Required | Notes |
|---|---|---|
| TM1 Connection | Yes | The [TM1 connection](/guides/connections/tm1/) to read through. |
| Environment | Yes | The connection's environment. |
| Database | Yes | The TM1 database (instance) to read from. Defaults to the connection's Default Database if one is set. |
| TM1 Dimension | Yes | The TM1 dimension to read. Discovered live from the connected database, or typed by hand. |
| TM1 Hierarchy | No | The hierarchy within the dimension. Discovered live once a dimension is chosen, or typed by hand. Leave blank to read the dimension's own (implicit) hierarchy, which TM1 names after the dimension. |
| Staging Table | Yes | The table the raw parent/child/attribute rows land in before the PlaidCloud dimension is built from it. |

Once a dimension and hierarchy are chosen, the form shows which TM1 element attributes will land as PlaidCloud **aliases** and which as **properties** — driven by TM1's own attribute type (`Alias` vs. `Numeric`/`String`). Every element's own TM1 type (Numeric, String, or Consolidated) also lands as a property, named `tm1_element_type`.

### Target PlaidCloud Dimension

| Field | Required | Notes |
|---|---|---|
| Specify Dimension Dynamically | One of the two | Target dimension name, which may contain `{variable}` tokens resolved at run time. Selected by default. |
| Use Specific Dimension | One of the two | Pick a pre-existing PlaidCloud dimension from the tree instead. |
| Alternate Hierarchy | No | A PlaidCloud alternate-hierarchy key to load into. Leave blank to load the main hierarchy. |

Loading into an alternate hierarchy is validated before anything is written: a PlaidCloud alternate hierarchy may not reparent a node that already exists in the dimension's main hierarchy, and a TM1 alternate hierarchy shares its elements with TM1's own main hierarchy by definition, so this is the normal shape for that option, not an edge case. If any parsed row's parent already exists in the target dimension's main hierarchy, the step fails up front, before the staging table is touched, naming the clashing parents.

## What This Step Cannot Represent

| Limitation | What it means |
|---|---|
| Multi-parent elements are refused | A PlaidCloud dimension node has exactly one parent per hierarchy. A TM1 element sitting under two consolidations in the same hierarchy cannot be loaded — the step fails with a named error listing every offending element and its parents, rather than silently dropping the element from the first consolidation. Read the alternate rollup as its own PlaidCloud dimension, or resolve the duplicate parentage in TM1 first. |
| Consolidation weights carry only a sign | A PlaidCloud edge carries a consolidation flag (`+`, `-`, or `~`), not a coefficient. TM1 weight `0` becomes `~` (the member does not roll up into its parent); a negative weight becomes `-`; a positive weight becomes `+`; an absent weight (TM1's own default) is treated as `+`. A **fractional or multiplier weight — 0.5, 2.0 — cannot be represented**: it lands as a plain `+` and the multiplier is lost. This is counted and named, not swallowed — the run's step warning reports how many edges were affected and lists them as `parent -> child (weight)`, for example `Total Revenue -> Product A (0.5)`, capped at 10 with "(and N more)" beyond that. A root edge (no parent) is named `(root)` rather than left blank. A present-but-non-numeric weight is refused outright rather than guessed at. |
| No agent-mediated discovery | This step is cloud-direct only — see [TM1 Query (Agent)](/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) for reading a TM1 server the cloud cannot reach. |

## Related

- [Connect to TM1 (guide)](/guides/connections/tm1/) — create the connection.
- [TM1 Connector](/reference/connectors/rest/tm1/) — connection field reference, including the on-prem agent path.
- [TM1 Query](/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — read cube data, cloud-direct.
- [TM1 Query (Agent)](/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — read cube data through an on-prem PlaidLink agent.
- [Dimension Load](/reference/workflow-steps/dimensions/dimension-load/) — the same dimension-load mechanism this step builds on.
- [IBM TM1 / Planning Analytics Steps](/reference/workflow-steps/ibm-planning-analytics/)
