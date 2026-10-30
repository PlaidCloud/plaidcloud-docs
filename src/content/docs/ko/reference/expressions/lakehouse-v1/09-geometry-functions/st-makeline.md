---
title: ST_MAKELINE (Lakehouse v1)
description: ST_MAKELINE — 입력한 두 GEOMETRY 객체의 점을 연결하는 선을 나타내는 GEOMETRY 객체를 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makeline.md
---

입력한 두 GEOMETRY 객체의 점을 연결하는 선을 나타내는 GEOMETRY 객체를 생성합니다.

## SQL 구문

```sql
ST_MAKELINE(<geometry1>, <geometry2>)
```

## 별칭

- [ST_MAKE_LINE](../st-make-line)

## 인수

| 인수      | 설명                                                                                                 |
|---------------|-------------------------------------------------------------------------------------------------------------|
| `<geometry1>` | 연결할 점을 포함하는 GEOMETRY 객체입니다. 이 객체는 Point, MultiPoint 또는 LineString이어야 합니다. |
| `<geometry2>` | 연결할 점을 포함하는 GEOMETRY 객체입니다. 이 객체는 Point, MultiPoint 또는 LineString이어야 합니다. |

## 반환 형식

Geometry.

## SQL 예제

```sql
SELECT
  ST_MAKELINE(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    ),
    ST_GEOMETRYFROMWKT(
      'POINT(-104.874173 56.714538)'
    )
  ) AS pipeline_line;

┌───────────────────────────────────────────────────────┐
│                     pipeline_line                     │
├───────────────────────────────────────────────────────┤
│ LINESTRING(-122.3061 37.554162,-104.874173 56.714538) │
└───────────────────────────────────────────────────────┘
```
