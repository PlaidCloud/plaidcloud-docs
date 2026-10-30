---
title: MAP_TRANSFORM_VALUES (Lakehouse v1)
description: MAP_TRANSFORM_VALUES — stosuje przekształcenie do każdej wartości w mapie za pomocą wyrażenia lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-values.md
---

Stosuje przekształcenie do każdej wartości w mapie za pomocą wyrażenia lambda.

## Składnia SQL

```sql
MAP_TRANSFORM_VALUES(<map>, (<key>, <value>) -> <value_transformation>)
```

## Typ zwracany

Zwraca mapę z takimi samymi kluczami jak mapa wejściowa, ale z wartościami zmodyfikowanymi zgodnie z podanym przekształceniem lambda.

## Przykłady SQL

Ten przykład obniża cenę każdego produktu o 10%, a identyfikatory produktów (klucze) pozostają bez zmian:

```sql
SELECT MAP_TRANSFORM_VALUES({101: 100.0, 102: 150.0, 103: 200.0}, (product_id, price) -> price * 0.9) AS discounted_prices;

┌───────────────────────────────────┐
│         discounted_prices         │
├───────────────────────────────────┤
│ {101:90.00,102:135.00,103:180.00} │
└───────────────────────────────────┘
```
