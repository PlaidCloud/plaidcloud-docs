---
title: BOOL_OR (Lakehouse v2)
description: BOOL_OR — devolve TRUE se algum valor do grupo for TRUE.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bool-or.md
---

Devolve TRUE se algum valor do grupo for TRUE.

## Sintaxe do Analyze

```python
func.bool_or(get_column(table, 'is_active'))
```

## Exemplos do Analyze

```python
func.bool_or(get_column(table, 'is_active'))
```

## Sintaxe SQL

```sql
BOOL_OR(<is_active>)
```

## Exemplos de SQL

```sql
SELECT department, BOOL_OR(is_active) FROM employees GROUP BY department;

┌────────────┬─────────────────────┐
│ department │ bool_or(is_active)  │
├────────────┼─────────────────────┤
│ Sales      │                   1 │
│ IT         │                   1 │
└────────────┴─────────────────────┘
```
