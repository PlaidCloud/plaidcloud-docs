---
title: ST_CONTAINS (Lakehouse v1)
description: ST_CONTAINS — zwraca TRUE, jeśli drugi obiekt GEOMETRY znajduje się całkowicie wewnątrz pierwszego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-contains.md
---

Zwraca TRUE, jeśli drugi obiekt GEOMETRY znajduje się całkowicie wewnątrz pierwszego obiektu GEOMETRY.

## Składnia SQL

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## Argumenty

| Argumenty     | Opis                                                                                         |
|---------------|----------------------------------------------------------------------------------------------|
| `<geometry1>` | Argument musi być wyrażeniem typu GEOMETRY, które nie jest obiektem GeometryCollection. |
| `<geometry2>` | Argument musi być wyrażeniem typu GEOMETRY, które nie jest obiektem GeometryCollection. |

:::note
- Funkcja zgłasza błąd, jeśli dwa wejściowe obiekty GEOMETRY mają różne identyfikatory SRID.
:::

## Typ zwracany

Boolean.

## Przykłady SQL

```sql
SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('POLYGON((-1 0, 0 1, 1 0, -1 0))')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-1 1, 0 2, 1 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ false    │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-2 0, 0 0, 0 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

```
