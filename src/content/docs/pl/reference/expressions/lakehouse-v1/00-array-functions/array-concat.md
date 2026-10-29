---
title: ARRAY_CONCAT (Lakehouse v1)
description: ARRAY_CONCAT — łączy dwie tablice.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-concat.md
---

Łączy dwie tablice.

## Składnia Analyze

```python
func.array_concat( <array1>, <array2> )
```

## Przykłady Analyze

```python
func.array_concat([1, 2], [3, 4])

┌────────────────────────────────────┐
│ func.array_concat([1, 2], [3, 4])  │
├────────────────────────────────────┤
│ [1,2,3,4]                          │
└────────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_CONCAT( <array1>, <array2> )
```

## Przykłady SQL

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌──────────────────────────────┐
│ array_concat([1, 2], [3, 4]) │
├──────────────────────────────┤
│ [1,2,3,4]                    │
└──────────────────────────────┘
```
