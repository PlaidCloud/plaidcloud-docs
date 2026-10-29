---
title: JSON_MAP_FILTER (Lakehouse v1)
description: JSON_MAP_FILTER — filtra pares chave-valor de um objeto JSON com base numa condição especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-filter.md
---

Filtra pares chave-valor de um objeto JSON com base numa condição especificada, definida através de uma expressão lambda.

## Sintaxe SQL

```sql
JSON_MAP_FILTER(<json_object>, (<key>, <value>) -> <condition>)
```

## Tipo de retorno

Devolve um objeto JSON apenas com os pares chave-valor que satisfazem a condição especificada.

## Exemplos de SQL

Este exemplo extrai apenas o par chave-valor `"status": "active"` do objeto JSON, filtrando os restantes campos:

```sql
SELECT JSON_MAP_FILTER('{"status":"active", "user":"admin", "time":"2024-11-01"}'::VARIANT, (k, v) -> k = 'status') AS filtered_metadata;

┌─────────────────────┐
│  filtered_metadata  │
├─────────────────────┤
│ {"status":"active"} │
└─────────────────────┘
```
