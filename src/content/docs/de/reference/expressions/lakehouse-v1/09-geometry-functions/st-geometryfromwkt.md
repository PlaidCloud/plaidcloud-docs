---
title: ST_GEOMETRYFROMWKT (Lakehouse v1)
description: ST_GEOMETRYFROMWKT — analysiert eine Eingabe im Format WKT (Well-Known Text) oder EWKT (Extended Well-Known Text) und gibt einen Wert vom Typ GEOMETRY zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geometryfromwkt.md
---

Analysiert eine Eingabe im Format [WKT (Well-Known Text)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) oder [EWKT (Extended Well-Known Text)](https://postgis.net/docs/ST_GeomFromEWKT.html) und gibt einen Wert vom Typ GEOMETRY zurück.

## SQL-Syntax

```sql
ST_GEOMETRYFROMWKT(<string>, [<srid>])
```

## Aliase

- [ST_GEOMFROMWKT](../st-geomfromwkt)
- [ST_GEOMETRYFROMEWKT](../st-geometryfromewkt)
- [ST_GEOMFROMEWKT](../st-geomfromewkt)
- [ST_GEOMFROMTEXT](../st-geomfromtext)
- [ST_GEOMETRYFROMTEXT](../st-geometryfromtext)

## Argumente

| Argumente   | Beschreibung                                                             |
|-------------|--------------------------------------------------------------------------|
| `<string>`  | Das Argument muss ein Zeichenfolgenausdruck im Format WKT oder EWKT sein. |
| `<srid>`    | Der ganzzahlige Wert der zu verwendenden SRID.                           |

## Rückgabetyp

Geometry.

## SQL-Beispiele

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
