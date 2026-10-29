---
title: ARRAY_MAP (Lakehouse v2)
description: ARRAY_MAP – wendet einen Lambda-Ausdruck auf jedes Element eines Arrays an.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-map.md
---

Wendet einen Lambda-Ausdruck auf jedes Element eines Arrays an.

## Analyze-Syntax

```python
func.array_map(get_column(table, 'arr'), lambda x: x * 2)
```

## Analyze-Beispiele

```python
func.array_map([1, 2, 3], lambda x: x * 2)

┌─────────┐
│ [2,4,6] │
└─────────┘
```

## SQL-Syntax

```sql
ARRAY_MAP(<arr>, lambda x: x * 2)
```

## SQL-Beispiele

```sql
SELECT ARRAY_MAP([1, 2, 3], x -> x * 2);

┌─────────┐
│ [2,4,6] │
└─────────┘
```
