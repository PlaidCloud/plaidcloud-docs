---
title: ST_SETSRID (Lakehouse v1)
description: ST_SETSRID — devuelve un objeto GEOMETRY cuyo SRID (identificador del sistema de referencia espacial) se establece en el valor especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-setsrid.md
---

Devuelve un objeto GEOMETRY cuyo [SRID (identificador del sistema de referencia espacial)](https://en.wikipedia.org/wiki/Spatial_reference_system#Identifier) se establece en el valor especificado. Esta función solo cambia el SRID sin afectar a las coordenadas del objeto. Si también necesita cambiar las coordenadas para que coincidan con el nuevo SRS (sistema de referencia espacial), use [ST_TRANSFORM](../st-transform) en su lugar.

## Sintaxis de SQL

```sql
ST_SETSRID(<geometry>, <srid>)
```

## Argumentos

| Argumentos   | Descripción                                                 |
|--------------|-------------------------------------------------------------|
| `<geometry>` | El argumento debe ser una expresión de tipo objeto GEOMETRY. |
| `<srid>`     | El entero SRID que se va a establecer en el objeto GEOMETRY devuelto.    |

## Tipo de valor devuelto

Geometría.

## Ejemplos de SQL

```sql
SET GEOMETRY_OUTPUT_FORMAT = 'EWKT'

SELECT ST_SETSRID(TO_GEOMETRY('POINT(13 51)'), 4326) AS geometry

┌────────────────────────┐
│        geometry        │
├────────────────────────┤
│ SRID=4326;POINT(13 51) │
└────────────────────────┘

```
