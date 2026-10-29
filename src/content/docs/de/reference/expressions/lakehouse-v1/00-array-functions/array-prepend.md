---
title: ARRAY_PREPEND (Lakehouse v1)
description: ARRAY_PREPEND – stellt dem Array ein Element voran.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-prepend.md
---

Stellt dem Array ein Element voran.

## Analyze-Syntax

```python
func.array_prepend( <element>, <array> )
```

## Analyze-Beispiele

```python
func.array_prepend(1, [3, 4])

┌────────────────────────────────┐
│ func.array_prepend(1, [3, 4])  │
├────────────────────────────────┤
│ [1,3,4]                        │
└────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_PREPEND( <element>, <array> )
```

## SQL-Beispiele

```sql
SELECT ARRAY_PREPEND(1, [3, 4]);

┌──────────────────────────┐
│ array_prepend(1, [3, 4]) │
├──────────────────────────┤
│ [1,3,4]                  │
└──────────────────────────┘
```
