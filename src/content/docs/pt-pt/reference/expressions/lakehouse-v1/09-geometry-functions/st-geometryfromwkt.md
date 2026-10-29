---
title: ST_GEOMETRYFROMWKT (Lakehouse v1)
description: ST_GEOMETRYFROMWKT — analisa uma entrada WKT (well-known-text) ou EWKT (extended well-known-text) e devolve um valor do tipo GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkt.md
---

Analisa uma entrada [WKT (well-known-text)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) ou [EWKT (extended well-known-text)](https://postgis.net/docs/ST_GeomFromEWKT.html) e devolve um valor do tipo GEOMETRY.

## Sintaxe SQL

```sql
ST_GEOMETRYFROMWKT(<string>, [<srid>])
```

## Aliases

- [ST_GEOMFROMWKT](../st-geomfromwkt)
- [ST_GEOMETRYFROMEWKT](../st-geometryfromewkt)
- [ST_GEOMFROMEWKT](../st-geomfromewkt)
- [ST_GEOMFROMTEXT](../st-geomfromtext)
- [ST_GEOMETRYFROMTEXT](../st-geometryfromtext)

## Argumentos

| Argumentos  | Descrição                                                       |
|-------------|-----------------------------------------------------------------|
| `<string>`  | O argumento tem de ser uma expressão de cadeia de caracteres em formato WKT ou EWKT. |
| `<srid>`    | O valor inteiro do SRID a utilizar.                             |

## Tipo de retorno

Geometry.

## Exemplos de SQL

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
