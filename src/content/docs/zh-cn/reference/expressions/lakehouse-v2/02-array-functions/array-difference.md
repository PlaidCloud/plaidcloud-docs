---
title: ARRAY_DIFFERENCE (Lakehouse v2)
description: ARRAY_DIFFERENCE：返回相邻元素之差组成的数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-difference.md
---

返回相邻元素之差组成的数组。

## Analyze 语法

```python
func.array_difference([1, 3, 6, 10])
```

## Analyze 示例

```python
func.array_difference([1, 3, 6, 10])

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```

## SQL 语法

```sql
ARRAY_DIFFERENCE([1, 3, 6, 10])
```

## SQL 示例

```sql
SELECT ARRAY_DIFFERENCE([1, 3, 6, 10]);

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```
