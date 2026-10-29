---
title: Dimension Clear
description: ディメンションの構造と設定を維持したまま、ワークフローステップでPlaidCloudディメンションのすべてのメンバーをクリアします。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-clear.md
---

## 説明
構造、値、エイリアス、プロパティ、代替階層を含め、ディメンションの内容をクリアします。


![Dimension Clearステップ](/images/dimension_clear.png)



## ディメンションの選択
### ディメンションを動的に指定
**ディメンション**または**パス**が動的に作成されている場合は、同じ変数を使ってクリアすることもできます。クリア処理で変数を使うと、Dimension Clearステップを定期的に手動で更新する必要がなくなるため便利です。



`current_month`変数を使ってMaterialsディメンションを動的にクリアする例です。

```text
/Dimensions/{current_month}/Products/Materials
```

### 特定のディメンションを使用

ドロップダウンメニューから、クリアする特定のディメンションを選択します。
