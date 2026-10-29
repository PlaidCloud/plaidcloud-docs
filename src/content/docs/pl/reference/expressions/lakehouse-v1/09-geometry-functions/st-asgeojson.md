---
title: ST_ASGEOJSON (Lakehouse v1)
description: ST_ASGEOJSON — konwertuje obiekt GEOMETRY na reprezentację GeoJSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-asgeojson.md
---

Konwertuje obiekt GEOMETRY na reprezentację [GeoJSON](https://geojson.org/).

## Składnia SQL

```sql
ST_ASGEOJSON(<geometry>)
```

## Argumenty

| Argumenty    | Opis                                                 |
|--------------|------------------------------------------------------|
| `<geometry>` | Argument musi być wyrażeniem typu GEOMETRY. |

## Typ zwracany

Variant.

## Przykłady SQL

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
