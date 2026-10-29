---
title: 导入 MongoDB
description: 以工作流步骤的形式，将 MongoDB 集合或聚合管道的结果读取到 PlaidCloud 表中。
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-mongodb.md
---

## 说明

将 MongoDB 集合的文档读取到项目表中，每个文档一行。可以使用筛选器只读取所需的文档，也可以使用聚合管道在文档写入之前先在 MongoDB 中重塑它们。步骤通过 [MongoDB 连接](/zh-cn/reference/connectors/databases/mongodb/)访问 MongoDB。

## 源和目标

| 设置 | 必填 | 作用 |
| --- | --- | --- |
| MongoDB 连接 | 是 | 用于读取的连接。 |
| 数据库 | 否 | 要读取的数据库。留空则使用连接的**默认数据库**。 |
| 集合 | 是 | 要读取的集合。 |
| 目标表 | 是 | 文档写入的表。必须是表，而不是视图。 |

## 查询

| 设置 | 作用 |
| --- | --- |
| 筛选器（JSON） | 以 JSON 对象形式给出的 MongoDB 查询筛选器，例如 `{"status": "open"}`。只读取匹配的文档。 |
| 聚合管道（JSON） | 以 JSON 数组形式给出的聚合管道，例如 `[{"$match": {"status": "open"}}]`。设置后，将对集合执行聚合，而不是筛选。包含 `$out` 或 `$merge` 阶段的管道会被拒绝，因为它会写入 MongoDB。 |
| 行数限制（0 = 全部） | 最多读取的文档数。`0` 表示读取每一个文档。 |
| 时间限制（秒） | MongoDB 在停止读取之前最多可花费的时间。 |
| 用于确定列的抽样文档数 | 当步骤未声明列时，从最前面开始用多少个文档来决定列及其类型：这些文档所带的每个顶层字段都会成为一列。默认值为 1000。 |

筛选器和管道可使用以 `{name}` 形式书写的工作流变量，例如 `{"region": "{region}"}`。每个变量的值会作为单个 JSON 字符串或数字插入，因此变量无法向查询中添加键或运算符。如果使用了未定义的变量，步骤会停止并报错，指出该变量。

## 列映射

在映射选项卡上，将每个文档字段映射到目标表的某一列。列会读取同名的文档字段。如果集合不存在，步骤会带警告完成，并保持目标表为空。

## 相关内容

- [导出 MongoDB 步骤](/zh-cn/reference/workflow-steps/export/export-mongodb/)
- [MongoDB 连接](/zh-cn/reference/connectors/databases/mongodb/)
