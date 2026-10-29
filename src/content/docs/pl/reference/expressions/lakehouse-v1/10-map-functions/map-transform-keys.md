---
title: MAP_TRANSFORM_KEYS (Lakehouse v1)
description: MAP_TRANSFORM_KEYS — stosuje przekształcenie do każdego klucza w mapie za pomocą wyrażenia lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-keys.md
---

Stosuje przekształcenie do każdego klucza w mapie za pomocą wyrażenia lambda.

## Składnia SQL

```sql
MAP_TRANSFORM_KEYS(<map>, (<key>, <value>) -> <key_transformation>)
```

## Typ zwracany

Zwraca mapę z takimi samymi wartościami jak mapa wejściowa, ale z kluczami zmodyfikowanymi zgodnie z podanym przekształceniem lambda.

## Przykłady SQL

Ten przykład dodaje 1000 do każdego identyfikatora produktu, tworząc nową mapę z zaktualizowanymi kluczami i niezmienionymi powiązanymi cenami:

```sql
SELECT MAP_TRANSFORM_KEYS({101: 29.99, 102: 45.50, 103: 15.00}, (product_id, price) -> product_id + 1000) AS updated_product_ids;

┌────────────────────────────────────┐
│         updated_product_ids        │
├────────────────────────────────────┤
│ {1101:29.99,1102:45.50,1103:15.00} │
└────────────────────────────────────┘
```
