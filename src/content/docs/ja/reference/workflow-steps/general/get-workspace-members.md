---
title: Get Workspace Members ステップ
description: ワークスペースのメンバーをプロジェクトテーブルに書き込み、含めるアイデンティティ情報とアクティビティ情報のフィールドを選択します。
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## 説明

ワークスペースのメンバーをプロジェクトテーブルに書き込みます。アクセス状況のレポート、メンバー一覧と人事フィードの照合、現在アクセス権を持つメンバーに基づく下流ステップの制御に使用します。

## 設定

### 含める情報

デフォルトでオンになっているのは、**姓**、**名**、**メール**、**ユーザー名**、**メンバー作成日**、**最終ログインのタイムスタンプ** です。

### 追加設定

デフォルトではオフです。

- **無効化されたメンバーを含める** — 出力を、有効なメンバー以外にも広げます。
- **ログイン履歴モード** — 最後のログインだけでなく、ログイン履歴を返します。

## 関連項目

- [一般ステップ](/ja/reference/workflow-steps/general/)
- [Deactivate Workspace Members ステップ](/ja/reference/workflow-steps/general/deactivate-workspace-members/)
- [メンバー管理](/ja/administration/access/)
