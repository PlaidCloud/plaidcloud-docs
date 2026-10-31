---
title: TO_GEOMETRY (Lakehouse v1)
description: TO_GEOMETRY — 입력을 구문 분석하여 GEOMETRY 형식의 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/to-geometry.md
---

입력을 구문 분석하여 GEOMETRY 형식의 값을 반환합니다.

`TRY_TO_GEOMETRY`는 구문 분석 중 오류가 발생하면 NULL 값을 반환합니다.

## SQL 구문

```sql
TO_GEOMETRY(<string>, [<srid>])
TO_GEOMETRY(<binary>, [<srid>])
TO_GEOMETRY(<variant>, [<srid>])
TRY_TO_GEOMETRY(<string>, [<srid>])
TRY_TO_GEOMETRY(<binary>, [<srid>])
TRY_TO_GEOMETRY(<variant>, [<srid>])
```

## 인수

| 인수   | 설명                                                                                               |
|-------------|-----------------------------------------------------------------------------------------------------------|
| `<string>`  | 인수는 WKT, EWKT, 16진수 형식의 WKB 또는 EWKB, GeoJSON 형식의 문자열 식이어야 합니다. |
| `<binary>`  | 인수는 WKB 또는 EWKB 형식의 이진 식이어야 합니다.                                           |
| `<variant>` | 인수는 GeoJSON 형식의 JSON OBJECT여야 합니다.                                                     |
| `<srid>`    | 사용할 SRID의 정수 값입니다.                                                                     |

## 반환 형식

Geometry.

## SQL 예제

```sql
SELECT
  TO_GEOMETRY(
    'POINT(1820.12 890.56)'
  ) AS pipeline_geometry;

┌───────────────────────┐
│   pipeline_geometry   │
├───────────────────────┤
│ POINT(1820.12 890.56) │
└───────────────────────┘

SELECT
  TO_GEOMETRY(
    '0101000020797f000066666666a9cb17411f85ebc19e325641', 4326
  ) AS pipeline_geometry;

┌───────────────────────────────────────┐
│           pipeline_geometry           │
├───────────────────────────────────────┤
│ SRID=4326;POINT(389866.35 5819003.03) │
└───────────────────────────────────────┘

SELECT
  TO_GEOMETRY(
    FROM_HEX('0101000020797f000066666666a9cb17411f85ebc19e325641'), 4326
  ) AS pipeline_geometry;

┌───────────────────────────────────────┐
│           pipeline_geometry           │
├───────────────────────────────────────┤
│ SRID=4326;POINT(389866.35 5819003.03) │
└───────────────────────────────────────┘

SELECT
  TO_GEOMETRY(
    '{"coordinates":[[389866,5819003],[390000,5830000]],"type":"LineString"}'
  ) AS pipeline_geometry;

┌───────────────────────────────────────────┐
│             pipeline_geometry             │
├───────────────────────────────────────────┤
│ LINESTRING(389866 5819003,390000 5830000) │
└───────────────────────────────────────────┘

SELECT
  TO_GEOMETRY(
    PARSE_JSON('{"coordinates":[[389866,5819003],[390000,5830000]],"type":"LineString"}')
  ) AS pipeline_geometry;

┌───────────────────────────────────────────┐
│             pipeline_geometry             │
├───────────────────────────────────────────┤
│ LINESTRING(389866 5819003,390000 5830000) │
└───────────────────────────────────────────┘
```
