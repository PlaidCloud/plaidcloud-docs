---
title: Microsoft Dynamics 365 RESTコネクター
description: PlaidCloudでMicrosoft Dynamics REST API接続を設定し、ERPとCRMのデータを分析ワークフローに統合します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics.md
---

## APIドキュメント
このコネクターのエンドポイントについては、[ベンダーのAPIリファレンス](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/)を参照してください。

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

### その他

| フィールド | タイプ | 説明 |
|---|---|---|
| Dynamicsテナント | テキスト | — |
| OAuth2クライアントID | テキスト | — |
| OAuth2クライアントシークレット | テキスト | シークレット資格情報。暗号化して保存されます。 |
| Dynamics CRM | テキスト | — |
