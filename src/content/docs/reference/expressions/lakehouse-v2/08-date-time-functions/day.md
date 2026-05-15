---
title: DAY (Lakehouse v2)
description: DAY — returns the day of the month from a date.
---

Returns the day of the month from a date.

## Analyze Syntax

```python
func.day(<date>)
```

## Analyze Examples

```python
func.day('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## SQL Syntax

```sql
DAY(<date>)
```

## SQL Examples

```sql
SELECT DAY('2024-06-15');

┌────┐
│ 15  │
└────┘
```
