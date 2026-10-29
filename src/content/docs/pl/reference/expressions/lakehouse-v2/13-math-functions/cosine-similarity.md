---
title: COSINE_SIMILARITY (Lakehouse v2)
description: COSINE_SIMILARITY — zwraca podobieństwo cosinusowe między dwiema tablicami (wektorami).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity.md
---

Zwraca podobieństwo cosinusowe między dwiema tablicami (wektorami).

## Składnia Analyze

```python
func.cosine_similarity(<array1>, <array2>)
```

## Przykłady Analyze

```python
func.cosine_similarity([1.0, 2.0], [2.0, 4.0])

┌─────┐
│ 1.0  │
└─────┘
```

## Składnia SQL

```sql
COSINE_SIMILARITY(<array1>, <array2>)
```

## Przykłady SQL

```sql
SELECT COSINE_SIMILARITY([1.0, 2.0], [2.0, 4.0]);

┌─────┐
│ 1.0  │
└─────┘
```
