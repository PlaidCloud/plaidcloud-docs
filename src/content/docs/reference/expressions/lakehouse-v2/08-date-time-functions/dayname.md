---
title: DAYNAME
description: DAYNAME — returns the name of the weekday for a date - see syntax, examples, and output.
---

Returns the name of the weekday for a date.

## Analyze Syntax

```python
func.dayname(<date>)
```

## Analyze Examples

```python
func.dayname('2024-06-15')

┌────────────┐
│ 'Saturday'  │
└────────────┘
```

## SQL Syntax

```sql
DAYNAME(<date>)
```

## SQL Examples

```sql
SELECT DAYNAME('2024-06-15');

┌──────────┐
│ Saturday  │
└──────────┘
```
