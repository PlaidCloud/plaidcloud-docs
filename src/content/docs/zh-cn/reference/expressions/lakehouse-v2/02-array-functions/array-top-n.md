---
title: ARRAY_TOP_N (Lakehouse v2)
description: ARRAY_TOP_N：返回数组中最大的前 N 个元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-top-n.md
---

返回数组中最大的前 N 个元素。

## Analyze 语法

```python
func.array_top_n([3,1,4,1,5], 3)
```

## Analyze 示例

```python
func.array_top_n([3, 1, 4, 1, 5], 3)

┌─────────┐
│ [5,4,3] │
└─────────┘
```

## SQL 语法

```sql
ARRAY_TOP_N([3,1,4,1,5], 3)
```

## SQL 示例

```sql
SELECT ARRAY_TOP_N([3, 1, 4, 1, 5], 3);

┌─────────┐
│ [5,4,3] │
└─────────┘
```
