---
title: ST_MAKEPOLYGON
description: "Learn how to use the ST_MAKEPOLYGON geometry function in PlaidCloud Lakehouse. Constructs a GEOMETRY object that represents a Polygon without holes."
---

Constructs a GEOMETRY object that represents a Polygon without holes. The function uses the specified LineString as the outer loop.

## SQL Syntax

```sql
ST_MAKEPOLYGON(<geometry>)
```

## Aliases

- [ST_POLYGON](../st-polygon)

## Arguments

| Arguments    | Description                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | The argument must be an expression of type GEOMETRY. |

## Return Type

Geometry.

## SQL Examples

```sql
SELECT
  ST_MAKEPOLYGON(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(0.0 0.0, 1.0 0.0, 1.0 2.0, 0.0 2.0, 0.0 0.0)'
    )
  ) AS pipeline_polygon;

┌────────────────────────────────┐
│        pipeline_polygon        │
├────────────────────────────────┤
│ POLYGON((0 0,1 0,1 2,0 2,0 0)) │
└────────────────────────────────┘
```
