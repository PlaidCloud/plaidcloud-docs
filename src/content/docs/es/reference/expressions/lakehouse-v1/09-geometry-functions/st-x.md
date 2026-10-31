---
title: ST_X (Lakehouse v1)
description: ST_X — devuelve la longitud (coordenada X) de un Point representado por un objeto GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-x.md
---

Devuelve la longitud (coordenada X) de un Point representado por un objeto GEOMETRY.

## Sintaxis de SQL

```sql
ST_X(<geometry>)
```

## Argumentos

| Argumentos   | Descripción                                                                   |
|--------------|-------------------------------------------------------------------------------|
| `<geometry>` | El argumento debe ser una expresión de tipo GEOMETRY y debe contener un Point. |

## Tipo de valor devuelto

Doble.

## Ejemplos de SQL

```sql
SELECT
  ST_X(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_x;

┌────────────┐
│ pipeline_x │
├────────────┤
│       37.5 │
└────────────┘
```
