---
title: TO_DAY_OF_MONTH (Lakehouse v1)
description: TO_DAY_OF_MONTH — convierte una fecha, o fecha con hora (marca de tiempo/datetime), en un número UInt8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-month.md
---

Convierte una fecha, o fecha con hora (marca de tiempo/datetime), en un número UInt8 que contiene el número del día del mes (1-31).

## Sintaxis de Analyze

```python
func.to_day_of_month(<expr>)
```

## Ejemplos de Analyze

```python
func.now(), func.to_day_of_month(func.now()), func.day(func.now())

┌──────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_day_of_month(func.now()) │ func.day(func.now()) │
├────────────────────────────┼──────────────────────────────────┼──────────────────────┤
│ 2024-03-14 23:35:41.947962 │                               14 │                   14 │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_DAY_OF_MONTH(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<expr>`  | fecha/marca de tiempo |

## Alias

- [DAY](../day)

## Tipo de valor devuelto

`TINYINT`

## Ejemplos de SQL

```sql
SELECT NOW(), TO_DAY_OF_MONTH(NOW()), DAY(NOW());

┌──────────────────────────────────────────────────────────────────┐
│            now()           │ to_day_of_month(now()) │ day(now()) │
├────────────────────────────┼────────────────────────┼────────────┤
│ 2024-03-14 23:35:41.947962 │                     14 │         14 │
└──────────────────────────────────────────────────────────────────┘
```
