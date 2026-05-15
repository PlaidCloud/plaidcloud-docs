---
title: ST_SRID (Lakehouse v1)
description: ST_SRID — returns the SRID (spatial reference system identifier) of a GEOMETRY object.
---

Returns the SRID (spatial reference system identifier) of a GEOMETRY object.

## SQL Syntax

```sql
ST_SRID(<geometry>)
```

## Arguments

| Arguments    | Description                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | The argument must be an expression of type GEOMETRY. |

## Return Type

INT32.

:::note
If the Geometry don't have a SRID, a default value 4326 will be returned.
:::

## SQL Examples

```sql
SELECT
  ST_SRID(
    TO_GEOMETRY(
      'POINT(-122.306100 37.554162)',
      1234
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          1234 │
└───────────────┘

SELECT
  ST_SRID(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          4326 │
└───────────────┘
```
