---
title: 配賦のトラブルシューティング
description: よくあるエラー、設定上の問題、結果をデバッグする手法など、PlaidCloudの配賦に関する問題をトラブルシューティングします。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/troubleshooting-allocations.md
---

## 配賦ステップを保存できない理由

PlaidCloudは、配賦ステップを保存するときに列マッピングをチェックします。実行できないマッピングはその時点で拒否され、修正が必要な内容を一覧にした**保存できません**という通知が表示されて、フォームは問題のあるタブに切り替わります。以前は、このようなステップはエラーなしで保存され、実行の途中（多くの場合、数分後）でワークフローが停止し、メッセージにはフィールドではなく件数が示されていました。

**配賦する値のテーブル**と**ドライバーデータテーブル**の両方を選択するまで、チェックは行われません。列マッピングはこの2つのテーブルから構築されるため、両方が設定されるまでは、ステップはテーブル自体のみを求めます。

### 配賦ソースマップ

**"No columns specified for allocation."**
少なくとも1つの列の**ロール**を**配賦する値**に設定してください。この列には、ターゲットに配分される値が格納されます。

**"Only numeric columns can be allocated, but ... is not numeric."**
**配賦する値**とマークされた列の**タイプ**が数値以外です。タイプを数値型に変更してください。Numeric、Currency、Integer、大整数、小整数、極小整数、Float、Double、Decimal、Serial、大シリアルのいずれかです。

**"Rename the `alloc_status` target column."**
配賦は、結果テーブルに独自の`alloc_status`列を書き込むため、同じ名前のターゲット列があると競合します。ご自身の列の名前を変更してください。

### ドライバーデータマップ

**"No driver split value column found."**
ドライバー列の1つの**ロール**を**分割値**に設定してください。この列には、配賦の除数となる重みまたはパーセンテージが格納されます。

**"The driver value column ... must be numeric."**
**分割値**列の**タイプ**を数値型に変更してください。

**"No driver relation columns specified."**
少なくとも1つのドライバー列の**ロール**を**ソースリレーション（分母）** に設定してください。これにより、ドライバー行がソース行に関連付けられます。

**"No allocation target columns are indicated."**
少なくとも1つのドライバー列の**ロール**を**配賦ターゲット（分子）** に設定してください。これらが配賦のターゲットとなり、結果テーブルに表示されます。

**"Driver relation columns do not exist in the source data."**
**ソースリレーション（分母）** とマークされた列に対応する同名の列が、**配賦ソースマップ**にありません。名前を合わせるか、その列をソースマップに追加してください。

**"Allocation value column ... is also used as a numerator or denominator column."**
同じ列名が、ソースマップでは**配賦する値**として、ドライバーマップでは**ソースリレーション（分母）** または**配賦ターゲット（分子）** として使われています。配賦される値と、その配賦先を表す列が区別されるよう、どちらかの名前を変更してください。

### ディメンションで分割する場合のみ

**"Please select a hierarchy to use for the allocation dimension."**
**データテーブルの設定**タブで**割り当てディメンションの階層**を選択してください。[配賦を構成する](/ja/guides/allocations/setup/configure-an-allocation/)を参照してください。

## 滞留コスト


滞留コストとは....



## コストの過剰配賦


コストの過剰配賦とは、出力されるコストが...



## コストの誤配賦


コストの誤配賦は、...という場合に発生します。
