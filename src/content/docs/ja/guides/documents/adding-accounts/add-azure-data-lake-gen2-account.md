---
title: Azure Data Lake Gen2 アカウントの追加
description: Azure の階層型名前空間ストレージを使ってデータファイルをインポートおよびエクスポートするために、Azure Data Lake Storage Gen2 アカウントを PlaidCloud に追加します。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-data-lake-gen2-account.md
---

## Azure Data Lake Gen2 のセットアップ

Azure Data Lake Storage Gen2 は、階層型名前空間を有効にした Azure Blob Storage の上に構築されています。以下の手順は、Azure ポータルで行う必要があります。

1. [Azure ポータル](https://portal.azure.com)にサインインします
2. **Storage accounts** に移動し、**Hierarchical namespace** が有効なストレージアカウントを選択するか、新規に作成します
3. 左側のサイドバーの **Security + networking** の下にある **Access keys** を選択します
4. **Storage account name** と、**Key** の値のいずれか1つをコピーします。以下の PlaidCloud ドキュメントのセットアップで使用するため、両方を保存しておきます。
5. **Data storage** の下の **Containers** に移動し、ファイルシステム（コンテナー）がまだない場合は作成します。ファイルシステム名を控えておきます。

これで、Azure Data Lake Gen2 アカウントを PlaidCloud のドキュメントに追加するために必要なものがすべて揃いました。


## PlaidCloud ドキュメントのセットアップ

1. PlaidCloud にサインインします
2. 新しいドキュメントアカウントを置くワークスペースを選択します
3. `Document > Manage Accounts` に移動します
4. `+ New Account` ボタンを選択します
5. **サービスタイプ**として `Azure Data Lake Gen2` を選択します
6. 名前と説明を入力します
7. **開始パス**フィールドに、ファイルシステム名と任意のパスプレフィックスを入力します（例: `my-filesystem/data`）。最初のパスセグメントがファイルシステム名です。
8. ユースケースに適した**セキュリティモデル**を選択します。不明な場合は `Private` のままにします。
9. **Storage account name** を、認証情報の下のアカウント名フィールドに貼り付けます
10. **Key** を、認証情報の下のアカウントキーフィールドに貼り付けます
11. 保存ボタンを選択すると、新しいドキュメントアカウントが利用可能になります
