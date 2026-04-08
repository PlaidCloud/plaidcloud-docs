---
title: ALL_MATCH
description: "Learn how to use the ALL_MATCH array function in PlaidCloud Lakehouse. Returns TRUE if all elements in an array match the given predicate."
---

Returns TRUE if all elements in an array match the given predicate.

## Analyze Syntax

```python
func.all_match(get_column(table, 'arr'), lambda x: x > 0)
```

## Analyze Examples

```python
func.all_match([1, 2, 3], lambda x: x > 0)

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
ALL_MATCH(<arr>, lambda x: x > 0)
```

## SQL Examples

```sql
SELECT ALL_MATCH([1, 2, 3], x -> x > 0);

┌───┐
│ 1 │
└───┘
```
