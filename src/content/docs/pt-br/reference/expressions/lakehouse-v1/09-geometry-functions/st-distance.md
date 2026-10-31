---
title: ST_DISTANCE (Lakehouse v1)
description: ST_DISTANCE — retorna a distância euclidiana mínima entre dois objetos GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-distance.md
---

Retorna a [distância euclidiana](https://en.wikipedia.org/wiki/Euclidean_distance) mínima entre dois objetos GEOMETRY.

## Sintaxe SQL

```sql
ST_DISTANCE(<geometry1>, <geometry2>)
```

## Argumentos

| Argumentos    | Descrição                                                                              |
|---------------|----------------------------------------------------------------------------------------|
| `<geometry1>` | O argumento deve ser uma expressão do tipo GEOMETRY e deve conter um Point.            |
| `<geometry2>` | O argumento deve ser uma expressão do tipo GEOMETRY e deve conter um Point.            |

:::note
- Retorna NULL se um ou mais pontos de entrada forem NULL.
- A função gera um erro se os dois objetos GEOMETRY de entrada tiverem SRIDs diferentes.
:::

## Tipo de retorno

Double.

## Exemplos de SQL

```sql
SELECT
  ST_DISTANCE(
    TO_GEOMETRY('POINT(0 0)'),
    TO_GEOMETRY('POINT(1 1)')
  ) AS distance

┌─────────────┐
│   distance  │
├─────────────┤
│ 1.414213562 │
└─────────────┘
```
