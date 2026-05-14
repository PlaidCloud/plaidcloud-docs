---
title: LOG10
description: "Learn how to use the LOG10 numeric function in PlaidCloud Lakehouse. Returns the base-10 logarithm of x. Reference with syntax and examples."
---

Returns the base-10 logarithm of `x`. If `x` is less than or equal to 0.0E0, the function returns NULL.


## Analyze Syntax

```python
func.log10( <x> )
```

## Analyze Examples

```python
func.log10(100)

┌─────────────────┐
│ func.log10(100) │
├─────────────────┤
│               2 │
└─────────────────┘
```

## SQL Syntax

```sql
LOG10( <x> )
```

## SQL Examples

```sql
SELECT LOG10(100);

┌────────────┐
│ log10(100) │
├────────────┤
│          2 │
└────────────┘
```
