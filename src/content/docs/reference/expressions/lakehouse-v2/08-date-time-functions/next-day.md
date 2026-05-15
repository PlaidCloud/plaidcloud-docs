---
title: NEXT_DAY (Lakehouse v2)
description: NEXT_DAY — returns the date of the next specified weekday after a given date.
---

Returns the date of the next specified weekday after a given date.

## Analyze Syntax

```python
func.next_day(<date>, <weekday>)
```

## Analyze Examples

```python
func.next_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-17'  │
└──────────────┘
```

## SQL Syntax

```sql
NEXT_DAY(<date>, <weekday>)
```

## SQL Examples

```sql
SELECT NEXT_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-17  │
└────────────┘
```
