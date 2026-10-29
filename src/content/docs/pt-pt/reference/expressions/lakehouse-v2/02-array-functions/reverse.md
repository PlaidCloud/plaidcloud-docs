---
title: "REVERSE (Matriz, Lakehouse v2)"
description: REVERSE — devolve uma matriz com os elementos por ordem inversa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/reverse.md
---

Devolve uma matriz com os elementos por ordem inversa.

## Sintaxe do Analyze

```python
func.reverse([1, 2, 3])
```

## Exemplos do Analyze

```python
func.reverse([1, 2, 3])

┌─────────┐
│ [3,2,1] │
└─────────┘
```

## Sintaxe SQL

```sql
REVERSE([1, 2, 3])
```

## Exemplos SQL

```sql
SELECT ARRAY_REVERSE([1, 2, 3]);

┌─────────┐
│ [3,2,1] │
└─────────┘
```
