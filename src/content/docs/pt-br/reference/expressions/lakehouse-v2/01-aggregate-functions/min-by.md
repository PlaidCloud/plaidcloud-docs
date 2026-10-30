---
title: MIN_BY (Lakehouse v2)
description: MIN_BY — retorna o valor de uma coluna associado ao valor mínimo de outra coluna.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min-by.md
---

Retorna o valor de uma coluna associado ao valor mínimo de outra coluna.

## Sintaxe do Analyze

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Exemplos do Analyze

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))

┌─────┐
│ Bob │
└─────┘
```

## Sintaxe SQL

```sql
MIN_BY(<name>, <salary>)
```

## Exemplos SQL

```sql
SELECT MIN_BY(name, salary) FROM employees;

┌─────┐
│ Bob │
└─────┘
```
