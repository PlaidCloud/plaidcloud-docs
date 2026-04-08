---
title: WEEKS_ADD
description: "Learn how to use the WEEKS_ADD date/time function in PlaidCloud Lakehouse. Adds a specified number of weeks to a date - see syntax, examples, and output."
---

Adds a specified number of weeks to a date.

## Analyze Syntax

```python
func.weeks_add(<date>, <n>)
```

## Analyze Examples

```python
func.weeks_add('2024-01-01', 2)

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## SQL Syntax

```sql
WEEKS_ADD(<date>, <n>)
```

## SQL Examples

```sql
SELECT WEEKS_ADD('2024-01-01', 2);

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
