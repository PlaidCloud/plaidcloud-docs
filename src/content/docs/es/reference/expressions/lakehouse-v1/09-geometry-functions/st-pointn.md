---
title: ST_POINTN (Lakehouse v1)
description: ST_POINTN — devuelve el Point que se encuentra en un índice especificado de un LineString.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-pointn.md
---

Devuelve el Point que se encuentra en un índice especificado de un LineString.

## Sintaxis de SQL

```sql
ST_POINTN(<geometry>, <index>)
```

## Argumentos

| Argumentos   | Descripción                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | El argumento debe ser una expresión de tipo GEOMETRY que represente un LineString. |
| `<index>`    | El índice del Point que se va a devolver.                                                 |

:::note
El índice empieza en 1, y un índice negativo se usa como desplazamiento desde el final del LineString. Si el índice está fuera de los límites, la función devuelve un error.
:::

## Tipo de valor devuelto

Geometría.

## Ejemplos de SQL

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
