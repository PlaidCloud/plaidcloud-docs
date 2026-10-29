---
title: Dimension Sort
description: ワークフローステップでPlaidCloudのディメンションメンバーを自動的にソートし、階層内の順序を一貫して保ちます。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-sort.md
---

## 説明

ディメンションのメンバーを、親ごとにソートします。アルファベット順、値順、プロパティ順、またはカスタムの順序列で並べ替えられます。階層メンバーを手作業でドラッグして正しい順序に並べる手間が省けるため、一括ロードや大規模な再構成の後に特に便利です。

ディメンションをその場で操作するため、ソーステーブルもターゲットテーブルも必要ありません。


## ディメンションの選択
### ディメンションを動的に指定
**ディメンション**または**パス**が動的に作成されている場合は、同じ変数を使ってソートすることもできます。ソート処理で変数を使うと、Dimension Sortステップを定期的に手動で更新する必要がなくなるため便利です。



`current_month`変数を使ってMaterialsディメンションを動的にソートする例です。

```text
/Dimensions/{current_month}/Products/Materials
```

### 特定のディメンションを使用

ドロップダウンメニューから、ソートする特定のディメンションを選択します。
