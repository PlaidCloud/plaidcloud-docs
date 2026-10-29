---
title: "CARDINALITY (Matriz, Lakehouse v2)"
description: CARDINALITY — devuelve el número de elementos de una matriz. Alias de `ARRAY_LENGTH`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/cardinality.md
---

Devuelve el número de elementos de una matriz. Alias de `ARRAY_LENGTH`.

## Sintaxis de Analyze

```python
func.cardinality([1, 2, 3])
```

## Ejemplos de Analyze

```python
func.cardinality([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## Sintaxis de SQL

```sql
CARDINALITY([1, 2, 3])
```

## Ejemplos de SQL

```sql
SELECT CARDINALITY([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
