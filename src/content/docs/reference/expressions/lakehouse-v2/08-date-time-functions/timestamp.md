---
title: TIMESTAMP (Lakehouse v2)
description: TIMESTAMP — converts a date or string to a datetime.
---

Converts a date or string to a datetime.

## Analyze Syntax

```python
func.timestamp(<expr>)
```

## Analyze Examples

```python
func.timestamp('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
TIMESTAMP(<expr>)
```

## SQL Examples

```sql
SELECT TIMESTAMP('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```
