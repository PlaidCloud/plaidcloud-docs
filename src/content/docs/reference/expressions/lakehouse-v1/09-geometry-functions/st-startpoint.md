---
title: ST_STARTPOINT
description: "Learn how to use the ST_STARTPOINT geometry function in PlaidCloud Lakehouse. Returns the first Point in a LineString. Includes syntax and examples."
---

Returns the first Point in a LineString.

## SQL Syntax

```sql
ST_STARTPOINT(<geometry>)
```

## Arguments

| Arguments    | Description                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | The argument must be an expression of type GEOMETRY that represents a LineString. |

## Return Type

Geometry.

## SQL Examples

```sql
SELECT
  ST_STARTPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(1 1)        │
└───────────────────┘
```
