---
title: TO_YYYYMMDDHH
---

Formats a given date or timestamp into a string representation in the format "YYYYMMDDHH" (Year, Month, Day, Hour).

## Analyze Syntax

```python
func.to_yyyymmddhh(<expr>)
```

## Analyze Examples

```python
func.to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ func.to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                   UInt32                         │
├──────────────────────────────────────────────────┤
│                                       2023111209 │
└──────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_YYYYMMDDHH(<expr>)
```

## Arguments

| Arguments | Description   |
|-----------|---------------|
| `<expr>`  | date/datetime |

## Return Type

Returns an unsigned 64-bit integer (UInt64) in the format "YYYYMMDDHH".

## SQL Examples

```sql
SELECT
  to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────┐
│ to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                    UInt32                   │
├─────────────────────────────────────────────┤
│                                  2023111209 │
└─────────────────────────────────────────────┘
```