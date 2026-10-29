---
title: ST_POINTN (Lakehouse v1)
description: ST_POINTN — devolve um Point num índice especificado de uma LineString.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-pointn.md
---

Devolve um Point num índice especificado de uma LineString.

## Sintaxe SQL

```sql
ST_POINTN(<geometry>, <index>)
```

## Argumentos

| Argumentos   | Descrição                                                                         |
|--------------|-----------------------------------------------------------------------------------|
| `<geometry>` | O argumento tem de ser uma expressão do tipo GEOMETRY que represente uma LineString. |
| `<index>`    | O índice do Point a devolver.                                                     |

:::note
O índice começa em 1 e um índice negativo é utilizado como desvio a partir do fim da LineString. Se o índice estiver fora dos limites, a função devolve um erro.
:::

## Tipo de retorno

Geometry.

## Exemplos de SQL

```sql
SELECT
  ST_POINTN(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    ),
    1
  ) AS pipeline_pointn;

┌─────────────────┐
│ pipeline_pointn │
├─────────────────┤
│ POINT(1 1)      │
└─────────────────┘

SELECT
  ST_POINTN(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    ),
    -2
  ) AS pipeline_pointn;

┌─────────────────┐
│ pipeline_pointn │
├─────────────────┤
│ POINT(3 3)      │
└─────────────────┘
```
