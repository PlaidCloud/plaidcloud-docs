---
title: ARRAY_INDEXOF (Lakehouse v1)
description: ARRAY_INDEXOF retorna o índice (base 1) de um elemento se o array contiver esse elemento.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-indexof.md
---

Retorna o índice (base 1) de um elemento se o array contiver esse elemento.

## Sintaxe do Analyze

```python
func.array_indexof( <array>, <element> )
```

## Exemplos do Analyze

```python
func.array_indexof([1, 2, 9], 9)

┌───────────────────────────────────┐
│ func.array_indexof([1, 2, 9], 9)  │
├───────────────────────────────────┤
│                                 3 │
└───────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_INDEXOF( <array>, <element> )
```

## Exemplos de SQL

```sql
SELECT ARRAY_INDEXOF([1, 2, 9], 9);

┌─────────────────────────────┐
│ array_indexof([1, 2, 9], 9) │
├─────────────────────────────┤
│                           3 │
└─────────────────────────────┘
```
