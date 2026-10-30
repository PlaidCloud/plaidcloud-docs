---
title: ST_ASWKT (Lakehouse v1)
description: ST_ASWKT — GEOMETRY 객체를 WKT(well-known-text) 형식의 표현으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-aswkt.md
---

GEOMETRY 객체를 [WKT(well-known-text)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) 형식의 표현으로 변환합니다.

## SQL 구문

```sql
ST_ASWKT(<geometry>)
```

## 별칭

- [ST_ASTEXT](../st-astext)

## 인수

| 인수    | 설명                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | 인수는 GEOMETRY 형식의 식이어야 합니다. |

## 반환 형식

String.

## SQL 예제

```sql
SELECT
  ST_ASWKT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_wkt;

┌───────────────────────────────────────────┐
│                pipeline_wkt               │
├───────────────────────────────────────────┤
│ LINESTRING(400000 6000000,401000 6010000) │
└───────────────────────────────────────────┘

SELECT
  ST_ASTEXT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    )
  ) AS pipeline_wkt;

┌──────────────────────┐
│     pipeline_wkt     │
├──────────────────────┤
│ POINT(-122.35 37.55) │
└──────────────────────┘
```
