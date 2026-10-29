---
title: ST_GEOMFROMGEOHASH (Lakehouse v1)
description: ST_GEOMFROMGEOHASH — retorna um objeto GEOMETRY com o polígono que representa os limites.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geomfromgeohash.md
---

Retorna um objeto GEOMETRY com o polígono que representa os limites de um [geohash](https://en.wikipedia.org/wiki/Geohash).

## SQL Syntax

```sql
ST_GEOMFROMGEOHASH(<geohash>)
```

## Arguments

| Argumentos   | Descrição                       |
|-------------|---------------------------------|
| `<geohash>` | O argumento deve ser um geohash. |

## Return Type

Geometry.

## SQL Examples

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
