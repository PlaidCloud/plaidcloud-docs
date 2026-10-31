---
title: Table In-Place Deleteステップ
description: PlaidCloudのワークフローステップで、フィルター条件を使用してテーブルから特定の行を削除し、対象のレコードをその場で取り除きます。
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-in-place-delete.md
---

## 説明


指定したフィルター条件を使用して、テーブルに対して削除を実行します。操作は指定したテーブルに対して直接実行されるため、追加のテーブルは作成されません。フィルター条件を満たす行だけが削除されます。データサイズに関する懸念がある場合に、効果的な方法となります。



## 削除パラメーター


ドロップダウンリストから、削除対象となる **ソース** テーブルを選択します。このリストには、すべての*プロジェクト*および*ワークフロー*のデータテーブルが含まれます。

![Table In-Place Delete](/images/table_inplace_table_selection.png)

## 削除のデータフィルター

![Table In-Place Delete](/images/table_in-place_table_filter.png)




## 例
