---
title: ST_ENDPOINT (Lakehouse v1)
description: ST_ENDPOINT — renvoie le dernier Point d'un LineString.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-endpoint.md
---

Renvoie le dernier Point d'un LineString.

## Syntaxe SQL

```sql
ST_ENDPOINT(<geometry>)
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
  ST_ENDPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(4 4)        │
└───────────────────┘
```
