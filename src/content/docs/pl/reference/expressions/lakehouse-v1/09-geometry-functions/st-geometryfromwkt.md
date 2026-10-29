---
title: ST_GEOMETRYFROMWKT (Lakehouse v1)
description: ST_GEOMETRYFROMWKT — analizuje dane wejściowe w formacie WKT (well-known text) lub EWKT (rozszerzony well-known text) i zwraca wartość typu GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkt.md
---

Analizuje dane wejściowe w formacie [WKT (well-known text)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) lub [EWKT (rozszerzony well-known text)](https://postgis.net/docs/ST_GeomFromEWKT.html) i zwraca wartość typu GEOMETRY.

## Składnia SQL

```sql
ST_GEOMETRYFROMWKT(<string>, [<srid>])
```

## Aliasy

- [ST_GEOMFROMWKT](../st-geomfromwkt)
- [ST_GEOMETRYFROMEWKT](../st-geometryfromewkt)
- [ST_GEOMFROMEWKT](../st-geomfromewkt)
- [ST_GEOMFROMTEXT](../st-geomfromtext)
- [ST_GEOMETRYFROMTEXT](../st-geometryfromtext)

## Argumenty

| Argumenty   | Opis                                                            |
|-------------|-----------------------------------------------------------------|
| `<string>`  | Argument musi być wyrażeniem tekstowym w formacie WKT lub EWKT. |
| `<srid>`    | Wartość całkowita identyfikatora SRID, który ma zostać użyty.   |

## Typ zwracany

Geometry.

## Przykłady SQL

```sql
SELECT
  ST_GEOMETRYFROMWKT(
    'POINT(1820.12 890.56)'
  ) AS pipeline_geometry;

┌───────────────────────┐
│   pipeline_geometry   │
├───────────────────────┤
│ POINT(1820.12 890.56) │
└───────────────────────┘

SELECT
  ST_GEOMETRYFROMWKT(
    'POINT(1820.12 890.56)', 4326
  ) AS pipeline_geometry;

┌─────────────────────────────────┐
│        pipeline_geometry        │
│             Geometry            │
├─────────────────────────────────┤
│ SRID=4326;POINT(1820.12 890.56) │
└─────────────────────────────────┘
```
