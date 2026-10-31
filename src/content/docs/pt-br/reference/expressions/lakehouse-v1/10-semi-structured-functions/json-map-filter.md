---
title: JSON_MAP_FILTER (Lakehouse v1)
description: JSON_MAP_FILTER — filtra pares chave-valor de um objeto JSON com base em uma condição especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-filter.md
---

Filtra pares chave-valor de um objeto JSON com base em uma condição especificada, definida por meio de uma expressão lambda.

## Sintaxe SQL

```sql
JSON_MAP_FILTER(<json_object>, (<key>, <value>) -> <condition>)
```

## Tipo de retorno

Retorna um objeto JSON somente com os pares chave-valor que satisfazem a condição especificada.

## Exemplos de SQL

Este exemplo extrai apenas o par chave-valor `"status": "active"` do objeto JSON, filtrando os demais campos:

```sql
SELECT JSON_MAP_FILTER('{"status":"active", "user":"admin", "time":"2024-11-01"}'::VARIANT, (k, v) -> k = 'status') AS filtered_metadata;

┌─────────────────────┐
│  filtered_metadata  │
├─────────────────────┤
│ {"status":"active"} │
└─────────────────────┘
```
