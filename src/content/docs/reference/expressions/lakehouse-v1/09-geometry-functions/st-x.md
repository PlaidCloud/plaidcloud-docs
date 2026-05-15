---
title: ST_X
description: ST_X — returns the longitude (X coordinate) of a Point represented by a GEOMETRY object.
---

Returns the longitude (X coordinate) of a Point represented by a GEOMETRY object.

## SQL Syntax

```sql
ST_X(<geometry>)
```

## Arguments

| Arguments    | Description                                                                   |
|--------------|-------------------------------------------------------------------------------|
| `<geometry>` | The argument must be an expression of type GEOMETRY and must contain a Point. |

## Return Type

Double.

## SQL Examples

```sql
SELECT
  ST_X(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_x;

┌────────────┐
│ pipeline_x │
├────────────┤
│       37.5 │
└────────────┘
```
