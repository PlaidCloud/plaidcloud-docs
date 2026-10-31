---
title: ST_ASWKT (Lakehouse v1)
description: ST_ASWKT — convertit un objet GEOMETRY en sa représentation au format WKT (well-known text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-aswkt.md
---

Convertit un objet GEOMETRY en sa représentation au format [WKT (well-known text)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry).

## Syntaxe SQL

```sql
ST_ASWKT(<geometry>)
```

## Alias

- [ST_ASTEXT](../st-astext)

## Arguments

| Arguments    | Description                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | L'argument doit être une expression de type GEOMETRY. |

## Type de retour

String.

## Exemples SQL

```sql
SELECT
  ST_ASWKT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_wkt;

┌───────────────────────────────────────────┐
│                pipeline_wkt               │
├───────────────────────────────────────────┤
│ LINESTRING(400000 6000000,401000 6010000) │
└───────────────────────────────────────────┘

SELECT
  ST_ASTEXT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    )
  ) AS pipeline_wkt;

┌──────────────────────┐
│     pipeline_wkt     │
├──────────────────────┤
│ POINT(-122.35 37.55) │
└──────────────────────┘
```
