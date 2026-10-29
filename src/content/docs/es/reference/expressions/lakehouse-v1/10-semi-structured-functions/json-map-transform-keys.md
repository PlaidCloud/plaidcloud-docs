---
title: JSON_MAP_TRANSFORM_KEYS (Lakehouse v1)
description: JSON_MAP_TRANSFORM_KEYS — aplica una transformación a cada clave de un objeto JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-keys.md
---

Aplica una transformación a cada clave de un objeto JSON mediante una expresión lambda.

## Sintaxis SQL

```sql
JSON_MAP_TRANSFORM_KEYS(<json_object>, (<key>, <value>) -> <key_transformation>)
```

## Tipo de retorno

Devuelve un objeto JSON con los mismos valores que el objeto JSON de entrada, pero con las claves modificadas según la transformación lambda especificada.

## Ejemplos de SQL

Este ejemplo agrega "_v1" a cada clave y crea un nuevo objeto JSON con las claves modificadas:

```sql
SELECT JSON_MAP_TRANSFORM_KEYS('{"name":"John", "role":"admin"}'::VARIANT, (k, v) -> CONCAT(k, '_v1')) AS versioned_metadata;

┌──────────────────────────────────────┐
│          versioned_metadata          │
├──────────────────────────────────────┤
│ {"name_v1":"John","role_v1":"admin"} │
└──────────────────────────────────────┘
```
