---
title: JSON_MAP_TRANSFORM_VALUES (Lakehouse v1)
description: JSON_MAP_TRANSFORM_VALUES — aplica uma transformação a cada valor de um JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-values.md
---

Aplica uma transformação a cada valor de um objeto JSON através de uma expressão lambda.

## Sintaxe SQL

```sql
JSON_MAP_TRANSFORM_VALUES(<json_object>, (<key>, <value>) -> <value_transformation>)
```

## Tipo de retorno

Devolve um objeto JSON com as mesmas chaves do objeto JSON de entrada, mas com os valores modificados de acordo com a transformação lambda especificada.

## Exemplos de SQL

Este exemplo acrescenta " - Special Offer" à descrição de cada produto:

```sql
SELECT JSON_MAP_TRANSFORM_VALUES('{"product1":"laptop", "product2":"phone"}'::VARIANT, (k, v) -> CONCAT(v, ' - Special Offer')) AS promo_descriptions;

┌──────────────────────────────────────────────────────────────────────────┐
│                            promo_descriptions                            │
├──────────────────────────────────────────────────────────────────────────┤
│ {"product1":"laptop - Special Offer","product2":"phone - Special Offer"} │
└──────────────────────────────────────────────────────────────────────────┘
```
