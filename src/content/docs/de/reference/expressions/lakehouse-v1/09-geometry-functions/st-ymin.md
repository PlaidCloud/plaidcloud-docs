---
title: ST_YMIN (Lakehouse v1)
description: ST_YMIN — gibt den minimalen Breitengrad (Y-Koordinate) aller im angegebenen GEOMETRY-Objekt enthaltenen Punkte zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-ymin.md
---

Gibt den minimalen Breitengrad (Y-Koordinate) aller im angegebenen GEOMETRY-Objekt enthaltenen Punkte zurück.

## SQL-Syntax

```sql
ST_YMIN(<geometry>)
```

## Argumente

| Argumente    | Beschreibung                                          |
|--------------|-------------------------------------------------------|
| `<geometry>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein. |

## Rückgabetyp

Double.

## SQL-Beispiele

```sql
SELECT
  ST_YMIN(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(-180 -10),LINESTRING(-179 0, 179 30),POINT EMPTY)'
    )
  ) AS pipeline_ymin;

┌───────────────┐
│ pipeline_ymin │
├───────────────┤
│           -10 │
└───────────────┘

SELECT
  ST_YMIN(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(180 0),LINESTRING(-60 -30, 60 30),POLYGON((40 40,20 45,45 30,40 40)))'
    )
  ) AS pipeline_ymin;

┌───────────────┐
│ pipeline_ymin │
├───────────────┤
│           -30 │
└───────────────┘
```
