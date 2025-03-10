---
title: ATAN
---

Returns the arc tangent of `x`, that is, the value whose tangent is `x`.

## Analyze Syntax

```python
func.atan( <x> )
```

## Analyze Examples

```python
func.atan(-2)

┌─────────────────────┐
│  func.atan((- 2))   │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```

## SQL Syntax

```sql
ATAN( <x> )
```

## SQL Examples

```sql
SELECT ATAN(-2);

┌─────────────────────┐
│     atan((- 2))     │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```