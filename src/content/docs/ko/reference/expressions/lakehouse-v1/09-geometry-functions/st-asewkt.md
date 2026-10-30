---
title: ST_ASEWKT (Lakehouse v1)
description: ST_ASEWKT — GEOMETRY 객체를 EWKT(확장 WKT, extended well-known-text) 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-asewkt.md
---

GEOMETRY 객체를 [EWKT(extended well-known-text)](https://postgis.net/docs/ST_GeomFromEWKT.html) 형식의 표현으로 변환합니다.

## SQL 구문

```sql
ST_ASEWKT(<geometry>)
```

## 인수

| 인수    | 설명                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | 인수는 GEOMETRY 형식의 식이어야 합니다. |

## 반환 형식

String.

## SQL 예제

```sql
SELECT
  ST_ASEWKT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_ewkt;

┌─────────────────────────────────────────────────────┐
│                    pipeline_ewkt                    │
├─────────────────────────────────────────────────────┤
│ SRID=4326;LINESTRING(400000 6000000,401000 6010000) │
└─────────────────────────────────────────────────────┘

SELECT
  ST_ASEWKT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    )
  ) AS pipeline_ewkt;

┌────────────────────────────────┐
│          pipeline_ewkt         │
├────────────────────────────────┤
│ SRID=4326;POINT(-122.35 37.55) │
└────────────────────────────────┘
```
