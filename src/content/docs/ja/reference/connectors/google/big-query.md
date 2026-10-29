---
title: Google BigQueryコネクター
description: PlaidCloudでGoogle BigQuery接続を設定し、分析クエリを実行して大規模データをワークフローに統合します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/google/big-query.md
---

## 接続のドキュメント
[Google BigQueryのドキュメント](https://docs.cloud.google.com/bigquery/docs)。

## 設定

この接続の作成時または編集時に、次のフィールドが表示されます。必須かどうかは、有効にする認証オプションによって異なります。

### 識別情報

| フィールド | タイプ | 説明 |
|---|---|---|
| 名前 | テキスト | この接続の表示名。 |
| エイリアス | テキスト（複数行） | 接続に関する任意のエイリアスまたはメモ。 |
| 有効 | トグル | 接続を有効にするかどうか。削除せずに一時停止するには無効にします。 |
| DB読み取り専用 | トグル | 接続を読み取り専用の操作に制限します。 |
| アクセスタイプ | 選択 | この接続の読み取り専用、書き込み専用、読み取り/書き込みのいずれかのアクセスレベル。 |

### BigQuery接続

| フィールド | 必須 | 説明 |
|---|---|---|
| プロジェクト | はい | データセットを保持するGoogle Cloudプロジェクト。 |
| データセット | はい | 読み取りと書き込みの対象となるBigQueryデータセット。 |
| テーブル | はい | データセット内のテーブル。 |

### 認証情報

| フィールド | 必須 | 説明 |
|---|---|---|
| サービスアカウントキー（JSON） | はい | データセットを読み取れるGoogleサービスアカウントのJSONキーファイル全体を貼り付けます。データセットに書き込む場合にのみ、書き込みアクセスを付与してください。キーは書き込み専用です。編集時に空白のままにすると、保存済みのキーが保持されます。 |

この接続は、指定したサービスアカウントキーのみで認証します。[Import SQL](/ja/reference/workflow-steps/import/import-sql/)ステップはこの接続を通じてBigQueryを読み取り、[Export External Database Tables](/ja/reference/workflow-steps/export/export-external-tables/)ステップはBigQueryのロードジョブで書き込みます。
