---
title: ARRAY_INTERSECT (Lakehouse v2)
description: ARRAY_INTERSECT – gibt die Schnittmenge zweier Arrays zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-intersect.md
---

Gibt die Schnittmenge zweier Arrays zurück.

## Analyze-Syntax

```python
func.array_intersect([1,2,3], [2,3,4])
```

## Analyze-Beispiele

```python
func.array_intersect([1, 2, 3], [2, 3, 4])

┌───────┐
│ [2,3] │
└───────┘
```

## SQL-Syntax

```sql
ARRAY_INTERSECT([1,2,3], [2,3,4])
```

## SQL-Beispiele

```sql
SELECT ARRAY_INTERSECT([1, 2, 3], [2, 3, 4]);

┌───────┐
│ [2,3] │
└───────┘
```
