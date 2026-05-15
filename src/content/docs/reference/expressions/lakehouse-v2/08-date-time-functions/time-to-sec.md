---
title: TIME_TO_SEC
description: TIME_TO_SEC — converts a time value to seconds - see syntax, examples, and output.
---

Converts a time value to seconds.

## Analyze Syntax

```python
func.time_to_sec(<time>)
```

## Analyze Examples

```python
func.time_to_sec('01:01:01')

┌──────┐
│ 3661  │
└──────┘
```

## SQL Syntax

```sql
TIME_TO_SEC(<time>)
```

## SQL Examples

```sql
SELECT TIME_TO_SEC('01:01:01');

┌──────┐
│ 3661  │
└──────┘
```
