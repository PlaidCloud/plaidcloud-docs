---
title: Export to SQL 步骤
description: 通过 PlaidCloud 工作流步骤将数据导出到外部 SQL 数据库，以便把结果加载到下游数据库系统。
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## 说明



将 PlaidCloud 项目中的表写入文档账户，生成包含 CREATE TABLE 和 INSERT 语句的 SQL 文件。当需要把数据交给只接收 SQL 脚本、而不接收 CSV 或 Parquet 的系统时，这个步骤很有用。

若要直接加载到远程数据库，请改用相应的数据库导出步骤或 [Agent Remote Import](/zh-cn/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/)，它们速度更快，也不需要中间文件。

## 预览

在**源**选项卡上点击**预览**，无需运行步骤即可显示源表的前 100 行。如果表的行数超过 100，预览会说明显示的是前若干行。如果源表尚不存在，预览会提示没有可预览的内容。已锁定的项目不支持预览。

## 其他设置

在**行顺序**中，**行排序依据**（`sort_columns`）按这些源列对写入的行排序，先按第一个键，每个键都有**列**、**升序**和**空值**设置。键列不必写入。**空值**默认为升序时排在最前、降序时排在最后。它不与**汇总**或**非重复**一起使用。

## 示例


暂无示例……
