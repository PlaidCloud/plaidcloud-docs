---
title: ST_SRID (Lakehouse v1)
description: ST_SRID — GEOMETRY 객체의 SRID(공간 참조 시스템 식별자)를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-srid.md
---

GEOMETRY 객체의 SRID(공간 참조 시스템 식별자)를 반환합니다.

## SQL 구문

```sql
ST_SRID(<geometry>)
```

## 인수

| 인수    | 설명                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | 인수는 GEOMETRY 형식의 식이어야 합니다. |

## 반환 형식

INT32.

:::note
지오메트리에 SRID가 없으면 기본값 4326을 반환합니다.
:::

## SQL 예제

```sql
SELECT
  ST_SRID(
    TO_GEOMETRY(
      'POINT(-122.306100 37.554162)',
      1234
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          1234 │
└───────────────┘

SELECT
  ST_SRID(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          4326 │
└───────────────┘
```
