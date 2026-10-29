---
title: TRY_TO_TIMESTAMP (Lakehouse v1)
description: TRY_TO_TIMESTAMP — wariant funkcji TO_TIMESTAMP w PlaidCloud Lakehouse, który wykonuje tę samą konwersję, ale zwraca NULL zamiast błędu, gdy konwersja się nie powiedzie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/try-to-timestamp.md
---

Wariant funkcji [TO_TIMESTAMP](../to-timestamp) w PlaidCloud Lakehouse, który wykonuje tę samą konwersję wyrażenia wejściowego na timestamp, ale obsługuje błędy: jeśli konwersja się nie powiedzie, zwraca NULL zamiast zgłaszać błąd.

Zobacz także: [TO_TIMESTAMP](../to-timestamp)

## Składnia Analyze

```python
func.try_to_timestamp(<expr>)
```

## Przykłady Analyze

```python
func.try_to_timestamp('2022-01-02 02:00:11'), func.try_to_datetime('2022-01-02 02:00:11'), func.try_to_timestamp('plaidcloud')
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.try_to_timestamp('2022-01-02 02:00:11') │ func.try_to_datetime('2022-01-02 02:00:11') │ func.try_to_timestamp('plaidcloud') │
│                Timestamp                │                Timestamp                         │                                     │
├─────────────────────────────────────────┼──────────────────────────────────────────────────┤─────────────────────────────────────│
│ 2022-01-02 02:00:11                     │ 2022-01-02 02:00:11                              │ NULL                                │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
-- Convert a string or integer to a timestamp
TRY_TO_TIMESTAMP(<expr>)

-- Convert a string to a timestamp using the given pattern
TRY_TO_TIMESTAMP(<expr, expr>)
```

## Aliasy

- [TRY_TO_DATETIME](../try-to-datetime)

## Przykłady SQL

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
