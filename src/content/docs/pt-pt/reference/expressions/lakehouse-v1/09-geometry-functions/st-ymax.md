---
title: ST_YMAX (Lakehouse v1)
description: ST_YMAX — devolve a latitude máxima (coordenada Y) de todos os pontos contidos no objeto GEOMETRY especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-ymax.md
---

Devolve a latitude máxima (coordenada Y) de todos os pontos contidos no objeto GEOMETRY especificado.

## Sintaxe SQL

```sql
ST_YMAX(<geometry>)
```

## Argumentos

| Argumentos   | Descrição                                            |
|--------------|------------------------------------------------------|
| `<geometry>` | O argumento tem de ser uma expressão do tipo GEOMETRY. |

## Tipo de retorno

Double.

## Exemplos de SQL

```sql
SELECT
  ST_YMAX(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(180 50),LINESTRING(10 10,20 20,10 40),POINT EMPTY)'
    )
  ) AS pipeline_ymax;

┌───────────────┐
│ pipeline_ymax │
├───────────────┤
│            50 │
└───────────────┘

SELECT
  ST_YMAX(
    TO_GEOMETRY(
      'GEOMETRYCOLLECTION(POINT(40 10),LINESTRING(10 10,20 20,10 40),POLYGON((40 40,20 45,45 30,40 40)))'
    )
  ) AS pipeline_ymax;

┌───────────────┐
│ pipeline_ymax │
├───────────────┤
│            45 │
└───────────────┘
```
