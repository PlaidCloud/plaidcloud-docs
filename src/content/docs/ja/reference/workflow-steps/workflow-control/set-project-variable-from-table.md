---
title: Set Project Variable Values from Table ステップ
description: プロジェクトテーブルから値を読み取り、ワークフローの実行をまたいで保持されるプロジェクト変数に割り当てます。
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable-from-table.md
---

## 説明

プロジェクトテーブルから値を読み取り、*プロジェクト*変数に割り当てます。[Set Workflow Variable Values from Table ステップ](/ja/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/)とは異なり、値は実行後も保持されます。何かが変更するまで、プロジェクト内のすべてのワークフローから参照できます。

1回の実行より長く残る状態に使用します。たとえば、最後に正常にロードされた期間、ウォーターマークのタイムスタンプ、現在のシナリオ名などです。

## 構成

### ソース列

各ソース列を、値を設定するプロジェクト変数にマッピングします。ステップは1行だけを読み取るため、実行前にテーブルを1行に絞り込んでください。

### データのサブセットを選択

ソース行を絞り込むフィルター式です。

### 結果データに二次フィルターを適用

集計後に適用される、`HAVING` 形式のフィルターです。

### Final Data Table Slicing (Limit)

デフォルトではオフで、オンにすると1行に制限されます。ソースから複数の候補行が返される可能性がある場合は、明示的な並べ替えを指定したうえでオンにしてください。

## 関連項目

- [ワークフロー制御ステップ](/ja/reference/workflow-steps/workflow-control/)
- [Set Project Variable ステップ](/ja/reference/workflow-steps/workflow-control/set-project-variable/)
- [Set Workflow Variable Values from Table ステップ](/ja/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/)
