---
title: COSINE_SIMILARITY (Lakehouse v2)
description: COSINE_SIMILARITY — devolve a semelhança de cosseno entre duas matrizes (vetores).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity.md
---

Devolve a semelhança de cosseno entre duas matrizes (vetores).

## Sintaxe de Analyze

```python
func.cosine_similarity(<array1>, <array2>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT COSINE_SIMILARITY([1.0, 2.0], [2.0, 4.0]);

┌─────┐
│ 1.0  │
└─────┘
```
