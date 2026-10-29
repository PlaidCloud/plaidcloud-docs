---
title: ARRAY_CONCAT (Lakehouse v2)
description: ARRAY_CONCAT — concatena vários arrays em um único array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-concat.md
---

Concatena vários arrays em um único array.

## Sintaxe do Analyze

```python
func.array_concat([1, 2], [3, 4])
```

## Exemplos do Analyze

```python
func.array_concat([1, 2], [3, 4])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## Sintaxe SQL

```sql
ARRAY_CONCAT([1, 2], [3, 4])
```

## Exemplos SQL

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
