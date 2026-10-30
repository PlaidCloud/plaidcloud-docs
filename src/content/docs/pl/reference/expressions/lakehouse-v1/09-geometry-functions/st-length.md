---
title: ST_LENGTH (Lakehouse v1)
description: ST_LENGTH — zwraca długość euklidesową obiektów LineString w obiekcie GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-length.md
---

Zwraca długość euklidesową obiektów LineString w obiekcie GEOMETRY.

## Składnia SQL

```sql
ST_LENGTH(<geometry>)
```

## Argumenty

| Argumenty    | Opis                                                                        |
|--------------|-----------------------------------------------------------------------------|
| `<geometry>` | Argument musi być wyrażeniem typu GEOMETRY zawierającym linie łamane (linestring). |

:::note
- Jeśli `<geometry>` nie jest obiektem `LineString`, `MultiLineString` ani `GeometryCollection` zawierającym linie łamane, zwraca 0.
- Jeśli `<geometry>` jest obiektem `GeometryCollection`, zwraca sumę długości linii łamanych w kolekcji.
:::

## Typ zwracany

Double.

## Przykłady SQL

```sql
SELECT
  ST_LENGTH(TO_GEOMETRY('POINT(1 1)')) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘

SELECT
  ST_LENGTH(TO_GEOMETRY('LINESTRING(0 0, 1 1)')) AS length

┌─────────────┐
│    length   │
├─────────────┤
│ 1.414213562 │
└─────────────┘

SELECT
  ST_LENGTH(
    TO_GEOMETRY('POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))')
  ) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘
```
