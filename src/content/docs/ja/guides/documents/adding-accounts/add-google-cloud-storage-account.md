---
title: Google Cloud Storage アカウントの追加
description: Google のクラウドオブジェクトストレージを使ってデータファイルをインポートおよびエクスポートするために、Google Cloud Storage アカウントを PlaidCloud に追加します。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-cloud-storage-account.md
---

## Google Cloud のセットアップ


以下の手順は、Google Cloud Platform で行う必要があります


1. Google Cloud Platform アカウントにサインインするか、新規に作成します
2. Google Cloud Storage アカウントを置くプロジェクトを選択するか、新規に作成します
3. Google Cloud Platform コンソールで `Cloud Storage > Browser` に移動します
4. デフォルトまたはテスト用のバケットを作成します
5. Google Cloud Platform コンソールで `IAM & Admin > Service Accounts` に移動します
6. `+ Create Service Account` ボタンを選択します
7. サービスアカウントの情報を入力して、アカウントを作成します
8. サービスアカウントの一覧で、作成したばかりのサービスアカウントを見つけ、右側のコンテキストメニューから `Manage Keys` を選択します
9. `Add Key` メニューの下で、`Create a Key` を選択します
10. 求められたら、キーの形式として JSON を選択します。キーが生成され、デスクトップに自動的にダウンロードされます。このキーは再度取得できないため、必ず控えておいてください。キーを再生成する必要がある場合は、上記の手順 8 に戻ってください。
11. Google Cloud Platform コンソールで `IAM & Admin > IAM` に移動します
12. 作成したばかりのサービスアカウントを見つけ、権限の編集アイコンをクリックします
13. サービスアカウントに `Storage Admin` と `Storage Transfer Admin` の権限を追加して保存します。より制限の緩い権限を割り当てることもできますが、その場合、ドキュメントで利用できる機能に影響します。

これで、GCS アカウントを PlaidCloud のドキュメントに追加するために必要なものがすべて揃いました。



## PlaidCloud ドキュメントのセットアップ

1. PlaidCloud にサインインします
2. 新しいドキュメントアカウントを置くワークスペースを選択します
3. `Document > Manage Accounts` に移動します
4. `+ New Account` ボタンを選択します
5. **サービスタイプ**として `Google Cloud Storage` を選択します
6. 名前と説明を入力します
7. **開始パス**フィールドに、バケット名と任意のパスプレフィックスを入力します（例: `my-bucket` または `my-bucket/data`）。最初のパスセグメントがバケット名です。
8. ユースケースに適した**セキュリティモデル**を選択します。不明な場合は `Private` のままにします。
9. 上記の手順 10 でダウンロードしたサービスアカウントの JSON キーファイルを開き、内容全体をコピーします
10. 認証情報の下の**システムユーザーJSONキー**フィールドに、その内容を貼り付けます
11. 保存ボタンを選択すると、新しいドキュメントアカウントが利用可能になります

有効なサービスアカウントキーが必要です。キーなし、または Google のサービスアカウントキーではないものでアカウントを保存しようとすると、「GCS document accounts require a valid service-account key.」というメッセージが表示されて拒否されます。有効なキーなしで保存された既存のアカウントは、**システムユーザーJSONキー**フィールドにキーを貼り付けるまで動作しなくなります。
