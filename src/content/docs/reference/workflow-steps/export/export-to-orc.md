---
title: Export to ORC
description: Export PlaidCloud project tables to a document account as Apache ORC files, in columnar form with the compression codec you choose.
sidebar:
  order: 13.5
---

## Description

Writes project tables to a document account as [Apache ORC](https://orc.apache.org/) files, one file for each table. ORC is a columnar format read by Hive, Spark, and most cloud data platforms, with the schema carried in the file. Pair it with [Import ORC](/reference/workflow-steps/import/import-orc/).

Create and set the step with an AI assistant or the REST API; it does not have a step form yet. [Migrated KNIME workflows](/guides/workflows/migrate-knime-workflows/) use this step for ORC writers.

## Configuration

* `output_file` — the Document account and folder the files are written to.
* `file_name` — the file prefix. Each table is written as `<prefix><table name>.orc`.
* `compression` — the ORC codec used inside the file: `snappy`, `zlib` (`gzip` is accepted as `zlib`), `zstd`, or `lz4`. Empty writes the file uncompressed. Any other value stops the export.
* `frames` — the tables to export, each with its column mapping, filter, and an optional `sort_columns` list that orders the written rows.
* `if_exists` — `overwrite` (default) replaces a file that is already there; `fail` stops the step, writing nothing, when a file it would write already exists.

## Related

- [Export steps](/reference/workflow-steps/export/)
- [Import ORC](/reference/workflow-steps/import/import-orc/)
- [Export to Parquet](/reference/workflow-steps/export/export-to-parquet/)
