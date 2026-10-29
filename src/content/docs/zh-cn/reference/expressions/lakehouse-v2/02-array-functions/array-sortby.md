---
title: ARRAY_SORTBY (Lakehouse v2)
description: ARRAY_SORTBY：按另一个数组中对应的元素对一个数组的元素排序。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sortby.md
---

按另一个数组中对应的元素对一个数组的元素排序。

## Analyze 语法

```python
func.array_sortby(get_column(table, 'names'), get_column(table, 'scores'))
```

## Analyze 示例

```python
func.array_sortby(['c','a','b'], [3,1,2])

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQL 语法

```sql
ARRAY_SORTBY(<names>, <scores>)
```

## SQL 示例

```sql
SELECT ARRAY_SORTBY(['c','a','b'], [3,1,2]);

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
