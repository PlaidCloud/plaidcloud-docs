---
title: ARRAY_UNIQUE_AGG (Lakehouse v2)
description: ARRAY_UNIQUE_AGG – aggregiert Werte zu einem Array aus eindeutigen Werten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-unique-agg.md
---

Aggregiert Werte zu einem Array aus eindeutigen Werten.

## Analyze-Syntax

```python
func.array_unique_agg(get_column(table, 'tag'))
```

## Analyze-Beispiele

```python
func.array_unique_agg(get_column(table, 'tag'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQL-Syntax

```sql
ARRAY_UNIQUE_AGG(<tag>)
```

## SQL-Beispiele

```sql
SELECT ARRAY_UNIQUE_AGG(tag) FROM tags;

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
