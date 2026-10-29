---
title: AVG (Lakehouse v2)
description: AVG — retorna o valor médio de uma coluna numérica.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/avg.md
---

Retorna o valor médio de uma coluna numérica.

## Sintaxe do Analyze

```python
func.avg(get_column(table, 'salary'))
```

## Exemplos do Analyze

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
