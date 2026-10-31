---
title: Amazon Redshift
description: PlaidCloud で Amazon Redshift データベースへの接続を設定し、Redshift ウェアハウスのデータのクエリ、インポート、エクスポートを行います。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/amazon-redshift.md
---

**Amazon Redshift** は、大規模なデータセットに対する分析ワークロード向けに設計された、AWS のマネージドクラウドデータウェアハウスです。このコネクターを使用すると、PlaidCloud のワークフローから Redshift のテーブルを読み書きできます。コネクターは PostgreSQL のワイヤープロトコルを使用し、認証には標準のデータベース認証情報、または IAM ベースの一時的な認証情報を使用します。

## 公式ドキュメント
ガイドとリファレンス資料については、[Amazon Redshift のドキュメント](https://docs.aws.amazon.com/redshift/)を参照してください。

## 設定

これらのフィールドは、この接続を作成または編集するときに表示されます。必須かどうかは、有効にする認証オプションによって異なります。

### 識別情報

| フィールド | 種類 | 説明 |
|---|---|---|
| Name | テキスト | この接続の表示名です。 |
| Alias | テキスト（複数行） | 接続に関する任意のエイリアスまたはメモです。 |
| Is active | トグル | 接続が有効かどうかを示します。削除せずに一時停止するには無効にします。 |
| Db read only | トグル | 接続を読み取り専用の操作に制限します。 |
| Access type | 選択 | この接続のアクセスレベルです（読み取り専用、書き込み専用、読み書き可能）。 |

### 接続

| フィールド | 種類 | 説明 |
|---|---|---|
| Db host | テキスト | データベースサーバーのホスト名または IP アドレスです。 |
| Db port | 数値 | データベース接続のポート番号です。 |
| Db catalog | テキスト | 接続先のデータベース、カタログ、またはスキーマです。 |

### 認証

| フィールド | 種類 | 説明 |
|---|---|---|
| Db user | テキスト | データベース認証用のユーザー名です。 |
| Use sso | トグル | ユーザー名とパスワードの代わりにシングルサインオンで認証します。 |
| Db password | パスワード | データベース認証用のパスワードです。 |

### SSL / TLS

| フィールド | 種類 | 説明 |
|---|---|---|
| Use ssl | トグル | 接続を SSL/TLS で暗号化します。 |
| Ssl mode | 選択 | SSL の検証モードです（例: disable、require、verify-ca、verify-full）。 |
| Ssl auth client cert | テキスト（複数行） | 相互 TLS 認証用のクライアント証明書（PEM）です。 |
| Ssl auth client key | テキスト（複数行） | 相互 TLS 認証用のクライアント秘密鍵（PEM）です。 |
| Ssl auth root cert | テキスト（複数行） | サーバー証明書を検証するためのルート CA証明書（PEM）です。 |
| Ssl auth cert revoke | テキスト（複数行） | 環境で使用している場合の証明書失効リストです。 |

### SSH トンネル

| フィールド | 種類 | 説明 |
|---|---|---|
| Use ssh | トグル | SSH 踏み台サーバー経由で接続をトンネリングします。 |
| Ssh host | テキスト | SSH 踏み台サーバーのホスト名です。 |
| Ssh port | 数値 | SSH 踏み台サーバーのポートです（デフォルトは 22）。 |
| Ssh user | テキスト | SSH 踏み台サーバーのユーザー名です。 |
| Ssh password | パスワード | SSH 踏み台サーバーのパスワードです（パスワード認証を使用する場合）。 |
| Use ssh cert | トグル | パスワードの代わりに秘密鍵で SSH 踏み台サーバーに認証します。 |
| Ssh private key | テキスト（複数行） | 踏み台サーバーの認証用の SSH 秘密鍵（PEM）です。 |
| Ssh host key | テキスト（複数行） | 踏み台サーバーのフィンガープリントを検証するための、想定される SSH ホストキーです。 |
