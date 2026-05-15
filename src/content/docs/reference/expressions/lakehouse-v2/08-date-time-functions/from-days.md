---
title: FROM_DAYS (Lakehouse v2)
description: FROM_DAYS — converts a day count to a date.
---

Converts a day count to a date.

## Analyze Syntax

```python
func.from_days(<n>)
```

## Analyze Examples

```python
func.from_days(738886)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL Syntax

```sql
FROM_DAYS(<n>)
```

## SQL Examples

```sql
SELECT FROM_DAYS(738886);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
