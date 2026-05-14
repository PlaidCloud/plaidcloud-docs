---
title: COSINE_SIMILARITY_NORM
description: "Learn how to use the COSINE_SIMILARITY_NORM math function in PlaidCloud Lakehouse. Returns the cosine similarity between two normalized arrays."
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
