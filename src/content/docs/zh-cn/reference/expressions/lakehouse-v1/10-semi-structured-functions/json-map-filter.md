---
title: JSON_MAP_FILTER（Lakehouse v1）
description: JSON_MAP_FILTER — 根据指定条件筛选 JSON 对象中的键值对。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-filter.md
---

根据用 lambda 表达式定义的指定条件，筛选 JSON 对象中的键值对。

## SQL 语法

```sql
JSON_MAP_FILTER(<json_object>, (<key>, <value>) -> <condition>)
```

## 返回类型

返回仅包含满足指定条件的键值对的 JSON 对象。

## SQL 示例

此示例仅从 JSON 对象中提取 `"status": "active"` 键值对，过滤掉其他字段：

```sql
SELECT JSON_MAP_FILTER('{"status":"active", "user":"admin", "time":"2024-11-01"}'::VARIANT, (k, v) -> k = 'status') AS filtered_metadata;

┌─────────────────────┐
│  filtered_metadata  │
├─────────────────────┤
│ {"status":"active"} │
└─────────────────────┘
```
