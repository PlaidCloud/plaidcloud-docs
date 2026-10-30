---
title: MAP_TRANSFORM_VALUES (Lakehouse v1)
description: MAP_TRANSFORM_VALUES — 람다 식을 사용하여 MAP의 각 값에 변환을 적용합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-values.md
---

람다 식을 사용하여 MAP의 각 값에 변환을 적용합니다.

## SQL 구문

```sql
MAP_TRANSFORM_VALUES(<map>, (<key>, <value>) -> <value_transformation>)
```

## 반환 형식

입력 MAP과 키는 같지만 값은 지정한 람다 변환에 따라 수정된 MAP을 반환합니다.

## SQL 예제

이 예제는 제품 ID(키)는 그대로 두고 각 제품의 가격을 10% 낮춥니다.

```sql
SELECT MAP_TRANSFORM_VALUES({101: 100.0, 102: 150.0, 103: 200.0}, (product_id, price) -> price * 0.9) AS discounted_prices;

┌───────────────────────────────────┐
│         discounted_prices         │
├───────────────────────────────────┤
│ {101:90.00,102:135.00,103:180.00} │
└───────────────────────────────────┘
```
