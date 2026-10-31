---
title: ARRAY_TRANSFORM (Lakehouse v1)
description: ARRAY_TRANSFORM — devuelve un arreglo resultante de aplicar la función lambda a cada elemento del arreglo de entrada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-transform.md
---

Devuelve un arreglo resultante de aplicar la función lambda a cada elemento del arreglo de entrada.

## Sintaxis de Analyze

```python
func.array_transform( <array>, <lambda> )
```

## Ejemplos de Analyze

```python
func.array_transform([1, 2, 3], x -> (x + 1))

┌───────────────────────────────────────────────┐
│ func.array_transform([1, 2, 3], x -> (x + 1)) │
├───────────────────────────────────────────────┤
│ [2,3,4]                                       │
└───────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_TRANSFORM( <array>, <lambda> )
```

## Alias

- [ARRAY_APPLY](../array-apply)

## Ejemplos de SQL

```sql
SELECT ARRAY_TRANSFORM([1, 2, 3], x -> x + 1);

┌──────────────────────────────────────────┐
│ array_transform([1, 2, 3], x -> (x + 1)) │
├──────────────────────────────────────────┤
│ [2,3,4]                                  │
└──────────────────────────────────────────┘
```
