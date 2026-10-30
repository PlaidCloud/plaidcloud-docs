---
title: Set Workflow Variable Values from Table ステップ
description: プロジェクトテーブルから値を読み取ってワークフロー変数に割り当て、後続のステップがハードコードされた値ではなくデータに基づいて分岐やフィルターを行えるようにします。
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-workflow-variable-from-table.md
---

## 説明

プロジェクトテーブルから値を読み取り、ワークフロー変数に割り当てます。ワークフロー自身のデータでワークフローを動かすために使用します。たとえば、制御テーブルから最新の締め済み期間、行数、ファイルパスを読み取り、下流のステップから参照できるようにします。

ここで設定した変数は、そのワークフローの実行中だけ有効です。プロジェクト内のワークフロー間で保持される値を設定するには、[Set Project Variable Values from Table ステップ](/ja/reference/workflow-steps/workflow-control/set-project-variable-from-table/)を使用します。

## 構成

### ソース列

各ソース列を、値を設定するワークフロー変数にマッピングします。ステップは1行だけを読み取るため、実行前にテーブルを1行に絞り込んでください。

### データのサブセットを選択

ソース行を絞り込むフィルター式です。通常は、必要な値を保持する1行に絞り込みます。

### 結果データに二次フィルターを適用

集計後に適用される `HAVING` 形式のフィルターです。値がグループ化された計算から得られる場合に使用します。

### Final Data Table Slicing (Limit)

デフォルトではオフで、オンにすると1行に制限されます。ソースから複数の候補行が返される可能性があり、特定の1行が必要な場合は、明示的な並べ替えを指定したうえでオンにしてください。

## 関連項目

- [ワークフロー制御ステップ](/ja/reference/workflow-steps/workflow-control/)
- [Set Workflow Variable ステップ](/ja/reference/workflow-steps/workflow-control/set-workflow-variable/)
- [Set Project Variable Values from Table ステップ](/ja/reference/workflow-steps/workflow-control/set-project-variable-from-table/)
- [ワークフロー変数の管理](/ja/guides/workflows/manage-workflow-variables/)
