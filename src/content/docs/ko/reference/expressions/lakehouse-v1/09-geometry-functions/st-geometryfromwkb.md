---
title: ST_GEOMETRYFROMWKB (Lakehouse v1)
description: ST_GEOMETRYFROMWKB — WKB(well-known-binary) 또는 EWKB(extended well-known-binary) 입력을 구문 분석합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkb.md
---

[WKB(well-known-binary)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) 또는 [EWKB(extended well-known-binary)](https://postgis.net/docs/ST_GeomFromEWKB.html) 입력을 구문 분석하여 GEOMETRY 형식의 값을 반환합니다.

## SQL 구문

```sql
ST_GEOMETRYFROMWKB(<string>, [<srid>])
ST_GEOMETRYFROMWKB(<binary>, [<srid>])
```

## 별칭

- [ST_GEOMFROMWKB](../st-geomfromwkb)
- [ST_GEOMETRYFROMEWKB](../st-geometryfromewkb)
- [ST_GEOMFROMEWKB](../st-geomfromewkb)

## 인수

| 인수   | 설명                                                                    |
|-------------|--------------------------------------------------------------------------------|
| `<string>`  | 인수는 16진수 형식의 WKB 또는 EWKB 문자열 식이어야 합니다. |
| `<binary>`  | 인수는 WKB 또는 EWKB 형식의 이진 식이어야 합니다.                |
| `<srid>`    | 사용할 SRID의 정수 값입니다.                                          |

## 반환 형식

Geometry.

## SQL 예제

```sql
SELECT
  ST_GEOMETRYFROMWKB(
    '0101000020797f000066666666a9cb17411f85ebc19e325641'
  ) AS pipeline_geometry;

┌────────────────────────────────────────┐
│            pipeline_geometry           │
├────────────────────────────────────────┤
│ SRID=32633;POINT(389866.35 5819003.03) │
└────────────────────────────────────────┘

SELECT
  ST_GEOMETRYFROMWKB(
    FROM_HEX('0101000020797f000066666666a9cb17411f85ebc19e325641'), 4326
  ) AS pipeline_geometry;

┌───────────────────────────────────────┐
│           pipeline_geometry           │
├───────────────────────────────────────┤
│ SRID=4326;POINT(389866.35 5819003.03) │
└───────────────────────────────────────┘
```
