---
title: ST_CONTAINS (Lakehouse v1)
description: ST_CONTAINS — devuelve TRUE si el segundo objeto GEOMETRY está completamente dentro del primero.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-contains.md
---

Devuelve TRUE si el segundo objeto GEOMETRY está completamente dentro del primer objeto GEOMETRY.

## Sintaxis de SQL

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## Argumentos

| Argumentos    | Descripción                                                                                  |
|---------------|----------------------------------------------------------------------------------------------|
| `<geometry1>` | El argumento debe ser una expresión de tipo objeto GEOMETRY que no sea una GeometryCollection. |
| `<geometry2>` | El argumento debe ser una expresión de tipo objeto GEOMETRY que no sea una GeometryCollection. |

:::note
- La función genera un error si los dos objetos GEOMETRY de entrada tienen SRID distintos.
:::

## Tipo de valor devuelto

Booleano.

## Ejemplos de SQL

```sql
SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('POLYGON((-1 0, 0 1, 1 0, -1 0))')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-1 1, 0 2, 1 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ false    │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-2 0, 0 0, 0 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

```
