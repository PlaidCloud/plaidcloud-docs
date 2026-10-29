---
title: ST_XMAX (Lakehouse v1)
description: ST_XMAX — renvoie la longitude maximale (coordonnée X) de tous les points contenus dans l'objet GEOMETRY indiqué.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-xmax.md
---

Renvoie la longitude maximale (coordonnée X) de tous les points contenus dans l'objet GEOMETRY indiqué.

## Syntaxe SQL

```sql
ST_XMAX(<geometry>)
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
  ST_XMAX(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(40 10),LINESTRING(10 10,20 20,10 40),POINT EMPTY)'
    )
  ) AS pipeline_xmax;

┌───────────────┐
│ pipeline_xmax │
├───────────────┤
│            40 │
└───────────────┘

SELECT
  ST_XMAX(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(40 10),LINESTRING(10 10,20 20,10 40),POLYGON((40 40,20 45,45 30,40 40)))'
    )
  ) AS pipeline_xmax;

┌───────────────┐
│ pipeline_xmax │
├───────────────┤
│            45 │
└───────────────┘
```
