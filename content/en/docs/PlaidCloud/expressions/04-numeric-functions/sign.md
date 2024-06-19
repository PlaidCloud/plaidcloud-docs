---
title: SIGN
---

Returns the sign of the argument as -1, 0, or 1, depending on whether `x` is negative, zero, or positive or NULL if the argument was NULL.

## Analyze Syntax

```python
func.sign( <x> )
```

## Analyze Examples

```python
func.sign(0)

┌──────────────┐
│ func.sign(0) │
├──────────────┤
│            0 │
└──────────────┘
```

## SQL Syntax

```sql
SIGN( <x> )
```

## SQL Examples

```sql
SELECT SIGN(0);

┌─────────┐
│ sign(0) │
├─────────┤
│       0 │
└─────────┘
```