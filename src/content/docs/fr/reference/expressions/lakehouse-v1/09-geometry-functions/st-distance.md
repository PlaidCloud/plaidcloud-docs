---
title: ST_DISTANCE (Lakehouse v1)
description: ST_DISTANCE — renvoie la distance euclidienne minimale entre deux objets GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-distance.md
---

Renvoie la [distance euclidienne](https://en.wikipedia.org/wiki/Euclidean_distance) minimale entre deux objets GEOMETRY.

## Syntaxe SQL

```sql
ST_DISTANCE(<geometry1>, <geometry2>)
```

## Arguments

| Arguments     | Description                                                                   |
|---------------|-------------------------------------------------------------------------------|
| `<geometry1>` | L'argument doit être une expression de type GEOMETRY et doit contenir un Point. |
| `<geometry2>` | L'argument doit être une expression de type GEOMETRY et doit contenir un Point. |

:::note
- Renvoie NULL si au moins un des points en entrée est NULL.
- La fonction signale une erreur si les deux objets GEOMETRY en entrée ont des SRID différents.
:::

## Type de retour

Double.

## Exemples SQL

```sql
SELECT
  ST_DISTANCE(
    TO_GEOMETRY('POINT(0 0)'),
    TO_GEOMETRY('POINT(1 1)')
  ) AS distance

┌─────────────┐
│   distance  │
├─────────────┤
│ 1.414213562 │
└─────────────┘
```
