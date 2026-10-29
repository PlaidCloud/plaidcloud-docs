---
title: ARRAY_LENGTH (Lakehouse v2)
description: ARRAY_LENGTH — retorna o número de elementos de um array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-length.md
---

Retorna o número de elementos de um array.

## Sintaxe do Analyze

```python
func.array_length([1, 2, 3])
```

## Exemplos do Analyze

```python
func.array_length([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## Sintaxe SQL

```sql
ARRAY_LENGTH([1, 2, 3])
```

## Exemplos SQL

```sql
SELECT ARRAY_LENGTH([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
