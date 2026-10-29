---
title: SAP Profitability and Cost Management（PCM）コネクタ
description: PlaidCloudでSAP Profitability and Cost Management接続を構成し、コスト配賦データをワークフローに統合します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/sap-pcm.md
---

## 上流のドキュメント
[SAP PCMレガシーのドキュメント](https://help.sap.com/docs/SAP_PROFITABILITY_AND_COST_MANAGEMENT)。

## 構成

次のフィールドは、この接続の作成時または編集時に表示されます。必須かどうかは、有効にする認証オプションによって異なります。

### 識別情報

| フィールド | タイプ | 説明 |
|---|---|---|
| 名前 | テキスト | この接続の表示名。 |
| エイリアス | テキスト（複数行） | 接続のエイリアスやメモ（任意）。 |
| 有効 | トグル | 接続が有効かどうか。削除せずに一時停止するには無効にします。 |
| DB読み取り専用 | トグル | 接続を読み取り専用の操作に制限します。 |
| アクセスタイプ | 選択 | この接続のアクセスレベル（読み取り専用、書き込み専用、読み取り/書き込み）。 |

### 認証

| フィールド | タイプ | 説明 |
|---|---|---|
| DBユーザー | テキスト | データベース認証用のユーザー名。 |
| SSOを使用 | トグル | ユーザー名とパスワードの代わりに、シングルサインオンで認証します。 |
| DBパスワード | パスワード | データベース認証用のパスワード。 |
