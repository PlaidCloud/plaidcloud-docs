---
title: H3_EDGE_LENGTH_M (Lakehouse v1)
description: H3_EDGE_LENGTH_M — 지정한 해상도에서 육각형 모서리의 평균 길이를 미터 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-m.md
---

지정한 해상도에서 육각형 모서리의 평균 길이를 미터 단위로 반환합니다. 오각형은 제외합니다.

## Analyze 구문

```python
func.h3_edge_length(1)
```

## Analyze 예제

```python
func.h3_edge_length(1)

┌──────────────────────────┐
│ func.h3_edge_length_m(1) │
├──────────────────────────┤
│        483056.8390711111 │
└──────────────────────────┘
```

## SQL 구문

```sql
H3_EDGE_LENGTH_M(1)
```

## SQL 예제

```sql
┌─────────────────────┐
│ h3_edge_length_m(1) │
├─────────────────────┤
│   483056.8390711111 │
└─────────────────────┘
```
