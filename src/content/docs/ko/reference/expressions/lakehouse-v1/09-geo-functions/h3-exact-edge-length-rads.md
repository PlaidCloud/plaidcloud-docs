---
title: H3_EXACT_EDGE_LENGTH_RADS (Lakehouse v1)
description: H3_EXACT_EDGE_LENGTH_RADS — 이 방향성 모서리의 길이를 라디안 단위로 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-exact-edge-length-rads.md
---

이 방향성 모서리의 길이를 라디안 단위로 계산합니다.

## Analyze 구문

```python
func.h3_exact_edge_length_km(h3)
```

## Analyze 예제

```python
func.h3_exact_edge_length_km(1319695429381652479)

┌───────────────────────────────────────────────────┐
│ func.h3_exact_edge_length_km(1319695429381652479) │
├───────────────────────────────────────────────────┤
│                                 8.267326832647143 │
└───────────────────────────────────────────────────┘
```

## SQL 구문

```sql
H3_EXACT_EDGE_LENGTH_RADS(h3)
```

## SQL 예제

```sql
SELECT H3_EXACT_EDGE_LENGTH_KM(1319695429381652479);

┌──────────────────────────────────────────────┐
│ h3_exact_edge_length_km(1319695429381652479) │
├──────────────────────────────────────────────┤
│                            8.267326832647143 │
└──────────────────────────────────────────────┘
```
