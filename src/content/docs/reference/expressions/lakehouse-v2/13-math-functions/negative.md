---
title: NEGATIVE (Lakehouse v2)
description: NEGATIVE — returns the negation of a number.
---

Returns the negation of a number.

## Analyze Syntax

```python
func.negative(<x>)
```

## Analyze Examples

```python
func.negative(5)

┌────┐
│ -5  │
└────┘
```

## SQL Syntax

```sql
NEGATIVE(<x>)
```

## SQL Examples

```sql
SELECT NEGATIVE(5);

┌────┐
│ -5  │
└────┘
```
