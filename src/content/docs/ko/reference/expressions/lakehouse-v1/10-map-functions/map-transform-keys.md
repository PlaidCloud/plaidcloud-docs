---
title: MAP_TRANSFORM_KEYS (Lakehouse v1)
description: MAP_TRANSFORM_KEYS — 람다 식을 사용하여 MAP의 각 키에 변환을 적용합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-keys.md
---

람다 식을 사용하여 MAP의 각 키에 변환을 적용합니다.

## SQL 구문

```sql
MAP_TRANSFORM_KEYS(<map>, (<key>, <value>) -> <key_transformation>)
```

## 반환 형식

입력 MAP과 값은 같지만 키는 지정한 람다 변환에 따라 수정된 MAP을 반환합니다.

## SQL 예제

이 예제는 각 제품 ID에 1,000을 더하여, 연결된 가격은 그대로 두고 키만 갱신한 새 MAP을 만듭니다.

```sql
SELECT MAP_TRANSFORM_KEYS({101: 29.99, 102: 45.50, 103: 15.00}, (product_id, price) -> product_id + 1000) AS updated_product_ids;

┌────────────────────────────────────┐
│         updated_product_ids        │
├────────────────────────────────────┤
│ {1101:29.99,1102:45.50,1103:15.00} │
└────────────────────────────────────┘
```
