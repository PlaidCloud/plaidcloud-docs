---
title: ARRAY_CONTAINS_ALL (Lakehouse v2)
description: ARRAY_CONTAINS_ALL — verifica se um array contém todos os elementos de outro array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-all.md
---

Verifica se um array contém todos os elementos de outro array.

## Sintaxe do Analyze

```python
func.array_contains_all([1,2,3], [1,2])
```

## Exemplos do Analyze

```python
func.array_contains_all([1, 2, 3], [1, 2])

┌───┐
│ 1 │
└───┘
```

## Sintaxe SQL

```sql
ARRAY_CONTAINS_ALL([1,2,3], [1,2])
```

## Exemplos SQL

```sql
SELECT ARRAY_CONTAINS_ALL([1, 2, 3], [1, 2]);

┌───┐
│ 1 │
└───┘
```
