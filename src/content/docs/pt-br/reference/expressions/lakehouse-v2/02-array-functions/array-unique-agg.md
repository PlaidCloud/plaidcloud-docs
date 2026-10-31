---
title: ARRAY_UNIQUE_AGG (Lakehouse v2)
description: ARRAY_UNIQUE_AGG — agrega valores em um array de valores distintos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-unique-agg.md
---

Agrega valores em um array de valores distintos.

## Sintaxe do Analyze

```python
func.array_unique_agg(get_column(table, 'tag'))
```

## Exemplos do Analyze

```python
func.array_unique_agg(get_column(table, 'tag'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## Sintaxe SQL

```sql
ARRAY_UNIQUE_AGG(<tag>)
```

## Exemplos SQL

```sql
SELECT ARRAY_UNIQUE_AGG(tag) FROM tags;

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
