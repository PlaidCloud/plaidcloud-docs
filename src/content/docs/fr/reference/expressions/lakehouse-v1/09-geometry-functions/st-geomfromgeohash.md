---
title: ST_GEOMFROMGEOHASH (Lakehouse v1)
description: ST_GEOMFROMGEOHASH — renvoie un objet GEOMETRY pour le polygone qui représente les limites d'un geohash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geomfromgeohash.md
---

Renvoie un objet GEOMETRY pour le polygone qui représente les limites d'un [geohash](https://en.wikipedia.org/wiki/Geohash).

## Syntaxe SQL

```sql
ST_GEOMFROMGEOHASH(<geohash>)
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
  ST_GEOMFROMGEOHASH(
    '9q60y60rhs'
  ) AS pipeline_geometry;

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                     st_geomfromgeohash('9q60y60rhs')                                                                                     │
├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ POLYGON((-120.66230535507202 35.30029535293579,-120.66230535507202 35.30030071735382,-120.66229462623596 35.30030071735382,-120.66229462623596 35.30029535293579,-120.66230535507202 35.30029535293579)) │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
