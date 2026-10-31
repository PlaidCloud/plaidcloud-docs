---
title: Sage Intacct RESTコネクター
description: PlaidCloudでSage Intacct REST API接続を設定し、財務データと会計データをワークフローに統合します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/sage-intacct.md
---

## APIドキュメント

Sage Intacct REST APIのドキュメントは、[Sage Developerサイト](https://developer.sage.com/intacct/docs/1/sage-intacct-rest-api/get-started/quick-start)で公開されています。


## セキュリティ要件

PlaidCloudには、REST接続ファミリーに専用の**Intacct**接続があります（**REST - Intacct**として一覧表示されます）。この接続は、Intacct REST APIに対するOAuth2クライアント資格情報で認証します。Sage Intacctの**Web Services**のSender IDとSenderパスワードのペアを、接続の**クライアントID**と**クライアントシークレット**として入力し、さらにWebサービスユーザーのユーザー名と会社IDを指定します。センダー資格情報は、Sageサポートによって会社に対して有効化されている必要があります。Webサービスユーザーには、コネクターが読み取るすべてのIntacctオブジェクトに対する権限が必要です。

クライアントIDとクライアントシークレットはシークレットとして扱ってください。PlaidCloudの**Credentials**エリアでのみ保存し、接続から参照します。


## 資格情報の取得

1. Sage Intacctの**Company Setup**エリアを開きます
2. Sageから提供されたSender IDに対してWeb Servicesを有効にします
3. PlaidCloud用のWeb Servicesユーザーを作成または選択します
4. クエリする予定のすべてのオブジェクトに対する権限をユーザーに付与します
5. 会社ID、Webサービスユーザーのユーザー名、Sender ID、Senderパスワードを控えます


## Sage Intacctコネクターの作成

1. **Tools > Connections**に移動し、`Add Connection`をクリックします
2. **REST**の下で**Intacct**（**REST - Intacct**として一覧表示）を選択します
3. 次を入力します。
    * **接続名** — ワークフローステップに表示されるわかりやすい名前
    * **クライアントID** — IntacctのSender ID
    * **クライアントシークレット** — IntacctのSenderパスワード
    * **Webサービスユーザーのユーザー名** — Webサービスユーザーのログイン名
    * **会社ID** — 接続先のIntacct会社
4. `Test`をクリックして資格情報を検証します
5. `Save`をクリックします


## ワークフローステップでの使用

同じ接続で、Intacctからの読み取りとIntacctへの転記の両方を行えます。次のステップで選択できます。

* [Import Sage AP](../../../workflow-steps/sage-intacct/import-sage-ap/)ステップ — AP請求書ヘッダー
* [Import Sage AP Lines](../../../workflow-steps/sage-intacct/import-sage-ap-lines/)ステップ — AP請求書の明細詳細
* [Import Sage Intacct Query](../../../workflow-steps/sage-intacct/import-intacct-query/)ステップ — 任意のIntacctオブジェクトに対する汎用クエリ
* [Import Intacct Entity](../../../workflow-steps/sage-intacct/import-intacct-entity/)ステップ — 総勘定元帳の明細、残高、エントリ、ディメンションマスターを自動ページングで取得
* [Intacct: 仕訳の転記](../../../workflow-steps/sage-intacct/export-to-sage/)ステップ — 仕訳を転記
