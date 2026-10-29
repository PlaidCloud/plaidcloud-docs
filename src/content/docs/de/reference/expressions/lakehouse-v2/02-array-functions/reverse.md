---
title: "REVERSE (Array, Lakehouse v2)"
description: REVERSE – gibt ein Array mit den Elementen in umgekehrter Reihenfolge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/reverse.md
---

Gibt ein Array mit den Elementen in umgekehrter Reihenfolge zurück.

## Analyze-Syntax

```python
func.reverse([1, 2, 3])
```

## Analyze-Beispiele

```python
func.reverse([1, 2, 3])

┌─────────┐
│ [3,2,1] │
└─────────┘
```

## SQL-Syntax

```sql
REVERSE([1, 2, 3])
```

## SQL-Beispiele

```sql
SELECT ARRAY_REVERSE([1, 2, 3]);

┌─────────┐
│ [3,2,1] │
└─────────┘
```
