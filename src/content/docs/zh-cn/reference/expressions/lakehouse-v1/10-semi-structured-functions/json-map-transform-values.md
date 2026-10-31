---
title: JSON_MAP_TRANSFORM_VALUES（Lakehouse v1）
description: JSON_MAP_TRANSFORM_VALUES — 对 JSON 对象中的每个值应用转换。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-values.md
---

使用 lambda 表达式对 JSON 对象中的每个值应用转换。

## SQL 语法

```sql
JSON_MAP_TRANSFORM_VALUES(<json_object>, (<key>, <value>) -> <value_transformation>)
```

## 返回类型

返回一个 JSON 对象，其键与输入 JSON 对象相同，但值已根据指定的 lambda 转换进行了修改。

## SQL 示例

此示例在每个产品描述后追加 " - Special Offer"：

```sql
SELECT JSON_MAP_TRANSFORM_VALUES('{"product1":"laptop", "product2":"phone"}'::VARIANT, (k, v) -> CONCAT(v, ' - Special Offer')) AS promo_descriptions;

┌──────────────────────────────────────────────────────────────────────────┐
│                            promo_descriptions                            │
├──────────────────────────────────────────────────────────────────────────┤
│ {"product1":"laptop - Special Offer","product2":"phone - Special Offer"} │
└──────────────────────────────────────────────────────────────────────────┘
```
