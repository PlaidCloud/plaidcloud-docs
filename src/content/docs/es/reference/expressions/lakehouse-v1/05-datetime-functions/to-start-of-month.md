---
title: TO_START_OF_MONTH (Lakehouse v1)
description: TO_START_OF_MONTH — redondea hacia abajo una fecha, o fecha con hora (marca de tiempo/datetime), al primer día del mes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-month.md
---

Redondea hacia abajo una fecha, o fecha con hora (marca de tiempo/datetime), al primer día del mes.
Devuelve la fecha.

## Sintaxis de Analyze

```python
func.to_start_of_month(<expr>)
```

## Ejemplos de Analyze

```python
func.to_start_of_month('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_month('2023-11-12 09:38:18.165575')           │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_START_OF_MONTH(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<expr>`  | fecha/marca de tiempo |

## Tipo de valor devuelto

`DATE`, devuelve la fecha en el formato “YYYY-MM-DD”.

## Ejemplos de SQL

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
