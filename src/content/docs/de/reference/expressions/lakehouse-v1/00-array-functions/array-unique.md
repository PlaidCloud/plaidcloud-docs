---
title: ARRAY_UNIQUE (Lakehouse v1)
description: ARRAY_UNIQUE – zählt die eindeutigen Elemente im Array (außer NULL).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-unique.md
---

Zählt die eindeutigen Elemente im Array (außer NULL).

## Analyze-Syntax

```python
func.array_unique( <array> )
```

## Analyze-Beispiele

```python
func.array_unique([1, 2, 3, 3, 4])

┌─────────────────────────────────────┐
│ func.array_unique([1, 2, 3, 3, 4])  │
├─────────────────────────────────────┤
│                                   4 │
└─────────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_UNIQUE( <array> )
```

## SQL-Beispiele

```sql
SELECT ARRAY_UNIQUE([1, 2, 3, 3, 4]);

┌───────────────────────────────┐
│ array_unique([1, 2, 3, 3, 4]) │
├───────────────────────────────┤
│                             4 │
└───────────────────────────────┘
```
