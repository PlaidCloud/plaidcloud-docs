---
title: "CARDINALITY (Array, Lakehouse v2)"
description: CARDINALITY — retorna o número de elementos de um array. Alias de `ARRAY_LENGTH`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/cardinality.md
---

Retorna o número de elementos de um array. Alias de `ARRAY_LENGTH`.

## Sintaxe do Analyze

```python
func.cardinality([1, 2, 3])
```

## Exemplos do Analyze

```python
func.cardinality([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## Sintaxe SQL

```sql
CARDINALITY([1, 2, 3])
```

## Exemplos SQL

```sql
SELECT CARDINALITY([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
