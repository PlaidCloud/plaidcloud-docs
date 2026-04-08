---
title: YEARS_ADD
description: "Learn how to use the YEARS_ADD date/time function in PlaidCloud Lakehouse. Adds a specified number of years to a date - see syntax, examples, and output."
---

Adds a specified number of years to a date.

## Analyze Syntax

```python
func.years_add(<date>, <n>)
```

## Analyze Examples

```python
func.years_add('2024-01-01', 5)

┌──────────────┐
│ '2029-01-01'  │
└──────────────┘
```

## SQL Syntax

```sql
YEARS_ADD(<date>, <n>)
```

## SQL Examples

```sql
SELECT YEARS_ADD('2024-01-01', 5);

┌────────────┐
│ 2029-01-01  │
└────────────┘
```
