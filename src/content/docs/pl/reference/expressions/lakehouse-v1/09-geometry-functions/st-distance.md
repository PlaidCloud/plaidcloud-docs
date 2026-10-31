---
title: ST_DISTANCE (Lakehouse v1)
description: ST_DISTANCE — zwraca minimalną odległość euklidesową między dwoma obiektami GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-distance.md
---

Zwraca minimalną [odległość euklidesową](https://en.wikipedia.org/wiki/Euclidean_distance) między dwoma obiektami GEOMETRY.

## Składnia SQL

```sql
ST_DISTANCE(<geometry1>, <geometry2>)
```

## Argumenty

| Argumenty     | Opis                                                                          |
|---------------|-------------------------------------------------------------------------------|
| `<geometry1>` | Argument musi być wyrażeniem typu GEOMETRY i musi zawierać punkt (Point). |
| `<geometry2>` | Argument musi być wyrażeniem typu GEOMETRY i musi zawierać punkt (Point). |

:::note
- Zwraca NULL, jeśli co najmniej jeden z wejściowych punktów ma wartość NULL.
- Funkcja zgłasza błąd, jeśli dwa wejściowe obiekty GEOMETRY mają różne identyfikatory SRID.
:::

## Typ zwracany

Double.

## Przykłady SQL

```sql
SELECT
  ST_DISTANCE(
    TO_GEOMETRY('POINT(0 0)'),
    TO_GEOMETRY('POINT(1 1)')
  ) AS distance

┌─────────────┐
│   distance  │
├─────────────┤
│ 1.414213562 │
└─────────────┘
```
