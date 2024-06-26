---
title: ACOS
---

Returns the arc cosine of `x`, that is, the value whose cosine is `x`. Returns NULL if `x` is not in the range -1 to 1.

## Analyze Syntax

```python
func.abs( <x> )
```

## Analyze Examples

```python
func.abs(1)

┌──────────────┐
│ func.acos(1) │
├──────────────┤
│            0 │
└──────────────┘
```

## SQL Syntax

```sql
ACOS( <x> )
```

## SQL Examples

```sql
SELECT ACOS(1);

┌─────────┐
│ acos(1) │
├─────────┤
│       0 │
└─────────┘
```