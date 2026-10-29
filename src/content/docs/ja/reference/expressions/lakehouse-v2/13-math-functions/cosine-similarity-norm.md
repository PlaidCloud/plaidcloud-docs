---
title: COSINE_SIMILARITY_NORM (Lakehouse v2)
description: COSINE_SIMILARITY_NORM — 正規化された2つの配列間のコサイン類似度を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity-norm.md
---

正規化された2つの配列間のコサイン類似度を返します。

## Analyzeの構文

```python
func.cosine_similarity_norm(<array1>, <array2>)
```

## Analyzeの例

```python
func.cosine_similarity_norm([0.6, 0.8], [0.8, 0.6])

┌──────┐
│ 0.96  │
└──────┘
```

## SQLの構文

```sql
COSINE_SIMILARITY_NORM(<array1>, <array2>)
```

## SQLの例

```sql
SELECT COSINE_SIMILARITY_NORM([0.6, 0.8], [0.8, 0.6]);

┌──────┐
│ 0.96  │
└──────┘
```
