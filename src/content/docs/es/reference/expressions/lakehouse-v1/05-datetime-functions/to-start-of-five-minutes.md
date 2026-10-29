---
title: TO_START_OF_FIVE_MINUTES (Lakehouse v1)
description: TO_START_OF_FIVE_MINUTES — redondea hacia abajo una fecha con hora (marca de tiempo/datetime) al inicio del intervalo de cinco minutos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-five-minutes.md
---

Redondea hacia abajo una fecha con hora (marca de tiempo/datetime) al inicio del intervalo de cinco minutos.

## Sintaxis de Analyze

```python
func.to_start_of_five_minutes(<expr>)
```

## Ejemplos de Analyze

```python
func.to_start_of_five_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_five_minutes('2023-11-12 09:38:18.165575')    │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:35:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_START_OF_FIVE_MINUTES(<expr>)
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
  to_start_of_five_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────┐
│ to_start_of_five_minutes('2023-11-12 09:38:18.165575') │
│                        Timestamp                       │
├────────────────────────────────────────────────────────┤
│ 2023-11-12 09:35:00                                    │
└────────────────────────────────────────────────────────┘
```
