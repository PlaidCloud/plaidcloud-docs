---
title: COSINE_SIMILARITY_NORM (Lakehouse v2)
description: COSINE_SIMILARITY_NORM — zwraca podobieństwo cosinusowe między dwiema znormalizowanymi tablicami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity-norm.md
---

Zwraca podobieństwo cosinusowe między dwiema znormalizowanymi tablicami.

## Składnia Analyze

```python
func.cosine_similarity_norm(<array1>, <array2>)
```

## Przykłady Analyze

```python
func.cosine_similarity_norm([0.6, 0.8], [0.8, 0.6])

┌──────┐
│ 0.96  │
└──────┘
```

## Składnia SQL

```sql
COSINE_SIMILARITY_NORM(<array1>, <array2>)
```

## Przykłady SQL

```sql
SELECT COSINE_SIMILARITY_NORM([0.6, 0.8], [0.8, 0.6]);

┌──────┐
│ 0.96  │
└──────┘
```
