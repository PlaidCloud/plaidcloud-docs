---
title: ARRAY_REMOVE_LAST (Lakehouse v1)
description: ARRAY_REMOVE_LAST – entfernt das letzte Element aus dem Array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-remove-last.md
---

Entfernt das letzte Element aus dem Array.

## Analyze-Syntax

```python
func.array_remove_last( <array> )
```

## Analyze-Beispiele

```python
func.array_remove_last([1, 2, 3]) 

┌────────────────────────────────────┐
│ func.array_remove_last([1, 2, 3])  │
├────────────────────────────────────┤
│ [1,2]                              │
└────────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_REMOVE_LAST( <array> )
```

## SQL-Beispiele

```sql
SELECT ARRAY_REMOVE_LAST([1, 2, 3]);

┌──────────────────────────────┐
│ array_remove_last([1, 2, 3]) │
├──────────────────────────────┤
│ [1,2]                        │
└──────────────────────────────┘
```
