---
title: "REVERSE (Array, Lakehouse v2)"
description: REVERSE — retorna um array com os elementos em ordem inversa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/reverse.md
---

Retorna um array com os elementos em ordem inversa.

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
