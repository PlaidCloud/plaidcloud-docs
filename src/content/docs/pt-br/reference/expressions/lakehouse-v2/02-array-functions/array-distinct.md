---
title: ARRAY_DISTINCT (Lakehouse v2)
description: ARRAY_DISTINCT — remove elementos duplicados de um array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-distinct.md
---

Remove elementos duplicados de um array.

## Sintaxe do Analyze

```python
func.array_distinct([1, 2, 2, 3, 3])
```

## Exemplos do Analyze

```python
func.array_distinct([1, 2, 2, 3, 3])

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## Sintaxe SQL

```sql
ARRAY_DISTINCT([1, 2, 2, 3, 3])
```

## Exemplos SQL

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 3, 3]);

┌─────────┐
│ [1,2,3] │
└─────────┘
```
