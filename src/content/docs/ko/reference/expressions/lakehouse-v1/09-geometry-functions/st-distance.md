---
title: ST_DISTANCE (Lakehouse v1)
description: ST_DISTANCE — 두 GEOMETRY 객체 사이의 최소 유클리드 거리를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-distance.md
---

두 GEOMETRY 객체 사이의 최소 [유클리드 거리](https://en.wikipedia.org/wiki/Euclidean_distance)를 반환합니다.

## SQL 구문

```sql
ST_DISTANCE(<geometry1>, <geometry2>)
```

## 인수

| 인수     | 설명                                                                   |
|---------------|-------------------------------------------------------------------------------|
| `<geometry1>` | 인수는 GEOMETRY 형식의 식이어야 하며 Point를 포함해야 합니다. |
| `<geometry2>` | 인수는 GEOMETRY 형식의 식이어야 하며 Point를 포함해야 합니다. |

:::note
- 입력한 점 중 하나 이상이 NULL이면 NULL을 반환합니다.
- 입력한 두 GEOMETRY 객체의 SRID가 다르면 함수가 오류를 보고합니다.
:::

## 반환 형식

Double.

## SQL 예제

```sql
SELECT
  ST_DISTANCE(
    TO_GEOMETRY('POINT(0 0)'),
    TO_GEOMETRY('POINT(1 1)')
  ) AS distance

┌─────────────┐
│   distance  │
├─────────────┤
│ 1.414213562 │
└─────────────┘
```
