---
title: ST_XMIN (Lakehouse v1)
description: ST_XMIN — devuelve la longitud mínima (coordenada X) de todos los puntos contenidos en el objeto GEOMETRY especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-xmin.md
---

Devuelve la longitud mínima (coordenada X) de todos los puntos contenidos en el objeto GEOMETRY especificado.

## Sintaxis de SQL

```sql
ST_XMIN(<geometry>)
```

## Argumentos

| Argumentos   | Descripción                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | El argumento debe ser una expresión de tipo GEOMETRY. |

## Tipo de valor devuelto

Doble.

## Ejemplos de SQL

```sql
SELECT
  ST_XMIN(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(180 10),LINESTRING(20 10,30 20,40 40),POINT EMPTY)'
    )
  ) AS pipeline_xmin;

┌───────────────┐
│ pipeline_xmin │
├───────────────┤
│            20 │
└───────────────┘

SELECT
  ST_XMIN(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(40 10),LINESTRING(20 10,30 20,10 40),POLYGON((40 40,20 45,45 30,40 40)))'
    )
  ) AS pipeline_xmin;

┌───────────────┐
│ pipeline_xmin │
├───────────────┤
│            10 │
└───────────────┘
```
