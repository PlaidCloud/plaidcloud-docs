---
title: MONTHS_ADD
---

Adds a specified number of months to a date.

## Analyze Syntax

```python
func.months_add(<date>, <n>)
```

## Analyze Examples

```python
func.months_add('2024-01-15', 3)

┌──────────────┐
│ '2024-04-15'  │
└──────────────┘
```

## SQL Syntax

```sql
MONTHS_ADD(<date>, <n>)
```

## SQL Examples

```sql
SELECT MONTHS_ADD('2024-01-15', 3);

┌────────────┐
│ 2024-04-15  │
└────────────┘
```
