---
title: TO_START_OF_TEN_MINUTES
description: "Learn how to use the TO_START_OF_TEN_MINUTES datetime function in PlaidCloud Lakehouse. Rounds down a date with time (timestamp/datetime) to the start of..."
---

Rounds down a date with time (timestamp/datetime) to the start of the ten-minute interval.

## Analyze Syntax

```python
func.to_start_of_ten_minutes(<expr>)
```

## Analyze Examples

```python
func.to_start_of_ten_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_ten_minutes('2023-11-12 09:38:18.165575')     │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:30:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_START_OF_TEN_MINUTES(<expr>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<expr>`  | timestamp   |

## Return Type

`TIMESTAMP`, returns date in “YYYY-MM-DD hh:mm:ss.ffffff” format.

## SQL Examples

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
