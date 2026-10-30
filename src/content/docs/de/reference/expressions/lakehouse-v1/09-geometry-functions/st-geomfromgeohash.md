---
title: ST_GEOMFROMGEOHASH (Lakehouse v1)
description: ST_GEOMFROMGEOHASH — gibt ein GEOMETRY-Objekt für das Polygon zurück, das die Grenzen eines Geohash darstellt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geomfromgeohash.md
---

Gibt ein GEOMETRY-Objekt für das Polygon zurück, das die Grenzen eines [Geohash](https://en.wikipedia.org/wiki/Geohash) darstellt.

## SQL-Syntax

```sql
ST_GEOMFROMGEOHASH(<geohash>)
```

## Argumente

| Argumente   | Beschreibung                         |
|-------------|--------------------------------------|
| `<geohash>` | Das Argument muss ein Geohash sein.  |

## Rückgabetyp

Geometry.

## SQL-Beispiele

```sql
SELECT
  ST_GEOMFROMGEOHASH(
    '9q60y60rhs'
  ) AS pipeline_geometry;

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                     st_geomfromgeohash('9q60y60rhs')                                                                                     │
├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ POLYGON((-120.66230535507202 35.30029535293579,-120.66230535507202 35.30030071735382,-120.66229462623596 35.30030071735382,-120.66229462623596 35.30029535293579,-120.66230535507202 35.30029535293579)) │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
