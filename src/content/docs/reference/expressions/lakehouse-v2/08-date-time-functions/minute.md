---
title: MINUTE (Lakehouse v2)
description: MINUTE — returns the minute from a datetime.
---

Returns the minute from a datetime.

## Analyze Syntax

```python
func.minute(<datetime>)
```

## Analyze Examples

```python
func.minute('2024-06-15 14:30:00')

┌────┐
│ 30  │
└────┘
```

## SQL Syntax

```sql
MINUTE(<datetime>)
```

## SQL Examples

```sql
SELECT MINUTE('2024-06-15 14:30:00');

┌────┐
│ 30  │
└────┘
```
