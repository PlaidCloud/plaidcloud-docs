---
title: TO_WEEK_OF_YEAR (Lakehouse v1)
description: TO_WEEK_OF_YEAR — calcula o número da semana dentro de um ano para uma determinada data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-week-of-year.md
---

Calcula o número da semana dentro de um ano para uma determinada data.

A numeração de semanas ISO funciona da seguinte forma: 4 de janeiro faz sempre parte da primeira semana. Se 1 de janeiro for uma quinta-feira, a semana que vai de segunda-feira, 29 de dezembro, a domingo, 4 de janeiro, é designada como a semana ISO 1. Se 1 de janeiro for uma sexta-feira, a semana que vai de segunda-feira, 4 de janeiro, a domingo, 10 de janeiro, é marcada como a semana ISO 1.

## Sintaxe do Analyze

```python
func.to_week_of_year(<expr>)
```

## Exemplos do Analyze

```python
func.now(), func.to_week_of_year(func.now()), func.week(func.now()), func.weekofyear(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_week_of_year(func.now()) │ func.week(func.now()) │ func.weekofyear(func.now()) │
├────────────────────────────┼──────────────────────────────────┼───────────────────────┼─────────────────────────────┤
│ 2024-03-14 23:30:04.011624 │                               11 │                    11 │                          11 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_WEEK_OF_YEAR(<expr>)
```

## Argumentos

| Argumentos | Descrição      |
|-----------|----------------|
| `<expr>`  | data/timestamp |

## Aliases

- [WEEK](../week)
- [WEEKOFYEAR](../weekofyear)

## Tipo de Retorno

Devolve um número inteiro que representa o número da semana dentro de um ano, com numeração de 1 a 53.

## Exemplos SQL

```sql
SELECT NOW(), TO_WEEK_OF_YEAR(NOW()), WEEK(NOW()), WEEKOFYEAR(NOW());

┌───────────────────────────────────────────────────────────────────────────────────────┐
│            now()           │ to_week_of_year(now()) │ week(now()) │ weekofyear(now()) │
├────────────────────────────┼────────────────────────┼─────────────┼───────────────────┤
│ 2024-03-14 23:30:04.011624 │                     11 │          11 │                11 │
└───────────────────────────────────────────────────────────────────────────────────────┘
```
