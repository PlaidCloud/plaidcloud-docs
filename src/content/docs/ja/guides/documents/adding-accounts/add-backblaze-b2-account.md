---
title: Backblaze B2 アカウントの追加
description: 低コストのクラウドオブジェクトストレージを使ってデータファイルをインポートおよびエクスポートするために、Backblaze B2 ストレージアカウントを PlaidCloud に追加します。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-backblaze-b2-account.md
---

## Backblaze B2 のセットアップ

以下の手順は、Backblaze B2 コンソールで行う必要があります。

1. [Backblaze B2 コンソール](https://secure.backblaze.com/b2_buckets.htm)にサインインします
2. **Buckets** に移動し、バケットがまだない場合は作成します。バケット名を控えておきます。
3. **App Keys** に移動します
4. **Add a New Application Key** を選択します
5. キーに名前を付け、アクセスさせるバケットを選択し、適切な権限（読み取りと書き込み）を選択します
6. **Create New Key** を選択します
7. **keyID**（アクセスキーに相当）と **applicationKey**（シークレットキーに相当）をコピーします。以下の PlaidCloud ドキュメントのセットアップで使用するため、両方を保存しておきます。アプリケーションキーは1度しか表示されません。
8. バケットのリージョンの **S3 Endpoint** を控えておきます。形式は `https://s3.{region}.backblazeb2.com` です（例: `https://s3.us-west-004.backblazeb2.com`）。バケットの詳細ページで確認できます。

これで、Backblaze B2 アカウントを PlaidCloud のドキュメントに追加するために必要なものがすべて揃いました。


## PlaidCloud ドキュメントのセットアップ

1. PlaidCloud にサインインします
2. 新しいドキュメントアカウントを置くワークスペースを選択します
3. `Document > Manage Accounts` に移動します
4. `+ New Account` ボタンを選択します
5. **サービスタイプ**として `Backblaze B2` を選択します
6. 名前と説明を入力します
7. **開始パス**に、S3 互換のエンドポイントとそれに続くバケット名を入力します: `https://s3.us-west-004.backblazeb2.com/my-bucket`
8. バケットの**リージョン**を入力します（例: `us-west-004`）
9. ユースケースに適した**セキュリティモデル**を選択します。不明な場合は `Private` のままにします。
10. **keyID** を、認証情報の下のアクセスキーIDフィールドに貼り付けます
11. **applicationKey** を、認証情報の下のシークレットアクセスキーフィールドに貼り付けます
12. 保存ボタンを選択すると、新しいドキュメントアカウントが利用可能になります
