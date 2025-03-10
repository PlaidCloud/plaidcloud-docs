---
title: TO_MINUTE
---

Converts a date with time (timestamp/datetime) to a UInt8 number containing the number of the minute of the hour (0-59).


## Analyze Syntax

```python
func.to_minute(<expr>)
```

## Analyze Examples

```python
func.to_minute('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_minute('2023-11-12 09:38:18.165575')       │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                 38 │
└────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_MINUTE(<expr>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<expr>`  | timestamp   |

## Return Type

 `TINYINT`

## SQL Examples

```sql
SELECT
    to_minute('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_minute('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      38 │
└─────────────────────────────────────────┘
```
