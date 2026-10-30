---
title: ST_DISTANCE_SPHERE (Lakehouse v2)
description: ST_DISTANCE_SPHERE – gibt die sphärische Entfernung zwischen zwei Punkten in Metern zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-distance-sphere.md
---

Gibt die sphärische Entfernung zwischen zwei Punkten in Metern zurück.

## Analyze-Syntax

```python
func.st_distance_sphere(<lng1>, <lat1>, <lng2>, <lat2>)
```

## Analyze-Beispiele

```python
func.st_distance_sphere(-73.9857, 40.7484, -0.1278, 51.5074)

┌───────────┐
│ 5570222.5  │
└───────────┘
```

## SQL-Syntax

```sql
ST_DISTANCE_SPHERE(<lng1>, <lat1>, <lng2>, <lat2>)
```

## SQL-Beispiele

Entfernung in Metern zwischen New York City und London:

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) AS distance_meters;

┌─────────────────┐
│ distance_meters │
├─────────────────┤
│     5570222.50  │
└─────────────────┘
```

Entfernung in Kilometern (Meter durch 1000 teilen):

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) / 1000 AS distance_km;

┌─────────────┐
│ distance_km │
├─────────────┤
│     5570.22 │
└─────────────┘
```

Entfernung in Meilen (Meter durch 1609,344 teilen):

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) / 1609.344 AS distance_miles;

┌────────────────┐
│ distance_miles │
├────────────────┤
│        3461.02 │
└────────────────┘
```
