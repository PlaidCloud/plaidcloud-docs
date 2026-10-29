---
title: ST_X (Lakehouse v1)
description: ST_X — zwraca długość geograficzną (współrzędną X) punktu reprezentowanego przez obiekt GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-x.md
---

Zwraca długość geograficzną (współrzędną X) punktu (Point) reprezentowanego przez obiekt GEOMETRY.

## Składnia SQL

```sql
ST_X(<geometry>)
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
  ST_X(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_x;

┌────────────┐
│ pipeline_x │
├────────────┤
│       37.5 │
└────────────┘
```
