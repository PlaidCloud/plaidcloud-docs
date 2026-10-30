---
title: ARRAY_UNIQUE_AGG (Lakehouse v2)
description: ARRAY_UNIQUE_AGG — agrega valores en una matriz de valores distintos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-unique-agg.md
---

Agrega valores en una matriz de valores distintos.

## Sintaxis de Analyze

```python
func.array_unique_agg(get_column(table, 'tag'))
```

## Ejemplos de Analyze

```python
func.array_unique_agg(get_column(table, 'tag'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_UNIQUE_AGG(<tag>)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_UNIQUE_AGG(tag) FROM tags;

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
