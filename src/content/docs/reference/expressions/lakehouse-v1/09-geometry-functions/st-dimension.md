---
title: ST_DIMENSION
description: "Learn how to use the ST_DIMENSION geometry function in PlaidCloud Lakehouse. Return the dimension for a geometry object. Includes syntax and examples."
---

Return the dimension for a geometry object. The dimension of a GEOMETRY object is:

| Geospatial Object Type       | Dimension  |
|------------------------------|------------|
| Point / MultiPoint           | 0          |
| LineString / MultiLineString | 1          |
| Polygon / MultiPolygon       | 2          |

## SQL Syntax

```sql
ST_DIMENSION(<geometry>)
```

## Arguments

| Arguments    | Description                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | The argument must be an expression of type GEOMETRY. |

## Return Type

UInt8.

## SQL Examples

```sql
SELECT
  ST_DIMENSION(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    )
  ) AS pipeline_dimension;

┌────────────────────┐
│ pipeline_dimension │
├────────────────────┤
│                  0 │
└────────────────────┘

SELECT
  ST_DIMENSION(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(-124.20 42.00, -120.01 41.99)'
    )
  ) AS pipeline_dimension;

┌────────────────────┐
│ pipeline_dimension │
├────────────────────┤
│                  1 │
└────────────────────┘

SELECT
  ST_DIMENSION(
    ST_GEOMETRYFROMWKT(
      'POLYGON((-124.20 42.00, -120.01 41.99, -121.1 42.01, -124.20 42.00))'
    )
  ) AS pipeline_dimension;

┌────────────────────┐
│ pipeline_dimension │
├────────────────────┤
│                  2 │
└────────────────────┘
```
