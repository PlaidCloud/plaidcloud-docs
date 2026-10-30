---
title: 导出 MongoDB
description: 将 PlaidCloud 表写入 MongoDB 集合，作为插入、替换、更新或 upsert 的文档。
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-mongodb.md
---

## 说明

将项目表的每一行作为一个文档写入 MongoDB 集合。集合不存在时会被创建。步骤通过 [MongoDB 连接](/zh-cn/reference/connectors/databases/mongodb/)访问 MongoDB。

## 源和目标

| 设置 | 是否必填 | 作用 |
| --- | --- | --- |
| 源表 | 是 | 要写入的表。 |
| MongoDB 连接 | 是 | 用于写入的连接。 |
| 数据库 | 否 | 要写入的数据库。留空则使用连接的**默认数据库**。 |
| 集合 | 是 | 要写入的集合。 |

## 写入选项

| 设置 | 作用 |
| --- | --- |
| 写入模式 | **每行插入一个文档**（默认）、**替换匹配的文档**、**更新匹配文档的字段**、**替换匹配的文档，若无则插入**，或**更新匹配文档的字段，若无则插入**。 |
| 匹配列 | 标识文档的列，以逗号分隔。除插入外的每种模式都必填。 |
| 写入前删除集合中的每个文档 | 先清空集合，使其只包含本次运行的行。 |
| 遇到第一次写入失败时停止 | 在 MongoDB 拒绝第一个文档时停止。取消勾选则继续处理其余文档。 |
| 等待写入到达日志 | 等待 MongoDB 将每个批次写入其日志。 |
| Write Concern | 留空表示使用连接的设置，也可填写服务器数量或 `majority`。 |
| 每次请求的文档数 | 每次请求发送的文档数量。 |

插入模式每次运行步骤都会再次添加这些文档。替换或更新的模式则无论步骤运行多少次，集合都保持不变，因此当工作流可能对相同的行运行两次时，请使用其中之一。

## 相关内容

- [导入 MongoDB](/zh-cn/reference/workflow-steps/import/import-mongodb/)
- [MongoDB 连接](/zh-cn/reference/connectors/databases/mongodb/)
