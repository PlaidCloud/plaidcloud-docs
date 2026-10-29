---
title: JSON_MAP_TRANSFORM_KEYS (Lakehouse v1)
description: JSON_MAP_TRANSFORM_KEYS — JSON 객체의 각 키에 변환을 적용합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-keys.md
---

람다 식을 사용하여 JSON 객체의 각 키에 변환을 적용합니다.

## SQL Syntax

```sql
JSON_MAP_TRANSFORM_KEYS(<json_object>, (<key>, <value>) -> <key_transformation>)
```

## 반환 타입

입력 JSON 객체와 값은 같지만, 지정한 람다 변환에 따라 키가 수정된 JSON 객체를 반환합니다.

## SQL Examples

이 예제는 각 키에 "_v1"을 덧붙여 키가 수정된 새 JSON 객체를 만듭니다.

```sql
SELECT JSON_MAP_TRANSFORM_KEYS('{"name":"John", "role":"admin"}'::VARIANT, (k, v) -> CONCAT(k, '_v1')) AS versioned_metadata;

┌──────────────────────────────────────┐
│          versioned_metadata          │
├──────────────────────────────────────┤
│ {"name_v1":"John","role_v1":"admin"} │
└──────────────────────────────────────┘
```
