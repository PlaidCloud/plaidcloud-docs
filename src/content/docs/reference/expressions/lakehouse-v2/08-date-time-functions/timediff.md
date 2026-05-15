---
title: TIMEDIFF
description: TIMEDIFF — returns the difference between two time values - see syntax, examples, and output.
---

Returns the difference between two time values.

## Analyze Syntax

```python
func.timediff(<time1>, <time2>)
```

## Analyze Examples

```python
func.timediff('15:30:00', '10:00:00')

┌────────────┐
│ '05:30:00'  │
└────────────┘
```

## SQL Syntax

```sql
TIMEDIFF(<time1>, <time2>)
```

## SQL Examples

```sql
SELECT TIMEDIFF('15:30:00', '10:00:00');

┌──────────┐
│ 05:30:00  │
└──────────┘
```
