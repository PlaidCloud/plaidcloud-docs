---
title: Cloudflare R2 アカウントの追加
description: Cloudflare のエグレス料金ゼロのオブジェクトストレージを使ってデータファイルをインポートおよびエクスポートするために、Cloudflare R2 ストレージアカウントを PlaidCloud に追加します。
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-cloudflare-r2-account.md
---

## Cloudflare R2 のセットアップ

以下の手順は、Cloudflare ダッシュボードで行う必要があります。

1. [Cloudflare ダッシュボード](https://dash.cloudflare.com)にサインインします
2. アカウントを選択し、左側のサイドバーの **R2 Object Storage** に移動します
3. バケットがまだない場合は作成します。バケット名を控えておきます。
4. **R2 Object Storage > Manage R2 API Tokens** に移動します
5. **Create API Token** を選択します
6. トークンに名前を付け、アクセスさせるバケットを選択し、**Object Read & Write** 権限を選択します
7. **Create API Token** を選択します
8. **Access Key ID** と **Secret Access Key** をコピーします。以下の PlaidCloud ドキュメントのセットアップで使用するため、両方を保存しておきます。シークレットは1度しか表示されません。
9. アカウントの **S3 API endpoint** を控えておきます。形式は `https://{account_id}.r2.cloudflarestorage.com` で、R2 の概要ページに表示されます。

これで、Cloudflare R2 アカウントを PlaidCloud のドキュメントに追加するために必要なものがすべて揃いました。


## PlaidCloud ドキュメントのセットアップ

1. PlaidCloud にサインインします
2. 新しいドキュメントアカウントを置くワークスペースを選択します
3. `Document > Manage Accounts` に移動します
4. `+ New Account` ボタンを選択します
5. **サービスタイプ**として `Cloudflare R2` を選択します
6. 名前と説明を入力します
7. **開始パス**に、R2 のエンドポイントとそれに続くバケット名を入力します: `https://{account_id}.r2.cloudflarestorage.com/my-bucket`
8. **リージョン**フィールドは `auto` に設定するか、空白のままにできます。R2 が最も近いリージョンを自動的に選択します
9. ユースケースに適した**セキュリティモデル**を選択します。不明な場合は `Private` のままにします。
10. **アクセスキーID**を、認証情報の下のアクセスキーIDフィールドに貼り付けます
11. **シークレットアクセスキー**を、認証情報の下のシークレットアクセスキーフィールドに貼り付けます
12. 保存ボタンを選択すると、新しいドキュメントアカウントが利用可能になります
