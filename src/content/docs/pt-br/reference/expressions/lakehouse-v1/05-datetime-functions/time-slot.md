---
title: TIME_SLOT (Lakehouse v1)
description: TIME_SLOT — arredonda a hora para a meia hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/time-slot.md
---

Arredonda a hora para a meia hora.

## Sintaxe do Analyze

```python
func.time_slot(<expr>)
```

## Exemplos do Analyze

```python
func.time_slot('2023-11-12 09:38:18.165575')
┌───────────────────────────────-───-───-──────┐
│ func.time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                     │
├─────────────────────────────────-───-────────┤
│ 2023-11-12 09:30:00                          │
└─────────────────────────────────-───-────────┘
```

## Sintaxe SQL

```sql
time_slot(<expr>)
```

## Argumentos

| Argumentos  | Descrição   |
| ----------- | ----------- |
| `<expr>`    | timestamp   |

## Tipo de retorno

`TIMESTAMP`, retornado no formato “YYYY-MM-DD hh:mm:ss.ffffff”.

## Exemplos de SQL

```sql
SELECT
  time_slot('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                │
├─────────────────────────────────────────┤
│ 2023-11-12 09:30:00                     │
└─────────────────────────────────────────┘
```
