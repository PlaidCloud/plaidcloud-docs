---
title: ルールベースのタグ付け
description: 定義した条件に基づいてデータレコードを自動的に分類してラベル付けするために、PlaidCloudの配賦でルールベースのタグ付けを設定します。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/rule-based-tagging.md
---

ルールベースのタグ付けを使うと、配賦エンジンが行の配賦先を決めるために使うメタデータをソース行に付与できます。行ごとに配賦の動作を変えたい場合に使用します。たとえば、あるコストセンターのコストは人員数で配賦し、別のコストセンターのコストは収益で配賦する場合などです。

## 使用する場面

- 単純な配賦ルールでは、コストを実際にどう配賦すべきかを表現しきれない場合（コストの種類ごとにルールが異なるなど）。
- 特定のソース行を特定のターゲットに振り向け、それ以外の行は通常どおり配賦したい場合。
- 各プールが異なるドライバーを使う、複数プールの配賦をモデル化する場合。

## タグ付けの仕組み

1. **ソースにタグを付けます。** 値のテーブルに、各行を分類するタグ列を1つ以上追加します。
2. **配賦ルールでタグを参照します。** 配賦ステップを設定するときに、「ソースのタグXが値Yの場合、ドライバーDとターゲットディメンションTを使って配賦する」という形式でルールを記述します。
3. **エンジンが行を振り分けます。** 各ソース行は順番にルールと照合され、最初に一致したルールが配賦の動作を決定します。

## タグ付けに適したソースのパターン

- `payroll`、`facilities`、`it`、`marketing` などの値を持つ `cost_category` という列
- 行が属する配賦プールを示す `pool` という列
- 異なる処理を適用するための `is_overhead` のようなブール列

## 例

`cost_center` と `cost_category` を持つコストテーブルです。

| cost_center | cost_category | amount |
|---|---|---|
| 1010 | payroll | 50,000 |
| 1010 | it | 8,000 |
| 1020 | payroll | 35,000 |

次の2つの配賦ルールを設定できます。

- **payroll の行**は人員数ドライバーで配賦
- **it の行**はユーザー数ドライバーで配賦

どちらのルールも同じソーステーブルに対して実行され、各行にどちらを適用するかはタグによって決まります。

## 関連情報

- [配賦のクイックスタート](/ja/guides/allocations/getting-started/allocations-quick-start/) — タグ付けを追加する前の基本的な流れ
- [配賦を設定する](/ja/guides/allocations/setup/configure-an-allocation/) — ステップの詳細リファレンス
- [配賦ルールステップ](/ja/reference/workflow-steps/allocation/allocation-rules/) — タグ付けされたデータを使用するワークフローステップ
