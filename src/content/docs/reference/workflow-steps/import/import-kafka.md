---
title: Import Kafka
description: Read the messages of Apache Kafka topics between two offsets into a PlaidCloud table, one row per message.
sidebar:
  order: 16
---

## Description

Reads the messages of one or more Apache Kafka topics into a project table, one row per message. The step reads a fixed range: from the starting offsets to the ending offsets, where `latest` means the end of each partition when the step starts. Messages that arrive while the step runs are not read. The step reaches Kafka through an [Apache Kafka connection](/reference/connectors/databases/apache-kafka/).

## Source and Target

| Setting | Required | What it does |
| --- | --- | --- |
| Kafka Connection | Yes | The connection to read through. |
| Topics | One of the two | The topics to read, one per line. |
| Topic Pattern | One of the two | A regular expression that selects the topics to read, used instead of **Topics**. |
| Target Table | Yes | The table the messages land in. |

## Message Range

| Setting | Default | What it does |
| --- | --- | --- |
| Starting Offsets | `earliest` | `earliest`, `latest`, or JSON naming an offset for each partition, such as `{"orders": {"0": 1200, "1": 980}}`. In JSON, `-2` means earliest and `-1` latest. |
| Ending Offsets | `latest` | `latest`, or JSON in the same form as the starting offsets. |
| Message Limit (0 = All) | `0` | The most messages to read. `0` reads every message in the range. |
| Idle Timeout (Seconds) | `10` | The read ends after this many seconds without a new message. |
| Time Limit (Seconds) | `10800` | The longest the read may run. |

The offsets take workflow variables written as `{name}`.

## Message Value

| Setting | What it does |
| --- | --- |
| Value Format | **JSON**, **Text**, or **Avro**. |
| Avro Schema (JSON) | The Avro schema of the message value. Required when the format is **Avro**. |
| Extra Consumer Settings (JSON) | Additional Kafka consumer settings as a JSON object, such as `{"fetch.min.bytes": 1}`. Only settings PlaidCloud allows are accepted. |

## Column Mapping

Map at least one column on the mapping tab. A column reads one of the message's parts, `key`, `value`, `topic`, `partition`, `offset`, `timestamp`, `timestamp_type` or `headers`, or a field of the parsed value by its path. There's no **Inspect Source** for this step, so enter the columns by hand.

## Related

- [Export Kafka](/reference/workflow-steps/export/export-kafka/)
- [Apache Kafka connection](/reference/connectors/databases/apache-kafka/)
