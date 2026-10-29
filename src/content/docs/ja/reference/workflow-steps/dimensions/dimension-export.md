---
title: Dimension Export
description: ワークフローステップでPlaidCloudのディメンションデータをエクスポートし、階層構造をファイルとして保存したり、他のシステムに転送したりします。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-export.md
---

## 説明

ディメンションを、表形式のPlaidCloudテーブルにフラット化します。メンバーごとに1行で、親、レベル、値、エイリアス、プロパティの列があります。PlaidCloudの階層形式を直接読み取れない下流のシステムに対して、ディメンションの構造をクエリ、結合、または受け渡ししたい場合に使用します。

よくある使い方: ディメンションをテーブルとしてエクスポートし、通常のエクスポートステップを使って外部システム（BIツール、レポート用データベース、ファイル配信）に書き込みます。

## すべての階層のエクスポート

**すべての階層**を選択すると、すべての階層が1つのテーブルにまとめられます。結果には各行がどの階層に属するかを示す`hierarchy`列が追加され、行はメイン階層が先頭に、続いて代替階層がアルファベット順に並びます。
