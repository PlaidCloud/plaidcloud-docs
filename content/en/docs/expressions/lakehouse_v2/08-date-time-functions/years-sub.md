---
title: YEARS_SUB
description: "Learn how to use the YEARS_SUB date/time function in PlaidCloud Lakehouse. Subtracts a specified number of years from a date - with syntax and examples."
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
