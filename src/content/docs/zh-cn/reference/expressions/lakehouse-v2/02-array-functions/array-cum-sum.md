---
title: ARRAY_CUM_SUM (Lakehouse v2)
description: ARRAY_CUM_SUM：返回数组中元素的累计和。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-cum-sum.md
---

返回数组中元素的累计和。

## Analyze 语法

```python
func.array_cum_sum([1, 2, 3, 4])
```

## Analyze 示例

```python
func.array_cum_sum([1, 2, 3, 4])

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```

## SQL 语法

```sql
ARRAY_CUM_SUM([1, 2, 3, 4])
```

## SQL 示例

```sql
SELECT ARRAY_CUM_SUM([1, 2, 3, 4]);

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```
