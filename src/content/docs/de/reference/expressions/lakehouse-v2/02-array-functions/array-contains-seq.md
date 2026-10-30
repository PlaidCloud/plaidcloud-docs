---
title: ARRAY_CONTAINS_SEQ (Lakehouse v2)
description: ARRAY_CONTAINS_SEQ – prüft, ob ein Array alle Elemente eines anderen Arrays in derselben Reihenfolge enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-seq.md
---

Prüft, ob ein Array alle Elemente eines anderen Arrays in derselben Reihenfolge enthält.

## Analyze-Syntax

```python
func.array_contains_seq([1,2,3], [1,2])
```

## Analyze-Beispiele

```python
func.array_contains_seq([1, 2, 3, 4], [2, 3])

┌───┐
│ 1 │
└───┘
```

## SQL-Syntax

```sql
ARRAY_CONTAINS_SEQ([1,2,3], [1,2])
```

## SQL-Beispiele

```sql
SELECT ARRAY_CONTAINS_SEQ([1, 2, 3, 4], [2, 3]);

┌───┐
│ 1 │
└───┘
```
