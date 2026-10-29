---
title: ST_ENDPOINT (Lakehouse v1)
description: ST_ENDPOINT — zwraca ostatni punkt (Point) w obiekcie LineString.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-endpoint.md
---

Zwraca ostatni punkt (Point) w obiekcie LineString.

## Składnia SQL

```sql
ST_ENDPOINT(<geometry>)
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
  ST_ENDPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(4 4)        │
└───────────────────┘
```
