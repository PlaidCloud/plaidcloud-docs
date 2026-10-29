---
title: ARRAY_FILTER (Lakehouse v2)
description: ARRAY_FILTER – filtert die Elemente eines Arrays mit einem Lambda-Ausdruck.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-filter.md
---

Filtert die Elemente eines Arrays mit einem Lambda-Ausdruck.

## Analyze-Syntax

```python
func.array_filter(get_column(table, 'arr'), lambda x: x > 2)
```

## Analyze-Beispiele

```python
func.array_filter([1, 2, 3, 4, 5], lambda x: x > 2)

┌─────────┐
│ [3,4,5] │
└─────────┘
```

## SQL-Syntax

```sql
ARRAY_FILTER(<arr>, lambda x: x > 2)
```

## SQL-Beispiele

```sql
SELECT ARRAY_FILTER([1, 2, 3, 4, 5], x -> x > 2);

┌─────────┐
│ [3,4,5] │
└─────────┘
```
