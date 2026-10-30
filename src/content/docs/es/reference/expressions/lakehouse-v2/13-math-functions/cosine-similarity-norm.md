---
title: COSINE_SIMILARITY_NORM (Lakehouse v2)
description: COSINE_SIMILARITY_NORM — devuelve la similitud del coseno entre dos matrices normalizadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity-norm.md
---

Devuelve la similitud del coseno entre dos matrices normalizadas.

## Sintaxis de Analyze

```python
func.cosine_similarity_norm(<array1>, <array2>)
```

## Ejemplos de Analyze

```python
func.cosine_similarity_norm([0.6, 0.8], [0.8, 0.6])

┌──────┐
│ 0.96  │
└──────┘
```

## Sintaxis de SQL

```sql
COSINE_SIMILARITY_NORM(<array1>, <array2>)
```

## Ejemplos de SQL

```sql
SELECT COSINE_SIMILARITY_NORM([0.6, 0.8], [0.8, 0.6]);

┌──────┐
│ 0.96  │
└──────┘
```
