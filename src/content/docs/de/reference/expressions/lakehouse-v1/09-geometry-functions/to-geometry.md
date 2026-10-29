---
title: TO_GEOMETRY (Lakehouse v1)
description: TO_GEOMETRY — analysiert eine Eingabe und gibt einen Wert vom Typ GEOMETRY zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/to-geometry.md
---

Analysiert eine Eingabe und gibt einen Wert vom Typ GEOMETRY zurück.

`TRY_TO_GEOMETRY` gibt einen NULL-Wert zurück, wenn beim Analysieren ein Fehler auftritt.

## SQL-Syntax

```sql
TO_GEOMETRY(<string>, [<srid>])
TO_GEOMETRY(<binary>, [<srid>])
TO_GEOMETRY(<variant>, [<srid>])
TRY_TO_GEOMETRY(<string>, [<srid>])
TRY_TO_GEOMETRY(<binary>, [<srid>])
TRY_TO_GEOMETRY(<variant>, [<srid>])
```

## Argumente

| Argumente   | Beschreibung                                                                                                                  |
|-------------|-------------------------------------------------------------------------------------------------------------------------------|
| `<string>`  | Das Argument muss ein Zeichenfolgenausdruck in WKT, EWKT, WKB oder EWKB im Hexadezimalformat oder im GeoJSON-Format sein.      |
| `<binary>`  | Das Argument muss ein Binärausdruck im Format WKB oder EWKB sein.                                                             |
| `<variant>` | Das Argument muss ein JSON-OBJECT im GeoJSON-Format sein.                                                                     |
| `<srid>`    | Der ganzzahlige Wert der zu verwendenden SRID.                                                                                |

## Rückgabetyp

Geometry.

## SQL-Beispiele

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
