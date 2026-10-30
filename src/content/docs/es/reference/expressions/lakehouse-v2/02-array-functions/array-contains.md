---
title: ARRAY_CONTAINS (Lakehouse v2)
description: ARRAY_CONTAINS — comprueba si una matriz contiene un elemento específico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains.md
---

Comprueba si una matriz contiene un elemento específico.

## Sintaxis de Analyze

```python
func.array_contains([1, 2, 3], 2)
```

## Ejemplos de Analyze

```python
func.array_contains([1, 2, 3], 2)

┌───┐
│ 1 │
└───┘
```

## Sintaxis de SQL

```sql
ARRAY_CONTAINS([1, 2, 3], 2)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_CONTAINS([1, 2, 3], 2);

┌───┐
│ 1 │
└───┘
```
