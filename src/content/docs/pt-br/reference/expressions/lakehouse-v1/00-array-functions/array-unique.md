---
title: ARRAY_UNIQUE (Lakehouse v1)
description: ARRAY_UNIQUE conta os elementos exclusivos do array (exceto NULL).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-unique.md
---

Conta os elementos exclusivos do array (exceto NULL).

## Sintaxe do Analyze

```python
func.array_unique( <array> )
```

## Exemplos do Analyze

```python
func.array_unique([1, 2, 3, 3, 4])

┌─────────────────────────────────────┐
│ func.array_unique([1, 2, 3, 3, 4])  │
├─────────────────────────────────────┤
│                                   4 │
└─────────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_UNIQUE( <array> )
```

## Exemplos de SQL

```sql
SELECT ARRAY_UNIQUE([1, 2, 3, 3, 4]);

┌───────────────────────────────┐
│ array_unique([1, 2, 3, 3, 4]) │
├───────────────────────────────┤
│                             4 │
└───────────────────────────────┘
```
