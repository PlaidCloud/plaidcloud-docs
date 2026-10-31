---
title: ST_GEOMPOINTFROMGEOHASH (Lakehouse v1)
description: ST_GEOMPOINTFROMGEOHASH — devuelve un objeto GEOMETRY para el punto que representa el centro de un geohash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geompointfromgeohash.md
---

Devuelve un objeto GEOMETRY para el punto que representa el centro de un [geohash](https://en.wikipedia.org/wiki/Geohash).

## Sintaxis de SQL

```sql
ST_GEOMPOINTFROMGEOHASH(<geohash>)
```

## Argumentos

| Argumentos  | Descripción                     |
|-------------|---------------------------------|
| `<geohash>` | El argumento debe ser un geohash. |

## Tipo de valor devuelto

Geometría.

## Ejemplos de SQL

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
