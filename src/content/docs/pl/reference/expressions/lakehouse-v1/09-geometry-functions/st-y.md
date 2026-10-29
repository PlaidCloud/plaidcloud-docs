---
title: ST_Y (Lakehouse v1)
description: ST_Y — zwraca szerokość geograficzną (współrzędną Y) punktu reprezentowanego przez obiekt GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-y.md
---

Zwraca szerokość geograficzną (współrzędną Y) punktu (Point) reprezentowanego przez obiekt GEOMETRY.

## Składnia SQL

```sql
ST_Y(<geometry>)
```

## Argumenty

| Argumenty    | Opis                                                                          |
|--------------|-------------------------------------------------------------------------------|
| `<geometry>` | Argument musi być wyrażeniem typu GEOMETRY i musi zawierać punkt (Point). |

## Typ zwracany

Double.

## Przykłady SQL

```sql
SELECT
  ST_Y(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_y;

┌────────────┐
│ pipeline_y │
├────────────┤
│       45.5 │
└────────────┘
```
