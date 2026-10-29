---
title: ST_LENGTH (Lakehouse v1)
description: ST_LENGTH — GEOMETRY 객체에 포함된 LineString의 유클리드 길이를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-length.md
---

GEOMETRY 객체에 포함된 LineString의 유클리드 길이를 반환합니다.

## SQL 구문

```sql
ST_LENGTH(<geometry>)
```

## 인수

| 인수    | 설명                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `<geometry>` | 인수는 선 문자열(linestring)을 포함하는 GEOMETRY 형식의 식이어야 합니다. |

:::note
- `<geometry>`가 `LineString`, `MultiLineString` 또는 선 문자열을 포함하는 `GeometryCollection`이 아니면 0을 반환합니다.
- `<geometry>`가 `GeometryCollection`이면 컬렉션에 포함된 선 문자열 길이의 합을 반환합니다.
:::

## 반환 형식

Double.

## SQL 예제

```sql
SELECT
  ST_LENGTH(TO_GEOMETRY('POINT(1 1)')) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘

SELECT
  ST_LENGTH(TO_GEOMETRY('LINESTRING(0 0, 1 1)')) AS length

┌─────────────┐
│    length   │
├─────────────┤
│ 1.414213562 │
└─────────────┘

SELECT
  ST_LENGTH(
    TO_GEOMETRY('POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))')
  ) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘
```
