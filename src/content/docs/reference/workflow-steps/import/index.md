---
title: Import Steps
description: Workflow steps that bring data from external sources into project tables.
---

Workflow steps that bring data from external sources into project tables.

A file import checks the query that loads its target table before it runs. A query that carries anything other than a plain SQL statement over typed columns is refused before the target table is created, replaced or loaded, so the table is left exactly as it was.

A missing source file is not an error. The import warns with the path and leaves the target table empty with its declared columns, so later steps read zero rows. This applies to CSV, Excel, JSON, fixed-width, YXDB, dBASE, ORC, Avro, Parquet, XML and Db2 extract imports. A tagged XML import creates an empty table only for each tag that declares fields. Archive and Access imports also warn, but they declare no columns, so they create no table. An archive import that finds its files by a document search gives no missing-file warning.

## Steps

- [Import Access](/reference/workflow-steps/import/import-access/)
- [Import Alteryx YXDB](/reference/workflow-steps/import/import-alteryx-yxdb/)
- [Import Archive](/reference/workflow-steps/import/import-archive/)
- [Import Avro](/reference/workflow-steps/import/import-avro/)
- [Import CSV](/reference/workflow-steps/import/import-csv/)
- [Import Db2 Extract](/reference/workflow-steps/import/import-db2-extract/)
- [Import dBASE](/reference/workflow-steps/import/import-dbf/)
- [Import Excel](/reference/workflow-steps/import/import-excel/)
- [Import Delimited](/reference/workflow-steps/import/import-delimited/)
- [Import External Database Tables](/reference/workflow-steps/import/import-external-database-tables/)
- [Import Fixed Width](/reference/workflow-steps/import/import-fixed-width/)
- [Import Google Bigquery](/reference/workflow-steps/import/import-google-bigquery/)
- [Import Google Spreadsheet](/reference/workflow-steps/import/import-google-spreadsheet/)
- [Import HDF](/reference/workflow-steps/import/import-hdf/)
- [Import JSON](/reference/workflow-steps/import/import-json/)
- [Import Kafka](/reference/workflow-steps/import/import-kafka/)
- [Import Monday](/reference/workflow-steps/import/import-monday/)
- [Import MongoDB](/reference/workflow-steps/import/import-mongodb/)
- [Import ORC](/reference/workflow-steps/import/import-orc/) — set with an AI assistant or the REST API
- [Import Parquet](/reference/workflow-steps/import/import-parquet/)
- [Import Project Table](/reference/workflow-steps/import/import-project-table/)
- [Import Quandl](/reference/workflow-steps/import/import-quandl/)
- [Import Singer Source](/reference/workflow-steps/import/import-singer/)
- [Import SPSS](/reference/workflow-steps/import/import-spss/)
- [Import SQL](/reference/workflow-steps/import/import-sql/)
- [Import Stata](/reference/workflow-steps/import/import-stata/)
- [Import XML](/reference/workflow-steps/import/import-xml/)
- [Restore Tables](/reference/workflow-steps/import/restore-tables/)
