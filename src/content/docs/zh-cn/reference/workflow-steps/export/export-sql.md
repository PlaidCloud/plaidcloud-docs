---
title: Export to SQL 步骤
description: 通过 PlaidCloud 工作流步骤将数据导出到外部 SQL 数据库，以便将结果加载到下游数据库系统中。
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## 描述



将 PlaidCloud 项目表写入文档账户，生成包含 CREATE TABLE 和 INSERT 语句的 SQL 文件。当您需要将数据交给接收 SQL 脚本而不是 CSV 或 Parquet 的系统时，此步骤很有用。

如需直接加载到远程数据库，请改用相应的数据库导出步骤或 [Agent Remote Import](/zh-cn/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/)，它们速度更快，且不需要中间文件。

## 预览

**预览**最多显示步骤从源表读取的查询的 100 行，而不运行该查询。请单击**源**选项卡上的**预览**。如果还有更多行，预览会说明它只显示了前几行，需要运行步骤才能读取全部行。预览填充变量的方式与运行相同，但不支持 `{x:>9}` 之类的变量格式。

预览只读取数据。如果查询使用了预览无法确认是只读的函数，则会显示*预览仅支持标准 SQL 函数。请运行该步骤以查看结果。*请运行步骤以查看结果。在已锁定的项目中，预览不可用。

## 其他设置

在**行顺序**中，**行排序依据**（`sort_columns`）按这些源列对写入的行排序，第一个键优先，每个键都有**列**、**升序**和**空值**设置。键列不必写入。**空值**默认为升序时在前、降序时在后。它不能与**汇总**或**非重复**一起使用。

## 示例


暂无示例…
