---
title: DISTINCT_MAP_KEYS (Lakehouse v2)
description: DISTINCT_MAP_KEYS — devuelve las claves distintas de un mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/distinct-map-keys.md
---

Devuelve las claves distintas de un mapa.

## Sintaxis de Analyze

```python
func.distinct_map_keys(get_column(table, 'map_col'))
```

## Ejemplos de Analyze

```python
func.distinct_map_keys(get_column(table, 'tags'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## Sintaxis de SQL

```sql
DISTINCT_MAP_KEYS(<map_col>)
```

## Ejemplos de SQL

```sql
SELECT DISTINCT_MAP_KEYS(MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
