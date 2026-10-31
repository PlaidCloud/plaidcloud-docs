---
title: ST_GEOMETRYFROMWKB (Lakehouse v1)
description: ST_GEOMETRYFROMWKB — analyse une entrée WKB (well-known binary) ou EWKB (extended well-known binary).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkb.md
---

Analyse une entrée [WKB (well-known binary)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) ou [EWKB (extended well-known binary)](https://postgis.net/docs/ST_GeomFromEWKB.html) et renvoie une valeur de type GEOMETRY.

## Syntaxe SQL

```sql
ST_GEOMETRYFROMWKB(<string>, [<srid>])
ST_GEOMETRYFROMWKB(<binary>, [<srid>])
```

## Alias

- [ST_GEOMFROMWKB](../st-geomfromwkb)
- [ST_GEOMETRYFROMEWKB](../st-geometryfromewkb)
- [ST_GEOMFROMEWKB](../st-geomfromewkb)

## Arguments

| Arguments   | Description                                                                    |
|-------------|--------------------------------------------------------------------------------|
| `<string>`  | L'argument doit être une expression de chaîne en WKB ou EWKB au format hexadécimal. |
| `<binary>`  | L'argument doit être une expression binaire au format WKB ou EWKB.             |
| `<srid>`    | La valeur entière du SRID à utiliser.                                          |

## Type de retour

Geometry.

## Exemples SQL

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
