---
title: TO_MONDAY
---

Round down a date or date with time (timestamp/datetime) to the nearest Monday.
Returns the date.

## Analyze Syntax

```python
func.to_monday(<expr>)
```

## Analyze Examples

```python
func.to_monday('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_monday('2023-11-12 09:38:18.165575')       │
│                      Date                          │
├────────────────────────────────────────────────────┤
│ 2023-11-06                                         │
└────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_MONDAY(<expr>)
```

## Arguments

| Arguments   | Description |
| ----------- | ----------- |
| `<expr>` | date/timestamp |

## Return Type

`DATE`, returns date in “YYYY-MM-DD” format.

## SQL Examples

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
