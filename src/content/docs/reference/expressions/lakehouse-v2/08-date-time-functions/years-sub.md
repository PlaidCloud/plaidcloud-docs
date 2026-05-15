---
title: YEARS_SUB (Lakehouse v2)
description: YEARS_SUB — subtracts a specified number of years from a date.
---

Subtracts a specified number of years from a date.

## Analyze Syntax

```python
func.years_sub(<date>, <n>)
```

## Analyze Examples

```python
func.years_sub('2029-01-01', 5)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL Syntax

```sql
YEARS_SUB(<date>, <n>)
```

## SQL Examples

```sql
SELECT YEARS_SUB('2029-01-01', 5);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
