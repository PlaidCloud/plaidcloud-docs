---
title: ARRAY_UNIQUE_AGG (Lakehouse v2)
description: ARRAY_UNIQUE_AGG：将值聚合为由不同值组成的数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-unique-agg.md
---

将值聚合为由不同值组成的数组。

## Analyze 语法

```python
func.array_unique_agg(get_column(table, 'tag'))
```

## Analyze 示例

```python
func.array_unique_agg(get_column(table, 'tag'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQL 语法

```sql
ARRAY_UNIQUE_AGG(<tag>)
```

## SQL 示例

```sql
SELECT ARRAY_UNIQUE_AGG(tag) FROM tags;

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
