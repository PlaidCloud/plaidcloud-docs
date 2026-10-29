---
title: ST_NPOINTS (Lakehouse v1)
description: ST_NPOINTS — GEOMETRY 객체에 포함된 점의 개수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-npoints.md
---

GEOMETRY 객체에 포함된 점의 개수를 반환합니다.

## SQL 구문

```sql
ST_NPOINTS(<geometry>)
```

## 별칭

- [ST_NUMPOINTS](../st-numpoints)

## 인수

| 인수    | 설명                                                 |
|--------------|-------------------------------------------------------------|
| `<geometry>` | 인수는 GEOMETRY 객체 형식의 식이어야 합니다. |

## 반환 형식

UInt8.

## SQL 예제

```sql
SELECT ST_NPOINTS(TO_GEOMETRY('POINT(66 12)')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       1 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('MULTIPOINT((45 21),(12 54))')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       2 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('LINESTRING(40 60,50 50,60 40)')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       3 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('MULTILINESTRING((1 1,32 17),(33 12,73 49,87.1 6.1))')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       5 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('GEOMETRYCOLLECTION(POLYGON((-10 0,0 10,10 0,-10 0)),LINESTRING(40 60,50 50,60 40),POINT(99 11))')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       8 │
└─────────┘
```
