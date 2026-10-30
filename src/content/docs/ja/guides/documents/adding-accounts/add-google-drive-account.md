---
title: Google ドライブ アカウントの追加
description: Google ドライブのクラウドストレージを使ってデータファイルをインポートおよびエクスポートするために、Google ドライブのストレージアカウントを PlaidCloud に追加します。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-drive-account.md
---

## Google ドライブのセットアップ

以下の手順は、PlaidCloud が Google ドライブにアクセスするために使用するサービスアカウントを作成するため、Google Cloud コンソールで行う必要があります。

### Google Cloud プロジェクトの作成

1. [Google Cloud コンソール](https://console.cloud.google.com)にサインインします
2. 新しいプロジェクトを作成するか、既存のプロジェクトを選択します

### Google Drive API の有効化

1. **APIs & Services > Library** に移動します
2. **Google Drive API** を検索します
3. それを選択して、**有効にする**をクリックします

### サービスアカウントの作成

1. **APIs & Services > Credentials** に移動します
2. **+ Create Credentials > Service account** を選択します
3. サービスアカウントの名前を入力します（例: `plaidcloud-drive`）
4. **Create and Continue** を選択します
5. 必要に応じてロールを付与します（例: 読み取り専用なら **閲覧者**、読み取りと書き込みなら **エディター**）。**続行**を選択します。
6. **完了**を選択します

### サービスアカウントキーの生成

1. **Service Accounts** の一覧で、作成したばかりのサービスアカウントを選択します
2. **Keys** タブに移動します
3. **Add Key > Create new key** を選択します
4. **JSON** 形式を選択して、**作成**を選択します
5. JSON キーファイルがダウンロードされます。このファイルには PlaidCloud が使用する認証情報が含まれているため、安全に保存してください。

### Drive のコンテンツをサービスアカウントと共有する

1. サービスアカウントのメールアドレスをコピーします（例: `plaidcloud-drive@your-project.iam.gserviceaccount.com`）
2. Google ドライブで、PlaidCloud にアクセスさせたいフォルダーをこのメールアドレスと共有し、**エディター**アクセスを付与します

これで、Google ドライブアカウントを PlaidCloud のドキュメントに追加するために必要なものがすべて揃いました。


## PlaidCloud ドキュメントのセットアップ

1. PlaidCloud にサインインします
2. 新しいドキュメントアカウントを置くワークスペースを選択します
3. `Document > Manage Accounts` に移動します
4. `+ New Account` ボタンを選択します
5. **サービスタイプ**として `Google Drive` を選択します
6. 名前と説明を入力します
7. **開始パス**フィールドに共有フォルダーのパスを入力します。共有されているすべてのコンテンツにアクセスする場合は空白のままにします
8. ユースケースに適した**セキュリティモデル**を選択します。不明な場合は `Private` のままにします。
9. JSON キーファイルの内容全体を、認証情報の下のOAuth2資格情報JSONフィールドに貼り付けます
10. 保存ボタンを選択すると、新しいドキュメントアカウントが利用可能になります
