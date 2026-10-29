---
title: 导入步骤
description: 将外部来源的数据引入项目表的工作流步骤。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/index.md
---

将外部来源的数据引入项目表的工作流步骤。

文件导入会在运行之前检查加载其目标表的查询。如果查询包含的不只是针对带类型列的普通 SQL 语句，则会在目标表被创建、替换或加载之前被拒绝，因此目标表保持原样。

源文件缺失不属于错误。导入会给出包含路径的警告，并使目标表保持为空（保留其已声明的列），因此后续步骤读取到的是零行。这适用于 CSV、Excel、JSON、固定宽度、YXDB、dBASE、ORC、Avro、Parquet、XML 和 Db2 提取导入。带标记的 XML 导入只会为每个声明了字段的标记创建空表。归档导入和 Access 导入同样会给出警告，但它们不声明列，因此不会创建表。通过文档搜索查找文件的归档导入不会给出文件缺失警告。

在步骤运行之前也是如此。当文件缺失或为空时，文件导入映射上的**填充**，以及通过 REST API 或 AI 助手读取文件的列，都会返回*没有可填充的内容*（API 则返回空的列列表）并给出指明路径的警告，而不是报错。从文档将缺失的文件导入新表或新步骤时，不会创建任何内容，会将该文件标记为**已跳过**，并显示指明路径的警告。

## 步骤

- [导入 Access](/zh-cn/reference/workflow-steps/import/import-access/)
- [导入 Alteryx YXDB](/zh-cn/reference/workflow-steps/import/import-alteryx-yxdb/)
- [导入归档](/zh-cn/reference/workflow-steps/import/import-archive/)
- [导入 Avro](/zh-cn/reference/workflow-steps/import/import-avro/)
- [导入 CSV](/zh-cn/reference/workflow-steps/import/import-csv/)
- [导入 Delta Lake](/zh-cn/reference/workflow-steps/import/import-delta/)
- [导入 DB2 提取](/zh-cn/reference/workflow-steps/import/import-db2-extract/)
- [Import dBASE 步骤](/zh-cn/reference/workflow-steps/import/import-dbf/)
- [导入 Excel](/zh-cn/reference/workflow-steps/import/import-excel/)
- [Import Delimited 步骤](/zh-cn/reference/workflow-steps/import/import-delimited/)
- [导入外部数据库表](/zh-cn/reference/workflow-steps/import/import-external-database-tables/)
- [导入固定宽度文件](/zh-cn/reference/workflow-steps/import/import-fixed-width/)
- [Import Google BigQuery 步骤](/zh-cn/reference/workflow-steps/import/import-google-bigquery/)
- [导入 Google 表格](/zh-cn/reference/workflow-steps/import/import-google-spreadsheet/)
- [Import HDF 步骤](/zh-cn/reference/workflow-steps/import/import-hdf/)
- [导入 JSON](/zh-cn/reference/workflow-steps/import/import-json/)
- [导入 Kafka](/zh-cn/reference/workflow-steps/import/import-kafka/)
- [导入 Monday](/zh-cn/reference/workflow-steps/import/import-monday/)
- [导入 MongoDB](/zh-cn/reference/workflow-steps/import/import-mongodb/)
- [导入 ORC](/zh-cn/reference/workflow-steps/import/import-orc/)
- [导入 Parquet](/zh-cn/reference/workflow-steps/import/import-parquet/)
- [Import Project Table 步骤](/zh-cn/reference/workflow-steps/import/import-project-table/)
- [Import Quandl 步骤](/zh-cn/reference/workflow-steps/import/import-quandl/)
- [Import Singer Source 步骤](/zh-cn/reference/workflow-steps/import/import-singer/)
- [Import SPSS 步骤](/zh-cn/reference/workflow-steps/import/import-spss/)
- [导入 SQL](/zh-cn/reference/workflow-steps/import/import-sql/)
- [Import Stata 步骤](/zh-cn/reference/workflow-steps/import/import-stata/)
- [导入 XML](/zh-cn/reference/workflow-steps/import/import-xml/)
- [还原表](/zh-cn/reference/workflow-steps/import/restore-tables/)
