---
title: ST_ENDPOINT (Lakehouse v1)
description: ST_ENDPOINT — devolve o último Point de uma LineString.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-endpoint.md
---

Devolve o último Point de uma LineString.

## Sintaxe SQL

```sql
ST_ENDPOINT(<geometry>)
```

## Argumentos

| Argumentos   | Descrição                                                                         |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | O argumento tem de ser uma expressão do tipo GEOMETRY que represente uma LineString. |

## Tipo de retorno

Geometry.

## Exemplos de SQL

```sql
SELECT
  ST_ENDPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(4 4)        │
└───────────────────┘
```
