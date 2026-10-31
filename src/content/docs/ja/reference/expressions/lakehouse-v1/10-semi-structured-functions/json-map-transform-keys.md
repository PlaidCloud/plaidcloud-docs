---
title: JSON_MAP_TRANSFORM_KEYS (Lakehouse v1)
description: JSON_MAP_TRANSFORM_KEYS — JSONオブジェクトの各キーに変換を適用します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-keys.md
---

ラムダ式を使って、JSONオブジェクトの各キーに変換を適用します。

## SQL構文

```sql
JSON_MAP_TRANSFORM_KEYS(<json_object>, (<key>, <value>) -> <key_transformation>)
```

## 戻り値の型

入力のJSONオブジェクトと同じ値を持ち、キーが指定したラムダ式の変換に従って変更されたJSONオブジェクトを返します。

## SQLの例

次の例では、各キーに「_v1」を付加して、キーが変更された新しいJSONオブジェクトを作成します。

```sql
SELECT JSON_MAP_TRANSFORM_KEYS('{"name":"John", "role":"admin"}'::VARIANT, (k, v) -> CONCAT(k, '_v1')) AS versioned_metadata;

┌──────────────────────────────────────┐
│          versioned_metadata          │
├──────────────────────────────────────┤
│ {"name_v1":"John","role_v1":"admin"} │
└──────────────────────────────────────┘
```
