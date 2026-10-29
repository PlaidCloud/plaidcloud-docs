---
title: AWS S3 アカウントの追加
description: Amazon のクラウドオブジェクトストレージを使ってデータファイルをインポートおよびエクスポートするために、AWS S3 ストレージアカウントを PlaidCloud に追加します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-aws-s3-account.md
---

## AWS S3 のセットアップ

以下の手順は、AWS コンソールで行う必要があります。

1. Amazon Web Services（AWS）アカウントにサインインするか、新規に作成します
2. コンソールで `All services > Storage > S3` に移動します
3. デフォルトまたはテスト用のバケットを作成します。バケット名とリージョン（例: `us-east-1`）を控えておきます。
4. コンソールで `All Services > Security Identity & Compliance > IAM > Users` に移動します
5. `Create User` ボタンを選択します
6. 求められたら、ユーザー名を入力し、`Access Key - Programmatic access` のみを選択します。`Next: Permissions` ボタンを選択します。
7. `Attach existing policies directly` というオプションボックスを選択します
8. フィルター検索ボックスに `s3` と入力します。S3 関連の項目に絞り込まれたら、左側のチェックボックスをオンにして `AmazonS3FullAccess` を選択します。`Next: Tags` ボタンを選択します。
9. `Next: Review` ボタンを選択して、この手順をスキップします
10. ユーザーの設定を確認し、`Create user` を選択します
11. ユーザー用に生成されたキーを、CSV をダウンロードするか、後で使えるようにどこかにコピーして貼り付けて保管します。このキーは再度取得できないため、必ず控えておいてください。キーを再生成する必要がある場合は、上記の手順 5 に戻ってください。

これで、S3 アカウントを PlaidCloud のドキュメントに追加するために必要なものがすべて揃いました。


## PlaidCloud ドキュメントのセットアップ

1. PlaidCloud にサインインします
2. 新しいドキュメントアカウントを置くワークスペースを選択します
3. `Document > Manage Accounts` に移動します
4. `+ New Account` ボタンを選択します
5. **サービスタイプ**として `Amazon S3` を選択します
6. 名前と説明を入力します
7. **開始パス**フィールドに、バケット名と任意のパスプレフィックスを入力します（例: `my-bucket` または `my-bucket/data`）。最初のパスセグメントがバケット名です。
8. ユースケースに適した**セキュリティモデル**を選択します。不明な場合は `Private` のままにします。
9. 上記の手順 11 で作成した**アクセスキー**を、認証情報の下のアクセスキーIDフィールドに貼り付けます
10. 上記の手順 11 で作成した**シークレットキー**を、認証情報の下のシークレットアクセスキーフィールドに貼り付けます
11. バケットの**リージョン**を入力します（例: `us-east-1`、`eu-west-1`）。空白のままにすると、デフォルトの `us-east-2` になります。
12. 保存ボタンを選択すると、新しいドキュメントアカウントが利用可能になります
