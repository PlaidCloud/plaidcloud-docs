---
title: Apache Kafka
description: PlaidCloudでApache Kafka接続を設定し、トピックのメッセージをテーブルに読み込み、テーブルの行をメッセージとして送信します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/apache-kafka.md
---

**Apache Kafka**は、分散型のイベントストリーミングプラットフォームです。この接続を[Kafkaのインポート](/ja/reference/workflow-steps/import/import-kafka/)ステップと組み合わせてトピックのメッセージをテーブルに読み込み、[Kafkaのエクスポート](/ja/reference/workflow-steps/export/export-kafka/)ステップと組み合わせてテーブルの各行をメッセージとして送信します。作成するには、接続タイプとして**Apache Kafka**を選択します。

## 上流のドキュメント
[Apache Kafkaのドキュメント](https://kafka.apache.org/documentation/)。

## 設定

### Kafka接続

| 項目 | 必須 | 説明 |
|---|---|---|
| ブローカー | はい | 接続先のブローカーをカンマで区切って指定します。例：`broker1:9092,broker2:9092`。 |
| セキュリティプロトコル | いいえ | `PLAINTEXT`（デフォルト）、`SSL`、`SASL_PLAINTEXT`、または`SASL_SSL`。 |
| セッションタイムアウト（ms） | いいえ | PlaidCloudからの応答がない状態で、ブローカーがPlaidCloudをコンシューマーグループから外すまでの待機時間。1000以上。 |

### SASL 資格情報

セキュリティプロトコルが`SASL_PLAINTEXT`または`SASL_SSL`の場合に使用します。

| 項目 | 説明 |
|---|---|
| SASL メカニズム | `PLAIN`（デフォルト）、`SCRAM-SHA-256`、`SCRAM-SHA-512`、または`OAUTHBEARER`。Kerberos（`GSSAPI`）は使用できません。 |
| ユーザー | `PLAIN`と`SCRAM`で、接続に使用するユーザー。 |
| パスワード | `PLAIN`と`SCRAM`で使用する、ユーザーのパスワード（書き込み専用）。 |

### OAuth（OAUTHBEARER）

SASLメカニズムが`OAUTHBEARER`の場合に使用します。PlaidCloudは、OAuthのクライアント資格情報グラントを使用してIDプロバイダーからトークンを取得し、有効期限が切れると新しいトークンを取得します。

| 項目 | 説明 |
|---|---|
| トークン エンドポイント URL | IDプロバイダーのトークンエンドポイント。パブリックインターネット上の`https`アドレスである必要があります。 |
| クライアントID | トークンを要求するクライアント。必須。 |
| クライアントシークレット | クライアントのシークレット（書き込み専用）。必須。 |
| スコープ | プロバイダーが必要とする場合に要求するスコープ。 |
| SASL 拡張 | トークンとともに送信される、カンマで区切った`key=value`のペア（任意）。Confluent Cloudが要求する`logicalCluster`や`identityPoolId`などです。 |

### TLS

| 項目 | 説明 |
|---|---|
| CA証明書（PEM） | ブローカーの証明書に署名した認証局。パブリックなものでない場合に指定します。編集時に空白のままにすると、保存済みの証明書が維持されます。 |
