---
title: ARRAY_FILTER (Lakehouse v1)
description: ARRAY_FILTER — constrói uma matriz com os elementos da matriz de entrada para os quais a função lambda devolve verdadeiro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-filter.md
---

Constrói uma matriz com os elementos da matriz de entrada para os quais a função lambda devolve verdadeiro.

## Sintaxe do Analyze

```python
func.array_filter( <array>, <lambda> )
```

## Exemplos do Analyze

```python
func.array_filter([1, 2, 3], x -> (x > 1))

┌─────────────────────────────────────────────┐
│ func.array_filter([1, 2, 3], x -> (x > 1))  │
├─────────────────────────────────────────────┤
│ [2,3]                                       │
└─────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_FILTER( <array>, <lambda> )
```

## Exemplos SQL

```sql
SELECT ARRAY_FILTER([1, 2, 3], x -> x > 1);

┌───────────────────────────────────────┐
│ array_filter([1, 2, 3], x -> (x > 1)) │
├───────────────────────────────────────┤
│ [2,3]                                 │
└───────────────────────────────────────┘
```
