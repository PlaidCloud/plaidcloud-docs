---
title: ST_TRANSFORM (Lakehouse v1)
description: ST_TRANSFORM — GEOMETRY 객체를 한 공간 참조 시스템(SRS)에서 다른 시스템으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-transform.md
---

GEOMETRY 객체를 한 [공간 참조 시스템(SRS)](https://en.wikipedia.org/wiki/Spatial_reference_system)에서 다른 시스템으로 변환합니다. 좌표는 바꾸지 않고 SRID만 변경하면 되는 경우(예: SRID가 잘못된 경우)에는 [ST_SETSRID](../st-setsrid)를 대신 사용하십시오.

## SQL 구문

```sql
ST_TRANSFORM(<geometry> [, <from_srid>], <to_srid>)
```

## 인수

| 인수     | 설명                                                                                                                                               |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<geometry>`  | 인수는 GEOMETRY 객체 형식의 식이어야 합니다.                                                                                               |
| `<from_srid>` | 입력 GEOMETRY 객체의 현재 SRS를 식별하는 선택적 SRID입니다. 이 인수를 생략하면 입력 GEOMETRY 객체에 지정된 SRID를 사용합니다. |
| `<to_srid>`   | 사용할 SRS를 식별하는 SRID입니다. 입력 GEOMETRY 객체를 이 SRS를 사용하는 새 객체로 변환합니다.                                         |

## 반환 형식

Geometry.

## SQL 예제

```sql
SET GEOMETRY_OUTPUT_FORMAT = 'EWKT'

SELECT ST_TRANSFORM(ST_GEOMFROMWKT('POINT(389866.35 5819003.03)', 32633), 3857) AS transformed_geom

┌───────────────────────────────────────────────┐
│                transformed_geom               │
├───────────────────────────────────────────────┤
│ SRID=3857;POINT(1489140.093766 6892872.19868) │
└───────────────────────────────────────────────┘

SELECT ST_TRANSFORM(ST_GEOMFROMWKT('POINT(4.500212 52.161170)'), 4326, 28992) AS transformed_geom

┌──────────────────────────────────────────────┐
│               transformed_geom               │
├──────────────────────────────────────────────┤
│ SRID=28992;POINT(94308.670475 464038.168827) │
└──────────────────────────────────────────────┘

```
