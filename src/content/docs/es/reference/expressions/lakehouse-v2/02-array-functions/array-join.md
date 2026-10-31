---
title: ARRAY_JOIN (Lakehouse v2)
description: ARRAY_JOIN — concatena los elementos de una matriz en una cadena con un separador.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-join.md
---

Concatena los elementos de una matriz en una cadena con un separador.

## Sintaxis de Analyze

```python
func.array_join([1,2,3], '-')
```

## Ejemplos de Analyze

```python
func.array_join(['a', 'b', 'c'], '-')

┌─────────┐
│ 'a-b-c' │
└─────────┘
```

## Sintaxis de SQL

```sql
ARRAY_JOIN([1,2,3], '-')
```

## Ejemplos de SQL

```sql
SELECT ARRAY_JOIN(['a', 'b', 'c'], '-');

┌───────┐
│ a-b-c │
└───────┘
```
