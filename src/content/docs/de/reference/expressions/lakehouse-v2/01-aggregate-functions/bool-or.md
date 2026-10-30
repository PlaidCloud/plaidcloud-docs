---
title: BOOL_OR (Lakehouse v2)
description: BOOL_OR gibt TRUE zurück, wenn ein beliebiger Wert in der Gruppe TRUE ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bool-or.md
---

Gibt TRUE zurück, wenn ein beliebiger Wert in der Gruppe TRUE ist.

## Analyze-Syntax

```python
func.bool_or(get_column(table, 'is_active'))
```

## Analyze-Beispiele

```python
func.bool_or(get_column(table, 'is_active'))
```

## SQL-Syntax

```sql
BOOL_OR(<is_active>)
```

## SQL-Beispiele

```sql
SELECT department, BOOL_OR(is_active) FROM employees GROUP BY department;

┌────────────┬─────────────────────┐
│ department │ bool_or(is_active)  │
├────────────┼─────────────────────┤
│ Sales      │                   1 │
│ IT         │                   1 │
└────────────┴─────────────────────┘
```
