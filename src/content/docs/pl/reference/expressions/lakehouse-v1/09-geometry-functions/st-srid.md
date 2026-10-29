---
title: ST_SRID (Lakehouse v1)
description: ST_SRID — zwraca SRID (identyfikator układu odniesienia przestrzennego) obiektu GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-srid.md
---

Zwraca SRID (identyfikator układu odniesienia przestrzennego) obiektu GEOMETRY.

## Składnia SQL

```sql
ST_SRID(<geometry>)
```

## Argumenty

| Argumenty    | Opis                                                 |
|--------------|------------------------------------------------------|
| `<geometry>` | Argument musi być wyrażeniem typu GEOMETRY. |

## Typ zwracany

INT32.

:::note
Jeśli obiekt Geometry nie ma identyfikatora SRID, zwracana jest wartość domyślna 4326.
:::

## Przykłady SQL

```sql
SELECT
  ST_SRID(
    TO_GEOMETRY(
      'POINT(-122.306100 37.554162)',
      1234
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          1234 │
└───────────────┘

SELECT
  ST_SRID(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          4326 │
└───────────────┘
```
