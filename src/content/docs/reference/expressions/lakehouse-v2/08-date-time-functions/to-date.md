---
title: TO_DATE
description: "Learn how to use the TO_DATE date/time function in PlaidCloud Lakehouse. Converts a datetime to a date - see syntax, examples, and output."
---

Converts a datetime to a date.

## Analyze Syntax

```python
func.to_date(<datetime>)
```

## Analyze Examples

```python
func.to_date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL Syntax

```sql
TO_DATE(<datetime>)
```

## SQL Examples

```sql
SELECT TO_DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
