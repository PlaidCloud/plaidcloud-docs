---
title: ST_GEOMETRYFROMWKT (Lakehouse v1)
description: ST_GEOMETRYFROMWKT — WKT(well-known-text) 또는 EWKT(extended well-known-text) 입력을 구문 분석하여 GEOMETRY 형식의 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkt.md
---

[WKT(well-known-text)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) 또는 [EWKT(extended well-known-text)](https://postgis.net/docs/ST_GeomFromEWKT.html) 입력을 구문 분석하여 GEOMETRY 형식의 값을 반환합니다.

## SQL 구문

```sql
ST_GEOMETRYFROMWKT(<string>, [<srid>])
```

## 별칭

- [ST_GEOMFROMWKT](../st-geomfromwkt)
- [ST_GEOMETRYFROMEWKT](../st-geometryfromewkt)
- [ST_GEOMFROMEWKT](../st-geomfromewkt)
- [ST_GEOMFROMTEXT](../st-geomfromtext)
- [ST_GEOMETRYFROMTEXT](../st-geometryfromtext)

## 인수

| 인수   | 설명                                                     |
|-------------|-----------------------------------------------------------------|
| `<string>`  | 인수는 WKT 또는 EWKT 형식의 문자열 식이어야 합니다. |
| `<srid>`    | 사용할 SRID의 정수 값입니다.                           |

## 반환 형식

Geometry.

## SQL 예제

```sql
SELECT
  ST_GEOMETRYFROMWKT(
    'POINT(1820.12 890.56)'
  ) AS pipeline_geometry;

┌───────────────────────┐
│   pipeline_geometry   │
├───────────────────────┤
│ POINT(1820.12 890.56) │
└───────────────────────┘

SELECT
  ST_GEOMETRYFROMWKT(
    'POINT(1820.12 890.56)', 4326
  ) AS pipeline_geometry;

┌─────────────────────────────────┐
│        pipeline_geometry        │
│             Geometry            │
├─────────────────────────────────┤
│ SRID=4326;POINT(1820.12 890.56) │
└─────────────────────────────────┘
```
