---
title: MinIOアカウントの追加
description: セルフホストのS3互換オブジェクトストレージを使用して、データファイルのインポートとエクスポートを行うために、MinIOストレージアカウントをPlaidCloudに追加します。
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-minio-account.md
---

## MinIOのセットアップ

以下の手順は、MinIOコンソールまたは `mc` CLIで実行します。

1. MinIOコンソール（例：`https://your-minio-host:9001`）にサインインします
2. **Buckets** に移動し、バケットがまだない場合は作成します。バケット名を控えておきます。
3. **Identity > Users**（または **Access Keys**）に移動します
4. 対象のバケットへの読み取り/書き込みアクセス権を持つ新しいユーザーまたはサービスアカウントを作成します
5. ユーザー用に生成された **Access Key** と **Secret Key** をコピーします。後述のPlaidCloud Documentのセットアップで使用するため、両方を保存しておきます。
6. MinIOのエンドポイントURL（例：`https://play.min.io` または `https://minio.yourcompany.com`）を控えておきます

これで、MinIOアカウントをPlaidCloud Documentに追加するために必要な情報がすべて揃いました。


## PlaidCloud Documentのセットアップ

1. PlaidCloudにサインインします
2. 新しいドキュメントアカウントを作成するワークスペースを選択します
3. `Document > Manage Accounts` に移動します
4. `+ New Account` ボタンを選択します
5. サービスタイプとして `MinIO` を選択します
6. 名前と説明を入力します
7. **開始パス**に、MinIOのエンドポイントURLに続けてバケット名と任意のプレフィックスを入力します：`https://minio.yourcompany.com/my-bucket/optional/prefix`
8. MinIOのデプロイでリージョンを使用する場合は**リージョン**を入力します。使用しない場合は空欄のままにします
9. 用途に合った**セキュリティモデル**を選択します。迷う場合は `Private` のままにします。
10. **Access Key** を、認証情報の下にあるアクセスキーIDフィールドに貼り付けます
11. **Secret Key** を、認証情報の下にあるシークレットアクセスキーフィールドに貼り付けます
12. 保存ボタンを選択すると、新しいドキュメントアカウントが有効になります
