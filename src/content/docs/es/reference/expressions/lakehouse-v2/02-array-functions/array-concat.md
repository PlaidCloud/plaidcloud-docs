---
title: ARRAY_CONCAT (Lakehouse v2)
description: ARRAY_CONCAT — concatena varias matrices en una sola matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-concat.md
---

Concatena varias matrices en una sola matriz.

## Sintaxis de Analyze

```python
func.array_concat([1, 2], [3, 4])
```

## Ejemplos de Analyze

```python
func.array_concat([1, 2], [3, 4])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## Sintaxis de SQL

```sql
ARRAY_CONCAT([1, 2], [3, 4])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
