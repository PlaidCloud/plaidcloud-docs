---
title: TO_DAY_OF_MONTH (Lakehouse v1)
description: TO_DAY_OF_MONTH — converte uma data ou data com hora (timestamp/datetime) em um número UInt8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-month.md
---

Converte uma data ou data com hora (timestamp/datetime) em um número UInt8 que contém o número do dia do mês (1-31).

## Sintaxe do Analyze

```python
func.to_day_of_month(<expr>)
```

## Exemplos do Analyze

```python
func.now(), func.to_day_of_month(func.now()), func.day(func.now())

┌──────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_day_of_month(func.now()) │ func.day(func.now()) │
├────────────────────────────┼──────────────────────────────────┼──────────────────────┤
│ 2024-03-14 23:35:41.947962 │                               14 │                   14 │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_DAY_OF_MONTH(<expr>)
```

## Argumentos

| Argumentos | Descrição      |
|-----------|----------------|
| `<expr>`  | data/timestamp |

## Aliases

- [DAY](../day)

## Tipo de retorno

`TINYINT`

## Exemplos de SQL

```sql
SELECT NOW(), TO_DAY_OF_MONTH(NOW()), DAY(NOW());

┌──────────────────────────────────────────────────────────────────┐
│            now()           │ to_day_of_month(now()) │ day(now()) │
├────────────────────────────┼────────────────────────┼────────────┤
│ 2024-03-14 23:35:41.947962 │                     14 │         14 │
└──────────────────────────────────────────────────────────────────┘
```
