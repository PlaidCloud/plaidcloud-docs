---
title: ST_LENGTH (Lakehouse v1)
description: ST_LENGTH — devuelve la longitud euclidiana de los LineString de un objeto GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-length.md
---

Devuelve la longitud euclidiana de los LineString de un objeto GEOMETRY.

## Sintaxis de SQL

```sql
ST_LENGTH(<geometry>)
```

## Argumentos

| Argumentos   | Descripción                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `<geometry>` | El argumento debe ser una expresión de tipo GEOMETRY que contenga linestrings. |

:::note
- Si `<geometry>` no es un `LineString`, un `MultiLineString` ni una `GeometryCollection` que contenga linestrings, devuelve 0.
- Si `<geometry>` es una `GeometryCollection`, devuelve la suma de las longitudes de los linestrings de la colección.
:::

## Tipo de valor devuelto

Doble.

## Ejemplos de SQL

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
