---
title: MAP_SIZE (Lakehouse v2)
description: MAP_SIZE — devuelve el número de pares clave-valor de un mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-size.md
---

Devuelve el número de pares clave-valor de un mapa.

## Sintaxis de Analyze

```python
func.map_size(get_column(table, 'map_col'))
```

## Ejemplos de Analyze

```python
func.map_size(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## Sintaxis de SQL

```sql
MAP_SIZE(<map_col>)
```

## Ejemplos de SQL

```sql
SELECT MAP_SIZE(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
