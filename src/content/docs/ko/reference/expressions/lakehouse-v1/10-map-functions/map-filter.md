---
title: MAP_FILTER (Lakehouse v1)
description: MAP_FILTER — 람다 식으로 조건을 정의하여 MAP에서 키-값 쌍을 필터링합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-filter.md
---

람다 식으로 조건을 정의하여 MAP에서 키-값 쌍을 필터링합니다.

## SQL 구문

```sql
MAP_FILTER(<map>, (<key>, <value>) -> <condition>)
```

## 반환 형식

람다 식에 지정한 조건을 충족하는 키-값 쌍만 포함하는 MAP을 반환합니다.

## SQL 예제

이 예제는 재고 수량이 10 미만인 제품만 포함하는 MAP을 반환합니다.

```sql
SELECT MAP_FILTER({101:15, 102:8, 103:12, 104:5}, (product_id, stock) -> (stock < 10)) AS low_stock_products;

┌────────────────────┐
│ low_stock_products │
├────────────────────┤
│ {102:8,104:5}      │
└────────────────────┘
```
