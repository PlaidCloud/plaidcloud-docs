---
title: LEAST (Lakehouse v2)
description: LEAST — returns the smallest value from a list of values.
---

Returns the smallest value from a list of values.

## Analyze Syntax

```python
func.least(<val1>, <val2>[, ...])
```

## Analyze Examples

```python
func.least(3, 7, 1, 9, 4)

┌───┐
│ 1  │
└───┘
```

## SQL Syntax

```sql
LEAST(<val1>, <val2>[, ...])
```

## SQL Examples

```sql
SELECT LEAST(3, 7, 1, 9, 4);

┌───┐
│ 1  │
└───┘
```
