---
title: ST_DISTANCE_SPHERE (Lakehouse v2)
description: ST_DISTANCE_SPHERE — retorna a distância esférica entre dois pontos em metros.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-distance-sphere.md
---

Retorna a distância esférica entre dois pontos em metros.

## Sintaxe do Analyze

```python
func.st_distance_sphere(<lng1>, <lat1>, <lng2>, <lat2>)
```

## Exemplos do Analyze

```python
func.st_distance_sphere(-73.9857, 40.7484, -0.1278, 51.5074)

┌───────────┐
│ 5570222.5  │
└───────────┘
```

## Sintaxe SQL

```sql
ST_DISTANCE_SPHERE(<lng1>, <lat1>, <lng2>, <lat2>)
```

## Exemplos de SQL

Distância em metros entre Nova York e Londres:

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) AS distance_meters;

┌─────────────────┐
│ distance_meters │
├─────────────────┤
│     5570222.50  │
└─────────────────┘
```

Distância em quilômetros (divida os metros por 1000):

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) / 1000 AS distance_km;

┌─────────────┐
│ distance_km │
├─────────────┤
│     5570.22 │
└─────────────┘
```

Distância em milhas (divida os metros por 1609.344):

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) / 1609.344 AS distance_miles;

┌────────────────┐
│ distance_miles │
├────────────────┤
│        3461.02 │
└────────────────┘
```
