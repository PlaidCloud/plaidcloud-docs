---
title: COUNT_IF (Lakehouse v2)
description: COUNT_IF gibt die Anzahl der Zeilen zurück, für die der Ausdruck TRUE ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count-if.md
---

Gibt die Anzahl der Zeilen zurück, für die der Ausdruck TRUE ist.

## Analyze-Syntax

```python
func.count_if(get_column(table, 'salary') > 80000)
```

## Analyze-Beispiele

```python
func.count_if(get_column(table, 'salary') > 80000)

┌────┐
│ 42 │
└────┘
```

## SQL-Syntax

```sql
COUNT_IF(<salary> > 80000)
```

## SQL-Beispiele

```sql
SELECT COUNT_IF(salary > 80000) FROM employees;

┌────┐
│ 42 │
└────┘
```
