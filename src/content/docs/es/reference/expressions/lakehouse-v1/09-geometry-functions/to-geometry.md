---
title: TO_GEOMETRY (Lakehouse v1)
description: TO_GEOMETRY — analiza una entrada y devuelve un valor de tipo GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/to-geometry.md
---

Analiza una entrada y devuelve un valor de tipo GEOMETRY.

`TRY_TO_GEOMETRY` devuelve un valor NULL si se produce un error durante el análisis.

## Sintaxis de SQL

```sql
TO_GEOMETRY(<string>, [<srid>])
TO_GEOMETRY(<binary>, [<srid>])
TO_GEOMETRY(<variant>, [<srid>])
TRY_TO_GEOMETRY(<string>, [<srid>])
TRY_TO_GEOMETRY(<binary>, [<srid>])
TRY_TO_GEOMETRY(<variant>, [<srid>])
```

## Argumentos

| Argumentos  | Descripción                                                                                               |
|-------------|-----------------------------------------------------------------------------------------------------------|
| `<string>`  | El argumento debe ser una expresión de cadena en WKT, EWKT, WKB o EWKB en formato hexadecimal, o en formato GeoJSON. |
| `<binary>`  | El argumento debe ser una expresión binaria en formato WKB o EWKB.                                           |
| `<variant>` | El argumento debe ser un OBJECT JSON en formato GeoJSON.                                                     |
| `<srid>`    | El valor entero del SRID que se va a usar.                                                                     |

## Tipo de valor devuelto

Geometría.

## Ejemplos de SQL

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
