---
title: ARRAY_INTERSECT (Lakehouse v2)
description: ARRAY_INTERSECT — retorna a interseção de dois arrays.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-intersect.md
---

Retorna a interseção de dois arrays.

## Sintaxe do Analyze

```python
func.array_intersect([1,2,3], [2,3,4])
```

## Exemplos do Analyze

```python
func.array_intersect([1, 2, 3], [2, 3, 4])

┌───────┐
│ [2,3] │
└───────┘
```

## Sintaxe SQL

```sql
ARRAY_INTERSECT([1,2,3], [2,3,4])
```

## Exemplos SQL

```sql
SELECT ARRAY_INTERSECT([1, 2, 3], [2, 3, 4]);

┌───────┐
│ [2,3] │
└───────┘
```
