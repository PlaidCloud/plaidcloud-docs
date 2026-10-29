---
title: MAP_FILTER（Lakehouse v1）
description: MAP_FILTER — 使用 lambda 表达式定义条件，从 MAP 中筛选键值对。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-filter.md
---

使用 lambda 表达式定义条件，从 MAP 中筛选键值对。

## SQL 语法

```sql
MAP_FILTER(<map>, (<key>, <value>) -> <condition>)
```

## 返回类型

返回仅包含满足 lambda 表达式所指定条件的键值对的 MAP。

## SQL 示例

此示例返回仅包含库存数量低于 10 的产品的 MAP：

```sql
SELECT MAP_FILTER({101:15, 102:8, 103:12, 104:5}, (product_id, stock) -> (stock < 10)) AS low_stock_products;

┌────────────────────┐
│ low_stock_products │
├────────────────────┤
│ {102:8,104:5}      │
└────────────────────┘
```
