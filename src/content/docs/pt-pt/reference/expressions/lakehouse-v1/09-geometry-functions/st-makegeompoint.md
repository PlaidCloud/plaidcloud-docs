---
title: ST_MAKEGEOMPOINT (Lakehouse v1)
description: ST_MAKEGEOMPOINT — constrói um objeto GEOMETRY que representa um Point com a longitude e a latitude especificadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makegeompoint.md
---

Constrói um objeto GEOMETRY que representa um Point com a longitude e a latitude especificadas.

## Sintaxe SQL

```sql
ST_MAKEGEOMPOINT(<longitude>, <latitude>)
```

## Aliases

- [ST_GEOM_POINT](../st-geom-point)

## Argumentos

| Argumentos    | Descrição                                     |
|---------------|-----------------------------------------------|
| `<longitude>` | Um valor Double que representa a longitude.   |
| `<latitude>`  | Um valor Double que representa a latitude.    |

## Tipo de retorno

Geometry.

## Exemplos de SQL

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
