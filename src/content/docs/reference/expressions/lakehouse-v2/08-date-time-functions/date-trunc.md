---
title: DATE_TRUNC
description: DATE_TRUNC — truncates a date or datetime value to the specified precision.
---

Truncates a date or datetime value to the specified precision.

## Analyze Syntax

```python
func.date_trunc(<unit>, <datetime>)
```

## Analyze Examples

```python
func.date_trunc('MONTH', '2024-06-15')

┌──────────────┐
│ '2024-06-01'  │
└──────────────┘
```

## SQL Syntax

```sql
DATE_TRUNC(<unit>, <datetime>)
```

## SQL Examples

```sql
SELECT DATE_TRUNC('MONTH', '2024-06-15');

┌────────────┐
│ 2024-06-01  │
└────────────┘
```
