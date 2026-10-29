---
title: MIN (Lakehouse v2)
description: MIN — devolve o valor mínimo de um conjunto de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min.md
---

Devolve o valor mínimo de um conjunto de valores.

## Sintaxe do Analyze

```python
func.min(get_column(table, 'salary'))
```

## Exemplos do Analyze

```python
func.min(get_column(table, 'salary'))

┌───────┐
│ 35000 │
└───────┘
```

## Sintaxe SQL

```sql
MIN(<salary>)
```

## Exemplos SQL

```sql
SELECT MIN(salary) FROM employees;

┌───────┐
│ 35000 │
└───────┘
```
