---
title: ST_MAKEPOLYGON (Lakehouse v1)
description: ST_MAKEPOLYGON — tworzy obiekt GEOMETRY reprezentujący wielokąt (Polygon) bez otworów.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makepolygon.md
---

Tworzy obiekt GEOMETRY reprezentujący wielokąt (Polygon) bez otworów. Funkcja używa podanego obiektu LineString jako pętli zewnętrznej.

## Składnia SQL

```sql
ST_MAKEPOLYGON(<geometry>)
```

## Aliasy

- [ST_POLYGON](../st-polygon)

## Argumenty

| Argumenty    | Opis                                                 |
|--------------|------------------------------------------------------|
| `<geometry>` | Argument musi być wyrażeniem typu GEOMETRY. |

## Typ zwracany

Geometry.

## Przykłady SQL

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
