---
title: TO_MONDAY (Lakehouse v1)
description: TO_MONDAY — redondea hacia abajo una fecha, o fecha con hora (marca de tiempo/datetime), al lunes más cercano.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-monday.md
---

Redondea hacia abajo una fecha, o fecha con hora (marca de tiempo/datetime), al lunes más cercano.
Devuelve la fecha.

## Sintaxis de Analyze

```python
func.to_monday(<expr>)
```

## Ejemplos de Analyze

```python
func.to_monday('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_monday('2023-11-12 09:38:18.165575')       │
│                      Date                          │
├────────────────────────────────────────────────────┤
│ 2023-11-06                                         │
└────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_MONDAY(<expr>)
```

## Argumentos

| Argumentos  | Descripción |
| ----------- | ----------- |
| `<expr>` | fecha/marca de tiempo |

## Tipo de valor devuelto

`DATE`, devuelve la fecha en el formato “YYYY-MM-DD”.

## Ejemplos de SQL

```sql
SELECT
    to_monday('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_monday('2023-11-12 09:38:18.165575') │
│                   Date                  │
├─────────────────────────────────────────┤
│ 2023-11-06                              │
└─────────────────────────────────────────┘
```
