---
title: ARRAY_REMOVE (Lakehouse v2)
description: ARRAY_REMOVE — remove todas as ocorrências de um elemento especificado de um array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-remove.md
---

Remove todas as ocorrências de um elemento especificado de um array.

## Sintaxe do Analyze

```python
func.array_remove([1, 2, 3, 2, 1], 2)
```

## Exemplos do Analyze

```python
func.array_remove([1, 2, 3, 2, 1], 2)

┌─────────┐
│ [1,3,1] │
└─────────┘
```

## Sintaxe SQL

```sql
ARRAY_REMOVE([1, 2, 3, 2, 1], 2)
```

## Exemplos SQL

```sql
SELECT ARRAY_REMOVE([1, 2, 3, 2, 1], 2);

┌─────────┐
│ [1,3,1] │
└─────────┘
```
