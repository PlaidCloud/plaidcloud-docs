---
title: TO_DATETIME
description: "Learn how to use the TO_DATETIME date/time function in PlaidCloud Lakehouse. Converts a value to a datetime - see syntax, examples, and output."
---

Converts a value to a datetime.

## Analyze Syntax

```python
func.to_datetime(<expr>)
```

## Analyze Examples

```python
func.to_datetime('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
TO_DATETIME(<expr>)
```

## SQL Examples

```sql
SELECT TO_DATETIME('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```
