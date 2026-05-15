---
title: ST_Y (Lakehouse v1)
description: ST_Y — returns the latitude (Y coordinate) of a Point represented by a GEOMETRY object.
---

Returns the latitude (Y coordinate) of a Point represented by a GEOMETRY object.

## SQL Syntax

```sql
ST_Y(<geometry>)
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
  ST_Y(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_y;

┌────────────┐
│ pipeline_y │
├────────────┤
│       45.5 │
└────────────┘
```
