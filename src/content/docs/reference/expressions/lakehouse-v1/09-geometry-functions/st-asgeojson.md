---
title: ST_ASGEOJSON
description: "Learn how to use the ST_ASGEOJSON geometry function in PlaidCloud Lakehouse. Converts a GEOMETRY object into a GeoJSON representation. With syntax and examples."
---

Converts a GEOMETRY object into a [GeoJSON](https://geojson.org/) representation.

## SQL Syntax

```sql
ST_ASGEOJSON(<geometry>)
```

## Arguments

| Arguments    | Description                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | The argument must be an expression of type GEOMETRY. |

## Return Type

Variant.

## SQL Examples

```sql
SELECT
  ST_ASGEOJSON(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geojson;

┌─────────────────────────────────────────────────────────────────────────┐
│                             pipeline_geojson                            │
├─────────────────────────────────────────────────────────────────────────┤
│ {"coordinates":[[400000,6000000],[401000,6010000]],"type":"LineString"} │
└─────────────────────────────────────────────────────────────────────────┘
```
