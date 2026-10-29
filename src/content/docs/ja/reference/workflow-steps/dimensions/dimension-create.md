---
title: Dimension Create ステップ
description: PlaidCloud のワークフローステップで新しい階層型ディメンションを作成し、データの分類体系を整理して構造化します。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-create.md
---

## 説明
使用およびロード用のディメンションを作成します。


![Dimension Create](/images/dimension_create.png)

## 作成するディメンション
### 名前
作成するディメンションには、特定の名前を使用することも、動的に名前を付けるために変数を含めることもできます。


ディメンションを定期的に更新し、過去のビューを保持したい場合に、変数が役立ちます。

次の例では、`current_month` 変数を使用してディメンションに動的に名前を付けています。

```text
dimension_name_{current_month}
```
### パス
パスを使用すると、ディメンションを保存するフォルダー構造を作成できます。ここでも変数を使用して、フォルダー構造を動的にできます。
次の例では、`current_month` 変数を使用してフォルダーに動的に名前を付けています。

```text
/Dimensions/{current_month}/Product/
```

### メモ
メモフィールドは、コメントやメモを保存する場所として使用します。
