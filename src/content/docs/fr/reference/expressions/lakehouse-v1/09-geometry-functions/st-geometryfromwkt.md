---
title: ST_GEOMETRYFROMWKT (Lakehouse v1)
description: ST_GEOMETRYFROMWKT — analyse une entrée WKT (well-known text) ou EWKT (extended well-known text) et renvoie une valeur de type GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkt.md
---

Analyse une entrée [WKT (well-known text)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) ou [EWKT (extended well-known text)](https://postgis.net/docs/ST_GeomFromEWKT.html) et renvoie une valeur de type GEOMETRY.

## Syntaxe SQL

```sql
ST_GEOMETRYFROMWKT(<string>, [<srid>])
```

## Alias

- [ST_GEOMFROMWKT](../st-geomfromwkt)
- [ST_GEOMETRYFROMEWKT](../st-geometryfromewkt)
- [ST_GEOMFROMEWKT](../st-geomfromewkt)
- [ST_GEOMFROMTEXT](../st-geomfromtext)
- [ST_GEOMETRYFROMTEXT](../st-geometryfromtext)

## Arguments

| Arguments   | Description                                                     |
|-------------|-----------------------------------------------------------------|
| `<string>`  | L'argument doit être une expression de chaîne au format WKT ou EWKT. |
| `<srid>`    | La valeur entière du SRID à utiliser.                           |

## Type de retour

Geometry.

## Exemples SQL

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
