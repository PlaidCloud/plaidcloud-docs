---
title: ST_MAKEPOLYGON (Lakehouse v1)
description: ST_MAKEPOLYGON — construit un objet GEOMETRY qui représente un Polygon sans trou.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makepolygon.md
---

Construit un objet GEOMETRY qui représente un Polygon sans trou. La fonction utilise le LineString indiqué comme boucle extérieure.

## Syntaxe SQL

```sql
ST_MAKEPOLYGON(<geometry>)
```

## Alias

- [ST_POLYGON](../st-polygon)

## Arguments

| Arguments    | Description                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | L'argument doit être une expression de type GEOMETRY. |

## Type de retour

Geometry.

## Exemples SQL

```sql
SELECT
  ST_MAKEPOLYGON(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(0.0 0.0, 1.0 0.0, 1.0 2.0, 0.0 2.0, 0.0 0.0)'
    )
  ) AS pipeline_polygon;

┌────────────────────────────────┐
│        pipeline_polygon        │
├────────────────────────────────┤
│ POLYGON((0 0,1 0,1 2,0 2,0 0)) │
└────────────────────────────────┘
```
