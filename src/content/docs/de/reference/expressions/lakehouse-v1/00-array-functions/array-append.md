---
title: ARRAY_APPEND (Lakehouse v1)
description: ARRAY_APPEND – stellt dem Array ein Element voran.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-append.md
---

Stellt dem Array ein Element voran.

## Analyze-Syntax

```python
func.array_append( <array>, <element>)
```

## Analyze-Beispiele

```python
func.array_append([3, 4], 5)

┌──────────────────────────────┐
│ func.array_append([3, 4], 5) │
├──────────────────────────────┤
│ [3,4,5]                      │
└──────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_APPEND( <array>, <element>)
```

## SQL-Beispiele

```sql
SELECT ARRAY_APPEND([3, 4], 5);

┌─────────────────────────┐
│ array_append([3, 4], 5) │
├─────────────────────────┤
│ [3,4,5]                 │
└─────────────────────────┘
```
