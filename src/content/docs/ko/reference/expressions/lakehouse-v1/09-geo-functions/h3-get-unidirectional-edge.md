---
title: H3_GET_UNIDIRECTIONAL_EDGE (Lakehouse v1)
description: H3_GET_UNIDIRECTIONAL_EDGE — 지정한 두 H3 인덱스 사이의 모서리를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-unidirectional-edge.md
---

지정한 두 [H3](https://eng.uber.com/h3/) 인덱스 사이의 모서리를 반환합니다.

## Analyze 구문

```python
func.h3_get_unidirectional_edge(h3, a_h3)
```

## Analyze 예제

```python
func.h3_get_unidirectional_edge(644325524701193897, 644325524701193754)

┌─────────────────────────────────────────────────────────────────────────┐
│ func.h3_get_unidirectional_edge(644325524701193897, 644325524701193754) │
├─────────────────────────────────────────────────────────────────────────┤
│                                                     1581074247194257065 │
└─────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
H3_GET_UNIDIRECTIONAL_EDGE(h3, a_h3)
```

## SQL 예제

```sql
SELECT H3_GET_UNIDIRECTIONAL_EDGE(644325524701193897, 644325524701193754);

┌────────────────────────────────────────────────────────────────────┐
│ h3_get_unidirectional_edge(644325524701193897, 644325524701193754) │
├────────────────────────────────────────────────────────────────────┤
│                                                1581074247194257065 │
└────────────────────────────────────────────────────────────────────┘
```
