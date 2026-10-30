---
title: ARRAY_CONCAT (Lakehouse v2)
description: ARRAY_CONCAT – verkettet mehrere Arrays zu einem einzigen Array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-concat.md
---

Verkettet mehrere Arrays zu einem einzigen Array.

## Analyze-Syntax

```python
func.array_concat([1, 2], [3, 4])
```

## Analyze-Beispiele

```python
func.array_concat([1, 2], [3, 4])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQL-Syntax

```sql
ARRAY_CONCAT([1, 2], [3, 4])
```

## SQL-Beispiele

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
