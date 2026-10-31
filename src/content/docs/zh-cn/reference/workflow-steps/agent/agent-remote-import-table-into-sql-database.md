---
title: Agent Remote Import Table into SQL Database 步骤
description: 通过 PlaidLink 代理将 PlaidCloud 表数据导入远程 SQL 数据库，在防火墙之后安全地加载数据。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database.md
---

## 说明



将 PlaidCloud 项目表推送到只能通过 PlaidLink 代理访问的数据库。代理从 PlaidCloud 接收数据并在本地执行加载，适合让本地运营数据库与 PlaidCloud 分析保持同步。

典型用法：PlaidCloud 生成刷新后的预测或分摊结果，由代理将其加载到本地 ERP、数据集市或运营报表数据库中。


## 数据如何到达代理

1.2.33 或更高版本的 PlaidLink 代理会以单个 Parquet 文件的形式接收表的行。数字、日期、时间戳和真/假值以其自身类型到达。其他列（例如时间、间隔和 JSON 列）以文本形式到达。空文本值仍与以往一样，以空值（NULL）到达。

较旧的代理仍像以前一样，以压缩的制表符分隔文件形式接收行。[升级代理](/zh-cn/reference/cli/plaidlink/upgrade/)即可接收 Parquet。

## 示例

暂无示例...
