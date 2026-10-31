---
title: ST_MAKEGEOMPOINT (Lakehouse v1)
description: ST_MAKEGEOMPOINT — 지정한 경도와 위도를 가진 Point를 나타내는 GEOMETRY 객체를 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makegeompoint.md
---

지정한 경도와 위도를 가진 Point를 나타내는 GEOMETRY 객체를 생성합니다.

## SQL 구문

```sql
ST_MAKEGEOMPOINT(<longitude>, <latitude>)
```

## 별칭

- [ST_GEOM_POINT](../st-geom-point)

## 인수

| 인수      | 설명                                   |
|---------------|-----------------------------------------------|
| `<longitude>` | 경도를 나타내는 Double 값입니다. |
| `<latitude>`  | 위도를 나타내는 Double 값입니다.  |

## 반환 형식

Geometry.

## SQL 예제

```sql
SELECT
  ST_MAKEGEOMPOINT(
    7.0, 8.0
  ) AS pipeline_point;

┌────────────────┐
│ pipeline_point │
├────────────────┤
│ POINT(7 8)     │
└────────────────┘

SELECT
  ST_MAKEGEOMPOINT(
    -122.3061, 37.554162
  ) AS pipeline_point;

┌────────────────────────────┐
│       pipeline_point       │
├────────────────────────────┤
│ POINT(-122.3061 37.554162) │
└────────────────────────────┘
```
