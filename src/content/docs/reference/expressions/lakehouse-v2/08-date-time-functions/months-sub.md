---
title: MONTHS_SUB
description: "Learn how to use the MONTHS_SUB date/time function in PlaidCloud Lakehouse. Subtracts a specified number of months from a date - with syntax and examples."
---

Subtracts a specified number of months from a date.

## Analyze Syntax

```python
func.months_sub(<date>, <n>)
```

## Analyze Examples

```python
func.months_sub('2024-06-15', 3)

┌──────────────┐
│ '2024-03-15'  │
└──────────────┘
```

## SQL Syntax

```sql
MONTHS_SUB(<date>, <n>)
```

## SQL Examples

```sql
SELECT MONTHS_SUB('2024-06-15', 3);

┌────────────┐
│ 2024-03-15  │
└────────────┘
```
