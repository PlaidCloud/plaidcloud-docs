---
title: ST_MAKEGEOMPOINT (Lakehouse v1)
description: ST_MAKEGEOMPOINT — construye un objeto GEOMETRY que representa un Point con la longitud y la latitud especificadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makegeompoint.md
---

Construye un objeto GEOMETRY que representa un Point con la longitud y la latitud especificadas.

## Sintaxis de SQL

```sql
ST_MAKEGEOMPOINT(<longitude>, <latitude>)
```

## Alias

- [ST_GEOM_POINT](../st-geom-point)

## Argumentos

| Argumentos    | Descripción                                   |
|---------------|-----------------------------------------------|
| `<longitude>` | Un valor Double que representa la longitud. |
| `<latitude>`  | Un valor Double que representa la latitud.  |

## Tipo de valor devuelto

Geometría.

## Ejemplos de SQL

```sql
SELECT
  ST_MAKEGEOMPOINT(
    7.0, 8.0
  ) AS pipeline_point;

┌────────────────┐
│ pipeline_point │
├────────────────┤
│ POINT(7 8)     │
└────────────────┘

SELECT
  ST_MAKEGEOMPOINT(
    -122.3061, 37.554162
  ) AS pipeline_point;

┌────────────────────────────┐
│       pipeline_point       │
├────────────────────────────┤
│ POINT(-122.3061 37.554162) │
└────────────────────────────┘
```
