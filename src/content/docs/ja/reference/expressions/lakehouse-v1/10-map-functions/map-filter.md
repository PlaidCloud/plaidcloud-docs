---
title: MAP_FILTER（Lakehouse v1）
description: MAP_FILTER — ラムダ式で条件を定義して、マップからキーと値のペアをフィルターします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-filter.md
---

ラムダ式で条件を定義して、マップからキーと値のペアをフィルターします。

## SQL Syntax

```sql
MAP_FILTER(<map>, (<key>, <value>) -> <condition>)
```

## 戻り値の型

ラムダ式で指定した条件を満たすキーと値のペアのみを含むマップを返します。

## SQL Examples

この例では、在庫数量が10未満の商品のみを含むマップを返します。

```sql
SELECT MAP_FILTER({101:15, 102:8, 103:12, 104:5}, (product_id, stock) -> (stock < 10)) AS low_stock_products;

┌────────────────────┐
│ low_stock_products │
├────────────────────┤
│ {102:8,104:5}      │
└────────────────────┘
```
