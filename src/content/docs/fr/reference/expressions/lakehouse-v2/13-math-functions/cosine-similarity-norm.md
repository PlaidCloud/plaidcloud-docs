---
title: COSINE_SIMILARITY_NORM (Lakehouse v2)
description: COSINE_SIMILARITY_NORM — renvoie la similarité cosinus entre deux tableaux normalisés.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity-norm.md
---

Renvoie la similarité cosinus entre deux tableaux normalisés.

## Syntaxe Analyze

```python
func.cosine_similarity_norm(<array1>, <array2>)
```

## Exemples Analyze

```python
func.cosine_similarity_norm([0.6, 0.8], [0.8, 0.6])

┌──────┐
│ 0.96  │
└──────┘
```

## Syntaxe SQL

```sql
COSINE_SIMILARITY_NORM(<array1>, <array2>)
```

## Exemples SQL

```sql
SELECT COSINE_SIMILARITY_NORM([0.6, 0.8], [0.8, 0.6]);

┌──────┐
│ 0.96  │
└──────┘
```
