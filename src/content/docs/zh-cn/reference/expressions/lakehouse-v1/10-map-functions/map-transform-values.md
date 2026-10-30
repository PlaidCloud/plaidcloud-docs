---
title: MAP_TRANSFORM_VALUES（Lakehouse v1）
description: MAP_TRANSFORM_VALUES — 使用 lambda 表达式对 MAP 中的每个值应用转换。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-values.md
---

使用 lambda 表达式对 MAP 中的每个值应用转换。

## SQL 语法

```sql
MAP_TRANSFORM_VALUES(<map>, (<key>, <value>) -> <value_transformation>)
```

## 返回类型

返回一个 MAP，其键与输入 MAP 相同，但值已按指定的 lambda 转换进行修改。

## SQL 示例

此示例将每个产品的价格降低 10%，而产品 ID（键）保持不变：

```sql
SELECT MAP_TRANSFORM_VALUES({101: 100.0, 102: 150.0, 103: 200.0}, (product_id, price) -> price * 0.9) AS discounted_prices;

┌───────────────────────────────────┐
│         discounted_prices         │
├───────────────────────────────────┤
│ {101:90.00,102:135.00,103:180.00} │
└───────────────────────────────────┘
```
