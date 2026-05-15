---
title: MONTHS_SUB (Lakehouse v2)
description: MONTHS_SUB — subtracts a specified number of months from a date.
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
