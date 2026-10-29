---
title: Linode Object Storage アカウントの追加
description: Linode の S3 互換クラウドストレージを使ってデータファイルをインポートおよびエクスポートするために、Linode（Akamai）Object Storage アカウントを PlaidCloud に追加します。
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-linode-object-storage-account.md
---

## Linode Object Storage のセットアップ

以下の手順は、Linode Cloud Manager で行う必要があります。

1. [Linode Cloud Manager](https://cloud.linode.com)にサインインします
2. 左側のサイドバーの **Object Storage** に移動します
3. バケットがまだない場合は作成します。バケット名（**label** と呼ばれます）とリージョン（例: `us-east-1`）を控えておきます。
4. **Object Storage > Access Keys** に移動します
5. **Create Access Key** を選択します
6. キーにラベルを付け、読み取りと書き込みの権限でアクセスさせるバケットを選択します
7. **Create Access Key** を選択します
8. **Access Key** と **Secret Key** をコピーします。以下の PlaidCloud ドキュメントのセットアップで使用するため、両方を保存しておきます。シークレットは1度しか表示されません。
9. バケットのリージョンのエンドポイント URL を控えておきます。形式は `https://{region}.linodeobjects.com` です（例: `https://us-east-1.linodeobjects.com`）

これで、Linode Object Storage アカウントを PlaidCloud のドキュメントに追加するために必要なものがすべて揃いました。


## PlaidCloud ドキュメントのセットアップ

1. PlaidCloud にサインインします
2. 新しいドキュメントアカウントを置くワークスペースを選択します
3. `Document > Manage Accounts` に移動します
4. `+ New Account` ボタンを選択します
5. **サービスタイプ**として `Linode Object Storage` を選択します
6. 名前と説明を入力します
7. **開始パス**に、エンドポイント URL とそれに続くバケット名を入力します: `https://us-east-1.linodeobjects.com/my-bucket`
8. **リージョン**を入力します（例: `us-east-1`）
9. ユースケースに適した**セキュリティモデル**を選択します。不明な場合は `Private` のままにします。
10. **Access Key** を、認証情報の下のアクセスキーIDフィールドに貼り付けます
11. **Secret Key** を、認証情報の下のシークレットアクセスキーフィールドに貼り付けます
12. 保存ボタンを選択すると、新しいドキュメントアカウントが利用可能になります
