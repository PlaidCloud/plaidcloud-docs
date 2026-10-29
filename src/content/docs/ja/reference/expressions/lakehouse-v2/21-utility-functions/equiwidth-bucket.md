---
title: EQUIWIDTH_BUCKET（Lakehouse v2）
description: "PlaidCloud Lakehouse で EQUIWIDTH_BUCKET ユーティリティ関数を使用します。等幅ヒストグラムにおける値のバケット番号を返します。範囲 [min, max] を等幅の区間に分割します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/equiwidth-bucket.md
---

等幅ヒストグラムにおける値のバケット番号を返します。範囲 [min, max] を等幅の区間に分割します。

## Analyze 構文

```python
func.equiwidth_bucket(<expr>, <min>, <max>, <num_buckets>)
```

## Analyze の例

```python
func.equiwidth_bucket(75, 0, 100, 10)

┌───┐
│ 8 │
└───┘
```

## SQL 構文

```sql
EQUIWIDTH_BUCKET(<expr>, <min>, <max>, <num_buckets>)
```

## SQL の例

```sql
SELECT score, EQUIWIDTH_BUCKET(score, 0, 100, 10) AS bucket
FROM students;

┌───────┬────────┐
│ score │ bucket │
├───────┼────────┤
│    25 │      3 │
│    75 │      8 │
│    95 │     10 │
└───────┴────────┘
```
