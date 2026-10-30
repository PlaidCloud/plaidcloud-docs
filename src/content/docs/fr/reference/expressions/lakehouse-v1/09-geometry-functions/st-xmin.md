---
title: ST_XMIN (Lakehouse v1)
description: ST_XMIN — renvoie la longitude minimale (coordonnée X) de tous les points contenus dans l'objet GEOMETRY indiqué.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-xmin.md
---

Renvoie la longitude minimale (coordonnée X) de tous les points contenus dans l'objet GEOMETRY indiqué.

## Syntaxe SQL

```sql
ST_XMIN(<geometry>)
```

## Arguments

| Arguments    | Description                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | L'argument doit être une expression de type GEOMETRY. |

## Type de retour

Double.

## Exemples SQL

```sql
SELECT
  ST_XMIN(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(180 10),LINESTRING(20 10,30 20,40 40),POINT EMPTY)'
    )
  ) AS pipeline_xmin;

┌───────────────┐
│ pipeline_xmin │
├───────────────┤
│            20 │
└───────────────┘

SELECT
  ST_XMIN(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(40 10),LINESTRING(20 10,30 20,10 40),POLYGON((40 40,20 45,45 30,40 40)))'
    )
  ) AS pipeline_xmin;

┌───────────────┐
│ pipeline_xmin │
├───────────────┤
│            10 │
└───────────────┘
```
