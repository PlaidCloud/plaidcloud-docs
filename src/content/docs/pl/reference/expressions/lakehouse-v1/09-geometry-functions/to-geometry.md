---
title: TO_GEOMETRY (Lakehouse v1)
description: TO_GEOMETRY — analizuje dane wejściowe i zwraca wartość typu GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/to-geometry.md
---

Analizuje dane wejściowe i zwraca wartość typu GEOMETRY.

`TRY_TO_GEOMETRY` zwraca wartość NULL, jeśli podczas analizy wystąpi błąd.

## Składnia SQL

```sql
TO_GEOMETRY(<string>, [<srid>])
TO_GEOMETRY(<binary>, [<srid>])
TO_GEOMETRY(<variant>, [<srid>])
TRY_TO_GEOMETRY(<string>, [<srid>])
TRY_TO_GEOMETRY(<binary>, [<srid>])
TRY_TO_GEOMETRY(<variant>, [<srid>])
```

## Argumenty

| Argumenty   | Opis                                                                                                      |
|-------------|-----------------------------------------------------------------------------------------------------------|
| `<string>`  | Argument musi być wyrażeniem tekstowym w formacie WKT, EWKT, WKB lub EWKB w zapisie szesnastkowym albo w formacie GeoJSON. |
| `<binary>`  | Argument musi być wyrażeniem binarnym w formacie WKB lub EWKB.                                            |
| `<variant>` | Argument musi być obiektem JSON OBJECT w formacie GeoJSON.                                                |
| `<srid>`    | Wartość całkowita identyfikatora SRID, który ma zostać użyty.                                             |

## Typ zwracany

Geometry.

## Przykłady SQL

```sql
SELECT
  TO_GEOMETRY(
    'POINT(1820.12 890.56)'
  ) AS pipeline_geometry;

┌───────────────────────┐
│   pipeline_geometry   │
├───────────────────────┤
│ POINT(1820.12 890.56) │
└───────────────────────┘

SELECT
  TO_GEOMETRY(
    '0101000020797f000066666666a9cb17411f85ebc19e325641', 4326
  ) AS pipeline_geometry;

┌───────────────────────────────────────┐
│           pipeline_geometry           │
├───────────────────────────────────────┤
│ SRID=4326;POINT(389866.35 5819003.03) │
└───────────────────────────────────────┘

SELECT
  TO_GEOMETRY(
    FROM_HEX('0101000020797f000066666666a9cb17411f85ebc19e325641'), 4326
  ) AS pipeline_geometry;

┌───────────────────────────────────────┐
│           pipeline_geometry           │
├───────────────────────────────────────┤
│ SRID=4326;POINT(389866.35 5819003.03) │
└───────────────────────────────────────┘

SELECT
  TO_GEOMETRY(
    '{"coordinates":[[389866,5819003],[390000,5830000]],"type":"LineString"}'
  ) AS pipeline_geometry;

┌───────────────────────────────────────────┐
│             pipeline_geometry             │
├───────────────────────────────────────────┤
│ LINESTRING(389866 5819003,390000 5830000) │
└───────────────────────────────────────────┘

SELECT
  TO_GEOMETRY(
    PARSE_JSON('{"coordinates":[[389866,5819003],[390000,5830000]],"type":"LineString"}')
  ) AS pipeline_geometry;

┌───────────────────────────────────────────┐
│             pipeline_geometry             │
├───────────────────────────────────────────┤
│ LINESTRING(389866 5819003,390000 5830000) │
└───────────────────────────────────────────┘
```
