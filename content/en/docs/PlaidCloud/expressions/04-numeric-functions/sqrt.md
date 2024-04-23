---
title: SQRT
---

Returns the square root of a nonnegative number `x`. Returns Nan for negative input.

## Analyze Syntax

```python
func.sqrt( <x> )
```

## Analyze Examples

```python
func.sqrt(4)

┌──────────────┐
│ func.sqrt(4) │
├──────────────┤
│            2 │
└──────────────┘
```

## SQL Syntax

```sql
SQRT( <x> )
```

## SQL Examples

```sql
SELECT SQRT(4);

┌─────────┐
│ sqrt(4) │
├─────────┤
│       2 │
└─────────┘
```