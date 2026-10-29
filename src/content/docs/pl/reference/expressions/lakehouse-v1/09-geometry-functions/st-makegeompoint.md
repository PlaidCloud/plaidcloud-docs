---
title: ST_MAKEGEOMPOINT (Lakehouse v1)
description: ST_MAKEGEOMPOINT — tworzy obiekt GEOMETRY reprezentujący punkt (Point) o podanej długości i szerokości geograficznej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makegeompoint.md
---

Tworzy obiekt GEOMETRY reprezentujący punkt (Point) o podanej długości i szerokości geograficznej.

## Składnia SQL

```sql
ST_MAKEGEOMPOINT(<longitude>, <latitude>)
```

## Aliasy

- [ST_GEOM_POINT](../st-geom-point)

## Argumenty

| Argumenty     | Opis                                          |
|---------------|-----------------------------------------------|
| `<longitude>` | Wartość typu Double reprezentująca długość geograficzną. |
| `<latitude>`  | Wartość typu Double reprezentująca szerokość geograficzną. |

## Typ zwracany

Geometry.

## Przykłady SQL

```sql
SELECT
  ST_MAKEGEOMPOINT(
    7.0, 8.0
  ) AS pipeline_point;

┌────────────────┐
│ pipeline_point │
├────────────────┤
│ POINT(7 8)     │
└────────────────┘

SELECT
  ST_MAKEGEOMPOINT(
    -122.3061, 37.554162
  ) AS pipeline_point;

┌────────────────────────────┐
│       pipeline_point       │
├────────────────────────────┤
│ POINT(-122.3061 37.554162) │
└────────────────────────────┘
```
