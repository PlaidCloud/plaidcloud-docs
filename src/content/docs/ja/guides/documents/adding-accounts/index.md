---
title: 新しいドキュメントアカウントの追加
description: クラウドおよびオンプレミスのドキュメントストレージ（S3、GCS、Azure Blob、Google ドライブ、OneDrive、SFTP、WebDAVなど）をPlaidCloudに接続します。
sidebar:
  label: 新しいドキュメントアカウントの追加
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/index.md
---

クラウドおよびオンプレミスのドキュメントストレージ（S3、Google Cloud Storage、Azure Blob、Google ドライブ、OneDrive、SFTP、WebDAVなど）をPlaidCloudに接続します。プロバイダーごとに、認証情報と接続の流れが異なります。

最も手軽な方法は **PlaidCloudマネージドバケット**です。PlaidCloudがストレージのセットアップと運用を行うため、名前を選ぶだけで、ほかに設定する項目はありません。すでにお持ちのストレージに接続する場合は、以下から該当するプロバイダーを選択してください。

## 保存されたシークレットは書き込み専用

アカウントのシークレットは書き込み専用です。シークレットは、**秘密キー / パスワード**というラベルのフィールドで、アカウントの種類によっては**シークレットアクセスキー**、**アカウントキー**、**クライアントシークレット**、**アクセストークン**、**パスワード**、**システムユーザーJSONキー**、**OAuth2資格情報JSON**のいずれかです。SFTPアカウントの **RSA秘密鍵**も同様に書き込み専用です。保存後は、フォーム、API、AIアシスタントのいずれにも再表示されません。アカウントを編集すると、フィールドは空になり、*Paste the value; leave blank on edit to keep the saved one.* というヒントが表示されます。保存済みのシークレットを維持するには空欄のままにし、置き換えるには新しい値を貼り付けます。

アカウントの接続先を変更する場合は、シークレットの再入力が必要です。**開始パス**の先頭部分（クラウドストレージの場合はバケットまたはコンテナー）、SFTPアカウントの**ホストまたはIPアドレス**や**SSH接続ポート**、OneDriveアカウントの**OneDriveテナントID**を変更する場合も、シークレットを貼り付けてください。貼り付けないと、*Changing where the account connects needs its secret entered again* というメッセージとともに保存が拒否されます。これにより、アカウントを編集できてもシークレットを知らない人が、そのシークレットを任意のサーバーに送信することを防ぎます。

PlaidCloud MCPコネクターを介して接続されたAIアシスタントも、ストレージタイプ、認証情報、開始パスを指定してアカウントを作成および更新できます。認証情報は書き込み専用で、アカウントを読み戻す際には表示されません。具体的な例については、[OneDrive / SharePointアカウントの追加](/ja/guides/documents/adding-accounts/add-onedrive-account/#aiアシスタントを使用したアカウントの作成)を参照してください。
