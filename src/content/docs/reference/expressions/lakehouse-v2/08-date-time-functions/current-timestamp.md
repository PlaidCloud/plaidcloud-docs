---
title: CURRENT_TIMESTAMP
description: "Learn how to use the CURRENT_TIMESTAMP date/time function in PlaidCloud Lakehouse. Returns the current date and time - see syntax, examples, and output."
---

Returns the current date and time.

## Analyze Syntax

```python
func.current_timestamp()
```

## Analyze Examples

```python
func.current_timestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
CURRENT_TIMESTAMP()
```

## SQL Examples

```sql
SELECT CURRENT_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
