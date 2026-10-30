---
title: ST_LENGTH (Lakehouse v1)
description: ST_LENGTH — retorna o comprimento euclidiano das LineStrings de um objeto GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-length.md
---

Retorna o comprimento euclidiano das LineStrings de um objeto GEOMETRY.

## Sintaxe SQL

```sql
ST_LENGTH(<geometry>)
```

## Argumentos

| Argumentos   | Descrição                                                                           |
|--------------|-------------------------------------------------------------------------------------|
| `<geometry>` | O argumento deve ser uma expressão do tipo GEOMETRY que contenha linestrings.       |

:::note
- Se `<geometry>` não for uma `LineString`, uma `MultiLineString` nem uma `GeometryCollection` que contenha linestrings, retorna 0.
- Se `<geometry>` for uma `GeometryCollection`, retorna a soma dos comprimentos das linestrings da coleção.
:::

## Tipo de retorno

Double.

## Exemplos de SQL

```sql
SELECT
  ST_LENGTH(TO_GEOMETRY('POINT(1 1)')) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘

SELECT
  ST_LENGTH(TO_GEOMETRY('LINESTRING(0 0, 1 1)')) AS length

┌─────────────┐
│    length   │
├─────────────┤
│ 1.414213562 │
└─────────────┘

SELECT
  ST_LENGTH(
    TO_GEOMETRY('POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))')
  ) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘
```
