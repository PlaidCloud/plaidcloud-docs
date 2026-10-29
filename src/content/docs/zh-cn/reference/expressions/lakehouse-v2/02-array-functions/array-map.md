---
title: ARRAY_MAP (Lakehouse v2)
description: ARRAY_MAP：对数组的每个元素应用 lambda 表达式。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-map.md
---

对数组的每个元素应用 lambda 表达式。

## Analyze 语法

```python
func.array_map(get_column(table, 'arr'), lambda x: x * 2)
```

## Analyze 示例

```python
func.array_map([1, 2, 3], lambda x: x * 2)

┌─────────┐
│ [2,4,6] │
└─────────┘
```

## SQL 语法

```sql
ARRAY_MAP(<arr>, lambda x: x * 2)
```

## SQL 示例

```sql
SELECT ARRAY_MAP([1, 2, 3], x -> x * 2);

┌─────────┐
│ [2,4,6] │
└─────────┘
```
