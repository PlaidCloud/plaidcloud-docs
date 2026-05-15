---
title: PREVIOUS_DAY (Lakehouse v2)
description: PREVIOUS_DAY — returns the date of the previous specified weekday before a given date.
---

Returns the date of the previous specified weekday before a given date.

## Analyze Syntax

```python
func.previous_day(<date>, <weekday>)
```

## Analyze Examples

```python
func.previous_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-10'  │
└──────────────┘
```

## SQL Syntax

```sql
PREVIOUS_DAY(<date>, <weekday>)
```

## SQL Examples

```sql
SELECT PREVIOUS_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-10  │
└────────────┘
```
