---
title: TIME_FORMAT
description: "Learn how to use the TIME_FORMAT date/time function in PlaidCloud Lakehouse. Formats a time value according to a format string - with syntax and examples."
---

Formats a time value according to a format string.

## Analyze Syntax

```python
func.time_format(<time>, <format>)
```

## Analyze Examples

```python
func.time_format('14:30:00', '%H hours %i minutes')

┌───────────────────────┐
│ '14 hours 30 minutes'  │
└───────────────────────┘
```

## SQL Syntax

```sql
TIME_FORMAT(<time>, <format>)
```

## SQL Examples

```sql
SELECT TIME_FORMAT('14:30:00', '%H hours %i minutes');

┌─────────────────────┐
│ 14 hours 30 minutes  │
└─────────────────────┘
```
