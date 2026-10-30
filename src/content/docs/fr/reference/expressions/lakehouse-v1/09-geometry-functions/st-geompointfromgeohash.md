---
title: ST_GEOMPOINTFROMGEOHASH (Lakehouse v1)
description: ST_GEOMPOINTFROMGEOHASH — renvoie un objet GEOMETRY pour le point qui représente le centre d'un geohash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geompointfromgeohash.md
---

Renvoie un objet GEOMETRY pour le point qui représente le centre d'un [geohash](https://en.wikipedia.org/wiki/Geohash).

## Syntaxe SQL

```sql
ST_GEOMPOINTFROMGEOHASH(<geohash>)
```

## Arguments

| Arguments   | Description                     |
|-------------|---------------------------------|
| `<geohash>` | L'argument doit être un geohash. |

## Type de retour

Geometry.

## Exemples SQL

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
