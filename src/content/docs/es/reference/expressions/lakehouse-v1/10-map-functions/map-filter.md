---
title: MAP_FILTER (Lakehouse v1)
description: MAP_FILTER — filtra los pares clave-valor de un mapa mediante una expresión lambda que define la condición.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-filter.md
---

Filtra los pares clave-valor de un mapa mediante una expresión lambda que define la condición.

## Sintaxis de SQL

```sql
MAP_FILTER(<map>, (<key>, <value>) -> <condition>)
```

## Tipo de valor devuelto

Devuelve un mapa que incluye solo los pares clave-valor que cumplen la condición especificada por la expresión lambda.

## Ejemplos de SQL

Este ejemplo devuelve un mapa que contiene solo los productos con existencias inferiores a 10:

```sql
SELECT MAP_FILTER({101:15, 102:8, 103:12, 104:5}, (product_id, stock) -> (stock < 10)) AS low_stock_products;

┌────────────────────┐
│ low_stock_products │
├────────────────────┤
│ {102:8,104:5}      │
└────────────────────┘
```
