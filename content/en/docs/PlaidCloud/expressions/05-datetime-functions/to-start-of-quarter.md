---
title: TO_START_OF_QUARTER
---

Rounds down a date or date with time (timestamp/datetime) to the first day of the quarter.
The first day of the quarter is either 1 January, 1 April, 1 July, or 1 October.
Returns the date.

## Analyze Syntax

```python
func.to_start_of_quarter(<expr>)
```

## Analyze Examples

```python
func.to_start_of_quarter('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_quarter('2023-11-12 09:38:18.165575')         │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-10-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_START_OF_QUARTER(<expr>)
```

## Arguments

| Arguments | Description    |
|-----------|----------------|
| `<expr>`   | date/timestamp |

## Return Type

`DATE`, returns date in “YYYY-MM-DD” format.

## SQL Examples

```sql
SELECT
  to_start_of_quarter('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────┐
│ to_start_of_quarter('2023-11-12 09:38:18.165575') │
│                        Date                       │
├───────────────────────────────────────────────────┤
│ 2023-10-01                                        │
└───────────────────────────────────────────────────┘
```
