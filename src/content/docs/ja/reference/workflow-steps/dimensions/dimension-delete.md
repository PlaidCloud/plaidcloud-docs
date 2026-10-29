---
title: Dimension Delete
description: 不要になった階層データ構造を削除するために、ワークフローステップでPlaidCloudからディメンションを削除します。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-delete.md
---

## 説明
関連するすべての構造、値、プロパティ、エイリアス、代替階層とともに、ディメンションを削除します。


![Dimension Clearステップ](/images/dimension_clear.png)



## ディメンションの選択
### ディメンションを動的に指定
**ディメンション**または**パス**が動的に作成されている場合は、同じ変数を使って削除することもできます。削除処理で変数を使うと、Dimension Deleteステップを定期的に手動で更新する必要がなくなるため便利です。



`current_month`変数を使ってMaterialsディメンションを動的に削除する例です。

```text
/Dimensions/{current_month}/Products/Materials
```

### 特定のディメンションを使用

ドロップダウンメニューから、削除する特定のディメンションを選択します。
