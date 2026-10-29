---
title: ST_CONTAINS (Lakehouse v1)
description: ST_CONTAINS — 두 번째 GEOMETRY 객체가 첫 번째 객체 안에 완전히 포함되면 TRUE를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-contains.md
---

두 번째 GEOMETRY 객체가 첫 번째 GEOMETRY 객체 안에 완전히 포함되면 TRUE를 반환합니다.

## SQL 구문

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## 인수

| 인수     | 설명                                                                                  |
|---------------|----------------------------------------------------------------------------------------------|
| `<geometry1>` | 인수는 GeometryCollection이 아닌 GEOMETRY 객체 형식의 식이어야 합니다. |
| `<geometry2>` | 인수는 GeometryCollection이 아닌 GEOMETRY 객체 형식의 식이어야 합니다. |

:::note
- 입력한 두 GEOMETRY 객체의 SRID가 다르면 함수가 오류를 보고합니다.
:::

## 반환 형식

Boolean.

## SQL 예제

```sql
SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('POLYGON((-1 0, 0 1, 1 0, -1 0))')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-1 1, 0 2, 1 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ false    │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-2 0, 0 0, 0 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

```
