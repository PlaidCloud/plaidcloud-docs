---
title: "CARDINALITY (Mapa, Lakehouse v2)"
description: CARDINALITY — devuelve el número de pares clave-valor de un mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/cardinality.md
---

Devuelve el número de pares clave-valor de un mapa.

## Sintaxis de Analyze

```python
func.cardinality(get_column(table, 'map_col'))
```

## Ejemplos de Analyze

```python
func.cardinality(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## Sintaxis de SQL

```sql
CARDINALITY(<map_col>)
```

## Ejemplos de SQL

```sql
SELECT CARDINALITY(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
