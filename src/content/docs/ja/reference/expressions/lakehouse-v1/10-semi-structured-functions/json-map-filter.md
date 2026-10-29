---
title: JSON_MAP_FILTER (Lakehouse v1)
description: JSON_MAP_FILTER — 指定した条件に基づいて、JSONオブジェクトのキーと値のペアをフィルターします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-filter.md
---

ラムダ式で定義した条件に基づいて、JSONオブジェクトのキーと値のペアをフィルターします。

## SQL構文

```sql
JSON_MAP_FILTER(<json_object>, (<key>, <value>) -> <condition>)
```

## 戻り値の型

指定した条件を満たすキーと値のペアだけを含むJSONオブジェクトを返します。

## SQLの例

次の例では、JSONオブジェクトから `"status": "active"` のキーと値のペアだけを抽出し、他のフィールドを除外します。

```sql
SELECT JSON_MAP_FILTER('{"status":"active", "user":"admin", "time":"2024-11-01"}'::VARIANT, (k, v) -> k = 'status') AS filtered_metadata;

┌─────────────────────┐
│  filtered_metadata  │
├─────────────────────┤
│ {"status":"active"} │
└─────────────────────┘
```
