---
title: COSINE_SIMILARITY (Lakehouse v2)
description: COSINE_SIMILARITY — retorna a similaridade de cosseno entre dois arrays (vetores).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity.md
---

Retorna a similaridade de cosseno entre dois arrays (vetores).

## Sintaxe do Analyze

```python
func.cosine_similarity(<array1>, <array2>)
```

## Exemplos do Analyze

```python
func.cosine_similarity([1.0, 2.0], [2.0, 4.0])

┌─────┐
│ 1.0  │
└─────┘
```

## Sintaxe SQL

```sql
COSINE_SIMILARITY(<array1>, <array2>)
```

## Exemplos de SQL

```sql
SELECT COSINE_SIMILARITY([1.0, 2.0], [2.0, 4.0]);

┌─────┐
│ 1.0  │
└─────┘
```
