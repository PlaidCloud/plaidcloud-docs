---
title: ST_YMAX (Lakehouse v1)
description: ST_YMAX — 지정한 GEOMETRY 객체에 포함된 모든 점의 최대 위도(Y 좌표)를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-ymax.md
---

지정한 GEOMETRY 객체에 포함된 모든 점의 최대 위도(Y 좌표)를 반환합니다.

## SQL 구문

```sql
ST_YMAX(<geometry>)
```

## 인수

| 인수    | 설명                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | 인수는 GEOMETRY 형식의 식이어야 합니다. |

## 반환 형식

Double.

## SQL 예제

```sql
SELECT
  ST_YMAX(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(180 50),LINESTRING(10 10,20 20,10 40),POINT EMPTY)'
    )
  ) AS pipeline_ymax;

┌───────────────┐
│ pipeline_ymax │
├───────────────┤
│            50 │
└───────────────┘

SELECT
  ST_YMAX(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(40 10),LINESTRING(10 10,20 20,10 40),POLYGON((40 40,20 45,45 30,40 40)))'
    )
  ) AS pipeline_ymax;

┌───────────────┐
│ pipeline_ymax │
├───────────────┤
│            45 │
└───────────────┘
```
