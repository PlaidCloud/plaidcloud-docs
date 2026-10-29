---
title: ARRAY_APPEND (Lakehouse v2)
description: ARRAY_APPEND – hängt ein Element an das Ende eines Arrays an.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-append.md
---

Hängt ein Element an das Ende eines Arrays an.

## Analyze-Syntax

```python
func.array_append([1, 2, 3], 4)
```

## Analyze-Beispiele

```python
func.array_append([1, 2, 3], 4)

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQL-Syntax

```sql
ARRAY_APPEND([1, 2, 3], 4)
```

## SQL-Beispiele

```sql
SELECT ARRAY_APPEND([1, 2, 3], 4);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
