---
title: ARRAY_MAP (Lakehouse v2)
description: ARRAY_MAP — stosuje wyrażenie lambda do każdego elementu tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-map.md
---

Stosuje wyrażenie lambda do każdego elementu tablicy.

## Składnia Analyze

```python
func.array_map(get_column(table, 'arr'), lambda x: x * 2)
```

## Przykłady Analyze

```python
func.array_map([1, 2, 3], lambda x: x * 2)

┌─────────┐
│ [2,4,6] │
└─────────┘
```

## Składnia SQL

```sql
ARRAY_MAP(<arr>, lambda x: x * 2)
```

## Przykłady SQL

```sql
SELECT ARRAY_MAP([1, 2, 3], x -> x * 2);

┌─────────┐
│ [2,4,6] │
└─────────┘
```
