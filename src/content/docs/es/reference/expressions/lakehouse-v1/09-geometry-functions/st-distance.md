---
title: ST_DISTANCE (Lakehouse v1)
description: ST_DISTANCE — devuelve la distancia euclidiana mínima entre dos objetos GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-distance.md
---

Devuelve la [distancia euclidiana](https://en.wikipedia.org/wiki/Euclidean_distance) mínima entre dos objetos GEOMETRY.

## Sintaxis de SQL

```sql
ST_DISTANCE(<geometry1>, <geometry2>)
```

## Argumentos

| Argumentos    | Descripción                                                                   |
|---------------|-------------------------------------------------------------------------------|
| `<geometry1>` | El argumento debe ser una expresión de tipo GEOMETRY y debe contener un Point. |
| `<geometry2>` | El argumento debe ser una expresión de tipo GEOMETRY y debe contener un Point. |

:::note
- Devuelve NULL si uno o más puntos de entrada son NULL.
- La función genera un error si los dos objetos GEOMETRY de entrada tienen SRID distintos.
:::

## Tipo de valor devuelto

Doble.

## Ejemplos de SQL

```sql
SELECT
  ST_DISTANCE(
    TO_GEOMETRY('POINT(0 0)'),
    TO_GEOMETRY('POINT(1 1)')
  ) AS distance

┌─────────────┐
│   distance  │
├─────────────┤
│ 1.414213562 │
└─────────────┘
```
