---
title: ST_GEOMETRYFROMWKB (Lakehouse v1)
description: ST_GEOMETRYFROMWKB — analiza una entrada WKB (binario conocido) o EWKB (binario conocido extendido).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkb.md
---

Analiza una entrada [WKB (binario conocido)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) o [EWKB (binario conocido extendido)](https://postgis.net/docs/ST_GeomFromEWKB.html) y devuelve un valor de tipo GEOMETRY.

## Sintaxis de SQL

```sql
ST_GEOMETRYFROMWKB(<string>, [<srid>])
ST_GEOMETRYFROMWKB(<binary>, [<srid>])
```

## Alias

- [ST_GEOMFROMWKB](../st-geomfromwkb)
- [ST_GEOMETRYFROMEWKB](../st-geometryfromewkb)
- [ST_GEOMFROMEWKB](../st-geomfromewkb)

## Argumentos

| Argumentos  | Descripción                                                                    |
|-------------|--------------------------------------------------------------------------------|
| `<string>`  | El argumento debe ser una expresión de cadena en WKB o EWKB en formato hexadecimal. |
| `<binary>`  | El argumento debe ser una expresión binaria en formato WKB o EWKB.                |
| `<srid>`    | El valor entero del SRID que se va a usar.                                          |

## Tipo de valor devuelto

Geometría.

## Ejemplos de SQL

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
