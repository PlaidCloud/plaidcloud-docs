---
title: GREATEST
---

Returns the maximum value from a set of values.

## Analyze Syntax

```python
func.greatest(<value1>, <value2> ...)
```

## Analyze Examples

```python
func.greatest((5, 9, 4))

┌──────────────────────────┐
│ func.greatest((5, 9, 4)) │
├──────────────────────────┤
│                        9 │
└──────────────────────────┘
```

## SQL Syntax

```sql
GREATEST(<value1>, <value2> ...)
```

## SQL Examples

```sql
SELECT GREATEST(5, 9, 4);

┌───────────────────┐
│ greatest(5, 9, 4) │
├───────────────────┤
│                 9 │
└───────────────────┘
```