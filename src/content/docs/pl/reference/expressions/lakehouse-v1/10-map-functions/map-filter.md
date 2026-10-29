---
title: MAP_FILTER (Lakehouse v1)
description: MAP_FILTER — filtruje pary klucz-wartość z mapy za pomocą wyrażenia lambda definiującego warunek.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-filter.md
---

Filtruje pary klucz-wartość z mapy za pomocą wyrażenia lambda definiującego warunek.

## Składnia SQL

```sql
MAP_FILTER(<map>, (<key>, <value>) -> <condition>)
```

## Typ zwracany

Zwraca mapę zawierającą wyłącznie pary klucz-wartość spełniające warunek określony przez wyrażenie lambda.

## Przykłady SQL

Ten przykład zwraca mapę zawierającą wyłącznie produkty ze stanem magazynowym poniżej 10:

```sql
SELECT MAP_FILTER({101:15, 102:8, 103:12, 104:5}, (product_id, stock) -> (stock < 10)) AS low_stock_products;

┌────────────────────┐
│ low_stock_products │
├────────────────────┤
│ {102:8,104:5}      │
└────────────────────┘
```
