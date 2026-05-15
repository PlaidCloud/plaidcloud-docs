---
title: TO_DAYS (Lakehouse v2)
description: TO_DAYS — converts a date to a day count.
---

Converts a date to a day count.

## Analyze Syntax

```python
func.to_days(<date>)
```

## Analyze Examples

```python
func.to_days('2024-01-01')

┌────────┐
│ 738886  │
└────────┘
```

## SQL Syntax

```sql
TO_DAYS(<date>)
```

## SQL Examples

```sql
SELECT TO_DAYS('2024-01-01');

┌────────┐
│ 738886  │
└────────┘
```
