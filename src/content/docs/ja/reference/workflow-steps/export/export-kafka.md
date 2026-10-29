---
title: Kafkaのエクスポート
description: PlaidCloudテーブルの各行を、メッセージとしてApache Kafkaトピックに送信します。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-kafka.md
---

## 説明

プロジェクトテーブルの各行を、1件のメッセージとしてApache Kafkaトピックに送信します。送信したメッセージは取り消せないため、ステップを再実行すると、行が再び送信されます。このステップは、[Apache Kafka接続](/ja/reference/connectors/databases/apache-kafka/)を通じてKafkaに接続します。

## ソースとターゲット

| 設定 | 必須 | 内容 |
| --- | --- | --- |
| ソーステーブル | はい | 送信するテーブルです。 |
| Kafka接続 | はい | 送信に使用する接続です。 |
| トピック | はい | すべての行の送信先となるトピックです。 |

## メッセージ

| 設定 | 内容 |
| --- | --- |
| キー列 | 値がメッセージのキーになる列です。空欄にすると、キーなしでメッセージを送信します。 |
| 値の列 | メッセージの値を構成する列を、カンマ区切りで指定します。空欄にすると、すべての列を送信します。 |
| パーティション列 | 各メッセージのパーティションを指定する整数列です。空欄にすると、Kafkaが選択します。 |
| 値の形式 | **JSON**、**テキスト**、**Avro**のいずれかです。 |
| Avroスキーマ（JSON） | メッセージの値のAvroスキーマです。形式が**Avro**の場合は必須です。 |

## 配信

| 設定 | デフォルト | 内容 |
| --- | --- | --- |
| 配信待機時間（秒） | `60` | 最後に、Kafkaがすべてのメッセージを確認するまでステップが待機する時間です。 |
| 制限時間（秒） | `10800` | 送信の実行を許可する最長時間です。 |
| 追加のプロデューサー設定（JSON） | — | `{"compression.type": "gzip"}` のような、JSONオブジェクトで指定する追加のKafkaプロデューサー設定です。PlaidCloudが許可している設定のみ受け付けられます。 |

## 関連項目

- [Kafkaのインポート](/ja/reference/workflow-steps/import/import-kafka/)
- [Apache Kafka接続](/ja/reference/connectors/databases/apache-kafka/)
