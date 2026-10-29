---
title: MAP_TRANSFORM_KEYS（Lakehouse v1）
description: MAP_TRANSFORM_KEYS — 使用 lambda 表达式对 MAP 中的每个键应用转换。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-keys.md
---

使用 lambda 表达式对 MAP 中的每个键应用转换。

## SQL 语法

```sql
MAP_TRANSFORM_KEYS(<map>, (<key>, <value>) -> <key_transformation>)
```

## 返回类型

返回一个 MAP，其值与输入 MAP 相同，但键已按指定的 lambda 转换进行修改。

## SQL 示例

此示例将每个产品 ID 加上 1,000，创建一个键已更新、关联价格保持不变的新 MAP：

```sql
SELECT MAP_TRANSFORM_KEYS({101: 29.99, 102: 45.50, 103: 15.00}, (product_id, price) -> product_id + 1000) AS updated_product_ids;

┌────────────────────────────────────┐
│         updated_product_ids        │
├────────────────────────────────────┤
│ {1101:29.99,1102:45.50,1103:15.00} │
└────────────────────────────────────┘
```
