---
title: COSINE_SIMILARITY (Lakehouse v2)
description: COSINE_SIMILARITY — 두 배열(벡터) 사이의 코사인 유사도를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity.md
---

두 배열(벡터) 사이의 코사인 유사도를 반환합니다.

## Analyze 구문

```python
func.cosine_similarity(<array1>, <array2>)
```

## Analyze 예제

```python
func.cosine_similarity([1.0, 2.0], [2.0, 4.0])

┌─────┐
│ 1.0  │
└─────┘
```

## SQL 구문

```sql
COSINE_SIMILARITY(<array1>, <array2>)
```

## SQL 예제

```sql
SELECT COSINE_SIMILARITY([1.0, 2.0], [2.0, 4.0]);

┌─────┐
│ 1.0  │
└─────┘
```
