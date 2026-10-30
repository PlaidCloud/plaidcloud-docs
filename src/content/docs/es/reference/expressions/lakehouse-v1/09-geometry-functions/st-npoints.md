---
title: ST_NPOINTS (Lakehouse v1)
description: ST_NPOINTS — devuelve el número de puntos de un objeto GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-npoints.md
---

Devuelve el número de puntos de un objeto GEOMETRY.

## Sintaxis de SQL

```sql
ST_NPOINTS(<geometry>)
```

## Alias

- [ST_NUMPOINTS](../st-numpoints)

## Argumentos

| Argumentos   | Descripción                                                 |
|--------------|-------------------------------------------------------------|
| `<geometry>` | El argumento debe ser una expresión de tipo objeto GEOMETRY. |

## Tipo de valor devuelto

UInt8.

## Ejemplos de SQL

```sql
SELECT ST_NPOINTS(TO_GEOMETRY('POINT(66 12)')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       1 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('MULTIPOINT((45 21),(12 54))')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       2 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('LINESTRING(40 60,50 50,60 40)')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       3 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('MULTILINESTRING((1 1,32 17),(33 12,73 49,87.1 6.1))')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       5 │
└─────────┘

SELECT ST_NPOINTS(TO_GEOMETRY('GEOMETRYCOLLECTION(POLYGON((-10 0,0 10,10 0,-10 0)),LINESTRING(40 60,50 50,60 40),POINT(99 11))')) AS npoints

┌─────────┐
│ npoints │
├─────────┤
│       8 │
└─────────┘
```
