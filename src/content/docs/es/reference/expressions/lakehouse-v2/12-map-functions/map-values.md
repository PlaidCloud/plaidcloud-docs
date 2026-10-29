---
title: MAP_VALUES (Lakehouse v2)
description: MAP_VALUES — devuelve todos los valores de un mapa como una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-values.md
---

Devuelve todos los valores de un mapa como una matriz.

## Sintaxis de Analyze

```python
func.map_values(get_column(table, 'map_col'))
```

## Ejemplos de Analyze

```python
func.map_values(MAP{'a':1,'b':2})

┌───────┐
│ [1,2] │
└───────┘
```

## Sintaxis de SQL

```sql
MAP_VALUES(<map_col>)
```

## Ejemplos de SQL

```sql
SELECT MAP_VALUES(MAP{'a':1, 'b':2});

┌───────┐
│ [1,2] │
└───────┘
```
