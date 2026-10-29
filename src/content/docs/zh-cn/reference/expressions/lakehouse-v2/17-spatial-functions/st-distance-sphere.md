---
title: ST_DISTANCE_SPHERE (Lakehouse v2)
description: ST_DISTANCE_SPHERE — 返回两点之间的球面距离（单位为米）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-distance-sphere.md
---

返回两点之间的球面距离（单位为米）。

## Analyze 语法

```python
func.st_distance_sphere(<lng1>, <lat1>, <lng2>, <lat2>)
```

## Analyze 示例

```python
func.st_distance_sphere(-73.9857, 40.7484, -0.1278, 51.5074)

┌───────────┐
│ 5570222.5  │
└───────────┘
```

## SQL 语法

```sql
ST_DISTANCE_SPHERE(<lng1>, <lat1>, <lng2>, <lat2>)
```

## SQL 示例

纽约市与伦敦之间的距离（单位为米）：

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) AS distance_meters;

┌─────────────────┐
│ distance_meters │
├─────────────────┤
│     5570222.50  │
└─────────────────┘
```

以千米为单位的距离（将米数除以 1000）：

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) / 1000 AS distance_km;

┌─────────────┐
│ distance_km │
├─────────────┤
│     5570.22 │
└─────────────┘
```

以英里为单位的距离（将米数除以 1609.344）：

```sql
SELECT ST_DISTANCE_SPHERE(-73.9857, 40.7484, -0.1278, 51.5074) / 1609.344 AS distance_miles;

┌────────────────┐
│ distance_miles │
├────────────────┤
│        3461.02 │
└────────────────┘
```
