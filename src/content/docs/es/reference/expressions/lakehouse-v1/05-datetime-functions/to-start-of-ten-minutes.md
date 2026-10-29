---
title: TO_START_OF_TEN_MINUTES (Lakehouse v1)
description: TO_START_OF_TEN_MINUTES — redondea hacia abajo una fecha con hora (marca de tiempo) al inicio del intervalo de diez minutos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-ten-minutes.md
---

Redondea hacia abajo una fecha con hora (marca de tiempo/datetime) al inicio del intervalo de diez minutos.

## Sintaxis de Analyze

```python
func.to_start_of_ten_minutes(<expr>)
```

## Ejemplos de Analyze

```python
func.to_start_of_ten_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_ten_minutes('2023-11-12 09:38:18.165575')     │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:30:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_START_OF_TEN_MINUTES(<expr>)
```

## Argumentos

| Argumentos | Descripción |
|-----------|-------------|
| `<expr>`  | marca de tiempo |

## Tipo de retorno

`TIMESTAMP`, devuelve la fecha en formato “YYYY-MM-DD hh:mm:ss.ffffff”.

## Ejemplos de SQL

```sql
SELECT
  to_start_of_ten_minutes('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────────┐
│ to_start_of_ten_minutes('2023-11-12 09:38:18.165575') │
│                       Timestamp                       │
├───────────────────────────────────────────────────────┤
│ 2023-11-12 09:30:00                                   │
└───────────────────────────────────────────────────────┘
```
