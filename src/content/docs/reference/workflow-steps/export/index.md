---
title: Export Steps
description: Workflow steps that write project tables to external destinations — file formats, document accounts, external databases.
---

Workflow steps that write project tables to external destinations — file formats, document accounts, external databases.

## Steps

- [Archive Tables](/reference/workflow-steps/export/archive-tables/)
- [Export External Database Tables](/reference/workflow-steps/export/export-external-tables/)
- [Export Kafka](/reference/workflow-steps/export/export-kafka/)
- [Export MongoDB](/reference/workflow-steps/export/export-mongodb/)
- [Export Project Archive](/reference/workflow-steps/export/export-project-archive/)
- [Export Project Table](/reference/workflow-steps/export/export-project-table/)
- [Export Quandl](/reference/workflow-steps/export/export-quandl/)
- [Export SQL](/reference/workflow-steps/export/export-sql/)
- [Export Templated](/reference/workflow-steps/export/export-templated/)
- [Export to Avro](/reference/workflow-steps/export/export-to-avro/)
- [Export To CSV](/reference/workflow-steps/export/export-to-csv/)
- [Export To Excel](/reference/workflow-steps/export/export-to-excel/)
- [Export To Excel Sheets](/reference/workflow-steps/export/export-to-excel-sheets/)
- [Export To Google Spreadsheet](/reference/workflow-steps/export/export-to-google-spreadsheet/)
- [Export To HDF](/reference/workflow-steps/export/export-to-hdf/)
- [Export To JSON](/reference/workflow-steps/export/export-to-json/)
- [Export to ORC](/reference/workflow-steps/export/export-to-orc/)
- [Export to Parquet](/reference/workflow-steps/export/export-to-parquet/)
- [Export to PDF](/reference/workflow-steps/export/export-to-pdf/)
- [Export To Table Archive](/reference/workflow-steps/export/export-to-table-archive/)
- [Export To XML](/reference/workflow-steps/export/export-to-xml/)
- [Post Documents](/reference/workflow-steps/export/post-documents/) — post a table of documents to any ERP system you have set up
- [Spatial File Export](/reference/workflow-steps/spatial/spatial-file-export/)
- [Publish to Tableau](/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export](/reference/workflow-steps/export/export-hyper/)

## Columns Written

Most export steps write every column of the source table, as it is when the step runs and in the table's column order, when the Data Mapper lists no target columns, that is, when the right-hand table on the **Columns** tab is empty. A step left half-configured therefore exports the whole table to its destination instead of failing, so check the Data Mapper before you run an export against an external destination.

If no columns are mapped and the source table has none, an export of CSV, JSON, SQL, Excel, PDF, Google Spreadsheet or Kafka writes nothing and finishes with a warning. In an export of several tables, such as XML, Parquet, ORC, Avro or Excel Sheets, that table is skipped with a warning naming it.
