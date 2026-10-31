---
title: H3_EDGE_LENGTH_KM (Lakehouse v1)
description: H3_EDGE_LENGTH_KM — 지정한 해상도에서 육각형 모서리의 평균 길이를 킬로미터 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-km.md
---

지정한 해상도에서 육각형 모서리의 평균 길이를 킬로미터 단위로 반환합니다. 오각형은 제외합니다.

## Analyze 구문

```python
func.h3_edge_length_km(res)
```

## Analyze 예제

```python
func.h3_edge_length_km(1)

┌───────────────────────────┐
│ func.h3_edge_length_km(1) │
├───────────────────────────┤
│         483.0568390711111 │
└───────────────────────────┘
```

## SQL 구문

```sql
H3_EDGE_LENGTH_KM(res)
```

## SQL 예제

```sql
SELECT H3_EDGE_LENGTH_KM(1);

┌──────────────────────┐
│ h3_edge_length_km(1) │
├──────────────────────┤
│    483.0568390711111 │
└──────────────────────┘
```
