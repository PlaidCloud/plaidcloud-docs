---
title: DISTINCT_MAP_KEYS (Lakehouse v2)
description: DISTINCT_MAP_KEYS — devolve as chaves distintas de um mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/distinct-map-keys.md
---

Devolve as chaves distintas de um mapa.

## Sintaxe de Analyze

```python
func.distinct_map_keys(get_column(table, 'map_col'))
```

## Exemplos de Analyze

```python
func.distinct_map_keys(get_column(table, 'tags'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## Sintaxe SQL

```sql
DISTINCT_MAP_KEYS(<map_col>)
```

## Exemplos SQL

```sql
SELECT DISTINCT_MAP_KEYS(MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
