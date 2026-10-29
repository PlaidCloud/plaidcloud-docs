---
title: TO_START_OF_MONTH (Lakehouse v1)
description: TO_START_OF_MONTH — arredonda para baixo uma data ou data com hora (timestamp/datetime) até o primeiro dia do mês.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-month.md
---

Arredonda para baixo uma data ou data com hora (timestamp/datetime) até o primeiro dia do mês.
Retorna a data.

## Sintaxe do Analyze

```python
func.to_start_of_month(<expr>)
```

## Exemplos do Analyze

```python
func.to_start_of_month('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_month('2023-11-12 09:38:18.165575')           │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_START_OF_MONTH(<expr>)
```

## Argumentos

| Argumentos | Descrição      |
|-----------|----------------|
| `<expr>`  | data/timestamp |

## Tipo de retorno

`DATE`, retorna a data no formato “YYYY-MM-DD”.

## Exemplos de SQL

```sql
SELECT
  to_start_of_month('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_start_of_month('2023-11-12 09:38:18.165575') │
│                       Date                      │
├─────────────────────────────────────────────────┤
│ 2023-11-01                                      │
└─────────────────────────────────────────────────┘
```
