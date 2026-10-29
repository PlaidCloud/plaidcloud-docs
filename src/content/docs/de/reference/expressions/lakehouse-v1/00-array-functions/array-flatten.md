---
title: ARRAY_FLATTEN (Lakehouse v1)
description: ARRAY_FLATTEN – flacht verschachtelte Arrays ab und wandelt sie in ein einstufiges Array um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-flatten.md
---

Flacht verschachtelte Arrays ab und wandelt sie in ein einstufiges Array um.

## Analyze-Syntax

```python
func.array_flatten( <array> )
```

## Analyze-Beispiele

```python
func.array_flatten([[1, 2], [3, 4, 5]]) 

┌──────────────────────────────────────────┐
│ func.array_flatten([[1, 2], [3, 4, 5]])  │
├──────────────────────────────────────────┤
│ [1,2,3,4,5]                              │
└──────────────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_FLATTEN( <array> )
```

## SQL-Beispiele

```sql
SELECT ARRAY_FLATTEN([[1,2], [3,4,5]]);

┌────────────────────────────────────┐
│ array_flatten([[1, 2], [3, 4, 5]]) │
├────────────────────────────────────┤
│ [1,2,3,4,5]                        │
└────────────────────────────────────┘
```
