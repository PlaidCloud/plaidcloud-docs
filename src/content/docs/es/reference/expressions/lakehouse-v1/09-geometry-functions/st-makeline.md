---
title: ST_MAKELINE (Lakehouse v1)
description: ST_MAKELINE — construye un objeto GEOMETRY que representa una línea que conecta los puntos de los dos objetos GEOMETRY de entrada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makeline.md
---

Construye un objeto GEOMETRY que representa una línea que conecta los puntos de los dos objetos GEOMETRY de entrada.

## Sintaxis de SQL

```sql
ST_MAKELINE(<geometry1>, <geometry2>)
```

## Alias

- [ST_MAKE_LINE](../st-make-line)

## Argumentos

| Argumentos    | Descripción                                                                                                 |
|---------------|-------------------------------------------------------------------------------------------------------------|
| `<geometry1>` | Un objeto GEOMETRY que contiene los puntos que se van a conectar. Este objeto debe ser un Point, un MultiPoint o un LineString. |
| `<geometry2>` | Un objeto GEOMETRY que contiene los puntos que se van a conectar. Este objeto debe ser un Point, un MultiPoint o un LineString. |

## Tipo de valor devuelto

Geometría.

## Ejemplos de SQL

```sql
SELECT
  ST_MAKELINE(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    ),
    ST_GEOMETRYFROMWKT(
      'POINT(-104.874173 56.714538)'
    )
  ) AS pipeline_line;

┌───────────────────────────────────────────────────────┐
│                     pipeline_line                     │
├───────────────────────────────────────────────────────┤
│ LINESTRING(-122.3061 37.554162,-104.874173 56.714538) │
└───────────────────────────────────────────────────────┘
```
