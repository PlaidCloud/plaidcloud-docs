---
title: DISTINCT_MAP_KEYS (Lakehouse v2)
description: DISTINCT_MAP_KEYS — renvoie les clés distinctes d'un map.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/distinct-map-keys.md
---

Renvoie les clés distinctes d'un map.

## Syntaxe Analyze

```python
func.distinct_map_keys(get_column(table, 'map_col'))
```

## Exemples Analyze

```python
func.distinct_map_keys(get_column(table, 'tags'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## Syntaxe SQL

```sql
DISTINCT_MAP_KEYS(<map_col>)
```

## Exemples SQL

```sql
SELECT DISTINCT_MAP_KEYS(MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
