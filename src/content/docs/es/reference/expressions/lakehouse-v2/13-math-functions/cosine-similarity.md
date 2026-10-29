---
title: COSINE_SIMILARITY (Lakehouse v2)
description: COSINE_SIMILARITY — devuelve la similitud del coseno entre dos matrices (vectores).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity.md
---

Devuelve la similitud del coseno entre dos matrices (vectores).

## Sintaxis de Analyze

```python
func.cosine_similarity(<array1>, <array2>)
```

## Ejemplos de Analyze

```python
func.cosine_similarity([1.0, 2.0], [2.0, 4.0])

┌─────┐
│ 1.0  │
└─────┘
```

## Sintaxis de SQL

```sql
COSINE_SIMILARITY(<array1>, <array2>)
```

## Ejemplos de SQL

```sql
SELECT COSINE_SIMILARITY([1.0, 2.0], [2.0, 4.0]);

┌─────┐
│ 1.0  │
└─────┘
```
