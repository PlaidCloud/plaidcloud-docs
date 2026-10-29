---
title: ST_GEOMETRYFROMWKB (Lakehouse v1)
description: ST_GEOMETRYFROMWKB — analizuje dane wejściowe w formacie WKB (well-known binary) lub EWKB (rozszerzony well-known binary).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkb.md
---

Analizuje dane wejściowe w formacie [WKB (well-known binary)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) lub [EWKB (rozszerzony well-known binary)](https://postgis.net/docs/ST_GeomFromEWKB.html) i zwraca wartość typu GEOMETRY.

## Składnia SQL

```sql
ST_GEOMETRYFROMWKB(<string>, [<srid>])
ST_GEOMETRYFROMWKB(<binary>, [<srid>])
```

## Aliasy

- [ST_GEOMFROMWKB](../st-geomfromwkb)
- [ST_GEOMETRYFROMEWKB](../st-geometryfromewkb)
- [ST_GEOMFROMEWKB](../st-geomfromewkb)

## Argumenty

| Argumenty   | Opis                                                                           |
|-------------|--------------------------------------------------------------------------------|
| `<string>`  | Argument musi być wyrażeniem tekstowym w formacie WKB lub EWKB w zapisie szesnastkowym. |
| `<binary>`  | Argument musi być wyrażeniem binarnym w formacie WKB lub EWKB.                 |
| `<srid>`    | Wartość całkowita identyfikatora SRID, który ma zostać użyty.                  |

## Typ zwracany

Geometry.

## Przykłady SQL

```sql
SELECT
  ST_GEOMETRYFROMWKB(
    '0101000020797f000066666666a9cb17411f85ebc19e325641'
  ) AS pipeline_geometry;

┌────────────────────────────────────────┐
│            pipeline_geometry           │
├────────────────────────────────────────┤
│ SRID=32633;POINT(389866.35 5819003.03) │
└────────────────────────────────────────┘

SELECT
  ST_GEOMETRYFROMWKB(
    FROM_HEX('0101000020797f000066666666a9cb17411f85ebc19e325641'), 4326
  ) AS pipeline_geometry;

┌───────────────────────────────────────┐
│           pipeline_geometry           │
├───────────────────────────────────────┤
│ SRID=4326;POINT(389866.35 5819003.03) │
└───────────────────────────────────────┘
```
