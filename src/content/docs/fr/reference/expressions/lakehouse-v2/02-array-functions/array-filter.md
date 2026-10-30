---
title: ARRAY_FILTER (Lakehouse v2)
description: ARRAY_FILTER — filtre les éléments d'un tableau à l'aide d'une expression lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-filter.md
---

Filtre les éléments d'un tableau à l'aide d'une expression lambda.

## Syntaxe Analyze

```python
func.array_filter(get_column(table, 'arr'), lambda x: x > 2)
```

## Exemples Analyze

```python
func.array_filter([1, 2, 3, 4, 5], lambda x: x > 2)

┌─────────┐
│ [3,4,5] │
└─────────┘
```

## Syntaxe SQL

```sql
ARRAY_FILTER(<arr>, lambda x: x > 2)
```

## Exemples SQL

```sql
SELECT ARRAY_FILTER([1, 2, 3, 4, 5], x -> x > 2);

┌─────────┐
│ [3,4,5] │
└─────────┘
```
