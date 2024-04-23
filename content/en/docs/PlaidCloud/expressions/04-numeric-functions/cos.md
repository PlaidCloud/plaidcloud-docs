---
title: COS
---

Returns the cosine of `x`, where `x` is given in radians.

## Analyze Syntax

```python
func.cos( <x> )
```

## Analyze Examples

```python
func.cos(func.pi())

┌─────────────────────┐
│ func.cos(func.pi()) │
├─────────────────────┤
│                  -1 │
└─────────────────────┘
```

## SQL Syntax

```sql
COS( <x> )
```

## SQL Examples

```sql
SELECT COS(PI());

┌───────────┐
│ cos(pi()) │
├───────────┤
│        -1 │
└───────────┘
```