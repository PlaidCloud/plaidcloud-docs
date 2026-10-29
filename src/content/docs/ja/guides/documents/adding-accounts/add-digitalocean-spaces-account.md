---
title: DigitalOcean Spaces アカウントの追加
description: DigitalOcean の S3 互換オブジェクトストレージを使ってデータファイルをインポートおよびエクスポートするために、DigitalOcean Spaces ストレージアカウントを PlaidCloud に追加します。
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-digitalocean-spaces-account.md
---

## DigitalOcean Spaces のセットアップ

以下の手順は、DigitalOcean コントロールパネルで行う必要があります。

1. [DigitalOcean コントロールパネル](https://cloud.digitalocean.com)にサインインします
2. 左側のサイドバーの **Spaces Object Storage** に移動します
3. Space がまだない場合は作成します。Space 名とリージョン（例: `nyc3`）を控えておきます。
4. （Tokens セクションの下の）**API > Spaces Keys** に移動します
5. **Generate New Key** を選択します
6. キーに名前を付けます
7. **Key**（アクセスキー）と **Secret** をコピーします。以下の PlaidCloud ドキュメントのセットアップで使用するため、両方を保存しておきます。シークレットは1度しか表示されません。
8. Space のリージョンのエンドポイント URL を控えておきます。形式は `https://{region}.digitaloceanspaces.com` です（例: `https://nyc3.digitaloceanspaces.com`）

これで、DigitalOcean Spaces アカウントを PlaidCloud のドキュメントに追加するために必要なものがすべて揃いました。


## PlaidCloud ドキュメントのセットアップ

1. PlaidCloud にサインインします
2. 新しいドキュメントアカウントを置くワークスペースを選択します
3. `Document > Manage Accounts` に移動します
4. `+ New Account` ボタンを選択します
5. **サービスタイプ**として `DigitalOcean Spaces` を選択します
6. 名前と説明を入力します
7. **開始パス**に、エンドポイント URL とそれに続く Space 名を入力します: `https://nyc3.digitaloceanspaces.com/my-space`
8. **リージョン**を入力します（例: `nyc3`、`sfo3`、`ams3`）
9. ユースケースに適した**セキュリティモデル**を選択します。不明な場合は `Private` のままにします。
10. **Key** を、認証情報の下のアクセスキーIDフィールドに貼り付けます
11. **Secret** を、認証情報の下のシークレットアクセスキーフィールドに貼り付けます
12. 保存ボタンを選択すると、新しいドキュメントアカウントが利用可能になります
