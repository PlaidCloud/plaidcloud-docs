---
title: ARRAYS_OVERLAP (Lakehouse v2)
description: ARRAYS_OVERLAP – prüft, ob zwei Arrays gemeinsame Elemente haben.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/arrays-overlap.md
---

Prüft, ob zwei Arrays gemeinsame Elemente haben.

## Analyze-Syntax

```python
func.arrays_overlap([1,2,3], [3,4,5])
```

## Analyze-Beispiele

```python
func.arrays_overlap([1, 2, 3], [3, 4, 5])

┌───┐
│ 1 │
└───┘
```

## SQL-Syntax

```sql
ARRAYS_OVERLAP([1,2,3], [3,4,5])
```

## SQL-Beispiele

```sql
SELECT ARRAYS_OVERLAP([1, 2, 3], [3, 4, 5]);

┌───┐
│ 1 │
└───┘
```
