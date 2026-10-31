---
title: ST_GEOMETRYFROMWKB (Lakehouse v1)
description: ST_GEOMETRYFROMWKB — analisa uma entrada WKB (well-known-binary) ou EWKB (extended well-known-binary).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkb.md
---

Analisa uma entrada [WKB (well-known-binary)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) ou [EWKB (extended well-known-binary)](https://postgis.net/docs/ST_GeomFromEWKB.html) e devolve um valor do tipo GEOMETRY.

## Sintaxe SQL

```sql
ST_GEOMETRYFROMWKB(<string>, [<srid>])
ST_GEOMETRYFROMWKB(<binary>, [<srid>])
```

## Aliases

- [ST_GEOMFROMWKB](../st-geomfromwkb)
- [ST_GEOMETRYFROMEWKB](../st-geometryfromewkb)
- [ST_GEOMFROMEWKB](../st-geomfromewkb)

## Argumentos

| Argumentos  | Descrição                                                                      |
|-------------|--------------------------------------------------------------------------------|
| `<string>`  | O argumento tem de ser uma expressão de cadeia de caracteres em WKB ou EWKB em formato hexadecimal. |
| `<binary>`  | O argumento tem de ser uma expressão binária em formato WKB ou EWKB.           |
| `<srid>`    | O valor inteiro do SRID a utilizar.                                            |

## Tipo de retorno

Geometry.

## Exemplos de SQL

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
