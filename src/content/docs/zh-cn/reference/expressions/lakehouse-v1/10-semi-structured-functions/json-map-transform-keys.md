---
title: JSON_MAP_TRANSFORM_KEYS（Lakehouse v1）
description: JSON_MAP_TRANSFORM_KEYS — 对 JSON 对象中的每个键应用转换。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-keys.md
---

使用 lambda 表达式对 JSON 对象中的每个键应用转换。

## SQL 语法

```sql
JSON_MAP_TRANSFORM_KEYS(<json_object>, (<key>, <value>) -> <key_transformation>)
```

## 返回类型

返回一个 JSON 对象，其值与输入 JSON 对象相同，但键已根据指定的 lambda 转换进行了修改。

## SQL 示例

此示例在每个键后追加 "_v1"，创建带有修改后键的新 JSON 对象：

```sql
SELECT JSON_MAP_TRANSFORM_KEYS('{"name":"John", "role":"admin"}'::VARIANT, (k, v) -> CONCAT(k, '_v1')) AS versioned_metadata;

┌──────────────────────────────────────┐
│          versioned_metadata          │
├──────────────────────────────────────┤
│ {"name_v1":"John","role_v1":"admin"} │
└──────────────────────────────────────┘
```
