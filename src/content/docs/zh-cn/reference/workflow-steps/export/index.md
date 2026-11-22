---
title: 导出步骤
description: 将项目表写入外部目标的工作流步骤——文件格式、文档账户、外部数据库。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/index.md
---

将项目表写入外部目标的工作流步骤——文件格式、文档账户、外部数据库。

## 步骤

- [归档表](/zh-cn/reference/workflow-steps/export/archive-tables/)
- [Export External Database Tables](/zh-cn/reference/workflow-steps/export/export-external-tables/)
- [导出 Kafka](/zh-cn/reference/workflow-steps/export/export-kafka/)
- [导出 MongoDB](/zh-cn/reference/workflow-steps/export/export-mongodb/)
- [导出项目归档](/zh-cn/reference/workflow-steps/export/export-project-archive/)
- [Export Project Table](/zh-cn/reference/workflow-steps/export/export-project-table/)
- [Export Quandl](/zh-cn/reference/workflow-steps/export/export-quandl/)
- [导出 SQL](/zh-cn/reference/workflow-steps/export/export-sql/)
- [Export Templated](/zh-cn/reference/workflow-steps/export/export-templated/)
- [Export to Avro](/zh-cn/reference/workflow-steps/export/export-to-avro/)
- [Export To CSV](/zh-cn/reference/workflow-steps/export/export-to-csv/)
- [Export To Excel](/zh-cn/reference/workflow-steps/export/export-to-excel/)
- [Export To Excel Sheets](/zh-cn/reference/workflow-steps/export/export-to-excel-sheets/)
- [Export To Google Spreadsheet](/zh-cn/reference/workflow-steps/export/export-to-google-spreadsheet/)
- [Export To HDF](/zh-cn/reference/workflow-steps/export/export-to-hdf/)
- [Export To JSON](/zh-cn/reference/workflow-steps/export/export-to-json/)
- [Export to ORC](/zh-cn/reference/workflow-steps/export/export-to-orc/)
- [Export to Parquet](/zh-cn/reference/workflow-steps/export/export-to-parquet/)
- [Export to PDF](/zh-cn/reference/workflow-steps/export/export-to-pdf/)
- [Export To Table Archive](/zh-cn/reference/workflow-steps/export/export-to-table-archive/)
- [Export To XML](/zh-cn/reference/workflow-steps/export/export-to-xml/)
- [过账凭证](/zh-cn/reference/workflow-steps/export/post-documents/)——将一个凭证表过账到您已设置的任何 ERP 系统
- [空间文件导出](/zh-cn/reference/workflow-steps/spatial/spatial-file-export/)
- [Publish to Tableau](/zh-cn/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export](/zh-cn/reference/workflow-steps/export/export-hyper/)

## 写入的列

数据映射器未列出目标列时（即**列**选项卡上的右侧表为空），大多数导出步骤会按步骤运行时源表的实际状态，以表中的列顺序写入源表的所有列。因此，只配置了一半的步骤会将整个表导出到目标位置，而不是运行失败，所以在对外部目标运行导出之前，请检查数据映射器。

如果未映射任何列且源表没有列，CSV、JSON、SQL、Excel、PDF、Google 表格或 Kafka 的导出不会写入任何内容，并以警告结束。在多表导出（如 XML、Parquet、ORC、Avro 或 Excel Sheets）中，该表会被跳过并给出指明该表的警告。导出 MongoDB、Export External Database Tables、Tableau Hyper Export、空间文件导出和 Run SAP PCM Hyper Loader 也是如此：它们会成功并给出指明源或目标的警告，外部表会保留其之前的行。
