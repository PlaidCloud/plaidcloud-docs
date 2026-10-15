---
title: Table Restore to Timestamp
description: Restore a PlaidCloud table in place to its newest snapshot taken at or before a point in time, as a workflow step.
sidebar:
  order: 45
---

## Description

**Table: Restore to Timestamp** replaces a table in place with its newest snapshot taken at or before a point in time. Use it to roll a table back to how it stood at a period end, or before a load that went wrong. The restore changes the table itself, so every step and dashboard that reads it sees the restored rows.

## Restore to a Point in Time

| Setting | Required | What it does |
| --- | --- | --- |
| Table | Yes | The table to restore. |
| Timestamp | Yes | The point in time, as an ISO-8601 time such as `2026-09-30T23:59:59Z` or as seconds since 1970. A time with no zone is UTC. A workflow variable such as `{restore_time}` works too. |
| A snapshot taken exactly at the timestamp counts | No | On by default. Clear it to restore only to a snapshot taken before the timestamp. |

When no snapshot was taken at or before the timestamp, the step finishes with a warning, leaves the table as it is, and the workflow continues. A table that isn't found also finishes with a warning. On a storage engine that keeps only named snapshots, the table can be restored only to a snapshot taken exactly at the timestamp; take a named snapshot at the time you'll want to return to.

## Related

- [Restore Tables](/reference/workflow-steps/import/restore-tables/)
- [Table Steps](/reference/workflow-steps/tables/)
