---
title: ST_GEOMETRYFROMWKT (Lakehouse v1)
description: ST_GEOMETRYFROMWKT — analiza una entrada WKT (texto conocido) o EWKT (texto conocido extendido) y devuelve un valor de tipo GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkt.md
---

Analiza una entrada [WKT (texto conocido)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) o [EWKT (texto conocido extendido)](https://postgis.net/docs/ST_GeomFromEWKT.html) y devuelve un valor de tipo GEOMETRY.

## Sintaxis de SQL

```sql
ST_GEOMETRYFROMWKT(<string>, [<srid>])
```

## Alias

- [ST_GEOMFROMWKT](../st-geomfromwkt)
- [ST_GEOMETRYFROMEWKT](../st-geometryfromewkt)
- [ST_GEOMFROMEWKT](../st-geomfromewkt)
- [ST_GEOMFROMTEXT](../st-geomfromtext)
- [ST_GEOMETRYFROMTEXT](../st-geometryfromtext)

## Argumentos

| Argumentos  | Descripción                                                     |
|-------------|-----------------------------------------------------------------|
| `<string>`  | El argumento debe ser una expresión de cadena en formato WKT o EWKT. |
| `<srid>`    | El valor entero del SRID que se va a usar.                           |

## Tipo de valor devuelto

Geometría.

## Ejemplos de SQL

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
