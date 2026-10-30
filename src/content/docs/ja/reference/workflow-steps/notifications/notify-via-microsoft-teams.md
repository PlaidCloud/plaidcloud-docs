---
title: Notify via Microsoft Teams ステップ
description: PlaidCloud のワークフローステップから Microsoft Teams 通知を送信し、ワークフローのイベントやステータスをチャネルまたはユーザーに知らせます。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-microsoft-teams.md
---

ワークフローから Microsoft Teams 通知を追加するには、2 つの部分から成る手順が必要です。2 つの部分は次のとおりです。


1. Microsoft Teams の外部接続を作成する
2. ワークフローに Microsoft Teams 通知ステップを追加する

## ワークフローに Microsoft Teams 通知ステップを追加する


ワークフローへの Microsoft Teams 通知ステップの追加は、他のステップを追加する場合と同じです。ステップを追加したら、ステップの設定を開いてフォームに入力し、保存します。これで Microsoft Teams 通知をテストできます。



## Microsoft Teams メッセージの書式設定


Teams には、画像の追加やユーザーへのメンションなど、多くの書式設定オプションがあります。詳細については、[Teams メッセージのテキスト書式設定](https://support.microsoft.com/en-us/office/use-markdown-formatting-in-teams-4d10bd65-55e2-4b2d-a1f3-2bebdcd2c772)のドキュメントを参照してください。



## Microsoft Teams の外部接続を作成する


これは、PlaidCloud がお客様に代わって Microsoft Teams 通知を送信できるようにするための、1 回限りの設定です。Microsoft Teams では、ウェブフックアプリ（インターネット経由で通知を送信する汎用的な方法）を作成できます。Microsoft Teams でウェブフックアプリを作成したら、提供された認証情報を PlaidCloud に追加して、利用できるようにします。



### Microsoft Teams ウェブフックアプリの作成


これらの手順は、Microsoft Teams の管理者が実行する必要があります。[受信 Webhook の作成（Microsoft Teams のドキュメント）](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook#create-incoming-webhook-1)に記載されている手順に従ってください。



### PlaidCloud の外部接続の設定


これらの手順は、外部データ接続を作成する権限を持つ PlaidCloud ワークスペースの管理者が実行する必要があります。接続を作成するには、次の手順に従います。


1. `Analyze > Tools > External Data Connections` に移動します
2. `+ New Connection` の選択肢から、Microsoft Teamsウェブフックを選びます
3. 名前と説明を入力し、上記のウェブフックの作成時に生成されたウェブフック URL を貼り付けます。ここで指定した名前がワークフローステップの選択肢として表示されるため、可能であればわかりやすい名前にしてください。URL を知っている人は誰でもチャネルに投稿できるため、**Webhook URL** フィールドは貼り付け時にマスクされ、接続を開き直すと空白で表示されます。保存済みの URL を維持するには、空白のままにしてください。
4. `+ Create` ボタンを選択します


## 例

まだ例はありません...
