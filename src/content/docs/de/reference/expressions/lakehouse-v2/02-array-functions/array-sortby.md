---
title: ARRAY_SORTBY (Lakehouse v2)
description: ARRAY_SORTBY – sortiert die Elemente eines Arrays nach den entsprechenden Elementen eines anderen Arrays.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sortby.md
---

Sortiert die Elemente eines Arrays nach den entsprechenden Elementen eines anderen Arrays.

## Analyze-Syntax

```python
func.array_sortby(get_column(table, 'names'), get_column(table, 'scores'))
```

## Analyze-Beispiele

```python
func.array_sortby(['c','a','b'], [3,1,2])

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQL-Syntax

```sql
ARRAY_SORTBY(<names>, <scores>)
```

## SQL-Beispiele

```sql
SELECT ARRAY_SORTBY(['c','a','b'], [3,1,2]);

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
