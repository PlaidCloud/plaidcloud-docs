---
title: SUM (Lakehouse v2)
description: SUM – gibt die Summe aller Werte einer Gruppe zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum.md
---

Gibt die Summe aller Werte einer Gruppe zurück.

## Analyze-Syntax

```python
func.sum(get_column(table, 'amount'))
```

## Analyze-Beispiele

```python
func.sum(get_column(table, 'amount'))
```

## SQL-Syntax

```sql
SUM(<amount>)
```

## SQL-Beispiele

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
