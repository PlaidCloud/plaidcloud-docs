---
title: COSINE_SIMILARITY (Lakehouse v2)
description: COSINE_SIMILARITY — 返回两个数组（向量）之间的余弦相似度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity.md
---

返回两个数组（向量）之间的余弦相似度。

## Analyze 语法

```python
func.cosine_similarity(<array1>, <array2>)
```

## Analyze 示例

```python
func.cosine_similarity([1.0, 2.0], [2.0, 4.0])

┌─────┐
│ 1.0  │
└─────┘
```

## SQL 语法

```sql
COSINE_SIMILARITY(<array1>, <array2>)
```

## SQL 示例

```sql
SELECT COSINE_SIMILARITY([1.0, 2.0], [2.0, 4.0]);

┌─────┐
│ 1.0  │
└─────┘
```
