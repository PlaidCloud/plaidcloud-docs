---
title: Deactivate Workspace Members ステップ
description: プロジェクトテーブルに記載されたワークスペースのメンバーを、メールアドレスまたはユーザー名で照合して無効化します。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/deactivate-workspace-members.md
---

import { Aside } from '@astrojs/starlight/components';

## 説明

ソーステーブルに記載されたワークスペースのメンバーを無効化します。人事データの抽出やアクセスレビューなど、信頼できる一覧に基づいて退職・異動時の手続きを自動化する場合に使用します。手作業で一人ずつ無効化する必要はありません。

[Get Workspace Members](/ja/reference/workflow-steps/general/get-workspace-members/) ステップと組み合わせると、アクセス権を失うべきメンバーの一覧を作成できます。

<Aside type="caution" title="アクセス権が取り消されます">
  ステップが実行されると、一致したすべてのメンバーがアクセス権を失います。このステップをスケジュールする前に、ソーステーブルに対象とするメンバーだけが含まれていることを確認してください。
</Aside>

## 一覧に含まれるワークスペース管理者

[ワークスペース管理者を無効化できるのは、ワークスペース管理者だけです](/ja/administration/access/member-management/#ワークスペース管理者の変更)。ワークスペース管理者の権限なしでステップが実行され、一覧に管理者が含まれている場合、ステップはそれらの管理者を有効なまま残して他のメンバーをすべて無効化し、その後エラーで終了します。エラーメッセージには、無効化したメンバーの数と、有効なまま残した各管理者の名前が示されます。無効化されたメンバーは無効化されたままです。管理者を無効化するには、ワークスペース管理者が Identity で操作してください。

## 設定

### メンバー検索パラメーター

ソーステーブルの行をメンバーと照合する方法です。次のいずれかを選択します。

- **メール**（デフォルト）
- **ユーザー名**

## 関連項目

- [一般ステップ](/ja/reference/workflow-steps/general/)
- [Get Workspace Members ステップ](/ja/reference/workflow-steps/general/get-workspace-members/)
- [メンバー管理](/ja/administration/access/)
