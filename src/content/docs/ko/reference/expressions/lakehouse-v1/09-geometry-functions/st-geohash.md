---
title: ST_GEOHASH (Lakehouse v1)
description: ST_GEOHASH — GEOMETRY 객체의 geohash를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geohash.md
---

GEOMETRY 객체의 [geohash](https://en.wikipedia.org/wiki/Geohash)를 반환합니다. geohash는 전 세계의 특정 위치를 포함하는 측지 직사각형을 식별하는 짧은 base32 문자열입니다. 선택 사항인 정밀도 인수는 반환되는 geohash의 `precision`을 지정합니다. 예를 들어 `precision에 5를 전달하면 더 짧고(5자) 정밀도가 낮은 geohash가 반환됩니다.

## SQL Syntax

```sql
ST_GEOHASH(<geometry> [, <precision>])
```

## 인수

| 인수            | 설명                                                                      |
|-----------------|---------------------------------------------------------------------------|
| `geometry`    | 인수는 GEOMETRY 형식의 식이어야 합니다.                      |
| `[precision]` | 선택 사항입니다. 반환되는 geohash의 정밀도를 지정하며, 기본값은 12입니다. |

## 반환 형식

문자열.

## SQL Examples

```sql
SELECT
  ST_GEOHASH(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    )
  ) AS pipeline_geohash;

┌──────────────────┐
│ pipeline_geohash │
├──────────────────┤
│ 9q9j8ue2v71y     │
└──────────────────┘

SELECT
  ST_GEOHASH(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    ),
    5
  ) AS pipeline_geohash;

┌──────────────────┐
│ pipeline_geohash │
├──────────────────┤
│ 9q8vx            │
└──────────────────┘
```
