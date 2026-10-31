---
title: TRY_TO_TIMESTAMP (Lakehouse v1)
description: TRY_TO_TIMESTAMP — una variante de TO_TIMESTAMP en PlaidCloud Lakehouse que, al realizar la misma conversión, devuelve NULL si falla.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/try-to-timestamp.md
---

Una variante de [TO_TIMESTAMP](../to-timestamp) en PlaidCloud Lakehouse que, aunque realiza la misma conversión de una expresión de entrada a una marca de tiempo, incorpora control de errores: devuelve NULL si la conversión falla, en lugar de generar un error.

Consulte también: [TO_TIMESTAMP](../to-timestamp)

## Sintaxis de Analyze

```python
func.try_to_timestamp(<expr>)
```

## Ejemplos de Analyze

```python
func.try_to_timestamp('2022-01-02 02:00:11'), func.try_to_datetime('2022-01-02 02:00:11'), func.try_to_timestamp('plaidcloud')
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.try_to_timestamp('2022-01-02 02:00:11') │ func.try_to_datetime('2022-01-02 02:00:11') │ func.try_to_timestamp('plaidcloud') │
│                Timestamp                │                Timestamp                         │                                     │
├─────────────────────────────────────────┼──────────────────────────────────────────────────┤─────────────────────────────────────│
│ 2022-01-02 02:00:11                     │ 2022-01-02 02:00:11                              │ NULL                                │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
-- Convert a string or integer to a timestamp
TRY_TO_TIMESTAMP(<expr>)

-- Convert a string to a timestamp using the given pattern
TRY_TO_TIMESTAMP(<expr, expr>)
```

## Alias

- [TRY_TO_DATETIME](../try-to-datetime)

## Ejemplos de SQL

```sql
SELECT TRY_TO_TIMESTAMP('2022-01-02 02:00:11'), TRY_TO_DATETIME('2022-01-02 02:00:11');

┌──────────────────────────────────────────────────────────────────────────────────┐
│ try_to_timestamp('2022-01-02 02:00:11') │ try_to_datetime('2022-01-02 02:00:11') │
│                Timestamp                │                Timestamp               │
├─────────────────────────────────────────┼────────────────────────────────────────┤
│ 2022-01-02 02:00:11                     │ 2022-01-02 02:00:11                    │
└──────────────────────────────────────────────────────────────────────────────────┘

SELECT TRY_TO_TIMESTAMP('databend'), TRY_TO_DATETIME('databend');

┌────────────────────────────────────────────────────────────┐
│ try_to_timestamp('databend') │ try_to_datetime('databend') │
├──────────────────────────────┼─────────────────────────────┤
│ NULL                         │ NULL                        │
└────────────────────────────────────────────────────────────┘
```
