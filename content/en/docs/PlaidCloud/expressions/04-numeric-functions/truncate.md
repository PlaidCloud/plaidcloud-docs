---
title: TRUNCATE
---

Returns the number `x`, truncated to `d` decimal places. If `d` is 0, the result has no decimal point or fractional part. `d` can be negative to cause `d` digits left of the decimal point of the value `x` to become zero. The maximum absolute value for `d` is 30; any digits in excess of 30 (or -30) are truncated.

## Analyze Syntax

```python
func.truncate( <x, d> )
```

## Analyze Examples

```python
func.truncate(1.223, 1)

┌─────────────────────────┐
│ func.truncate(1.223, 1) │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQL Syntax

```sql
TRUNCATE( <x, d> )
```

## SQL Examples

```sql
SELECT TRUNCATE(1.223, 1);

┌────────────────────┐
│ truncate(1.223, 1) │
├────────────────────┤
│ 1.2                │
└────────────────────┘
```