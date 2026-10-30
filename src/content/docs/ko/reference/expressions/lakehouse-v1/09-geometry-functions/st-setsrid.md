---
title: ST_SETSRID (Lakehouse v1)
description: ST_SETSRID — SRID(공간 참조 시스템 식별자)를 지정한 값으로 설정한 GEOMETRY 객체를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-setsrid.md
---

[SRID(공간 참조 시스템 식별자)](https://en.wikipedia.org/wiki/Spatial_reference_system#Identifier)를 지정한 값으로 설정한 GEOMETRY 객체를 반환합니다. 이 함수는 객체의 좌표는 그대로 두고 SRID만 변경합니다. 좌표도 새 SRS(공간 참조 시스템)에 맞게 변경해야 하면 [ST_TRANSFORM](../st-transform)을 대신 사용하십시오.

## SQL 구문

```sql
ST_SETSRID(<geometry>, <srid>)
```

## 인수

| 인수    | 설명                                                 |
|--------------|-------------------------------------------------------------|
| `<geometry>` | 인수는 GEOMETRY 객체 형식의 식이어야 합니다. |
| `<srid>`     | 반환되는 GEOMETRY 객체에 설정할 SRID 정수입니다.    |

## 반환 형식

Geometry.

## SQL 예제

```sql
SET GEOMETRY_OUTPUT_FORMAT = 'EWKT'

SELECT ST_SETSRID(TO_GEOMETRY('POINT(13 51)'), 4326) AS geometry

┌────────────────────────┐
│        geometry        │
├────────────────────────┤
│ SRID=4326;POINT(13 51) │
└────────────────────────┘

```
