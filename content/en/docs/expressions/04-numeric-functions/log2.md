---
title: LOG2
---

Returns the base-2 logarithm of `x`. If `x` is less than or equal to 0.0E0, the function returns NULL.

## Analyze Syntax

```python
func.log2( <x> )
```

## Analyze Examples

```python
func.log2(65536)

┌──────────────────┐
│ func.log2(65536) │
├──────────────────┤
│               16 │
└──────────────────┘
```

## SQL Syntax

```sql
LOG2( <x> )
```

## SQL Examples

```sql
SELECT LOG2(65536);

┌─────────────┐
│ log2(65536) │
├─────────────┤
│          16 │
└─────────────┘
```