---
title: MAP_TRANSFORM_KEYS (Lakehouse v1)
description: MAP_TRANSFORM_KEYS — aplica uma transformação a cada chave de um mapa usando uma expressão lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-keys.md
---

Aplica uma transformação a cada chave de um mapa usando uma expressão lambda.

## Sintaxe SQL

```sql
MAP_TRANSFORM_KEYS(<map>, (<key>, <value>) -> <key_transformation>)
```

## Tipo de retorno

Retorna um mapa com os mesmos valores do mapa de entrada, mas com as chaves modificadas de acordo com a transformação lambda especificada.

## Exemplos de SQL

Este exemplo soma 1.000 a cada ID de produto, criando um novo mapa com as chaves atualizadas e mantendo os mesmos preços associados:

```sql
SELECT MAP_TRANSFORM_KEYS({101: 29.99, 102: 45.50, 103: 15.00}, (product_id, price) -> product_id + 1000) AS updated_product_ids;

┌────────────────────────────────────┐
│         updated_product_ids        │
├────────────────────────────────────┤
│ {1101:29.99,1102:45.50,1103:15.00} │
└────────────────────────────────────┘
```
