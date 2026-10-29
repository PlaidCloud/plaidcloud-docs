---
title: ARRAY_DISTINCT (Lakehouse v1)
description: ARRAY_DISTINCT – entfernt alle Duplikate und NULL-Werte aus dem Array, ohne die ursprüngliche Reihenfolge beizubehalten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-distinct.md
---

Entfernt alle Duplikate und NULL-Werte aus dem Array, ohne die ursprüngliche Reihenfolge beizubehalten.

## Analyze-Syntax

```python
func.array_distinct( <array> )
```

## Analyze-Beispiele

```python
func.array_distinct([1, 2, 2, 4, 3])

┌───────────────────────────────────────┐
│ func.array_distinct([1, 2, 2, 4, 3])  │
├───────────────────────────────────────┤
│ [1,2,4,3]                             │
└───────────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_DISTINCT( <array> )
```

## SQL-Beispiele

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 4, 3]);

┌─────────────────────────────────┐
│ array_distinct([1, 2, 2, 4, 3]) │
├─────────────────────────────────┤
│ [1,2,4,3]                       │
└─────────────────────────────────┘
```
