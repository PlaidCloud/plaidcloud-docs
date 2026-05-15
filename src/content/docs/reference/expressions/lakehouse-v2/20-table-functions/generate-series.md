---
title: GENERATE_SERIES (Lakehouse v2)
description: GENERATE_SERIES — generates a series of values from start to stop with a given step.
---

Generates a series of values from start to stop with a given step.

## Analyze Syntax

```python
func.generate_series(<start>, <stop>[, <step>])
```

## Analyze Examples

```python
func.generate_series(1, 5)

┌─────────────────┐
│ [1, 2, 3, 4, 5]  │
└─────────────────┘
```

## SQL Syntax

```sql
GENERATE_SERIES(<start>, <stop>[, <step>])
```

## SQL Examples

```sql
SELECT * FROM TABLE(GENERATE_SERIES(1, 5));

┌───────────┐
│ 1
2
3
4
5  │
└───────────┘
```
