---
title: ST_GEOMFROMGEOHASH (Lakehouse v1)
description: ST_GEOMFROMGEOHASH — zwraca obiekt GEOMETRY dla wielokąta reprezentującego granice geohasha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geomfromgeohash.md
---

Zwraca obiekt GEOMETRY dla wielokąta reprezentującego granice [geohasha](https://en.wikipedia.org/wiki/Geohash).

## Składnia SQL

```sql
ST_GEOMFROMGEOHASH(<geohash>)
```

## Argumenty

| Argumenty   | Opis                            |
|-------------|---------------------------------|
| `<geohash>` | Argument musi być geohashem.    |

## Typ zwracany

Geometry.

## Przykłady SQL

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
