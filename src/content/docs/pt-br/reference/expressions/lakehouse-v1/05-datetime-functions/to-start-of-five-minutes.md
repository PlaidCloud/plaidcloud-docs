---
title: TO_START_OF_FIVE_MINUTES (Lakehouse v1)
description: TO_START_OF_FIVE_MINUTES — arredonda para baixo uma data com hora (timestamp/datetime) até o início do intervalo de cinco minutos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-five-minutes.md
---

Arredonda para baixo uma data com hora (timestamp/datetime) até o início do intervalo de cinco minutos.

## Sintaxe do Analyze

```python
func.to_start_of_five_minutes(<expr>)
```

## Exemplos do Analyze

```python
func.to_start_of_five_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_five_minutes('2023-11-12 09:38:18.165575')    │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:35:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_START_OF_FIVE_MINUTES(<expr>)
```

## Argumentos

| Argumentos | Descrição   |
|-----------|-------------|
| `<expr>`  | timestamp   |

## Tipo de retorno

`TIMESTAMP`, retorna a data no formato “YYYY-MM-DD hh:mm:ss.ffffff”.

## Exemplos de SQL

```sql
SELECT
  to_start_of_five_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────┐
│ to_start_of_five_minutes('2023-11-12 09:38:18.165575') │
│                        Timestamp                       │
├────────────────────────────────────────────────────────┤
│ 2023-11-12 09:35:00                                    │
└────────────────────────────────────────────────────────┘
```
