---
title: ST_STARTPOINT (Lakehouse v1)
description: ST_STARTPOINT — devuelve el primer Point de un LineString.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-startpoint.md
---

Devuelve el primer Point de un LineString.

## Sintaxis de SQL

```sql
ST_STARTPOINT(<geometry>)
```

## Argumentos

| Argumentos   | Descripción                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | El argumento debe ser una expresión de tipo GEOMETRY que represente un LineString. |

## Tipo de valor devuelto

Geometría.

## Ejemplos de SQL

```sql
SELECT
  ST_STARTPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(1 1)        │
└───────────────────┘
```
