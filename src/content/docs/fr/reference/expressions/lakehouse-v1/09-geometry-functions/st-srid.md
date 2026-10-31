---
title: ST_SRID (Lakehouse v1)
description: ST_SRID — renvoie le SRID (identifiant du système de référence spatiale) d'un objet GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-srid.md
---

Renvoie le SRID (identifiant du système de référence spatiale) d'un objet GEOMETRY.

## Syntaxe SQL

```sql
ST_SRID(<geometry>)
```

## Arguments

| Arguments    | Description                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | L'argument doit être une expression de type GEOMETRY. |

## Type de retour

INT32.

:::note
Si la géométrie n'a pas de SRID, la valeur par défaut 4326 est renvoyée.
:::

## Exemples SQL

```sql
SELECT
  ST_SRID(
    TO_GEOMETRY(
      'POINT(-122.306100 37.554162)',
      1234
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          1234 │
└───────────────┘

SELECT
  ST_SRID(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          4326 │
└───────────────┘
```
