---
title: MINUTE
description: "Learn how to use the MINUTE date/time function in PlaidCloud Lakehouse. Returns the minute from a datetime - see syntax, examples, and output."
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
