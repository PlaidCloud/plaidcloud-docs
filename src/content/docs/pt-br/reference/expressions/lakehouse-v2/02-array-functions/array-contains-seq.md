---
title: ARRAY_CONTAINS_SEQ (Lakehouse v2)
description: ARRAY_CONTAINS_SEQ — verifica se um array contém todos os elementos de outro array, na mesma ordem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-seq.md
---

Verifica se um array contém todos os elementos de outro array, na mesma ordem.

## Sintaxe do Analyze

```python
func.array_contains_seq([1,2,3], [1,2])
```

## Exemplos do Analyze

```python
func.array_contains_seq([1, 2, 3, 4], [2, 3])

┌───┐
│ 1 │
└───┘
```

## Sintaxe SQL

```sql
ARRAY_CONTAINS_SEQ([1,2,3], [1,2])
```

## Exemplos SQL

```sql
SELECT ARRAY_CONTAINS_SEQ([1, 2, 3, 4], [2, 3]);

┌───┐
│ 1 │
└───┘
```
