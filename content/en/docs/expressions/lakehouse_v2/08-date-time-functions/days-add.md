---
title: DAYS_ADD
---

Adds a specified number of days to a date.

## Analyze Syntax

```python
func.days_add(<date>, <n>)
```

## Analyze Examples

```python
func.days_add('2024-01-01', 30)

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## SQL Syntax

```sql
DAYS_ADD(<date>, <n>)
```

## SQL Examples

```sql
SELECT DAYS_ADD('2024-01-01', 30);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
