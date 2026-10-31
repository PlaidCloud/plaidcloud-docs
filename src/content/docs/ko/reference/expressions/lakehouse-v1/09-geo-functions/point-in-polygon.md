---
title: POINT_IN_POLYGON (Lakehouse v1)
description: POINT_IN_POLYGON — 지정한 점이 여러 점을 이어 만든 다각형 안에 있는지 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/point-in-polygon.md
---

지정한 점이 여러 점을 이어 만든 다각형 안에 있는지 계산합니다. 다각형은 좌표 쌍을 나타난 순서대로 연결한 닫힌 도형입니다. 좌표 쌍의 순서를 바꾸면 다른 도형이 될 수 있습니다.

## Analyze 구문

```python
func.point_in_polygon((x,y), [(a,b), (c,d), (e,f) ... ])
```

## Analyze 예제

```python
func.point_in_polygon((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)])

┌─────────────────────────────────────────────────────────────────┐
│ func.point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├─────────────────────────────────────────────────────────────────┤
│                                                               1 │
└─────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
POINT_IN_POLYGON((x,y), [(a,b), (c,d), (e,f) ... ])
```

## SQL 예제

```sql
SELECT POINT_IN_POLYGON((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)]);

┌────────────────────────────────────────────────────────────┐
│ point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├────────────────────────────────────────────────────────────┤
│                                                          1 │
└────────────────────────────────────────────────────────────┘
```
