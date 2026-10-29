---
title: MAP_TRANSFORM_VALUES (Lakehouse v1)
description: MAP_TRANSFORM_VALUES — aplica una transformación a cada valor de un mapa mediante una expresión lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-values.md
---

Aplica una transformación a cada valor de un mapa mediante una expresión lambda.

## Sintaxis de SQL

```sql
MAP_TRANSFORM_VALUES(<map>, (<key>, <value>) -> <value_transformation>)
```

## Tipo de valor devuelto

Devuelve un mapa con las mismas claves que el mapa de entrada, pero con los valores modificados según la transformación lambda especificada.

## Ejemplos de SQL

Este ejemplo reduce el precio de cada producto un 10 %, mientras que los identificadores de producto (claves) permanecen sin cambios:

```sql
SELECT MAP_TRANSFORM_VALUES({101: 100.0, 102: 150.0, 103: 200.0}, (product_id, price) -> price * 0.9) AS discounted_prices;

┌───────────────────────────────────┐
│         discounted_prices         │
├───────────────────────────────────┤
│ {101:90.00,102:135.00,103:180.00} │
└───────────────────────────────────┘
```
