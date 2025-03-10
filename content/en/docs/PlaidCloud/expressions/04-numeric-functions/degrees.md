---
title: DEGREES
---

Returns the argument `x`, converted from radians to degrees, where `x` is given in radians.

## Analyze Syntax

```python
func.degrees( <x> )
```

## Analyze Examples

```python
func.degrees(func.pi())

┌─────────────────────────┐
│ func.degrees(func.pi()) │
├─────────────────────────┤
│                     180 │
└─────────────────────────┘
```

## SQL Syntax

```sql
DEGREES( <x> )
```

## SQL Examples

```sql
SELECT DEGREES(PI());

┌───────────────┐
│ degrees(pi()) │
├───────────────┤
│           180 │
└───────────────┘
```