---
title: H3_UNIDIRECTIONAL_EDGE_IS_VALID (Lakehouse v1)
description: H3_UNIDIRECTIONAL_EDGE_IS_VALID — 지정한 H3Index가 유효한 단방향 모서리인지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-unidirectional-edge-is-valid.md
---

지정한 H3Index가 유효한 단방향 모서리 인덱스인지 확인합니다. 단방향 모서리이면 1을, 그렇지 않으면 0을 반환합니다.

## Analyze 구문

```python
func.h3_unidirectional_edge_is_valid(h3)
```

## Analyze 예제

```python
func.h3_unidirectional_edge_is_valid(1248204388774707199)

┌───────────────────────────────────────────────────────────┐
│ func.h3_unidirectional_edge_is_valid(1248204388774707199) │
├───────────────────────────────────────────────────────────┤
│ true                                                      │
└───────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
H3_UNIDIRECTIONAL_EDGE_IS_VALID(h3)
```

## SQL 예제

```sql
SELECT H3_UNIDIRECTIONAL_EDGE_IS_VALID(1248204388774707199);

┌──────────────────────────────────────────────────────┐
│ h3_unidirectional_edge_is_valid(1248204388774707199) │
├──────────────────────────────────────────────────────┤
│ true                                                 │
└──────────────────────────────────────────────────────┘
```
