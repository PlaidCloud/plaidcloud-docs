---
title: COSINE_SIMILARITY (Lakehouse v2)
description: COSINE_SIMILARITY — renvoie la similarité cosinus entre deux tableaux (vecteurs).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity.md
---

Renvoie la similarité cosinus entre deux tableaux (vecteurs).

## Syntaxe Analyze

```python
func.cosine_similarity(<array1>, <array2>)
```

## Exemples Analyze

```python
func.cosine_similarity([1.0, 2.0], [2.0, 4.0])

┌─────┐
│ 1.0  │
└─────┘
```

## Syntaxe SQL

```sql
COSINE_SIMILARITY(<array1>, <array2>)
```

## Exemples SQL

```sql
SELECT COSINE_SIMILARITY([1.0, 2.0], [2.0, 4.0]);

┌─────┐
│ 1.0  │
└─────┘
```
