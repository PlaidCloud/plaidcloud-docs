---
title: ARRAY_FILTER (Lakehouse v2)
description: ARRAY_FILTER：使用 lambda 表达式筛选数组中的元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-filter.md
---

使用 lambda 表达式筛选数组中的元素。

## Analyze 语法

```python
func.array_filter(get_column(table, 'arr'), lambda x: x > 2)
```

## Analyze 示例

```python
func.array_filter([1, 2, 3, 4, 5], lambda x: x > 2)

┌─────────┐
│ [3,4,5] │
└─────────┘
```

## SQL 语法

```sql
ARRAY_FILTER(<arr>, lambda x: x > 2)
```

## SQL 示例

```sql
SELECT ARRAY_FILTER([1, 2, 3, 4, 5], x -> x > 2);

┌─────────┐
│ [3,4,5] │
└─────────┘
```
