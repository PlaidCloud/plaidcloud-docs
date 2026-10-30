---
title: ARRAY_JOIN (Lakehouse v2)
description: ARRAY_JOIN — concatena os elementos de um array em uma string com um separador.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-join.md
---

Concatena os elementos de um array em uma string com um separador.

## Sintaxe do Analyze

```python
func.array_join([1,2,3], '-')
```

## Exemplos do Analyze

```python
func.array_join(['a', 'b', 'c'], '-')

┌─────────┐
│ 'a-b-c' │
└─────────┘
```

## Sintaxe SQL

```sql
ARRAY_JOIN([1,2,3], '-')
```

## Exemplos SQL

```sql
SELECT ARRAY_JOIN(['a', 'b', 'c'], '-');

┌───────┐
│ a-b-c │
└───────┘
```
