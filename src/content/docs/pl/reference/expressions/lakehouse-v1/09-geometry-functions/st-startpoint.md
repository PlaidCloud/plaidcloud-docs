---
title: ST_STARTPOINT (Lakehouse v1)
description: ST_STARTPOINT — zwraca pierwszy punkt (Point) w obiekcie LineString.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-startpoint.md
---

Zwraca pierwszy punkt (Point) w obiekcie LineString.

## Składnia SQL

```sql
ST_STARTPOINT(<geometry>)
```

## Argumenty

| Argumenty    | Opis                                                                              |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | Argument musi być wyrażeniem typu GEOMETRY reprezentującym obiekt LineString. |

## Typ zwracany

Geometry.

## Przykłady SQL

```sql
SELECT
  ST_STARTPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(1 1)        │
└───────────────────┘
```
