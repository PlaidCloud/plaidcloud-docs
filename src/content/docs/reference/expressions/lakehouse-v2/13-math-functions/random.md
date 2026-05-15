---
title: RANDOM (Lakehouse v2)
description: RANDOM — returns a random floating-point value between 0 and 1. Alias for `RAND`.
---

Returns a random floating-point value between 0 and 1. Alias for `RAND`.

## Analyze Syntax

```python
func.random([<seed>])
```

## Analyze Examples

```python
func.random()

┌───────────┐
│ 0.8123...  │
└───────────┘
```

## SQL Syntax

```sql
RANDOM([<seed>])
```

## SQL Examples

```sql
SELECT RANDOM();

┌───────────┐
│ 0.8123...  │
└───────────┘
```
