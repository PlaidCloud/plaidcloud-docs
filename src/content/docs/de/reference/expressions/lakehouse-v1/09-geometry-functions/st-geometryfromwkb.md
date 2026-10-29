---
title: ST_GEOMETRYFROMWKB (Lakehouse v1)
description: ST_GEOMETRYFROMWKB — analysiert eine Eingabe im Format WKB (Well-Known Binary) oder EWKB (Extended Well-Known Binary).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkb.md
---

Analysiert eine Eingabe im Format [WKB (Well-Known Binary)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) oder [EWKB (Extended Well-Known Binary)](https://postgis.net/docs/ST_GeomFromEWKB.html) und gibt einen Wert vom Typ GEOMETRY zurück.

## SQL-Syntax

```sql
ST_GEOMETRYFROMWKB(<string>, [<srid>])
ST_GEOMETRYFROMWKB(<binary>, [<srid>])
```

## Aliase

- [ST_GEOMFROMWKB](../st-geomfromwkb)
- [ST_GEOMETRYFROMEWKB](../st-geometryfromewkb)
- [ST_GEOMFROMEWKB](../st-geomfromewkb)

## Argumente

| Argumente   | Beschreibung                                                                                    |
|-------------|-------------------------------------------------------------------------------------------------|
| `<string>`  | Das Argument muss ein Zeichenfolgenausdruck in WKB oder EWKB im Hexadezimalformat sein.         |
| `<binary>`  | Das Argument muss ein Binärausdruck im Format WKB oder EWKB sein.                               |
| `<srid>`    | Der ganzzahlige Wert der zu verwendenden SRID.                                                  |

## Rückgabetyp

Geometry.

## SQL-Beispiele

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
