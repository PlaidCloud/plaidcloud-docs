---
title: ARRAY_SORTBY (Lakehouse v2)
description: ARRAY_SORTBY — sortuje elementy jednej tablicy według odpowiadających im elementów innej tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sortby.md
---

Sortuje elementy jednej tablicy według odpowiadających im elementów innej tablicy.

## Składnia Analyze

```python
func.array_sortby(get_column(table, 'names'), get_column(table, 'scores'))
```

## Przykłady Analyze

```python
func.array_sortby(['c','a','b'], [3,1,2])

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## Składnia SQL

```sql
ARRAY_SORTBY(<names>, <scores>)
```

## Przykłady SQL

```sql
SELECT ARRAY_SORTBY(['c','a','b'], [3,1,2]);

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
