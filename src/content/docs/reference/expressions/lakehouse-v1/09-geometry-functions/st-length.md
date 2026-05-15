---
title: ST_LENGTH (Lakehouse v1)
description: ST_LENGTH — returns the Euclidean length of the LineString(s) in a GEOMETRY object.
---

Returns the Euclidean length of the LineString(s) in a GEOMETRY object.

## SQL Syntax

```sql
ST_LENGTH(<geometry>)
```

## Arguments

| Arguments    | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `<geometry>` | The argument must be an expression of type GEOMETRY containing linestrings. |

:::note
- If `<geometry>` is not a `LineString`, `MultiLineString`, or `GeometryCollection` containing linestrings, returns 0.
- If `<geometry>` is a `GeometryCollection`, returns the sum of the lengths of the linestrings in the collection.
:::

## Return Type

Double.

## SQL Examples

```sql
SELECT
  ST_LENGTH(TO_GEOMETRY('POINT(1 1)')) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘

SELECT
  ST_LENGTH(TO_GEOMETRY('LINESTRING(0 0, 1 1)')) AS length

┌─────────────┐
│    length   │
├─────────────┤
│ 1.414213562 │
└─────────────┘

SELECT
  ST_LENGTH(
    TO_GEOMETRY('POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))')
  ) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘
```
