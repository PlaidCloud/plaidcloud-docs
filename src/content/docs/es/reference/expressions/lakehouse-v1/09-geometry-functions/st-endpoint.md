---
title: ST_ENDPOINT (Lakehouse v1)
description: ST_ENDPOINT — devuelve el último Point de un LineString.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-endpoint.md
---

Devuelve el último Point de un LineString.

## Sintaxis de SQL

```sql
ST_ENDPOINT(<geometry>)
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
  ST_ENDPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(4 4)        │
└───────────────────┘
```
