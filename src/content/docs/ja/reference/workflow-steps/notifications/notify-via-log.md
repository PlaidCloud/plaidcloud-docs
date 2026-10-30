---
title: Notify Via Log ステップ
description: PlaidCloud のワークフローステップからログエントリを書き込み、ステータスメッセージ、デバッグ情報、監査証跡のイベントを記録します。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-log.md
---

## 説明


Analyze のワークフローログにメッセージを書き込みます。



### メッセージパラメーター


ログに書き込むメッセージを入力します。続いて、次の 3 つの重大度レベルから 1 つを選択します。


* 情報
* 警告
* エラー

このトランスフォームでは、プロジェクト変数とワークフロー変数の両方を使用できます（ご注意）。


## 例


この例では、このトランスフォームを実行すると、ログに**情報**の項目が追加され、*Write a message to the workflow log. I believe you have my stapler, Demo.* と記録されます。
