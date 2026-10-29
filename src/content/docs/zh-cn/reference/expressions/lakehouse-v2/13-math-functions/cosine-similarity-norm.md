---
title: COSINE_SIMILARITY_NORM (Lakehouse v2)
description: COSINE_SIMILARITY_NORM — 返回两个已归一化数组之间的余弦相似度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity-norm.md
---

返回两个已归一化数组之间的余弦相似度。

## Analyze 语法

```python
func.cosine_similarity_norm(<array1>, <array2>)
```

## Analyze 示例

```python
func.cosine_similarity_norm([0.6, 0.8], [0.8, 0.6])

┌──────┐
│ 0.96  │
└──────┘
```

## SQL 语法

```sql
COSINE_SIMILARITY_NORM(<array1>, <array2>)
```

## SQL 示例

```sql
SELECT COSINE_SIMILARITY_NORM([0.6, 0.8], [0.8, 0.6]);

┌──────┐
│ 0.96  │
└──────┘
```
