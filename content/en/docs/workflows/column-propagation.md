---
title: Column Propagation
slug: column-propagation
weight: 14.0
description: Propagate a column rename, type change, or removal from a source table downstream through every workflow step that consumes it.
date: 2026-04-28T00:00:00
---


## Description

When you change a column at the source — rename it, change its type, or remove it — every downstream step that maps to that column has to be updated to match. **Column Propagation** does that work for you in one confirmation.

Propagation is available from the **ColumnMapper** in any step that has a mapper (Project Table, Calculate, Append, Merge, etc.).


## Propagate a Column Change

1. Open the workflow step containing the column you want to change
2. Make the change in the **ColumnMapper** (rename, retype, strip, etc.)
3. Click `Propagate Downstream` in the mapper toolbar
4. Review the **Confirm Propagation** dialog — it lists every downstream step the change will affect, with a per-row summary
5. Click `Confirm` to apply, or `Cancel` to back out

The dialog defaults safely: when a downstream row has no explicit mapping for the column, the source name is used as the target, so no information is lost on the way through.


## What Propagates

* Column rename (source → target)
* Type change
* Strip / multi-character strip
* Removal of an unused column

Steps that reference the column via expressions, filters, or downstream mappers are all updated. Steps that don't reference the column are skipped.


## Errors and Retries

If the propagation request fails (for example, an HTTP 412 from a stale step version), the dialog refetches and lets you retry without losing your selections. If the refetch itself fails, your selections are still preserved so you can correct the underlying issue and try again.

{{< note >}}
Column Propagation only modifies steps within the same workflow. If a downstream workflow consumes the table, update its mappers separately or run a Dependency Audit to find affected steps.
{{< /note >}}
