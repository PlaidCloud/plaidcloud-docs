---
title: TO_DAY_OF_YEAR (Lakehouse v1)
description: TO_DAY_OF_YEAR — converte uma data ou data com hora (timestamp/datetime) em um número UInt16.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-year.md
---

Converte uma data ou data com hora (timestamp/datetime) em um número UInt16 que contém o número do dia do ano (1-366).

## Sintaxe do Analyze

```python
func.to_day_of_year(<expr>)
```

## Exemplos do Analyze

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_year('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                316 │
└────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_DAY_OF_YEAR(<expr>)
```

## Argumentos

| Argumentos  | Descrição   |
| ----------- | ----------- |
| `<expr>` | data/timestamp |

## Tipo de retorno

`SMALLINT`

## Exemplos de SQL

```sql
SELECT
    to_day_of_year('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ to_day_of_year('2023-11-12 09:38:18.165575') │
│                    UInt16                    │
├──────────────────────────────────────────────┤
│                                          316 │
└──────────────────────────────────────────────┘
```
