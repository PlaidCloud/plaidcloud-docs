---
title: MAP_FILTER (Lakehouse v1)
description: MAP_FILTER — filtra pares chave-valor de um mapa usando uma expressão lambda para definir a condição.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-filter.md
---

Filtra pares chave-valor de um mapa usando uma expressão lambda para definir a condição.

## Sintaxe SQL

```sql
MAP_FILTER(<map>, (<key>, <value>) -> <condition>)
```

## Tipo de retorno

Retorna um mapa que inclui apenas os pares chave-valor que atendem à condição especificada pela expressão lambda.

## Exemplos de SQL

Este exemplo retorna um mapa contendo apenas os produtos com quantidades em estoque abaixo de 10:

```sql
SELECT MAP_FILTER({101:15, 102:8, 103:12, 104:5}, (product_id, stock) -> (stock < 10)) AS low_stock_products;

┌────────────────────┐
│ low_stock_products │
├────────────────────┤
│ {102:8,104:5}      │
└────────────────────┘
```
