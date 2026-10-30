---
title: ST_Y (Lakehouse v1)
description: ST_Y — devuelve la latitud (coordenada Y) de un Point representado por un objeto GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-y.md
---

Devuelve la latitud (coordenada Y) de un Point representado por un objeto GEOMETRY.

## Sintaxis de SQL

```sql
ST_Y(<geometry>)
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
  ST_Y(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_y;

┌────────────┐
│ pipeline_y │
├────────────┤
│       45.5 │
└────────────┘
```
