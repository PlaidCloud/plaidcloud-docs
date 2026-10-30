---
title: ARRAY_REMOVE_FIRST (Lakehouse v1)
description: ARRAY_REMOVE_FIRST — remove o primeiro elemento da matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-remove-first.md
---

Remove o primeiro elemento da matriz.

## Sintaxe do Analyze

```python
func.array_remove_first( <array> )
```

## Exemplos do Analyze

```python
func.array_remove_first([1, 2, 3]) 

┌─────────────────────────────────────┐
│ func.array_remove_first([1, 2, 3])  │
├─────────────────────────────────────┤
│ [2,3]                               │
└─────────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_REMOVE_FIRST( <array> )
```

## Exemplos SQL

```sql
SELECT ARRAY_REMOVE_FIRST([1, 2, 3]);

┌───────────────────────────────┐
│ array_remove_first([1, 2, 3]) │
├───────────────────────────────┤
│ [2,3]                         │
└───────────────────────────────┘
```
