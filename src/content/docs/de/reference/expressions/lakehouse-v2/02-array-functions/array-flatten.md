---
title: ARRAY_FLATTEN (Lakehouse v2)
description: ARRAY_FLATTEN – glättet verschachtelte Arrays zu einem einstufigen Array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-flatten.md
---

Glättet verschachtelte Arrays zu einem einstufigen Array.

## Analyze-Syntax

```python
func.array_flatten([[1,2],[3,4]])
```

## Analyze-Beispiele

```python
func.array_flatten([[1, 2], [3, 4]])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQL-Syntax

```sql
ARRAY_FLATTEN([[1,2],[3,4]])
```

## SQL-Beispiele

```sql
SELECT ARRAY_FLATTEN([[1, 2], [3, 4]]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
