---
title: H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE (Lakehouse v1)
description: H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE — 출발 및 도착 육각형 인덱스를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-indexes-from-unidirectional-edge.md
---

지정한 단방향 모서리 H3Index에서 출발 및 도착 육각형 인덱스를 반환합니다.

## Analyze 구문

```python
func.h3_get_indexes_from_unidirectional_edge(h3)
```

## Analyze 예제

```python
func.h3_get_indexes_from_unidirectional_edge(1248204388774707199)

┌────────────────────────────────────────────────────────────────────┐
│ func.h3_get_indexes_from_unidirectional_edge(1248204388774707199)  │
├────────────────────────────────────────────────────────────────────┤
│ (599686042433355775,599686043507097599)                            │
└────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE(h3)
```

## SQL 예제

```sql
SELECT H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE(1248204388774707199);

┌──────────────────────────────────────────────────────────────┐
│ h3_get_indexes_from_unidirectional_edge(1248204388774707199) │
├──────────────────────────────────────────────────────────────┤
│ (599686042433355775,599686043507097599)                      │
└──────────────────────────────────────────────────────────────┘
```
