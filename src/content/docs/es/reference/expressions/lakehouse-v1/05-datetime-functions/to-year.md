---
title: TO_YEAR (Lakehouse v1)
description: TO_YEAR — convierte una fecha o una fecha con hora (marca de tiempo) en un número UInt16 que contiene el año.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-year.md
---

Convierte una fecha o una fecha con hora (marca de tiempo/datetime) en un número UInt16 que contiene el número del año (d. C.).

## Sintaxis de Analyze

```python
func.to_year(<expr>)
```

## Ejemplos de Analyze

```python
func.now(), func.to_year(func.now()), func.year(func.now())

┌───────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_year(func.now()) │ func.year(func.now()) │
├────────────────────────────┼──────────────────────────┼───────────────────────┤
│ 2024-03-14 23:37:03.895166 │                     2024 │                  2024 │
└───────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_YEAR(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<expr>`  | fecha/marca de tiempo |

## Alias

- [YEAR](../year)

## Tipo de retorno

 `SMALLINT`

## Ejemplos de SQL

```sql
SELECT NOW(), TO_YEAR(NOW()), YEAR(NOW());

┌───────────────────────────────────────────────────────────┐
│            now()           │ to_year(now()) │ year(now()) │
├────────────────────────────┼────────────────┼─────────────┤
│ 2024-03-14 23:37:03.895166 │           2024 │        2024 │
└───────────────────────────────────────────────────────────┘
```
