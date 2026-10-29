---
title: MAP_FILTER (Lakehouse v1)
description: MAP_FILTER — filtra pares chave-valor de um mapa através de uma expressão lambda que define a condição.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-filter.md
---

Filtra pares chave-valor de um mapa através de uma expressão lambda que define a condição.

## Sintaxe SQL

```sql
MAP_FILTER(<map>, (<key>, <value>) -> <condition>)
```

## Tipo de retorno

Devolve um mapa que inclui apenas os pares chave-valor que cumprem a condição especificada pela expressão lambda.

## Exemplos de SQL

Este exemplo devolve um mapa que contém apenas os produtos com quantidades em stock inferiores a 10:

```sql
SELECT MAP_FILTER({101:15, 102:8, 103:12, 104:5}, (product_id, stock) -> (stock < 10)) AS low_stock_products;

┌────────────────────┐
│ low_stock_products │
├────────────────────┤
│ {102:8,104:5}      │
└────────────────────┘
```
