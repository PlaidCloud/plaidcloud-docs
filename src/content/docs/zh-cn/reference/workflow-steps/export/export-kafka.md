---
title: 导出 Kafka
description: 将 PlaidCloud 表的每一行作为一条消息发送到 Apache Kafka 主题。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-kafka.md
---

## 说明

将项目表的每一行作为一条消息发送到 Apache Kafka 主题。已发送的消息无法撤回，因此再次运行该步骤会再次发送这些行。步骤通过 [Apache Kafka 连接](/zh-cn/reference/connectors/databases/apache-kafka/)访问 Kafka。

## 源和目标

| 设置 | 是否必填 | 作用 |
| --- | --- | --- |
| 源表 | 是 | 要发送的表。 |
| Kafka 连接 | 是 | 用于发送的连接。 |
| 主题 | 是 | 每一行发送到的主题。 |

## 消息

| 设置 | 作用 |
| --- | --- |
| 键列 | 其值作为消息键的列。留空则发送不带键的消息。 |
| 值列 | 构成消息值的列，以逗号分隔。留空则发送所有列。 |
| 分区列 | 为每条消息指定分区的整数列。留空则由 Kafka 选择。 |
| 值格式 | **JSON**、**文本**或 **Avro**。 |
| Avro 架构 (JSON) | 消息值的 Avro 架构。格式为 **Avro** 时必填。 |

## 投递

| 设置 | 默认 | 作用 |
| --- | --- | --- |
| 投递等待时间（秒） | `60` | 步骤在结束时等待 Kafka 确认所有消息的时长。 |
| 时间限制（秒） | `10800` | 发送可运行的最长时间。 |
| 额外的生产者设置 (JSON) | — | 以 JSON 对象形式提供的其他 Kafka 生产者设置，例如 `{"compression.type": "gzip"}`。只接受 PlaidCloud 允许的设置。 |

## 相关内容

- [导入 Kafka](/zh-cn/reference/workflow-steps/import/import-kafka/)
- [Apache Kafka 连接](/zh-cn/reference/connectors/databases/apache-kafka/)
