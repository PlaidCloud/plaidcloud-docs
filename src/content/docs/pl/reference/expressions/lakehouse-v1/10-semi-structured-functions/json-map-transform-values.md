---
title: JSON_MAP_TRANSFORM_VALUES (Lakehouse v1)
description: JSON_MAP_TRANSFORM_VALUES — stosuje przekształcenie do każdej wartości w obiekcie JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-values.md
---

Stosuje przekształcenie do każdej wartości w obiekcie JSON za pomocą wyrażenia lambda.

## Składnia SQL

```sql
JSON_MAP_TRANSFORM_VALUES(<json_object>, (<key>, <value>) -> <value_transformation>)
```

## Typ zwracany

Zwraca obiekt JSON z tymi samymi kluczami co wejściowy obiekt JSON, ale z wartościami zmodyfikowanymi zgodnie z podanym przekształceniem lambda.

## Przykłady SQL

Ten przykład dopisuje „ - Special Offer” do opisu każdego produktu:

```sql
SELECT JSON_MAP_TRANSFORM_VALUES('{"product1":"laptop", "product2":"phone"}'::VARIANT, (k, v) -> CONCAT(v, ' - Special Offer')) AS promo_descriptions;

┌──────────────────────────────────────────────────────────────────────────┐
│                            promo_descriptions                            │
├──────────────────────────────────────────────────────────────────────────┤
│ {"product1":"laptop - Special Offer","product2":"phone - Special Offer"} │
└──────────────────────────────────────────────────────────────────────────┘
```
