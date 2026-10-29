---
title: TO_DAY_OF_WEEK (Lakehouse v1)
description: TO_DAY_OF_WEEK — convierte una fecha, o fecha con hora (marca de tiempo/datetime), en un número UInt8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-week.md
---

Convierte una fecha, o fecha con hora (marca de tiempo/datetime), en un número UInt8 que contiene el número del día de la semana (el lunes es 1 y el domingo es 7).

## Sintaxis de Analyze

```python
func.to_day_of_week(<expr>)
```

## Ejemplos de Analyze

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_week('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  7 │
└────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_DAY_OF_WEEK(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<expr>`  | fecha/marca de tiempo |

## Tipo de valor devuelto

``TINYINT`

## Ejemplos de SQL

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
