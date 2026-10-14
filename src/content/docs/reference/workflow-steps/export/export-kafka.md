---
title: Export Kafka
description: Send each row of a PlaidCloud table to an Apache Kafka topic as a message.
sidebar:
  order: 8
---

## Description

Sends each row of a project table to an Apache Kafka topic as one message. A sent message can't be taken back, so running the step again sends the rows again. The step reaches Kafka through an [Apache Kafka connection](/reference/connectors/databases/apache-kafka/).

## Source and Target

| Setting | Required | What it does |
| --- | --- | --- |
| Source Table | Yes | The table to send. |
| Kafka Connection | Yes | The connection to send through. |
| Topic | Yes | The topic every row is sent to. |

## Message

| Setting | What it does |
| --- | --- |
| Key Column | The column whose value is the message key. Leave it blank to send messages without a key. |
| Value Columns | The comma-separated columns that make up the message value. Leave it blank to send every column. |
| Partition Column | An integer column that names the partition for each message. Leave it blank to let Kafka choose. |
| Value Format | **JSON**, **Text**, or **Avro**. |
| Avro Schema (JSON) | The Avro schema of the message value. Required when the format is **Avro**. |

## Delivery

| Setting | Default | What it does |
| --- | --- | --- |
| Delivery Wait (Seconds) | `60` | How long the step waits at the end for Kafka to confirm every message. |
| Time Limit (Seconds) | `10800` | The longest the send may run. |
| Extra Producer Settings (JSON) | — | Additional Kafka producer settings as a JSON object, such as `{"compression.type": "gzip"}`. Only settings PlaidCloud allows are accepted. |

## Related

- [Import Kafka](/reference/workflow-steps/import/import-kafka/)
- [Apache Kafka connection](/reference/connectors/databases/apache-kafka/)
