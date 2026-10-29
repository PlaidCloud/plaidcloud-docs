---
title: ST_SRID (Lakehouse v1)
description: ST_SRID — devuelve el SRID (identificador del sistema de referencia espacial) de un objeto GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-srid.md
---

Devuelve el SRID (identificador del sistema de referencia espacial) de un objeto GEOMETRY.

## Sintaxis de SQL

```sql
ST_SRID(<geometry>)
```

## Argumentos

| Argumentos   | Descripción                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | El argumento debe ser una expresión de tipo GEOMETRY. |

## Tipo de valor devuelto

INT32.

:::note
Si la geometría no tiene SRID, se devuelve el valor predeterminado 4326.
:::

## Ejemplos de SQL

```sql
SELECT
  ST_SRID(
    TO_GEOMETRY(
      'POINT(-122.306100 37.554162)',
      1234
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          1234 │
└───────────────┘

SELECT
  ST_SRID(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          4326 │
└───────────────┘
```
