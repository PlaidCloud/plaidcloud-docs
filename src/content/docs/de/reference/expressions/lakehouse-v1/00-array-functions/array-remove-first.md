---
title: ARRAY_REMOVE_FIRST (Lakehouse v1)
description: ARRAY_REMOVE_FIRST – entfernt das erste Element aus dem Array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-remove-first.md
---

Entfernt das erste Element aus dem Array.

## Analyze-Syntax

```python
func.array_remove_first( <array> )
```

## Analyze-Beispiele

```python
func.array_remove_first([1, 2, 3]) 

┌─────────────────────────────────────┐
│ func.array_remove_first([1, 2, 3])  │
├─────────────────────────────────────┤
│ [2,3]                               │
└─────────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_REMOVE_FIRST( <array> )
```

## SQL-Beispiele

```sql
SELECT ARRAY_REMOVE_FIRST([1, 2, 3]);

┌───────────────────────────────┐
│ array_remove_first([1, 2, 3]) │
├───────────────────────────────┤
│ [2,3]                         │
└───────────────────────────────┘
```
