---
title: 大規模なバージョン履歴テーブルから最新のレコードを選択する
description: 最適化されたクエリ手法を使って、PlaidCloud の大規模な履歴テーブルから最新のレコードを効率よく選択する方法を説明します。
sidebar:
  label: 大規模なバージョン履歴テーブルから最新のレコードを選択する
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/selecting-latest-record-in-large-history-table.md
---

## 課題

各レコードの複数のバージョンを含むテーブルがあり、最新のバージョンを使用する必要があります。

## 考察

この問題は、ID と最大の更新日を一時テーブルに選択し、その一時テーブルを履歴テーブルに INNER JOIN で結合し直して結果を得る方法で解決できます。ただし、この方法には 2 つのステップが必要で、最新の更新を見つける以外に用途のない中間テーブルを保存しなければなりません。

1 つのクエリでこの処理を行う、よりエレガントな解決方法は、ソート付きのウィンドウ関数とフィルターを組み合わせる方法です。

## 解決方法

### バージョン履歴テーブル

| employee_id | department | salary    | update_date  |
|-------------|------------|-----------|--------------|
| 3           | IT         | 90000     | 2024-09-17   |
| 2           | HR         | 85000     | 2024-09-17   |
| 5           | HR         | 82000     | 2024-09-17   |
| 3           | IT         | 77000     | 2023-10-01   |
| 3           | IT         | 75000     | 2022-10-04   |
| 5           | IT         | 72000     | 2024-07-12   |
| 2           | IT         | 67000     | 2024-03-18   |
| 1           | Sales      | 62000     | 2022-02-28   |
| 5           | Sales      | 60000     | 2023-01-14   |
| 4           | Sales      | 58000     | 2021-11-19   |

### ステップの設定
抽出ステップで、`Rank` という列に次のようなウィンドウ関数の式を作成します。

```python
func.rank().over(order_by=table.updated_date.desc(), partition_by=table.employee_id)
```

抽出ステップのフィルタータブで、次のようなフィルターを設定します。

```python
table.Rank == 1
```

### 結果

| employee_id | department | salary    | update_date  | Rank |
|-------------|------------|-----------|--------------|------|
| 3           | IT         | 90000     | 2024-09-17   | 1    |
| 2           | HR         | 85000     | 2024-09-17   | 1    |
| 5           | HR         | 82000     | 2024-09-17   | 1    |
| 1           | Sales      | 62000     | 2022-02-28   | 1    |
| 4           | Sales      | 58000     | 2021-11-19   | 1    |

この方法は非常に効率がよく、複数バージョンの履歴テーブルから最新のレコードを 1 つのステップで選択できます。`employee_id` のグループ内で各レコードを `update_date` によって順位付けし、最初のレコードだけを選ぶことで実現しています。

一意な行キーが複数の列で構成されている場合は、次のように、それらを `partition_by` 引数にリストとして追加できます。

```python
partition_by=[table.first_column, table.second_column, table.third_column]
```

複数列でのソートが必要な場合も、次のように列のリストで指定できます。

```python
order_by=[table.first_column.desc(), table.second_column, table.third_column.desc()]
```
