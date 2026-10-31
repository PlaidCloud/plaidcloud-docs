---
title: DISTINCT_MAP_KEYS (Lakehouse v2)
description: DISTINCT_MAP_KEYS — zwraca unikatowe klucze z mapy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/distinct-map-keys.md
---

Zwraca unikatowe klucze z mapy.

## Składnia Analyze

```python
func.distinct_map_keys(get_column(table, 'map_col'))
```

## Przykłady Analyze

```python
func.distinct_map_keys(get_column(table, 'tags'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## Składnia SQL

```sql
DISTINCT_MAP_KEYS(<map_col>)
```

## Przykłady SQL

```sql
SELECT DISTINCT_MAP_KEYS(MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
