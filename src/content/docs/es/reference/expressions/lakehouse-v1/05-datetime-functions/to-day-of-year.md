---
title: TO_DAY_OF_YEAR (Lakehouse v1)
description: TO_DAY_OF_YEAR — convierte una fecha, o fecha con hora (marca de tiempo/datetime), en un número UInt16.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-year.md
---

Convierte una fecha, o fecha con hora (marca de tiempo/datetime), en un número UInt16 que contiene el número del día del año (1-366).

## Sintaxis de Analyze

```python
func.to_day_of_year(<expr>)
```

## Ejemplos de Analyze

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_year('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                316 │
└────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_DAY_OF_YEAR(<expr>)
```

## Argumentos

| Argumentos  | Descripción |
| ----------- | ----------- |
| `<expr>` | fecha/marca de tiempo |

## Tipo de valor devuelto

`SMALLINT`

## Ejemplos de SQL

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
