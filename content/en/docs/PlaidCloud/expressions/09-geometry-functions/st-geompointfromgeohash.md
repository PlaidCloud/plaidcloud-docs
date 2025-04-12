---
title: ST_GEOMPOINTFROMGEOHASH
---

Returns a GEOMETRY object for the point that represents center of a [geohash](https://en.wikipedia.org/wiki/Geohash).

## SQL Syntax

```sql
ST_GEOMPOINTFROMGEOHASH(<geohash>)
```

## Arguments

| Arguments   | Description                     |
|-------------|---------------------------------|
| `<geohash>` | The argument must be a geohash. |

## Return Type

Geometry.

## SQL Examples

```sql
SELECT
  ST_GEOMPOINTFROMGEOHASH(
    's02equ0'
  ) AS pipeline_geometry;

┌──────────────────────────────────────────────┐
│               pipeline_geometry              │
│                   Geometry                   │
├──────────────────────────────────────────────┤
│ POINT(1.0004425048828125 2.0001983642578125) │
└──────────────────────────────────────────────┘
```
