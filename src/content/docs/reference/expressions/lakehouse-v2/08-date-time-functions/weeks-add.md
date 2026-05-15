---
title: WEEKS_ADD (Lakehouse v2)
description: WEEKS_ADD — adds a specified number of weeks to a date.
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
