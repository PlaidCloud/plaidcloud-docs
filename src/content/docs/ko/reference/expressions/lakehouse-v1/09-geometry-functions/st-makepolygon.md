---
title: ST_MAKEPOLYGON (Lakehouse v1)
description: ST_MAKEPOLYGON — 구멍이 없는 Polygon을 나타내는 GEOMETRY 객체를 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makepolygon.md
---

구멍이 없는 Polygon을 나타내는 GEOMETRY 객체를 생성합니다. 이 함수는 지정한 LineString을 외부 루프로 사용합니다.

## SQL 구문

```sql
ST_MAKEPOLYGON(<geometry>)
```

## 별칭

- [ST_POLYGON](../st-polygon)

## 인수

| 인수    | 설명                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | 인수는 GEOMETRY 형식의 식이어야 합니다. |

## 반환 형식

Geometry.

## SQL 예제

```sql
SELECT
  ST_MAKEPOLYGON(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(0.0 0.0, 1.0 0.0, 1.0 2.0, 0.0 2.0, 0.0 0.0)'
    )
  ) AS pipeline_polygon;

┌────────────────────────────────┐
│        pipeline_polygon        │
├────────────────────────────────┤
│ POLYGON((0 0,1 0,1 2,0 2,0 0)) │
└────────────────────────────────┘
```
