---
title: LEAST
---

Returns the minimum value from a set of values.

## Analyze Syntax

```python
func.least((<value1>, <value2> ...))
```

## Analyze Examples

```python
func.least((5, 9, 4))

┌───────────────────────┐
│ func.least((5, 9, 4)) │
├───────────────────────┤
│                     4 │
└───────────────────────┘
```

## SQL Syntax

```sql
LEAST(<value1>, <value2> ...)
```

## SQL Examples

```sql
SELECT LEAST(5, 9, 4);

┌────────────────┐
│ least(5, 9, 4) │
├────────────────┤
│              4 │
└────────────────┘
```