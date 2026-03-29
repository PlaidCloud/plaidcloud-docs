---
title: DAYS_SUB
---

Subtracts a specified number of days from a date.

## Analyze Syntax

```python
func.days_sub(<date>, <n>)
```

## Analyze Examples

```python
func.days_sub('2024-01-31', 30)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL Syntax

```sql
DAYS_SUB(<date>, <n>)
```

## SQL Examples

```sql
SELECT DAYS_SUB('2024-01-31', 30);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
