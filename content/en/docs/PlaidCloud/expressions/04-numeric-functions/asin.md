---
title: ASIN
---

Returns the arc sine of `x`, that is, the value whose sine is `x`. Returns NULL if `x` is not in the range -1 to 1.

## Analyze Syntax

```python
func.asin( <x> )
```

## Analyze Examples

```python
func.asin(0.2)

┌────────────────────┐
│   func.asin(0.2)   │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```

## SQL Syntax

```sql
ASIN( <x> )
```

## SQL Examples

```sql
SELECT ASIN(0.2);

┌────────────────────┐
│      asin(0.2)     │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```