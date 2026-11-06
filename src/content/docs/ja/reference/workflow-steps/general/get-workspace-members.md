---
title: Get Workspace Membersステップ
description: ワークスペースのメンバーをプロジェクトのテーブルに書き込み、含める ID 情報とアクティビティ情報を選択します。
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## 説明

ワークスペースのメンバーをプロジェクトのテーブルに書き込みます。アクセス状況のレポート、メンバーリストと人事フィードの照合、現在アクセス権を持つ人に基づく後続ステップの実行などに使用します。

## 設定

### 含める情報

デフォルトでオンになっている項目は、**姓**、**名**、**メール**、**ユーザー名**、**メンバー作成日**、**最終ログインのタイムスタンプ**です。

### 追加設定

デフォルトではオフです。

- **無効化されたメンバーを含める** — 出力をアクティブなメンバー以外にも広げます。
- **ログイン履歴モード** — 最後のログインだけでなく、ログイン履歴を返します。

## セキュリティログ

実行のたびに、書き込まれた列、ターゲットテーブル、ワークフロー、ステップ、実行を記録したエントリがセキュリティログに書き込まれます。

## 関連項目

- [一般ステップ](/ja/reference/workflow-steps/general/)
- [Deactivate Workspace Membersステップ](/ja/reference/workflow-steps/general/deactivate-workspace-members/)
- [Get Workspace Usageステップ](/ja/reference/workflow-steps/general/get-workspace-usage/)
- [メンバー管理](/ja/administration/access/)
