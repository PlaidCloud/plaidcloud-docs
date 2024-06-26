---
title: TO_YYYYMMDD
---

Converts a date or date with time (timestamp/datetime) to a UInt32 number containing the year and month number (YYYY * 10000 + MM * 100 + DD).

## Analyze Syntax

```python
func.to_yyyymmdd(<expr>)
```

## Analyze Examples

```python
func.to_yyyymmdd('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ func.to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                       │
├────────────────────────────────────────────────┤
│                                       20231112 │
└────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_YYYYMMDD(<expr>)
```

## Arguments

| Arguments | Description   |
|-----------|---------------|
| `<expr>`  | date/datetime |

## Return Type

`INT`, returns in `YYYYMMDD` format.

## SQL Examples

```sql
SELECT
  to_yyyymmdd('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────┐
│ to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                  │
├───────────────────────────────────────────┤
│                                  20231112 │
└───────────────────────────────────────────┘
```
