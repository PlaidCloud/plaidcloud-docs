---
title: Export to SQL
description: Export data to external SQL databases from a PlaidCloud workflow step for loading results into downstream database systems.
sidebar:
  order: 9
---

## Description



Writes a PlaidCloud project table to a document account as a SQL file containing CREATE TABLE and INSERT statements. Useful when you need to hand off data to a system that ingests SQL scripts rather than CSV or Parquet.

For loading directly into a remote database, use the appropriate database export step or [Agent Remote Import](/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/) instead — those are faster and don't require an intermediate file.

## Additional Settings

In **Row Order**, **Order Rows By** (`sort_columns`) orders the written rows by these source columns, first key first, each with a **Column**, **Ascending** and **Nulls** setting. A key column need not be written. **Nulls** defaults to first ascending and last descending. It is not used with **Summarize** or **Distinct**.

## Examples


No examples yet...
