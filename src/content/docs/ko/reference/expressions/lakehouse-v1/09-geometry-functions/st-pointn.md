---
title: ST_POINTN (Lakehouse v1)
description: ST_POINTN — LineString에서 지정한 인덱스에 있는 Point를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-pointn.md
---

LineString에서 지정한 인덱스에 있는 Point를 반환합니다.

## SQL 구문

```sql
ST_POINTN(<geometry>, <index>)
```

## 인수

| 인수    | 설명                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | 인수는 LineString을 나타내는 GEOMETRY 형식의 식이어야 합니다. |
| `<index>`    | 반환할 Point의 인덱스입니다.                                                 |

:::note
인덱스는 1부터 시작하며, 음수 인덱스는 LineString의 끝에서부터의 오프셋으로 사용됩니다. 인덱스가 범위를 벗어나면 함수가 오류를 반환합니다.
:::

## 반환 형식

Geometry.

## SQL 예제

```sql
SELECT
  ST_POINTN(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    ),
    1
  ) AS pipeline_pointn;

┌─────────────────┐
│ pipeline_pointn │
├─────────────────┤
│ POINT(1 1)      │
└─────────────────┘

SELECT
  ST_POINTN(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    ),
    -2
  ) AS pipeline_pointn;

┌─────────────────┐
│ pipeline_pointn │
├─────────────────┤
│ POINT(3 3)      │
└─────────────────┘
```
