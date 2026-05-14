---
title: ST_POINTN
description: "Learn how to use the ST_POINTN geometry function in PlaidCloud Lakehouse. Returns a Point at a specified index in a LineString. Includes syntax and examples."
---

Returns a Point at a specified index in a LineString.

## SQL Syntax

```sql
ST_POINTN(<geometry>, <index>)
```

## Arguments

| Arguments    | Description                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | The argument must be an expression of type GEOMETRY that represents a LineString. |
| `<index>`    | The index of the Point to return.                                                 |

:::note
The index is 1-based, and a negative index is uesed as the offset from the end of LineString. If index is out of bounds, the function returns an error.
:::

## Return Type

Geometry.

## SQL Examples

```sql
SELECT
  ST_POINTN(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    ),
    1
  ) AS pipeline_pointn;

┌─────────────────┐
│ pipeline_pointn │
├─────────────────┤
│ POINT(1 1)      │
└─────────────────┘

SELECT
  ST_POINTN(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    ),
    -2
  ) AS pipeline_pointn;

┌─────────────────┐
│ pipeline_pointn │
├─────────────────┤
│ POINT(3 3)      │
└─────────────────┘
```
