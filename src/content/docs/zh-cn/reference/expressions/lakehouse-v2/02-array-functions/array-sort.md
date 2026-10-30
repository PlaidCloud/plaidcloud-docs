---
title: ARRAY_SORT (Lakehouse v2)
description: ARRAY_SORT：将数组元素按升序排序。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sort.md
---

将数组元素按升序排序。

## Analyze 语法

```python
func.array_sort([3, 1, 4, 1, 5])
```

## Analyze 示例

```python
func.array_sort([3, 1, 4, 1, 5])

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```

## SQL 语法

```sql
ARRAY_SORT([3, 1, 4, 1, 5])
```

## SQL 示例

```sql
SELECT ARRAY_SORT([3, 1, 4, 1, 5]);

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```
