---
title: ARRAY_DISTINCT (Lakehouse v2)
description: ARRAY_DISTINCT：移除数组中的重复元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-distinct.md
---

移除数组中的重复元素。

## Analyze 语法

```python
func.array_distinct([1, 2, 2, 3, 3])
```

## Analyze 示例

```python
func.array_distinct([1, 2, 2, 3, 3])

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## SQL 语法

```sql
ARRAY_DISTINCT([1, 2, 2, 3, 3])
```

## SQL 示例

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 3, 3]);

┌─────────┐
│ [1,2,3] │
└─────────┘
```
