---
title: FIELD
description: "Learn how to use the FIELD string function in PlaidCloud Lakehouse. Returns the index position of a value in a list of arguments - with syntax and examples."
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
