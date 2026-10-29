---
title: ST_Y (Lakehouse v1)
description: ST_Y — renvoie la latitude (coordonnée Y) d'un Point représenté par un objet GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-y.md
---

Renvoie la latitude (coordonnée Y) d'un Point représenté par un objet GEOMETRY.

## Syntaxe SQL

```sql
ST_Y(<geometry>)
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
  ST_Y(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_y;

┌────────────┐
│ pipeline_y │
├────────────┤
│       45.5 │
└────────────┘
```
