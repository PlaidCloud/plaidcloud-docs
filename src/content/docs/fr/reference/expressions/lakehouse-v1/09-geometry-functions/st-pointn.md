---
title: ST_POINTN (Lakehouse v1)
description: ST_POINTN — renvoie le Point situé à un index donné dans un LineString.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-pointn.md
---

Renvoie le Point situé à un index donné dans un LineString.

## Syntaxe SQL

```sql
ST_POINTN(<geometry>, <index>)
```

## Arguments

| Arguments    | Description                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | L'argument doit être une expression de type GEOMETRY qui représente un LineString. |
| `<index>`    | L'index du Point à renvoyer.                                                      |

:::note
L'index commence à 1, et un index négatif est utilisé comme décalage à partir de la fin du LineString. Si l'index est hors limites, la fonction renvoie une erreur.
:::

## Type de retour

Geometry.

## Exemples SQL

```sql
SELECT
  ST_POINTN(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    ),
    1
  ) AS pipeline_pointn;

┌─────────────────┐
│ pipeline_pointn │
├─────────────────┤
│ POINT(1 1)      │
└─────────────────┘

SELECT
  ST_POINTN(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    ),
    -2
  ) AS pipeline_pointn;

┌─────────────────┐
│ pipeline_pointn │
├─────────────────┤
│ POINT(3 3)      │
└─────────────────┘
```
