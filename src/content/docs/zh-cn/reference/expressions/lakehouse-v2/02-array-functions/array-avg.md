---
title: ARRAY_AVG (Lakehouse v2)
description: ARRAY_AVG：返回数组中元素的平均值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-avg.md
---

返回数组中元素的平均值。

## Analyze 语法

```python
func.array_avg([1, 2, 3, 4])
```

## Analyze 示例

```python
func.array_avg([10, 20, 30])

┌──────┐
│ 20.0 │
└──────┘
```

## SQL 语法

```sql
ARRAY_AVG([1, 2, 3, 4])
```

## SQL 示例

```sql
SELECT ARRAY_AVG([10, 20, 30]);

┌──────┐
│ 20.0 │
└──────┘
```
