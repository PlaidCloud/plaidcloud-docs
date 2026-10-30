---
title: ST_DISTANCE_SPHERE (Lakehouse v2)
description: ST_DISTANCE_SPHERE — 두 지점 사이의 구면 거리를 미터 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-distance-sphere.md
---

두 지점 사이의 구면 거리를 미터 단위로 반환합니다.

## Analyze 구문

```python
func.st_distance_sphere(<lng1>, <lat1>, <lng2>, <lat2>)
```

## Analyze 예제

```python
func.st_distance_sphere(-73.9857, 40.7484, -0.1278, 51.5074)

┌───────────┐
│ 5570222.5  │
└───────────┘
```

## SQL 구문

```sql
ST_DISTANCE_SPHERE(<lng1>, <lat1>, <lng2>, <lat2>)
```

## SQL 예제

뉴욕시와 런던 사이의 거리(미터):

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) AS distance_meters;

┌─────────────────┐
│ distance_meters │
├─────────────────┤
│     5570222.50  │
└─────────────────┘
```

킬로미터 단위 거리(미터를 1000으로 나눕니다):

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) / 1000 AS distance_km;

┌─────────────┐
│ distance_km │
├─────────────┤
│     5570.22 │
└─────────────┘
```

마일 단위 거리(미터를 1609.344로 나눕니다):

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) / 1609.344 AS distance_miles;

┌────────────────┐
│ distance_miles │
├────────────────┤
│        3461.02 │
└────────────────┘
```
