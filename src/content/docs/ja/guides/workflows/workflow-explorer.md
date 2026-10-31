---
title: ワークフローエクスプローラー
description: PlaidCloudのワークフローエクスプローラーを使って、ワークフローの詳細、ステップの構成、実行履歴、依存関係の情報を表示します。
sidebar:
  order: 1.1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/workflow-explorer.md
---

ワークフロー内の詳細を表示するには、プロジェクト内でワークフローを見つけ、ダブルクリックしてエクスプローラーで開きます。

![ワークフローエクスプローラー](/images/workflow_explorer.png)

ここでは、ワークフローのステップを管理できます。ステップの作成や既存のステップの変更、順序の変更、ステップの実行などが可能です。

## ステップの作成

**ステップを作成**をクリックして、ステップタイプを選択します。リストで1つのステップが選択されている場合、新しいTable Extract、Table Inner Join、Table Outer Join、Table Anti Join、Table Cross Join、またはTable Lookupの各ステップは、選択したステップが書き込むテーブルから開始されます。そのテーブルが新しいステップのソース（結合の場合は**Table 1**）になり、列は**ソースを検査**が入力するのと同じように入力されます。フォームの下部の注記にその旨が表示されます。新しいステップが別のものを読み取る場合は、ソースを変更してください。ステップを保存するまで、何も保存されません。
