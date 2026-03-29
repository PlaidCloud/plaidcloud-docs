---
title: TO_DATE
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
