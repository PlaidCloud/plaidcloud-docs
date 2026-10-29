---
title: BOOL_OR (Lakehouse v2)
description: BOOL_OR devuelve TRUE si algún valor del grupo es TRUE.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bool-or.md
---

Devuelve TRUE si algún valor del grupo es TRUE.

## Sintaxis de Analyze

```python
func.bool_or(get_column(table, 'is_active'))
```

## Ejemplos de Analyze

```python
func.bool_or(get_column(table, 'is_active'))
```

## Sintaxis de SQL

```sql
BOOL_OR(<is_active>)
```

## Ejemplos de SQL

```sql
SELECT department, BOOL_OR(is_active) FROM employees GROUP BY department;

┌────────────┬─────────────────────┐
│ department │ bool_or(is_active)  │
├────────────┼─────────────────────┤
│ Sales      │                   1 │
│ IT         │                   1 │
└────────────┴─────────────────────┘
```
