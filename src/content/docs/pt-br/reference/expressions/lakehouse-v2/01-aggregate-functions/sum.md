---
title: SUM (Lakehouse v2)
description: SUM — retorna a soma de todos os valores de um grupo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum.md
---

Retorna a soma de todos os valores de um grupo.

## Sintaxe do Analyze

```python
func.sum(get_column(table, 'amount'))
```

## Exemplos do Analyze

```python
func.sum(get_column(table, 'amount'))
```

## Sintaxe SQL

```sql
SUM(<amount>)
```

## Exemplos SQL

```sql
SELECT department, SUM(salary) FROM employees GROUP BY department;

┌────────────┬─────────────┐
│ department │ sum(salary) │
├────────────┼─────────────┤
│ Sales      │      195000 │
│ IT         │      246000 │
│ HR         │      210000 │
└────────────┴─────────────┘
```
