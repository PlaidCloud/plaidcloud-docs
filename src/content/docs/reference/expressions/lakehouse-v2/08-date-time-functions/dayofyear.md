---
title: DAYOFYEAR (Lakehouse v2)
description: DAYOFYEAR — returns the day of the year from a date.
---

Returns the day of the year from a date.

## Analyze Syntax

```python
func.dayofyear(<date>)
```

## Analyze Examples

```python
func.dayofyear('2024-06-15')

┌─────┐
│ 167  │
└─────┘
```

## SQL Syntax

```sql
DAYOFYEAR(<date>)
```

## SQL Examples

```sql
SELECT DAYOFYEAR('2024-06-15');

┌─────┐
│ 167  │
└─────┘
```
