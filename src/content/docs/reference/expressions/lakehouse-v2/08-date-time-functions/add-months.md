---
title: ADD_MONTHS
description: ADD_MONTHS — adds a specified number of months to a date - see syntax, examples, and output.
---

Adds a specified number of months to a date.

## Analyze Syntax

```python
func.add_months(<date>, <months>)
```

## Analyze Examples

```python
func.add_months('2024-01-31', 1)

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## SQL Syntax

```sql
ADD_MONTHS(<date>, <months>)
```

## SQL Examples

```sql
SELECT ADD_MONTHS('2024-01-31', 1);

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
