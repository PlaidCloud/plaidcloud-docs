---
title: BOOL_OR (Lakehouse v2)
description: BOOL_OR — renvoie TRUE si au moins une valeur du groupe est TRUE.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bool-or.md
---

Renvoie TRUE si au moins une valeur du groupe est TRUE.

## Syntaxe Analyze

```python
func.bool_or(get_column(table, 'is_active'))
```

## Exemples Analyze

```python
func.bool_or(get_column(table, 'is_active'))
```

## Syntaxe SQL

```sql
BOOL_OR(<is_active>)
```

## Exemples SQL

```sql
SELECT department, BOOL_OR(is_active) FROM employees GROUP BY department;

┌────────────┬─────────────────────┐
│ department │ bool_or(is_active)  │
├────────────┼─────────────────────┤
│ Sales      │                   1 │
│ IT         │                   1 │
└────────────┴─────────────────────┘
```
