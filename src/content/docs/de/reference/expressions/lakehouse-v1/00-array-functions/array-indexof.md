---
title: ARRAY_INDEXOF (Lakehouse v1)
description: ARRAY_INDEXOF – gibt den Index (1-basiert) eines Elements zurück, wenn das Array das Element enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-indexof.md
---

Gibt den Index (1-basiert) eines Elements zurück, wenn das Array das Element enthält.

## Analyze-Syntax

```python
func.array_indexof( <array>, <element> )
```

## Analyze-Beispiele

```python
func.array_indexof([1, 2, 9], 9)

┌───────────────────────────────────┐
│ func.array_indexof([1, 2, 9], 9)  │
├───────────────────────────────────┤
│                                 3 │
└───────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_INDEXOF( <array>, <element> )
```

## SQL-Beispiele

```sql
SELECT ARRAY_INDEXOF([1, 2, 9], 9);

┌─────────────────────────────┐
│ array_indexof([1, 2, 9], 9) │
├─────────────────────────────┤
│                           3 │
└─────────────────────────────┘
```
