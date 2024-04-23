---
title: MODULO
---

Returns the remainder of `x` divided by `y`. If `y` is 0, it returns an error.

## Analyze Syntax

```python
func.modulo( <x>, <y> )
```

## Analyze Examples

```python
func.modulo(9, 2)

┌───────────────────┐
│ func.modulo(9, 2) │
├───────────────────┤
│                 1 │
└───────────────────┘
```

## SQL Syntax

```sql
MODULO( <x>, <y> )
```

## Aliases

- [MOD](../mod)

## SQL Examples

```sql
SELECT MOD(9, 2), MODULO(9, 2);

┌──────────────────────────┐
│ mod(9, 2) │ modulo(9, 2) │
├───────────┼──────────────┤
│         1 │            1 │
└──────────────────────────┘
```