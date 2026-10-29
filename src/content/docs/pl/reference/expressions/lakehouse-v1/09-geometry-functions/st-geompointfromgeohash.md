---
title: ST_GEOMPOINTFROMGEOHASH (Lakehouse v1)
description: ST_GEOMPOINTFROMGEOHASH — zwraca obiekt GEOMETRY dla punktu reprezentującego środek geohasha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geompointfromgeohash.md
---

Zwraca obiekt GEOMETRY dla punktu reprezentującego środek [geohasha](https://en.wikipedia.org/wiki/Geohash).

## Składnia SQL

```sql
ST_GEOMPOINTFROMGEOHASH(<geohash>)
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
