---
title: FIELD (Lakehouse v2)
description: FIELD — Returns the index position of a value in a list of arguments.
---

Returns the index position of a value in a list of arguments.

## Analyze Syntax

```python
func.field(<str>, <val1>, <val2>[, ...])
```

## Analyze Examples

```python
func.field('b', 'a', 'b', 'c')

┌───┐
│ 2  │
└───┘
```

## SQL Syntax

```sql
FIELD(<str>, <val1>, <val2>[, ...])
```

## SQL Examples

```sql
SELECT FIELD('b', 'a', 'b', 'c');

┌───┐
│ 2  │
└───┘
```
