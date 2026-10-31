---
title: ST_Y (Lakehouse v1)
description: ST_Y — devolve a latitude (coordenada Y) de um Point representado por um objeto GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-y.md
---

Devolve a latitude (coordenada Y) de um Point representado por um objeto GEOMETRY.

## Sintaxe SQL

```sql
ST_Y(<geometry>)
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
  ST_Y(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_y;

┌────────────┐
│ pipeline_y │
├────────────┤
│       45.5 │
└────────────┘
```
