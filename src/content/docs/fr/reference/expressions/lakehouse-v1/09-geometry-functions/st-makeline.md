---
title: ST_MAKELINE (Lakehouse v1)
description: ST_MAKELINE — construit un objet GEOMETRY qui représente une ligne reliant les points des deux objets GEOMETRY en entrée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makeline.md
---

Construit un objet GEOMETRY qui représente une ligne reliant les points des deux objets GEOMETRY en entrée.

## Syntaxe SQL

```sql
ST_MAKELINE(<geometry1>, <geometry2>)
```

## Alias

- [ST_MAKE_LINE](../st-make-line)

## Arguments

| Arguments     | Description                                                                                                 |
|---------------|-------------------------------------------------------------------------------------------------------------|
| `<geometry1>` | Un objet GEOMETRY contenant les points à relier. Cet objet doit être un Point, un MultiPoint ou un LineString. |
| `<geometry2>` | Un objet GEOMETRY contenant les points à relier. Cet objet doit être un Point, un MultiPoint ou un LineString. |

## Type de retour

Geometry.

## Exemples SQL

```sql
SELECT
  ST_MAKELINE(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    ),
    ST_GEOMETRYFROMWKT(
      'POINT(-104.874173 56.714538)'
    )
  ) AS pipeline_line;

┌───────────────────────────────────────────────────────┐
│                     pipeline_line                     │
├───────────────────────────────────────────────────────┤
│ LINESTRING(-122.3061 37.554162,-104.874173 56.714538) │
└───────────────────────────────────────────────────────┘
```
