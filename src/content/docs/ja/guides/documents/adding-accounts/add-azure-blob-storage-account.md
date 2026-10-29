---
title: Azure Blob Storage アカウントの追加
description: Microsoft Azure のクラウドオブジェクトストレージを使ってデータファイルをインポートおよびエクスポートするために、Azure Blob Storage アカウントを PlaidCloud に追加します。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-blob-storage-account.md
---

## Azure Blob Storage のセットアップ

以下の手順は、Azure ポータルで行う必要があります。

1. [Azure ポータル](https://portal.azure.com)にサインインします
2. **Storage accounts** に移動し、ストレージアカウントを選択するか、新規に作成します
3. 左側のサイドバーの **Security + networking** の下にある **Access keys** を選択します
4. **Storage account name** と、**Key** の値のいずれか1つをコピーします。以下の PlaidCloud ドキュメントのセットアップで使用するため、両方を保存しておきます。
5. **Data storage** の下の **Containers** に移動し、コンテナーがまだない場合は作成します。コンテナー名を控えておきます。

これで、Azure Blob Storage アカウントを PlaidCloud のドキュメントに追加するために必要なものがすべて揃いました。


## PlaidCloud ドキュメントのセットアップ

1. PlaidCloud にサインインします
2. 新しいドキュメントアカウントを置くワークスペースを選択します
3. `Document > Manage Accounts` に移動します
4. `+ New Account` ボタンを選択します
5. **サービスタイプ**として `Azure Blob Storage` を選択します
6. 名前と説明を入力します
7. **開始パス**フィールドに、コンテナー名と任意のパスプレフィックスを入力します（例: `my-container/data`）。最初のパスセグメントがコンテナー名です。
8. ユースケースに適した**セキュリティモデル**を選択します。不明な場合は `Private` のままにします。
9. **Storage account name** を、認証情報の下のアカウント名フィールドに貼り付けます
10. **Key** を、認証情報の下のアカウントキーフィールドに貼り付けます
11. 保存ボタンを選択すると、新しいドキュメントアカウントが利用可能になります
