---
title: ARRAY_UNIQUE_AGG (Lakehouse v2)
description: ARRAY_UNIQUE_AGG — agrège des valeurs dans un tableau de valeurs distinctes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-unique-agg.md
---

Agrège des valeurs dans un tableau de valeurs distinctes.

## Syntaxe Analyze

```python
func.array_unique_agg(get_column(table, 'tag'))
```

## Exemples Analyze

```python
func.array_unique_agg(get_column(table, 'tag'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## Syntaxe SQL

```sql
ARRAY_UNIQUE_AGG(<tag>)
```

## Exemples SQL

```sql
SELECT ARRAY_UNIQUE_AGG(tag) FROM tags;

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
