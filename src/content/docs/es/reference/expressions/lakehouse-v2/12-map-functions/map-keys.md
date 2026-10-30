---
title: MAP_KEYS (Lakehouse v2)
description: MAP_KEYS — devuelve todas las claves de un mapa como una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-keys.md
---

Devuelve todas las claves de un mapa como una matriz.

## Sintaxis de Analyze

```python
func.map_keys(get_column(table, 'map_col'))
```

## Ejemplos de Analyze

```python
func.map_keys(MAP{'a':1,'b':2})

┌───────────┐
│ ['a','b'] │
└───────────┘
```

## Sintaxis de SQL

```sql
MAP_KEYS(<map_col>)
```

## Ejemplos de SQL

```sql
SELECT MAP_KEYS(MAP{'a':1, 'b':2});

┌───────────┐
│ ["a","b"] │
└───────────┘
```
