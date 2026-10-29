---
title: ARRAY_CONTAINS (Lakehouse v2)
description: ARRAY_CONTAINS – prüft, ob ein Array ein bestimmtes Element enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains.md
---

Prüft, ob ein Array ein bestimmtes Element enthält.

## Analyze-Syntax

```python
func.array_contains([1, 2, 3], 2)
```

## Analyze-Beispiele

```python
func.array_contains([1, 2, 3], 2)

┌───┐
│ 1 │
└───┘
```

## SQL-Syntax

```sql
ARRAY_CONTAINS([1, 2, 3], 2)
```

## SQL-Beispiele

```sql
SELECT ARRAY_CONTAINS([1, 2, 3], 2);

┌───┐
│ 1 │
└───┘
```
