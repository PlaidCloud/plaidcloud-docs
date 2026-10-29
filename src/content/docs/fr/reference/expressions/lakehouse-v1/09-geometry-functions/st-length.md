---
title: ST_LENGTH (Lakehouse v1)
description: ST_LENGTH — renvoie la longueur euclidienne des LineString d'un objet GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-length.md
---

Renvoie la longueur euclidienne des LineString d'un objet GEOMETRY.

## Syntaxe SQL

```sql
ST_LENGTH(<geometry>)
```

## Arguments

| Arguments    | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `<geometry>` | L'argument doit être une expression de type GEOMETRY contenant des linestrings. |

:::note
- Si `<geometry>` n'est ni un `LineString`, ni un `MultiLineString`, ni une `GeometryCollection` contenant des linestrings, la fonction renvoie 0.
- Si `<geometry>` est une `GeometryCollection`, la fonction renvoie la somme des longueurs des linestrings de la collection.
:::

## Type de retour

Double.

## Exemples SQL

```sql
SELECT
  ST_LENGTH(TO_GEOMETRY('POINT(1 1)')) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘

SELECT
  ST_LENGTH(TO_GEOMETRY('LINESTRING(0 0, 1 1)')) AS length

┌─────────────┐
│    length   │
├─────────────┤
│ 1.414213562 │
└─────────────┘

SELECT
  ST_LENGTH(
    TO_GEOMETRY('POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))')
  ) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘
```
