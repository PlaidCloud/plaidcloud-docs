---
title: COSINE_SIMILARITY_NORM (Lakehouse v2)
description: COSINE_SIMILARITY_NORM — 정규화된 두 배열 사이의 코사인 유사도를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity-norm.md
---

정규화된 두 배열 사이의 코사인 유사도를 반환합니다.

## Analyze 구문

```python
func.cosine_similarity_norm(<array1>, <array2>)
```

## Analyze 예제

```python
func.cosine_similarity_norm([0.6, 0.8], [0.8, 0.6])

┌──────┐
│ 0.96  │
└──────┘
```

## SQL 구문

```sql
COSINE_SIMILARITY_NORM(<array1>, <array2>)
```

## SQL 예제

```sql
SELECT COSINE_SIMILARITY_NORM([0.6, 0.8], [0.8, 0.6]);

┌──────┐
│ 0.96  │
└──────┘
```
