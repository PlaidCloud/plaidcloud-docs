---
title: ST_ASWKT (Lakehouse v1)
description: ST_ASWKT — converts a GEOMETRY object into a WKT(well-known-text) format representation.
---

Converts a GEOMETRY object into a [WKT(well-known-text)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) format representation.

## SQL Syntax

```sql
ST_ASWKT(<geometry>)
```

## Aliases

- [ST_ASTEXT](../st-astext)

## Arguments

| Arguments    | Description                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | The argument must be an expression of type GEOMETRY. |

## Return Type

String.

## SQL Examples

```sql
SELECT
  ST_ASWKT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_wkt;

┌───────────────────────────────────────────┐
│                pipeline_wkt               │
├───────────────────────────────────────────┤
│ LINESTRING(400000 6000000,401000 6010000) │
└───────────────────────────────────────────┘

SELECT
  ST_ASTEXT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    )
  ) AS pipeline_wkt;

┌──────────────────────┐
│     pipeline_wkt     │
├──────────────────────┤
│ POINT(-122.35 37.55) │
└──────────────────────┘
```
