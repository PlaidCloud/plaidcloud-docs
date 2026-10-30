---
title: ARRAY_GENERATE (Lakehouse v2)
description: ARRAY_GENERATE — genera una matriz de valores secuenciales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-generate.md
---

Genera una matriz de valores secuenciales.

## Sintaxis de Analyze

```python
func.array_generate(1, 5)
```

## Ejemplos de Analyze

```python
func.array_generate(1, 5)

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_GENERATE(1, 5)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_GENERATE(1, 5);

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```
