---
title: ST_STARTPOINT (Lakehouse v1)
description: ST_STARTPOINT — renvoie le premier Point d'un LineString.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-startpoint.md
---

Renvoie le premier Point d'un LineString.

## Syntaxe SQL

```sql
ST_STARTPOINT(<geometry>)
```

## Arguments

| Arguments    | Description                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | L'argument doit être une expression de type GEOMETRY qui représente un LineString. |

## Type de retour

Geometry.

## Exemples SQL

```sql
SELECT
  ST_STARTPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(1 1)        │
└───────────────────┘
```
