---
title: ARRAY_CONTAINS (Lakehouse v2)
description: ARRAY_CONTAINS — verifica se uma matriz contém um elemento específico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains.md
---

Verifica se uma matriz contém um elemento específico.

## Sintaxe do Analyze

```python
func.array_contains([1, 2, 3], 2)
```

## Exemplos do Analyze

```python
func.array_contains([1, 2, 3], 2)

┌───┐
│ 1 │
└───┘
```

## Sintaxe SQL

```sql
ARRAY_CONTAINS([1, 2, 3], 2)
```

## Exemplos SQL

```sql
SELECT ARRAY_CONTAINS([1, 2, 3], 2);

┌───┐
│ 1 │
└───┘
```
