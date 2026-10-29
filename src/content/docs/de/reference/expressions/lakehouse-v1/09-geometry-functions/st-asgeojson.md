---
title: ST_ASGEOJSON (Lakehouse v1)
description: ST_ASGEOJSON — wandelt ein GEOMETRY-Objekt in eine GeoJSON-Darstellung um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-asgeojson.md
---

Wandelt ein GEOMETRY-Objekt in eine [GeoJSON](https://geojson.org/)-Darstellung um.

## SQL-Syntax

```sql
ST_ASGEOJSON(<geometry>)
```

## Argumente

| Argumente    | Beschreibung                                          |
|--------------|-------------------------------------------------------|
| `<geometry>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein. |

## Rückgabetyp

Variant.

## SQL-Beispiele

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
