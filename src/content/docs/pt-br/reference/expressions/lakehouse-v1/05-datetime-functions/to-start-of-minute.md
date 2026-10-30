---
title: TO_START_OF_MINUTE (Lakehouse v1)
description: TO_START_OF_MINUTE — arredonda para baixo uma data com hora (timestamp/datetime) até o início do minuto.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-minute.md
---

Arredonda para baixo uma data com hora (timestamp/datetime) até o início do minuto.

## Sintaxe do Analyze

```python
func.to_start_of_minute(<expr>)
```

## Exemplos do Analyze

```python
func.to_start_of_minute('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_minute('2023-11-12 09:38:18.165575')          │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:38:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_START_OF_MINUTE( <expr> )
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
  to_start_of_minute('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ to_start_of_minute('2023-11-12 09:38:18.165575') │
│                     Timestamp                    │
├──────────────────────────────────────────────────┤
│ 2023-11-12 09:38:00                              │
└──────────────────────────────────────────────────┘
```
