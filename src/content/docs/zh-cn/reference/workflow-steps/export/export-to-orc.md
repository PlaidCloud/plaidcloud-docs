---
title: Export to ORC 步骤
description: 将 PlaidCloud 项目表作为 Apache ORC 文件导出到文档账户，以列式存储并使用您选择的压缩编解码器。
sidebar:
  order: 13.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-orc.md
---

## 说明

将项目表作为 [Apache ORC](https://orc.apache.org/) 文件写入文档账户，每个表一个文件。ORC 是一种列式格式，Hive、Spark 和大多数云数据平台都能读取，架构随文件一起保存。可与 [Import ORC](/zh-cn/reference/workflow-steps/import/import-orc/) 配合使用。

步骤表单包含一个**文件参数**页，用于设置目标文件、前缀、压缩方式以及文件已存在时的处理方式；还有一个**记录参数**页，列出要导出的表，每个表都有各自的表数据选择和数据筛选器。[迁移的 KNIME 工作流](/zh-cn/guides/workflows/migrate-knime-workflows/)使用此步骤来实现 ORC 写入器。

## 配置

* **目标文件**（`output_file`）——写入文件的文档账户和文件夹。
* **目标文件前缀**（`file_name`）——文件前缀。每个表写为 `<prefix><table name>.orc`。
* **压缩选项**（`compression`）——文件内部使用的 ORC 编解码器：**Snappy**、**zlib**、**gzip**（写为 `zlib`）、**Zstandard** 或 **LZ4**。**无**表示写入未压缩的文件。
* **记录参数**（`frames`）——要导出的表。每个 frame 带有各自的表设置；放在步骤顶层而不是 frame 内部的表级设置不会被读取。
  * `id` ——表在警告中的标签。
  * `source` ——要导出的项目表。每个文件以此命名。
  * `source_columns` 和 `target_columns` ——读取的列和写入的列，包括任何重命名、类型和按列聚合。
  * `source_where` ——对源行的筛选器。
  * `aggregate` 和 `aggregation_type` ——汇总行；`aggregation_type` 是应用于未自行设置汇总方式的列的汇总方式。
  * `having` ——对汇总后行的筛选器。
  * `distinct` ——只写入非重复行。
  * `use_target_slicer`、`limit_target_start` 和 `limit_target_end` ——只写入结果中从起始位置到结束位置的行。
  * `sort_columns` ——通过 AI 助手或 REST API 设置，按这些源列对写入的行排序，第一个键优先，每个键为 `{source, ascending, nulls}`。键列不必写入。`nulls` 默认为升序时 `first`、降序时 `last`。不能与 `aggregate` 或 `distinct` 一起使用。
* **已存在的文件**（`if_exists`），位于**文件已存在时**下——**覆盖它**（`overwrite`，默认）会替换已存在的文件；**使步骤失败且不写入任何内容**（`fail`）会在要写入的文件已存在时使步骤停止，且不写入任何内容。

## 相关内容

- [导出步骤](/zh-cn/reference/workflow-steps/export/)
- [Import ORC](/zh-cn/reference/workflow-steps/import/import-orc/)
- [Export to Parquet](/zh-cn/reference/workflow-steps/export/export-to-parquet/)
