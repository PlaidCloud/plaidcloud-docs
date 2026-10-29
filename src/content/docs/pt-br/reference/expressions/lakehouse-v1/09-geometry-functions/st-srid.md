---
title: ST_SRID (Lakehouse v1)
description: ST_SRID — retorna o SRID (identificador do sistema de referência espacial) de um objeto GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-srid.md
---

Retorna o SRID (identificador do sistema de referência espacial) de um objeto GEOMETRY.

## Sintaxe SQL

```sql
ST_SRID(<geometry>)
```

## Argumentos

| Argumentos   | Descrição                                            |
|--------------|------------------------------------------------------|
| `<geometry>` | O argumento deve ser uma expressão do tipo GEOMETRY. |

## Tipo de retorno

INT32.

:::note
Se a Geometry não tiver um SRID, o valor padrão 4326 será retornado.
:::

## Exemplos de SQL

```sql
SELECT
  ST_SRID(
    TO_GEOMETRY(
      'POINT(-122.306100 37.554162)',
      1234
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          1234 │
└───────────────┘

SELECT
  ST_SRID(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_srid;

┌───────────────┐
│ pipeline_srid │
├───────────────┤
│          4326 │
└───────────────┘
```
