---
title: ST_GEOMPOINTFROMGEOHASH (Lakehouse v1)
description: ST_GEOMPOINTFROMGEOHASH — gibt ein GEOMETRY-Objekt für den Punkt zurück, der die Mitte eines Geohash darstellt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geompointfromgeohash.md
---

Gibt ein GEOMETRY-Objekt für den Punkt zurück, der die Mitte eines [Geohash](https://en.wikipedia.org/wiki/Geohash) darstellt.

## SQL-Syntax

```sql
ST_GEOMPOINTFROMGEOHASH(<geohash>)
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
