---
title: DATE
---

Extracts the date part from a datetime expression.

## Analyze Syntax

```python
func.date(<datetime>)
```

## Analyze Examples

```python
func.date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL Syntax

```sql
DATE(<datetime>)
```

## SQL Examples

```sql
SELECT DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
