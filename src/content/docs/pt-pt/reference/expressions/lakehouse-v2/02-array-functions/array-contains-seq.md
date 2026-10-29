---
title: ARRAY_CONTAINS_SEQ (Lakehouse v2)
description: ARRAY_CONTAINS_SEQ — verifica se uma matriz contém, por ordem, todos os elementos de outra matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-seq.md
---

Verifica se uma matriz contém, por ordem, todos os elementos de outra matriz.

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
