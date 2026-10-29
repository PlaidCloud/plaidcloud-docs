---
title: ARRAY_CONCAT (Lakehouse v2)
description: ARRAY_CONCAT — concatena várias matrizes numa única matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-concat.md
---

Concatena várias matrizes numa única matriz.

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
