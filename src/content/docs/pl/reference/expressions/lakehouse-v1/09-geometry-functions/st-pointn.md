---
title: ST_POINTN (Lakehouse v1)
description: ST_POINTN — zwraca punkt (Point) o podanym indeksie w obiekcie LineString.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-pointn.md
---

Zwraca punkt (Point) o podanym indeksie w obiekcie LineString.

## Składnia SQL

```sql
ST_POINTN(<geometry>, <index>)
```

## Argumenty

| Argumenty    | Opis                                                                              |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | Argument musi być wyrażeniem typu GEOMETRY reprezentującym obiekt LineString. |
| `<index>`    | Indeks zwracanego punktu (Point).                                                 |

:::note
Indeksowanie zaczyna się od 1, a ujemny indeks jest używany jako przesunięcie od końca obiektu LineString. Jeśli indeks wykracza poza zakres, funkcja zwraca błąd.
:::

## Typ zwracany

Geometry.

## Przykłady SQL

```sql
SELECT
  ST_POINTN(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    ),
    1
  ) AS pipeline_pointn;

┌─────────────────┐
│ pipeline_pointn │
├─────────────────┤
│ POINT(1 1)      │
└─────────────────┘

SELECT
  ST_POINTN(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    ),
    -2
  ) AS pipeline_pointn;

┌─────────────────┐
│ pipeline_pointn │
├─────────────────┤
│ POINT(3 3)      │
└─────────────────┘
```
