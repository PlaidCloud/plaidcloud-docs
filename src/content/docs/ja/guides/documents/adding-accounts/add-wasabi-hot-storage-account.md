---
title: Wasabi Hot Storageアカウントの追加
description: コスト効率に優れたクラウドストレージを使用して、データファイルのインポートとエクスポートを行うために、Wasabi Hot StorageアカウントをPlaidCloudに追加します。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-wasabi-hot-storage-account.md
---

## Wasabi Hot Storageのセットアップ


以下の手順は、Wasabi Hot Storageコンソールで実行します。


1. Wasabi Hot Storageアカウントにサインインするか、新規に作成します
2. コンソールで `Buckets` に移動します
3. デフォルトのバケットまたはテスト用のバケットを作成します
4. コンソールで Users に移動します
5. `Create User` ボタンを選択します
6. 求められたら、ユーザー名を入力し、`Programmatic (create API key)` ユーザーを選択します
7. グループの割り当てはスキップします。`Next` ボタンを選択します
8. `WasabiFullAccess` ポリシーの横にあるプラスアイコンを選択して、ポリシーをユーザーにアタッチします。`Next` ボタンを選択します。
9. ユーザー設定を確認し、`Create User` を選択します
10. ユーザー用に生成されたキーを、CSVをダウンロードするか、後で使用できる場所にコピーして貼り付けて控えておきます。このキーは再取得できないため、必ず控えておいてください。キーを再生成する必要がある場合は、上記の手順5に戻ってください。

これで、WasabiアカウントをPlaidCloud Documentに追加するために必要な情報がすべて揃いました。



## PlaidCloud Documentのセットアップ

1. PlaidCloudにサインインします
2. 新しいドキュメントアカウントを作成するワークスペースを選択します
3. `Document > Manage Accounts` に移動します
4. `+ New Account` ボタンを選択します
5. サービスタイプとして `Wasabi Hot Storage` を選択します
6. 名前と説明を入力します
7. バケット名と任意のパスプレフィックスを**開始パス**フィールドに入力します（例：`my-bucket` または `my-bucket/data`）。最初のパスセグメントがバケット名です。
8. 用途に合った**セキュリティモデル**を選択します。迷う場合は `Private` のままにします。
9. 上記の手順10で作成した **Access Key** を、認証情報の下にあるアクセスキーIDフィールドに貼り付けます
10. 上記の手順10で作成した **Secret Key** を、認証情報の下にあるシークレットアクセスキーフィールドに貼り付けます
11. Wasabiアカウントで特定のリージョンを使用している場合は、**リージョン**を入力します。使用していない場合は空欄のままにします
12. 保存ボタンを選択すると、新しいドキュメントアカウントが有効になります
