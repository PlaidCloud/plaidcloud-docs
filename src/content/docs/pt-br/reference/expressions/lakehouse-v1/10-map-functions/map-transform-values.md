---
title: MAP_TRANSFORM_VALUES (Lakehouse v1)
description: MAP_TRANSFORM_VALUES — aplica uma transformação a cada valor de um mapa usando uma expressão lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-values.md
---

Aplica uma transformação a cada valor de um mapa usando uma expressão lambda.

## Sintaxe SQL

```sql
MAP_TRANSFORM_VALUES(<map>, (<key>, <value>) -> <value_transformation>)
```

## Tipo de retorno

Retorna um mapa com as mesmas chaves do mapa de entrada, mas com os valores modificados de acordo com a transformação lambda especificada.

## Exemplos de SQL

Este exemplo reduz em 10% o preço de cada produto, enquanto os IDs dos produtos (chaves) permanecem inalterados:

```sql
SELECT MAP_TRANSFORM_VALUES({101: 100.0, 102: 150.0, 103: 200.0}, (product_id, price) -> price * 0.9) AS discounted_prices;

┌───────────────────────────────────┐
│         discounted_prices         │
├───────────────────────────────────┤
│ {101:90.00,102:135.00,103:180.00} │
└───────────────────────────────────┘
```
