---
title: ARRAY_SUM (Lakehouse v2)
description: ARRAY_SUM：返回数组中元素之和。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sum.md
---

返回数组中元素之和。

## Analyze 语法

```python
func.array_sum([1, 2, 3, 4, 5])
```

## Analyze 示例

```python
func.array_sum([10, 20, 30])

┌────┐
│ 60 │
└────┘
```

## SQL 语法

```sql
ARRAY_SUM([1, 2, 3, 4, 5])
```

## SQL 示例

```sql
SELECT ARRAY_SUM([10, 20, 30]);

┌────┐
│ 60 │
└────┘
```
