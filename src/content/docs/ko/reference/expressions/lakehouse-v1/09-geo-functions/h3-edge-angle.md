---
title: H3_EDGE_ANGLE (Lakehouse v1)
description: H3_EDGE_ANGLE — H3 육각형 모서리의 평균 길이를 그레이드 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-angle.md
---

H3 육각형 모서리의 평균 길이를 그레이드 단위로 반환합니다.

## Analyze 구문

```python
func.h3_edge_angle(res)
```

## Analyze 예제

```python
func.h3_edge_angle(10)

┌────────────────────────────┐
│   func.h3_edge_angle(10)   │
├────────────────────────────┤
│      0.0006822586214153981 │
└────────────────────────────┘
```

## SQL 구문

```sql
H3_EDGE_ANGLE(res)
```

## SQL 예제

```sql
SELECT H3_EDGE_ANGLE(10);

┌───────────────────────┐
│   h3_edge_angle(10)   │
├───────────────────────┤
│ 0.0006822586214153981 │
└───────────────────────┘
```
