---
title: ARRAY_CONTAINS_ALL (Lakehouse v2)
description: ARRAY_CONTAINS_ALL – prüft, ob ein Array alle Elemente eines anderen Arrays enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-all.md
---

Prüft, ob ein Array alle Elemente eines anderen Arrays enthält.

## Analyze-Syntax

```python
func.array_contains_all([1,2,3], [1,2])
```

## Analyze-Beispiele

```python
func.array_contains_all([1, 2, 3], [1, 2])

┌───┐
│ 1 │
└───┘
```

## SQL-Syntax

```sql
ARRAY_CONTAINS_ALL([1,2,3], [1,2])
```

## SQL-Beispiele

```sql
SELECT ARRAY_CONTAINS_ALL([1, 2, 3], [1, 2]);

┌───┐
│ 1 │
└───┘
```
