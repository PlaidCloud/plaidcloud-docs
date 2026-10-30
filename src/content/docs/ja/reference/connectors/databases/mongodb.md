---
title: MongoDB
description: PlaidCloudでMongoDB接続を設定し、コレクションをテーブルに読み込んだり、テーブルをドキュメントとして書き戻したりします。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/mongodb.md
---

**MongoDB**はドキュメントデータベースです。この接続は、[Import MongoDB](/ja/reference/workflow-steps/import/import-mongodb/)でコレクションまたは集計パイプラインの結果をテーブルに読み込むとき、および[Export MongoDB](/ja/reference/workflow-steps/export/export-mongodb/)でテーブルをドキュメントとして書き戻すときに使います。作成するには、接続タイプとして**MongoDB**を選択します。

## 上流のドキュメント
[MongoDBのドキュメント](https://www.mongodb.com/docs/)。

## 構成

### MongoDB接続

| フィールド | 必須 | 説明 |
|---|---|---|
| ホスト | はい | サーバーのホスト名。 |
| SRVアドレスを使用（mongodb+srv://、ポートなし） | いいえ | MongoDB Atlasと同様に、DNSシードリスト経由で接続します。ポートは使用されません。 |
| ポート | いいえ | サーバーのポート。デフォルトは`27017`です。 |
| デフォルトのデータベース | いいえ | ステップでデータベースを指定しなかった場合に使用されるデータベース。 |

### 認証情報

| フィールド | 説明 |
|---|---|
| ユーザー | 接続に使用するユーザー。 |
| パスワード | ユーザーのパスワード（書き込み専用）。 |

### オプション

| フィールド | 説明 |
|---|---|
| 接続オプション | `&`で連結したMongoDB URIオプション（例：`authSource=admin&tls=true`）。PlaidCloudが許可しているオプションのみ受け付けられます。編集時に空白のままにすると、保存済みのオプションが維持されます。 |

### TLS

| フィールド | 説明 |
|---|---|
| CA証明書（PEM） | サーバー証明書に署名した認証局（公的な認証局でない場合）。編集時に空白のままにすると、保存済みの証明書が維持されます。 |
