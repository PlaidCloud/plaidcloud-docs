---
title: COUNT_IF (Lakehouse v2)
description: COUNT_IF — devolve o número de linhas para as quais a expressão é TRUE.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count-if.md
---

Devolve o número de linhas para as quais a expressão é TRUE.

## Sintaxe do Analyze

```python
func.count_if(get_column(table, 'salary') > 80000)
```

## Exemplos do Analyze

```python
func.count_if(get_column(table, 'salary') > 80000)

┌────┐
│ 42 │
└────┘
```

## Sintaxe SQL

```sql
COUNT_IF(<salary> > 80000)
```

## Exemplos de SQL

```sql
SELECT COUNT_IF(salary > 80000) FROM employees;

┌────┐
│ 42 │
└────┘
```
