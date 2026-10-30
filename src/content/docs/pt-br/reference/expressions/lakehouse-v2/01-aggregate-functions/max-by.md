---
title: MAX_BY (Lakehouse v2)
description: MAX_BY — retorna o valor de uma coluna associado ao valor máximo de outra coluna.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max-by.md
---

Retorna o valor de uma coluna associado ao valor máximo de outra coluna.

## Sintaxe do Analyze

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Exemplos do Analyze

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))

┌───────┐
│ Alice │
└───────┘
```

## Sintaxe SQL

```sql
MAX_BY(<name>, <salary>)
```

## Exemplos SQL

```sql
SELECT MAX_BY(name, salary) FROM employees;

┌───────┐
│ Alice │
└───────┘
```
