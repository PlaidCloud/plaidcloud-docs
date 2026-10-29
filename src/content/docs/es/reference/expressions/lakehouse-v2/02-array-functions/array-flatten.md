---
title: ARRAY_FLATTEN (Lakehouse v2)
description: ARRAY_FLATTEN — aplana matrices anidadas en una matriz de un solo nivel.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-flatten.md
---

Aplana matrices anidadas en una matriz de un solo nivel.

## Sintaxis de Analyze

```python
func.array_flatten([[1,2],[3,4]])
```

## Ejemplos de Analyze

```python
func.array_flatten([[1, 2], [3, 4]])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## Sintaxis de SQL

```sql
ARRAY_FLATTEN([[1,2],[3,4]])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_FLATTEN([[1, 2], [3, 4]]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
