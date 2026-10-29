---
title: MAX (Lakehouse v2)
description: MAX — retorna o valor máximo em um conjunto de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max.md
---

Retorna o valor máximo em um conjunto de valores.

## Sintaxe do Analyze

```python
func.max(get_column(table, 'salary'))
```

## Exemplos do Analyze

```python
func.max(get_column(table, 'salary'))

┌────────┐
│ 150000 │
└────────┘
```

## Sintaxe SQL

```sql
MAX(<salary>)
```

## Exemplos SQL

```sql
SELECT MAX(salary) FROM employees;

┌────────┐
│ 150000 │
└────────┘
```
