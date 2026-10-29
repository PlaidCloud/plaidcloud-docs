---
title: ARRAY_DIFFERENCE (Lakehouse v2)
description: ARRAY_DIFFERENCE – gibt ein Array mit den Differenzen zwischen aufeinanderfolgenden Elementen zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-difference.md
---

Gibt ein Array mit den Differenzen zwischen aufeinanderfolgenden Elementen zurück.

## Analyze-Syntax

```python
func.array_difference([1, 3, 6, 10])
```

## Analyze-Beispiele

```python
func.array_difference([1, 3, 6, 10])

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```

## SQL-Syntax

```sql
ARRAY_DIFFERENCE([1, 3, 6, 10])
```

## SQL-Beispiele

```sql
SELECT ARRAY_DIFFERENCE([1, 3, 6, 10]);

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```
