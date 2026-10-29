---
title: ARRAY_REMOVE (Lakehouse v2)
description: ARRAY_REMOVE：移除数组中所有指定元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-remove.md
---

移除数组中所有指定元素。

## Analyze 语法

```python
func.array_remove([1, 2, 3, 2, 1], 2)
```

## Analyze 示例

```python
func.array_remove([1, 2, 3, 2, 1], 2)

┌─────────┐
│ [1,3,1] │
└─────────┘
```

## SQL 语法

```sql
ARRAY_REMOVE([1, 2, 3, 2, 1], 2)
```

## SQL 示例

```sql
SELECT ARRAY_REMOVE([1, 2, 3, 2, 1], 2);

┌─────────┐
│ [1,3,1] │
└─────────┘
```
