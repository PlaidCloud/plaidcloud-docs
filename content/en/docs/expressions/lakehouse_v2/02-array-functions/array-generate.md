---
title: ARRAY_GENERATE
---

Generates an array of sequential values.

## Analyze Syntax

```python
func.array_generate(1, 5)
```

## Analyze Examples

```python
func.array_generate(1, 5)

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```

## SQL Syntax

```sql
ARRAY_GENERATE(1, 5)
```

## SQL Examples

```sql
SELECT ARRAY_GENERATE(1, 5);

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```
