---
title: JSON_MAP_FILTER (Lakehouse v1)
description: JSON_MAP_FILTER — filtra los pares clave-valor de un objeto JSON según una condición especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-filter.md
---

Filtra los pares clave-valor de un objeto JSON según una condición especificada, definida mediante una expresión lambda.

## Sintaxis SQL

```sql
JSON_MAP_FILTER(<json_object>, (<key>, <value>) -> <condition>)
```

## Tipo de retorno

Devuelve un objeto JSON con solo los pares clave-valor que cumplen la condición especificada.

## Ejemplos de SQL

Este ejemplo extrae solo el par clave-valor `"status": "active"` del objeto JSON y filtra los demás campos:

```sql
SELECT JSON_MAP_FILTER('{"status":"active", "user":"admin", "time":"2024-11-01"}'::VARIANT, (k, v) -> k = 'status') AS filtered_metadata;

┌─────────────────────┐
│  filtered_metadata  │
├─────────────────────┤
│ {"status":"active"} │
└─────────────────────┘
```
