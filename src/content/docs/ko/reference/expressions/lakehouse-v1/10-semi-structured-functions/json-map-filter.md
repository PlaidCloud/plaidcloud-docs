---
title: JSON_MAP_FILTER (Lakehouse v1)
description: JSON_MAP_FILTER — 지정한 조건을 기준으로 JSON 객체의 키-값 쌍을 필터링합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-filter.md
---

람다 식으로 정의한 지정 조건을 기준으로 JSON 객체의 키-값 쌍을 필터링합니다.

## SQL Syntax

```sql
JSON_MAP_FILTER(<json_object>, (<key>, <value>) -> <condition>)
```

## 반환 타입

지정한 조건을 만족하는 키-값 쌍만 담은 JSON 객체를 반환합니다.

## SQL Examples

이 예제는 JSON 객체에서 `"status": "active"` 키-값 쌍만 추출하고 나머지 필드는 걸러냅니다.

```sql
SELECT JSON_MAP_FILTER('{"status":"active", "user":"admin", "time":"2024-11-01"}'::VARIANT, (k, v) -> k = 'status') AS filtered_metadata;

┌─────────────────────┐
│  filtered_metadata  │
├─────────────────────┤
│ {"status":"active"} │
└─────────────────────┘
```
