---
title: COSINE_SIMILARITY_NORM (Lakehouse v2)
description: COSINE_SIMILARITY_NORM — devolve a semelhança de cosseno entre duas matrizes normalizadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity-norm.md
---

Devolve a semelhança de cosseno entre duas matrizes normalizadas.

## Sintaxe de Analyze

```python
func.cosine_similarity_norm(<array1>, <array2>)
```

## Exemplos de Analyze

```python
func.cosine_similarity_norm([0.6, 0.8], [0.8, 0.6])

┌──────┐
│ 0.96  │
└──────┘
```

## Sintaxe SQL

```sql
COSINE_SIMILARITY_NORM(<array1>, <array2>)
```

## Exemplos SQL

```sql
SELECT COSINE_SIMILARITY_NORM([0.6, 0.8], [0.8, 0.6]);

┌──────┐
│ 0.96  │
└──────┘
```
