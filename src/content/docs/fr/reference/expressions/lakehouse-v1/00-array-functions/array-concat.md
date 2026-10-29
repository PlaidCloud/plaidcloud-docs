---
title: ARRAY_CONCAT (Lakehouse v1)
description: "ARRAY_CONCAT : concatène deux tableaux."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-concat.md
---

Concatène deux tableaux.

## Syntaxe Analyze

```python
func.array_concat( <array1>, <array2> )
```

## Exemples Analyze

```python
func.array_concat([1, 2], [3, 4])

┌────────────────────────────────────┐
│ func.array_concat([1, 2], [3, 4])  │
├────────────────────────────────────┤
│ [1,2,3,4]                          │
└────────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_CONCAT( <array1>, <array2> )
```

## Exemples SQL

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌──────────────────────────────┐
│ array_concat([1, 2], [3, 4]) │
├──────────────────────────────┤
│ [1,2,3,4]                    │
└──────────────────────────────┘
```
