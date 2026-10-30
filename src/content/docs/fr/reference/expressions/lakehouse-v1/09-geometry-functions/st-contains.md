---
title: ST_CONTAINS (Lakehouse v1)
description: ST_CONTAINS — renvoie TRUE si le second objet GEOMETRY se trouve entièrement à l'intérieur du premier.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-contains.md
---

Renvoie TRUE si le second objet GEOMETRY se trouve entièrement à l'intérieur du premier objet GEOMETRY.

## Syntaxe SQL

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## Arguments

| Arguments     | Description                                                                                  |
|---------------|----------------------------------------------------------------------------------------------|
| `<geometry1>` | L'argument doit être une expression de type objet GEOMETRY qui n'est pas une GeometryCollection. |
| `<geometry2>` | L'argument doit être une expression de type objet GEOMETRY qui n'est pas une GeometryCollection. |

:::note
- La fonction signale une erreur si les deux objets GEOMETRY en entrée ont des SRID différents.
:::

## Type de retour

Boolean.

## Exemples SQL

```sql
SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('POLYGON((-1 0, 0 1, 1 0, -1 0))')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-1 1, 0 2, 1 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ false    │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-2 0, 0 0, 0 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

```
