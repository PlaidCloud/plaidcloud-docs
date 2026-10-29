---
title: EQUIWIDTH_BUCKET (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 EQUIWIDTH_BUCKET 实用函数。返回某个值在等宽直方图中的分桶编号，将 [min, max] 范围划分为等宽区间。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/equiwidth-bucket.md
---

返回某个值在等宽直方图中的分桶编号。将 [min, max] 范围划分为等宽区间。

## Analyze 语法

```python
func.equiwidth_bucket(<expr>, <min>, <max>, <num_buckets>)
```

## Analyze 示例

```python
func.equiwidth_bucket(75, 0, 100, 10)

┌───┐
│ 8 │
└───┘
```

## SQL 语法

```sql
EQUIWIDTH_BUCKET(<expr>, <min>, <max>, <num_buckets>)
```

## SQL 示例

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
