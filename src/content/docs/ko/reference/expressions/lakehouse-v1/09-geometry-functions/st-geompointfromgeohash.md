---
title: ST_GEOMPOINTFROMGEOHASH (Lakehouse v1)
description: ST_GEOMPOINTFROMGEOHASH — geohash의 중심을 나타내는 점의 GEOMETRY 객체를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geompointfromgeohash.md
---

[geohash](https://en.wikipedia.org/wiki/Geohash)의 중심을 나타내는 점의 GEOMETRY 객체를 반환합니다.

## SQL 구문

```sql
ST_GEOMPOINTFROMGEOHASH(<geohash>)
```

## 인수

| 인수   | 설명                     |
|-------------|---------------------------------|
| `<geohash>` | 인수는 geohash여야 합니다. |

## 반환 형식

Geometry.

## SQL 예제

```sql
SELECT
  ST_GEOMPOINTFROMGEOHASH(
    's02equ0'
  ) AS pipeline_geometry;

┌──────────────────────────────────────────────┐
│               pipeline_geometry              │
│                   Geometry                   │
├──────────────────────────────────────────────┤
│ POINT(1.0004425048828125 2.0001983642578125) │
└──────────────────────────────────────────────┘
```
