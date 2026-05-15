---
title: WEEK (Lakehouse v2)
description: WEEK — returns the week number of the year for a date.
---

Returns the week number of the year for a date.

## Analyze Syntax

```python
func.week(<date>[, <mode>])
```

## Analyze Examples

```python
func.week('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQL Syntax

```sql
WEEK(<date>[, <mode>])
```

## SQL Examples

```sql
SELECT WEEK('2024-06-15');

┌────┐
│ 24  │
└────┘
```
