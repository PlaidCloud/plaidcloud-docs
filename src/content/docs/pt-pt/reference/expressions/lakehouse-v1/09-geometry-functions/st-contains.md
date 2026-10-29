---
title: ST_CONTAINS (Lakehouse v1)
description: ST_CONTAINS — devolve TRUE se o segundo objeto GEOMETRY estiver completamente dentro do primeiro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-contains.md
---

Devolve TRUE se o segundo objeto GEOMETRY estiver completamente dentro do primeiro objeto GEOMETRY.

## Sintaxe SQL

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## Argumentos

| Argumentos    | Descrição                                                                                    |
|---------------|----------------------------------------------------------------------------------------------|
| `<geometry1>` | O argumento tem de ser uma expressão do tipo objeto GEOMETRY que não seja uma GeometryCollection. |
| `<geometry2>` | O argumento tem de ser uma expressão do tipo objeto GEOMETRY que não seja uma GeometryCollection. |

:::note
- A função comunica um erro se os dois objetos GEOMETRY de entrada tiverem SRID diferentes.
:::

## Tipo de retorno

Boolean.

## Exemplos de SQL

```sql
SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('POLYGON((-1 0, 0 1, 1 0, -1 0))')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-1 1, 0 2, 1 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ false    │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-2 0, 0 0, 0 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

```
