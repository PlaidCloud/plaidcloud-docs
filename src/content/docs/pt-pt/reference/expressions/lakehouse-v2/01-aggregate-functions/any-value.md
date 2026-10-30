---
title: ANY_VALUE (Lakehouse v2)
description: ANY_VALUE — devolve um valor arbitrário de um grupo de linhas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/any-value.md
---

Devolve um valor arbitrário de um grupo de linhas.

## Sintaxe do Analyze

```python
func.any_value(get_column(table, 'department'))
```

## Exemplos do Analyze

```python
func.any_value(get_column(table, 'department'))

┌───────┐
│ Sales │
└───────┘
```

## Sintaxe SQL

```sql
ANY_VALUE(<department>)
```

## Exemplos de SQL

```sql
SELECT ANY_VALUE(department) FROM employees;

┌───────┐
│ Sales │
└───────┘
```
