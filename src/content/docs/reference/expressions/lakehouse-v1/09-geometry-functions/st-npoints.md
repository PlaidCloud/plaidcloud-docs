---
title: ST_NPOINTS
description: "Learn how to use the ST_NPOINTS geometry function in PlaidCloud Lakehouse. Returns the number of points in a GEOMETRY object. Includes syntax and examples."
---

Returns the number of points in a GEOMETRY object.

## SQL Syntax

```sql
ST_NPOINTS(<geometry>)
```

## Aliases

- [ST_NUMPOINTS](../st-numpoints)

## Arguments

| Arguments    | Description                                                 |
|--------------|-------------------------------------------------------------|
| `<geometry>` | The argument must be an expression of type GEOMETRY object. |

## Return Type

UInt8.

## SQL Examples

```sql
SELECT ST_NPOINTS(TO_GEOMETRY('POINT(66 12)')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       1 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('MULTIPOINT((45 21),(12 54))')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       2 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('LINESTRING(40 60,50 50,60 40)')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       3 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('MULTILINESTRING((1 1,32 17),(33 12,73 49,87.1 6.1))')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       5 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('GEOMETRYCOLLECTION(POLYGON((-10 0,0 10,10 0,-10 0)),LINESTRING(40 60,50 50,60 40),POINT(99 11))')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       8 │
└─────────┘
```
