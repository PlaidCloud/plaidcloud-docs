---
title: 导入 Kafka
description: 将 Apache Kafka 主题在两个偏移量之间的消息读取到 PlaidCloud 表中，每条消息一行。
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-kafka.md
---

## 说明

将一个或多个 Apache Kafka 主题的消息读取到项目表中，每条消息一行。步骤读取固定范围：从起始偏移量到结束偏移量，其中 `latest` 表示步骤启动时每个分区的末尾。步骤运行期间到达的消息不会被读取。步骤通过 [Apache Kafka 连接](/zh-cn/reference/connectors/databases/apache-kafka/)访问 Kafka。

## 源和目标

| 设置 | 必填 | 作用 |
| --- | --- | --- |
| Kafka 连接 | 是 | 用于读取的连接。 |
| 主题 | 二选一 | 要读取的主题，每行一个。 |
| 主题模式 | 二选一 | 用于选择要读取主题的正则表达式，用于替代**主题**。 |
| 目标表 | 是 | 消息写入的表。 |

## 消息范围

| 设置 | 默认 | 作用 |
| --- | --- | --- |
| 起始偏移量 | `earliest` | `earliest`、`latest`，或为每个分区指定偏移量的 JSON，例如 `{"orders": {"0": 1200, "1": 980}}`。在 JSON 中，`-2` 表示 earliest，`-1` 表示 latest。 |
| 结束偏移量 | `latest` | `latest`，或与起始偏移量形式相同的 JSON。 |
| 消息数量上限（0 = 全部） | `0` | 最多读取的消息数。`0` 表示读取范围内的每条消息。 |
| 空闲超时（秒） | `10` | 在这么多秒内没有新消息时，读取结束。 |
| 时间限制（秒） | `10800` | 读取最长可以运行的时间。 |

偏移量可使用以 `{name}` 形式书写的工作流变量。

## 消息值

| 设置 | 作用 |
| --- | --- |
| 值格式 | **JSON**、**文本**或 **Avro**。 |
| Avro 架构（JSON） | 消息值的 Avro 架构。当格式为 **Avro** 时必填。 |
| 额外的消费者设置（JSON） | 以 JSON 对象形式给出的额外 Kafka 消费者设置，例如 `{"fetch.min.bytes": 1}`。只接受 PlaidCloud 允许的设置。 |

## 列映射

在映射选项卡上至少映射一列。一列可以读取消息的某个部分——`key`、`value`、`topic`、`partition`、`offset`、`timestamp`、`timestamp_type` 或 `headers`——也可以按路径读取已解析值中的某个字段。此步骤没有**检查源**，因此请手动输入列。

## 相关内容

- [导出 Kafka 步骤](/zh-cn/reference/workflow-steps/export/export-kafka/)
- [Apache Kafka 连接](/zh-cn/reference/connectors/databases/apache-kafka/)
