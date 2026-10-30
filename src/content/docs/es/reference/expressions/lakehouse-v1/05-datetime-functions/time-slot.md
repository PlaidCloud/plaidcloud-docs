---
title: TIME_SLOT (Lakehouse v1)
description: TIME_SLOT — redondea la hora a la media hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/time-slot.md
---

Redondea la hora a la media hora.

## Sintaxis de Analyze

```python
func.time_slot(<expr>)
```

## Ejemplos de Analyze

```python
func.time_slot('2023-11-12 09:38:18.165575')
┌───────────────────────────────-───-───-──────┐
│ func.time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                     │
├─────────────────────────────────-───-────────┤
│ 2023-11-12 09:30:00                          │
└─────────────────────────────────-───-────────┘
```

## Sintaxis de SQL

```sql
time_slot(<expr>)
```

## Argumentos

| Argumentos  | Descripción |
| ----------- | ----------- |
| `<expr>`    | marca de tiempo |

## Tipo de valor devuelto

`TIMESTAMP`, se devuelve en el formato “YYYY-MM-DD hh:mm:ss.ffffff”.

## Ejemplos de SQL

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
