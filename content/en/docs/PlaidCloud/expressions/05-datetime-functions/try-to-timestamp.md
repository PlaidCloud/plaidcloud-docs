---
title: TRY_TO_TIMESTAMP
---

A variant of [TO_TIMESTAMP](to-timestamp) in PlaidCloud Lakehouse that, while performing the same conversion of an input expression to a timestamp, incorporates error-handling support by returning NULL if the conversion fails instead of raising an error.

See also: [TO_TIMESTAMP](to-timestamp)

## Analyze Syntax

```python
func.try_to_timestamp(<expr>)
```

## Analyze Examples

```python
func.try_to_timestamp('2022-01-02 02:00:11'), func.try_to_datetime('2022-01-02 02:00:11'), func.try_to_timestamp('plaidcloud')
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.try_to_timestamp('2022-01-02 02:00:11') │ func.try_to_datetime('2022-01-02 02:00:11') │ func.try_to_timestamp('plaidcloud') │
│                Timestamp                │                Timestamp                         │                                     │
├─────────────────────────────────────────┼──────────────────────────────────────────────────┤─────────────────────────────────────│
│ 2022-01-02 02:00:11                     │ 2022-01-02 02:00:11                              │ NULL                                │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
-- Convert a string or integer to a timestamp
TRY_TO_TIMESTAMP(<expr>)

-- Convert a string to a timestamp using the given pattern
TRY_TO_TIMESTAMP(<expr, expr>)
```

## Aliases

- [TRY_TO_DATETIME](try-to-datetime)

## SQL Examples

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