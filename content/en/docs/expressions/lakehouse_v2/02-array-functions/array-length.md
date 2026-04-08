---
title: ARRAY_LENGTH
description: "Learn how to use the ARRAY_LENGTH array function in PlaidCloud Lakehouse. Returns the number of elements in an array - see syntax, examples, and output."
---

Returns the number of elements in an array.

## Analyze Syntax

```python
func.array_length([1, 2, 3])
```

## Analyze Examples

```python
func.array_length([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## SQL Syntax

```sql
ARRAY_LENGTH([1, 2, 3])
```

## SQL Examples

```sql
SELECT ARRAY_LENGTH([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
