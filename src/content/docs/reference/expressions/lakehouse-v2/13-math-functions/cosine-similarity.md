---
title: COSINE_SIMILARITY (Lakehouse v2)
description: COSINE_SIMILARITY — returns the cosine similarity between two arrays (vectors).
---

Returns the cosine similarity between two arrays (vectors).

## Analyze Syntax

```python
func.cosine_similarity(<array1>, <array2>)
```

## Analyze Examples

```python
func.cosine_similarity([1.0, 2.0], [2.0, 4.0])

┌─────┐
│ 1.0  │
└─────┘
```

## SQL Syntax

```sql
COSINE_SIMILARITY(<array1>, <array2>)
```

## SQL Examples

```sql
SELECT COSINE_SIMILARITY([1.0, 2.0], [2.0, 4.0]);

┌─────┐
│ 1.0  │
└─────┘
```
