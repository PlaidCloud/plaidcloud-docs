---
title: TO_START_OF_MINUTE (Lakehouse v1)
description: TO_START_OF_MINUTE — redondea hacia abajo una fecha con hora (marca de tiempo/datetime) al inicio del minuto.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-minute.md
---

Redondea hacia abajo una fecha con hora (marca de tiempo/datetime) al inicio del minuto.

## Sintaxis de Analyze

```python
func.to_start_of_minute(<expr>)
```

## Ejemplos de Analyze

```python
func.to_start_of_minute('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_minute('2023-11-12 09:38:18.165575')          │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:38:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_START_OF_MINUTE( <expr> )
```

## Argumentos

| Argumentos | Descripción |
|-----------|-------------|
| `<expr>`  | marca de tiempo |

## Tipo de valor devuelto

`TIMESTAMP`, devuelve la fecha en el formato “YYYY-MM-DD hh:mm:ss.ffffff”.

## Ejemplos de SQL

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
