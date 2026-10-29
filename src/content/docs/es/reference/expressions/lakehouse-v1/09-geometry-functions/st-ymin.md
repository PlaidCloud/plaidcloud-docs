---
title: ST_YMIN (Lakehouse v1)
description: ST_YMIN — devuelve la latitud mínima (coordenada Y) de todos los puntos contenidos en el objeto GEOMETRY especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-ymin.md
---

Devuelve la latitud mínima (coordenada Y) de todos los puntos contenidos en el objeto GEOMETRY especificado.

## Sintaxis de SQL

```sql
ST_YMIN(<geometry>)
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
  ST_YMIN(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(-180 -10),LINESTRING(-179 0, 179 30),POINT EMPTY)'
    )
  ) AS pipeline_ymin;

┌───────────────┐
│ pipeline_ymin │
├───────────────┤
│           -10 │
└───────────────┘

SELECT
  ST_YMIN(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(180 0),LINESTRING(-60 -30, 60 30),POLYGON((40 40,20 45,45 30,40 40)))'
    )
  ) AS pipeline_ymin;

┌───────────────┐
│ pipeline_ymin │
├───────────────┤
│           -30 │
└───────────────┘
```
