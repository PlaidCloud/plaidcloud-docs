---
title: FIND_IN_SET
description: FIND_IN_SET — returns the position of a string within a comma-separated list.
---

Returns the position of a string within a comma-separated list.

## Analyze Syntax

```python
func.find_in_set(<str>, <strlist>)
```

## Analyze Examples

```python
func.find_in_set('b', 'a,b,c')

┌───┐
│ 2  │
└───┘
```

## SQL Syntax

```sql
FIND_IN_SET(<str>, <strlist>)
```

## SQL Examples

```sql
SELECT FIND_IN_SET('b', 'a,b,c');

┌───┐
│ 2  │
└───┘
```
