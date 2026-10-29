---
title: ARRAY_UNIQUE_AGG (Lakehouse v2)
description: ARRAY_UNIQUE_AGG — agreguje wartości do tablicy różnych wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-unique-agg.md
---

Agreguje wartości do tablicy różnych wartości.

## Składnia Analyze

```python
func.array_unique_agg(get_column(table, 'tag'))
```

## Przykłady Analyze

```python
func.array_unique_agg(get_column(table, 'tag'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## Składnia SQL

```sql
ARRAY_UNIQUE_AGG(<tag>)
```

## Przykłady SQL

```sql
SELECT ARRAY_UNIQUE_AGG(tag) FROM tags;

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
