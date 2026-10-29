---
title: ST_ENDPOINT (Lakehouse v1)
description: ST_ENDPOINT — LineString의 마지막 Point를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-endpoint.md
---

LineString의 마지막 Point를 반환합니다.

## SQL 구문

```sql
ST_ENDPOINT(<geometry>)
```

## 인수

| 인수    | 설명                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | 인수는 LineString을 나타내는 GEOMETRY 형식의 식이어야 합니다. |

## 반환 형식

Geometry.

## SQL 예제

```sql
SELECT
  ST_ENDPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(4 4)        │
└───────────────────┘
```
