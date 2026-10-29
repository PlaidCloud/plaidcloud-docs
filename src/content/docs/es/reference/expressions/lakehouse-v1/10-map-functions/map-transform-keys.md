---
title: MAP_TRANSFORM_KEYS (Lakehouse v1)
description: MAP_TRANSFORM_KEYS — aplica una transformación a cada clave de un mapa mediante una expresión lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-keys.md
---

Aplica una transformación a cada clave de un mapa mediante una expresión lambda.

## Sintaxis de SQL

```sql
MAP_TRANSFORM_KEYS(<map>, (<key>, <value>) -> <key_transformation>)
```

## Tipo de valor devuelto

Devuelve un mapa con los mismos valores que el mapa de entrada, pero con las claves modificadas según la transformación lambda especificada.

## Ejemplos de SQL

Este ejemplo suma 1000 a cada identificador de producto y crea un mapa nuevo con las claves actualizadas, manteniendo los mismos precios asociados:

```sql
SELECT MAP_TRANSFORM_KEYS({101: 29.99, 102: 45.50, 103: 15.00}, (product_id, price) -> product_id + 1000) AS updated_product_ids;

┌────────────────────────────────────┐
│         updated_product_ids        │
├────────────────────────────────────┤
│ {1101:29.99,1102:45.50,1103:15.00} │
└────────────────────────────────────┘
```
