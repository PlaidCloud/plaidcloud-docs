---
title: Export to SQL 步骤
description: 在 PlaidCloud 工作流步骤中将数据导出到外部 SQL 数据库，以便将结果加载到下游数据库系统。
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## 说明



将 PlaidCloud 项目表写入文档账户，生成包含 CREATE TABLE 和 INSERT 语句的 SQL 文件。当需要将数据移交给摄取 SQL 脚本而非 CSV 或 Parquet 的系统时很有用。

如需直接加载到远程数据库，请改用相应的数据库导出步骤或 [Agent Remote Import 步骤](/zh-cn/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/) — 它们速度更快，并且不需要中间文件。

## 其他设置

在**行顺序**中，**行排序依据**（`sort_columns`）按这些源列对写入的行排序，第一个键优先，每个键都有**列**、**升序**和**空值**设置。键列不必写出。**空值**默认为升序时在前、降序时在后。它不与**汇总**或**非重复**一起使用。

## 示例


暂无示例……
