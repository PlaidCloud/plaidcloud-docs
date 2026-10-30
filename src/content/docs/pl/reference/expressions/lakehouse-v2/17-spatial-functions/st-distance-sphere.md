---
title: ST_DISTANCE_SPHERE (Lakehouse v2)
description: ST_DISTANCE_SPHERE — zwraca odległość sferyczną między dwoma punktami w metrach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-distance-sphere.md
---

Zwraca odległość sferyczną między dwoma punktami w metrach.

## Składnia Analyze

```python
func.st_distance_sphere(<lng1>, <lat1>, <lng2>, <lat2>)
```

## Przykłady Analyze

```python
func.st_distance_sphere(-73.9857, 40.7484, -0.1278, 51.5074)

┌───────────┐
│ 5570222.5  │
└───────────┘
```

## Składnia SQL

```sql
ST_DISTANCE_SPHERE(<lng1>, <lat1>, <lng2>, <lat2>)
```

## Przykłady SQL

Odległość w metrach między Nowym Jorkiem a Londynem:

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) AS distance_meters;

┌─────────────────┐
│ distance_meters │
├─────────────────┤
│     5570222.50  │
└─────────────────┘
```

Odległość w kilometrach (podziel metry przez 1000):

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) / 1000 AS distance_km;

┌─────────────┐
│ distance_km │
├─────────────┤
│     5570.22 │
└─────────────┘
```

Odległość w milach (podziel metry przez 1609,344):

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) / 1609.344 AS distance_miles;

┌────────────────┐
│ distance_miles │
├────────────────┤
│        3461.02 │
└────────────────┘
```
