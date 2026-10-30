---
title: AVG (Lakehouse v2)
description: AVG — devolve o valor médio de uma coluna numérica.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/avg.md
---

Devolve o valor médio de uma coluna numérica.

## Sintaxe no Analyze

```python
func.avg(get_column(table, 'salary'))
```

## Exemplos no Analyze

```python
func.avg(get_column(table, 'salary'))
```

## Sintaxe SQL

```sql
AVG(<salary>)
```

## Exemplos SQL

```sql
SELECT department, AVG(salary) FROM employees GROUP BY department;

┌────────────┬──────────────┐
│ department │ avg(salary)  │
├────────────┼──────────────┤
│ Sales      │     65000.00 │
│ IT         │     82000.00 │
└────────────┴──────────────┘
```
