---
title: ARRAY_AVG (Lakehouse v2)
description: ARRAY_AVG — retorna a média dos elementos de um array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-avg.md
---

Retorna a média dos elementos de um array.

## Sintaxe do Analyze

```python
func.array_avg([1, 2, 3, 4])
```

## Exemplos do Analyze

```python
func.array_avg([10, 20, 30])

┌──────┐
│ 20.0 │
└──────┘
```

## Sintaxe SQL

```sql
ARRAY_AVG([1, 2, 3, 4])
```

## Exemplos SQL

```sql
SELECT ARRAY_AVG([10, 20, 30]);

┌──────┐
│ 20.0 │
└──────┘
```
