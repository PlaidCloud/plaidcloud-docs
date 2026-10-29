---
title: ARRAY_TRANSFORM (Lakehouse v1)
description: ARRAY_TRANSFORM — devolve uma matriz que resulta de aplicar a função lambda a cada elemento da matriz de entrada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-transform.md
---

Devolve uma matriz que resulta de aplicar a função lambda a cada elemento da matriz de entrada.

## Sintaxe do Analyze

```python
func.array_transform( <array>, <lambda> )
```

## Exemplos do Analyze

```python
func.array_transform([1, 2, 3], x -> (x + 1))

┌───────────────────────────────────────────────┐
│ func.array_transform([1, 2, 3], x -> (x + 1)) │
├───────────────────────────────────────────────┤
│ [2,3,4]                                       │
└───────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_TRANSFORM( <array>, <lambda> )
```

## Alias

- [ARRAY_APPLY](../array-apply)

## Exemplos SQL

```sql
SELECT ARRAY_TRANSFORM([1, 2, 3], x -> x + 1);

┌──────────────────────────────────────────┐
│ array_transform([1, 2, 3], x -> (x + 1)) │
├──────────────────────────────────────────┤
│ [2,3,4]                                  │
└──────────────────────────────────────────┘
```
