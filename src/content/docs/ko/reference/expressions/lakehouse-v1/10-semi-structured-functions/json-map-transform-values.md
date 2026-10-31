---
title: JSON_MAP_TRANSFORM_VALUES (Lakehouse v1)
description: JSON_MAP_TRANSFORM_VALUES — JSON 객체의 각 값에 변환을 적용합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-values.md
---

람다 식을 사용하여 JSON 객체의 각 값에 변환을 적용합니다.

## SQL Syntax

```sql
JSON_MAP_TRANSFORM_VALUES(<json_object>, (<key>, <value>) -> <value_transformation>)
```

## 반환 타입

입력 JSON 객체와 키는 같지만, 지정한 람다 변환에 따라 값이 수정된 JSON 객체를 반환합니다.

## SQL Examples

이 예제는 각 제품 설명에 " - Special Offer"를 덧붙입니다.

```sql
SELECT JSON_MAP_TRANSFORM_VALUES('{"product1":"laptop", "product2":"phone"}'::VARIANT, (k, v) -> CONCAT(v, ' - Special Offer')) AS promo_descriptions;

┌──────────────────────────────────────────────────────────────────────────┐
│                            promo_descriptions                            │
├──────────────────────────────────────────────────────────────────────────┤
│ {"product1":"laptop - Special Offer","product2":"phone - Special Offer"} │
└──────────────────────────────────────────────────────────────────────────┘
```
