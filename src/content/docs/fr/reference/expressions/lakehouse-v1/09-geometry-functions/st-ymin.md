---
title: ST_YMIN (Lakehouse v1)
description: ST_YMIN — renvoie la latitude minimale (coordonnée Y) de tous les points contenus dans l'objet GEOMETRY indiqué.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-ymin.md
---

Renvoie la latitude minimale (coordonnée Y) de tous les points contenus dans l'objet GEOMETRY indiqué.

## Syntaxe SQL

```sql
ST_YMIN(<geometry>)
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
