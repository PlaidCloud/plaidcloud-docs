---
title: ARRAY_FILTER (Lakehouse v2)
description: ARRAY_FILTER — filtra elementos de um array usando uma expressão lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-filter.md
---

Filtra elementos de um array usando uma expressão lambda.

## Sintaxe do Analyze

```python
func.array_filter(get_column(table, 'arr'), lambda x: x > 2)
```

## Exemplos do Analyze

```python
func.array_filter([1, 2, 3, 4, 5], lambda x: x > 2)

┌─────────┐
│ [3,4,5] │
└─────────┘
```

## Sintaxe SQL

```sql
ARRAY_FILTER(<arr>, lambda x: x > 2)
```

## Exemplos SQL

```sql
SELECT ARRAY_FILTER([1, 2, 3, 4, 5], x -> x > 2);

┌─────────┐
│ [3,4,5] │
└─────────┘
```
