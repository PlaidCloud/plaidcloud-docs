---
title: ARRAY_REMOVE_FIRST (Lakehouse v1)
description: ARRAY_REMOVE_FIRST — usuwa pierwszy element z tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-remove-first.md
---

Usuwa pierwszy element z tablicy.

## Składnia Analyze

```python
func.array_remove_first( <array> )
```

## Przykłady Analyze

```python
func.array_remove_first([1, 2, 3]) 

┌─────────────────────────────────────┐
│ func.array_remove_first([1, 2, 3])  │
├─────────────────────────────────────┤
│ [2,3]                               │
└─────────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_REMOVE_FIRST( <array> )
```

## Przykłady SQL

```sql
SELECT ARRAY_REMOVE_FIRST([1, 2, 3]);

┌───────────────────────────────┐
│ array_remove_first([1, 2, 3]) │
├───────────────────────────────┤
│ [2,3]                         │
└───────────────────────────────┘
```
