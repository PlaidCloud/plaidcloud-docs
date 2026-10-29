---
title: ST_TRANSFORM (Lakehouse v1)
description: ST_TRANSFORM — convierte un objeto GEOMETRY de un sistema de referencia espacial (SRS) a otro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-transform.md
---

Convierte un objeto GEOMETRY de un [sistema de referencia espacial (SRS)](https://en.wikipedia.org/wiki/Spatial_reference_system) a otro. Si solo necesita cambiar el SRID sin modificar las coordenadas (por ejemplo, si el SRID era incorrecto), use [ST_SETSRID](../st-setsrid) en su lugar.

## Sintaxis de SQL

```sql
ST_TRANSFORM(<geometry> [, <from_srid>], <to_srid>)
```

## Argumentos

| Argumentos    | Descripción                                                                                                                                               |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<geometry>`  | El argumento debe ser una expresión de tipo objeto GEOMETRY.                                                                                               |
| `<from_srid>` | SRID opcional que identifica el SRS actual del objeto GEOMETRY de entrada; si se omite este argumento, se usa el SRID especificado en el objeto GEOMETRY de entrada. |
| `<to_srid>`   | El SRID que identifica el SRS que se va a usar; transforma el objeto GEOMETRY de entrada en un objeto nuevo que usa este SRS.                                         |

## Tipo de valor devuelto

Geometría.

## Ejemplos de SQL

```sql
SET GEOMETRY_OUTPUT_FORMAT = 'EWKT'

SELECT ST_TRANSFORM(ST_GEOMFROMWKT('POINT(389866.35 5819003.03)', 32633), 3857) AS transformed_geom

┌───────────────────────────────────────────────┐
│                transformed_geom               │
├───────────────────────────────────────────────┤
│ SRID=3857;POINT(1489140.093766 6892872.19868) │
└───────────────────────────────────────────────┘

SELECT ST_TRANSFORM(ST_GEOMFROMWKT('POINT(4.500212 52.161170)'), 4326, 28992) AS transformed_geom

┌──────────────────────────────────────────────┐
│               transformed_geom               │
├──────────────────────────────────────────────┤
│ SRID=28992;POINT(94308.670475 464038.168827) │
└──────────────────────────────────────────────┘

```
