---
title: ARRAY_REMOVE_LAST (Lakehouse v1)
description: ARRAY_REMOVE_LAST remove o último elemento do array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-remove-last.md
---

Remove o último elemento do array.

## Sintaxe do Analyze

```python
func.array_remove_last( <array> )
```

## Exemplos do Analyze

```python
func.array_remove_last([1, 2, 3]) 

┌────────────────────────────────────┐
│ func.array_remove_last([1, 2, 3])  │
├────────────────────────────────────┤
│ [1,2]                              │
└────────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_REMOVE_LAST( <array> )
```

## Exemplos de SQL

```sql
SELECT ARRAY_REMOVE_LAST([1, 2, 3]);

┌──────────────────────────────┐
│ array_remove_last([1, 2, 3]) │
├──────────────────────────────┤
│ [1,2]                        │
└──────────────────────────────┘
```
