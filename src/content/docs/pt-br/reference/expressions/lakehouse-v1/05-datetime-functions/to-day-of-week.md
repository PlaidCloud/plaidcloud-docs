---
title: TO_DAY_OF_WEEK (Lakehouse v1)
description: TO_DAY_OF_WEEK — converte uma data ou data com hora (timestamp/datetime) em um número UInt8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-week.md
---

Converte uma data ou data com hora (timestamp/datetime) em um número UInt8 que contém o número do dia da semana (segunda-feira é 1 e domingo é 7).

## Sintaxe do Analyze

```python
func.to_day_of_week(<expr>)
```

## Exemplos do Analyze

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_week('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  7 │
└────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_DAY_OF_WEEK(<expr>)
```

## Argumentos

| Argumentos | Descrição      |
|-----------|----------------|
| `<expr>`  | data/timestamp |

## Tipo de retorno

``TINYINT`

## Exemplos de SQL

```sql

SELECT
    to_day_of_week('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ to_day_of_week('2023-11-12 09:38:18.165575') │
│                     UInt8                    │
├──────────────────────────────────────────────┤
│                                            7 │
└──────────────────────────────────────────────┘
```
