---
title: "TO_STRING (Geometry, Lakehouse v1)"
description: TO_STRING — konwertuje obiekt GEOMETRY na reprezentację tekstową.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/to-string.md
---

Konwertuje obiekt GEOMETRY na reprezentację tekstową. Format wyświetlania danych wyjściowych jest kontrolowany przez ustawienie `geometry_output_format`, które może przyjmować następujące wartości:

| Parametr          | Opis                                                                |
|-------------------|---------------------------------------------------------------------|
| GeoJSON (default) | Wynik GEOMETRY jest renderowany jako obiekt JSON w formacie GeoJSON. |
| WKT               | Wynik GEOMETRY jest renderowany jako ciąg znaków (String) w formacie WKT. |
| WKB               | Wynik GEOMETRY jest renderowany jako dane binarne (Binary) w formacie WKB. |
| EWKT              | Wynik GEOMETRY jest renderowany jako ciąg znaków (String) w formacie EWKT. |
| EWKB              | Wynik GEOMETRY jest renderowany jako dane binarne (Binary) w formacie EWKB. |

## Składnia SQL

```sql
TO_STRING(<geometry>)
```

## Argumenty

| Argumenty    | Opis                                                 |
|--------------|------------------------------------------------------|
| `<geometry>` | Argument musi być wyrażeniem typu GEOMETRY. |

## Typ zwracany

String.

## Przykłady SQL

```sql
SET geometry_output_format='GeoJSON';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌────────────────────────────────────────────────────────────────────────────┐
│                              pipeline_geometry                             │
├────────────────────────────────────────────────────────────────────────────┤
│ {"type": "LineString", "coordinates": [[400000,6000000],[401000,6010000]]} │
└────────────────────────────────────────────────────────────────────────────┘

SET geometry_output_format='WKT';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌───────────────────────────────────────────┐
│             pipeline_geometry             │
├───────────────────────────────────────────┤
│ LINESTRING(400000 6000000,401000 6010000) │
└───────────────────────────────────────────┘

SET geometry_output_format='EWKT';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌─────────────────────────────────────────────────────┐
│                  pipeline_geometry                  │
├─────────────────────────────────────────────────────┤
│ SRID=4326;LINESTRING(400000 6000000,401000 6010000) │
└─────────────────────────────────────────────────────┘

SET geometry_output_format='WKB';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌────────────────────────────────────────────────────────────────────────────────────┐
│                                  pipeline_geometry                                 │
├────────────────────────────────────────────────────────────────────────────────────┤
│ 01020000000200000000000000006A18410000000060E3564100000000A07918410000000024ED5641 │
└────────────────────────────────────────────────────────────────────────────────────┘

SET geometry_output_format='EWKB';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌────────────────────────────────────────────────────────────────────────────────────────────┐
│                                      pipeline_geometry                                     │
├────────────────────────────────────────────────────────────────────────────────────────────┤
│ 0102000020E61000000200000000000000006A18410000000060E3564100000000A07918410000000024ED5641 │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```
