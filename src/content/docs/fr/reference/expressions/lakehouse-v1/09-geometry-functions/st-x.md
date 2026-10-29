---
title: ST_X (Lakehouse v1)
description: ST_X — renvoie la longitude (coordonnée X) d'un Point représenté par un objet GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-x.md
---

Renvoie la longitude (coordonnée X) d'un Point représenté par un objet GEOMETRY.

## Syntaxe SQL

```sql
ST_X(<geometry>)
```

## Arguments

| Arguments    | Description                                                                   |
|--------------|-------------------------------------------------------------------------------|
| `<geometry>` | L'argument doit être une expression de type GEOMETRY et doit contenir un Point. |

## Type de retour

Double.

## Exemples SQL

```sql
SELECT
  ST_X(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_x;

┌────────────┐
│ pipeline_x │
├────────────┤
│       37.5 │
└────────────┘
```
