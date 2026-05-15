---
title: CURRENT_TIME (Lakehouse v2)
description: CURRENT_TIME — returns the current time.
---

Returns the current time.

## Analyze Syntax

```python
func.current_time()
```

## Analyze Examples

```python
func.current_time()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## SQL Syntax

```sql
CURRENT_TIME()
```

## SQL Examples

```sql
SELECT CURRENT_TIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```
