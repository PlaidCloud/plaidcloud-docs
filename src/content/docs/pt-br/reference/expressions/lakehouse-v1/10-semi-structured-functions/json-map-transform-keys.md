---
title: JSON_MAP_TRANSFORM_KEYS (Lakehouse v1)
description: JSON_MAP_TRANSFORM_KEYS — aplica uma transformação a cada chave de um objeto JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-keys.md
---

Aplica uma transformação a cada chave de um objeto JSON usando uma expressão lambda.

## Sintaxe SQL

```sql
JSON_MAP_TRANSFORM_KEYS(<json_object>, (<key>, <value>) -> <key_transformation>)
```

## Tipo de retorno

Retorna um objeto JSON com os mesmos valores do objeto JSON de entrada, mas com as chaves modificadas de acordo com a transformação lambda especificada.

## Exemplos de SQL

Este exemplo acrescenta "_v1" a cada chave, criando um novo objeto JSON com as chaves modificadas:

```sql
SELECT JSON_MAP_TRANSFORM_KEYS('{"name":"John", "role":"admin"}'::VARIANT, (k, v) -> CONCAT(k, '_v1')) AS versioned_metadata;

┌──────────────────────────────────────┐
│          versioned_metadata          │
├──────────────────────────────────────┤
│ {"name_v1":"John","role_v1":"admin"} │
└──────────────────────────────────────┘
```
