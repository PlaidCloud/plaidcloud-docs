---
title: ARRAY_CONCAT (Lakehouse v1)
description: ARRAY_CONCAT – verkettet zwei Arrays.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-concat.md
---

Verkettet zwei Arrays.

## Analyze-Syntax

```python
func.array_concat( <array1>, <array2> )
```

## Analyze-Beispiele

```python
func.array_concat([1, 2], [3, 4])

┌────────────────────────────────────┐
│ func.array_concat([1, 2], [3, 4])  │
├────────────────────────────────────┤
│ [1,2,3,4]                          │
└────────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_CONCAT( <array1>, <array2> )
```

## SQL-Beispiele

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌──────────────────────────────┐
│ array_concat([1, 2], [3, 4]) │
├──────────────────────────────┤
│ [1,2,3,4]                    │
└──────────────────────────────┘
```
