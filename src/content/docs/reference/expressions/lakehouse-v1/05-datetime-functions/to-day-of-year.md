---
title: TO_DAY_OF_YEAR
description: "Learn how to use the TO_DAY_OF_YEAR datetime function in PlaidCloud Lakehouse. Convert a date or date with time (timestamp/datetime) to a UInt16 number..."
---

Convert a date or date with time (timestamp/datetime) to a UInt16 number containing the number of the day of the year (1-366).

## Analyze Syntax

```python
func.to_day_of_year(<expr>)
```

## Analyze Examples

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_year('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                316 │
└────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_DAY_OF_YEAR(<expr>)
```

## Arguments

| Arguments   | Description |
| ----------- | ----------- |
| `<expr>` | date/timestamp |

## Return Type

`SMALLINT`

## SQL Examples

```sql
SELECT
    to_day_of_year('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ to_day_of_year('2023-11-12 09:38:18.165575') │
│                    UInt16                    │
├──────────────────────────────────────────────┤
│                                          316 │
└──────────────────────────────────────────────┘
```
