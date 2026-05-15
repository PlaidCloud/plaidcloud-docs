---
title: CURRENT_TIMESTAMP (Lakehouse v2)
description: CURRENT_TIMESTAMP — returns the current date and time.
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
