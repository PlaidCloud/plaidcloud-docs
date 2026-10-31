---
title: ST_MAKELINE (Lakehouse v1)
description: ST_MAKELINE — tworzy obiekt GEOMETRY reprezentujący linię łączącą punkty z dwóch wejściowych obiektów GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makeline.md
---

Tworzy obiekt GEOMETRY reprezentujący linię łączącą punkty z dwóch wejściowych obiektów GEOMETRY.

## Składnia SQL

```sql
ST_MAKELINE(<geometry1>, <geometry2>)
```

## Aliasy

- [ST_MAKE_LINE](../st-make-line)

## Argumenty

| Argumenty     | Opis                                                                                                        |
|---------------|-------------------------------------------------------------------------------------------------------------|
| `<geometry1>` | Obiekt GEOMETRY zawierający punkty do połączenia. Musi to być obiekt Point, MultiPoint lub LineString. |
| `<geometry2>` | Obiekt GEOMETRY zawierający punkty do połączenia. Musi to być obiekt Point, MultiPoint lub LineString. |

## Typ zwracany

Geometry.

## Przykłady SQL

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
