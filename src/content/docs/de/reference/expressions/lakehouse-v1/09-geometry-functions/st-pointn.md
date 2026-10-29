---
title: ST_POINTN (Lakehouse v1)
description: ST_POINTN — gibt einen Point am angegebenen Index in einem LineString zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-pointn.md
---

Gibt einen Point am angegebenen Index in einem LineString zurück.

## SQL-Syntax

```sql
ST_POINTN(<geometry>, <index>)
```

## Argumente

| Argumente    | Beschreibung                                                                                   |
|--------------|------------------------------------------------------------------------------------------------|
| `<geometry>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein, der einen LineString darstellt.          |
| `<index>`    | Der Index des zurückzugebenden Points.                                                         |

:::note
Der Index beginnt bei 1, und ein negativer Index wird als Versatz vom Ende des LineString verwendet. Liegt der Index außerhalb des gültigen Bereichs, gibt die Funktion einen Fehler zurück.
:::

## Rückgabetyp

Geometry.

## SQL-Beispiele

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
