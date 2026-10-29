---
title: ST_Y (Lakehouse v1)
description: ST_Y — GEOMETRY 객체로 표현된 Point의 위도(Y 좌표)를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-y.md
---

GEOMETRY 객체로 표현된 Point의 위도(Y 좌표)를 반환합니다.

## SQL 구문

```sql
ST_Y(<geometry>)
```

## 인수

| 인수    | 설명                                                                   |
|--------------|-------------------------------------------------------------------------------|
| `<geometry>` | 인수는 GEOMETRY 형식의 식이어야 하며 Point를 포함해야 합니다. |

## 반환 형식

Double.

## SQL 예제

```sql
SELECT
  ST_Y(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_y;

┌────────────┐
│ pipeline_y │
├────────────┤
│       45.5 │
└────────────┘
```
