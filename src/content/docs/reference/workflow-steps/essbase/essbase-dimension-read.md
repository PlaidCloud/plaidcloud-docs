---
title: "Essbase Dimension Read"
description: Read an Oracle Essbase dimension outline into a PlaidCloud dimension's main hierarchy, cloud-direct — refusing by name any shared, label-only, Dynamic Calc, or attribute member, and anything else the outline can't represent.
---

## Description

Reads one dimension outline from an Oracle **Essbase** cube over your [Oracle Essbase connection](/guides/connections/essbase/) and loads it into a PlaidCloud dimension's **main hierarchy**.

This step appears in the step menu under **Oracle Essbase**.

The step reaches Essbase **cloud-direct** over its REST API — there is no on-premises agent path for this step, and no remote variant of it.

## Configuration

### Essbase Source

| Field | Required | Notes |
|---|---|---|
| Connection | Yes | The [Oracle Essbase connection](/guides/connections/essbase/) to read through. |
| Application | Yes | The Essbase application to read from. The picker lists the applications the connection's service account can see; if the connection sets a default application, it's pre-selected. |
| Cube (Database) | Yes | The cube within the chosen application to read the outline from. |
| Dimension | Yes | The Essbase dimension whose outline to read. |

### Target PlaidCloud Dimension

| Field | Required | Notes |
|---|---|---|
| Target Dimension | Yes | The PlaidCloud dimension the outline loads into. |

## What This Step Cannot Represent

| Limitation | What it means |
|---|---|
| Shared members | A shared member re-uses another member's data under a second parent. A PlaidCloud dimension node has exactly one parent, so a shared member is refused by name rather than loaded as a duplicate or silently dropped. Read the primary rollup as its own PlaidCloud dimension — a shared member's second parent isn't representable here. |
| Label-only members | A label-only member exists for navigation and never holds data of its own. It's refused by name rather than loaded as an ordinary member that nothing downstream expects to be empty. |
| Dynamic Calc members | A Dynamic Calc member's value is computed by Essbase on the fly and never stored. This step reads outline structure, not computed data, so a Dynamic Calc member is refused by name rather than loaded as if it were a stored member. |
| Attribute dimensions | An attribute dimension classifies members of a base dimension — it isn't a hierarchy of facts in its own right. Reading one is refused outright; read the base dimension instead. |
| Unrepresentable consolidation operators | A PlaidCloud edge carries a consolidation flag (`+`, `-`, or `~`). Essbase's `+` and `-` operators map directly. `*`, `/`, and `%` can't be represented as a plain rollup sign — a member that uses one of them is refused by name rather than loaded with the wrong sign. |
| Outlines past the member cap | A dimension outline with more members than the step supports is refused rather than partially loaded, with the count and the cap both named in the error. Read a shallower level of the hierarchy, or a smaller sub-tree, to bring it under the limit. |

## Related

- [Connect to Oracle Essbase (guide)](/guides/connections/essbase/) — create the connection.
- [Oracle Essbase Connector](/reference/connectors/erp/oracle-essbase/) — connection field reference.
- [Essbase Query](/reference/workflow-steps/essbase/essbase-query/) — run a live MDX query against a cube, cloud-direct.
- [Oracle Essbase Steps](/reference/workflow-steps/essbase/)
