---
title: COSINE_SIMILARITY_NORM (Lakehouse v2)
description: COSINE_SIMILARITY_NORM — returns the cosine similarity between two normalized arrays.
---

Returns the cosine similarity between two normalized arrays.

## Analyze Syntax

```python
func.cosine_similarity_norm(<array1>, <array2>)
```

## Analyze Examples

```python
func.cosine_similarity_norm([0.6, 0.8], [0.8, 0.6])

┌──────┐
│ 0.96  │
└──────┘
```

## SQL Syntax

```sql
COSINE_SIMILARITY_NORM(<array1>, <array2>)
```

## SQL Examples

```sql
SELECT COSINE_SIMILARITY_NORM([0.6, 0.8], [0.8, 0.6]);

┌──────┐
│ 0.96  │
└──────┘
```
