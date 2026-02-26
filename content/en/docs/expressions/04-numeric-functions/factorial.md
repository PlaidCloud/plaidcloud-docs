---
title: FACTORIAL
---

Returns the factorial logarithm of `x`. If `x` is less than or equal to 0, the function returns 0.

## Analyze Syntax

```python
func.factorial( <x> )
```

## Analyze Examples

```python
func.factorial(5)

┌───────────────────┐
│ func.factorial(5) │
├───────────────────┤
│               120 │
└───────────────────┘
```

## SQL Syntax

```sql
FACTORIAL( <x> )
```

## SQL Examples

```sql
SELECT FACTORIAL(5);

┌──────────────┐
│ factorial(5) │
├──────────────┤
│          120 │
└──────────────┘
```