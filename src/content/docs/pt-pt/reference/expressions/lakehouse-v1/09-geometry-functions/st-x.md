---
title: ST_X (Lakehouse v1)
description: ST_X — devolve a longitude (coordenada X) de um Point representado por um objeto GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-x.md
---

Devolve a longitude (coordenada X) de um Point representado por um objeto GEOMETRY.

## Sintaxe SQL

```sql
ST_X(<geometry>)
```

## Argumentos

| Argumentos   | Descrição                                                                     |
|--------------|-------------------------------------------------------------------------------|
| `<geometry>` | O argumento tem de ser uma expressão do tipo GEOMETRY e tem de conter um Point. |

## Tipo de retorno

Double.

## Exemplos de SQL

```sql
SELECT
  ST_X(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_x;

┌────────────┐
│ pipeline_x │
├────────────┤
│       37.5 │
└────────────┘
```
