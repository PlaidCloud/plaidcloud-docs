---
title: Workday RESTコネクタ
description: PlaidCloudでWorkday REST APIへの接続を設定し、人事、財務、計画のデータをワークフローに統合します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday.md
---

## APIドキュメント
このコネクタのエンドポイントについては、[ベンダーのAPIリファレンス](https://community.workday.com/sites/default/files/file-hosting/restapi/)を参照してください。

## 設定

これらのフィールドは、この接続の作成時または編集時に表示されます。必須かどうかは、有効にする認証オプションによって異なります。

### 識別情報

| フィールド | 種類 | 説明 |
|---|---|---|
| 名前 | テキスト | この接続の表示名です。 |
| エイリアス | テキスト（複数行） | 接続に関する任意のエイリアスまたはメモです。 |
| 有効 | トグル | 接続が有効かどうかを示します。削除せずに一時停止するには、無効にします。 |
| データベース読み取り専用 | トグル | 接続を読み取り専用の操作に制限します。 |
| アクセスタイプ | 選択 | この接続のアクセスレベルを、読み取り専用、書き込み専用、読み書きから選択します。 |

### その他

| フィールド | 種類 | 説明 |
|---|---|---|
| OAuth2クライアントID | テキスト | — |
| OAuth2クライアントシークレット | テキスト | 機密の認証情報です。暗号化して保存されます。 |
| WorkdayのURL | テキスト | URLエンドポイントです。 |
| OAuth2リフレッシュトークン | テキスト | — |
