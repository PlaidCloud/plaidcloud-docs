---
title: WEEKS_SUB (Lakehouse v2)
description: WEEKS_SUB — subtracts a specified number of weeks from a date.
---

Subtracts a specified number of weeks from a date.

## Analyze Syntax

```python
func.weeks_sub(<date>, <n>)
```

## Analyze Examples

```python
func.weeks_sub('2024-01-15', 2)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL Syntax

```sql
WEEKS_SUB(<date>, <n>)
```

## SQL Examples

```sql
SELECT WEEKS_SUB('2024-01-15', 2);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
