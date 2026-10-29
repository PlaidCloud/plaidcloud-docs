---
title: ARRAY_MAP (Lakehouse v2)
description: ARRAY_MAP — applique une expression lambda à chaque élément d'un tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-map.md
---

Applique une expression lambda à chaque élément d'un tableau.

## Syntaxe Analyze

```python
func.array_map(get_column(table, 'arr'), lambda x: x * 2)
```

## Exemples Analyze

```python
func.array_map([1, 2, 3], lambda x: x * 2)

┌─────────┐
│ [2,4,6] │
└─────────┘
```

## Syntaxe SQL

```sql
ARRAY_MAP(<arr>, lambda x: x * 2)
```

## Exemples SQL

```sql
SELECT ARRAY_MAP([1, 2, 3], x -> x * 2);

┌─────────┐
│ [2,4,6] │
└─────────┘
```
