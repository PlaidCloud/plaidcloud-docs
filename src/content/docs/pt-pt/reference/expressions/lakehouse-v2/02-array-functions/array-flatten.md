---
title: ARRAY_FLATTEN (Lakehouse v2)
description: ARRAY_FLATTEN — aplana matrizes aninhadas numa matriz de um só nível.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-flatten.md
---

Aplana matrizes aninhadas numa matriz de um só nível.

## Sintaxe do Analyze

```python
func.array_flatten([[1,2],[3,4]])
```

## Exemplos do Analyze

```python
func.array_flatten([[1, 2], [3, 4]])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## Sintaxe SQL

```sql
ARRAY_FLATTEN([[1,2],[3,4]])
```

## Exemplos SQL

```sql
SELECT ARRAY_FLATTEN([[1, 2], [3, 4]]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
