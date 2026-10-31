---
title: COUNT (Lakehouse v2)
description: COUNT gibt die Anzahl der Zeilen oder der Werte ungleich NULL zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count.md
---

Gibt die Anzahl der Zeilen oder der Werte ungleich NULL zurück.

## Analyze-Syntax

```python
func.count()
```

## Analyze-Beispiele

```python
func.count()
```

## SQL-Syntax

```sql
COUNT()
```

## SQL-Beispiele

```sql
SELECT COUNT(*) FROM employees;

┌──────────┐
│ count(*) │
├──────────┤
│     1000 │
└──────────┘

SELECT COUNT(DISTINCT department) FROM employees;

┌──────────────────────────────┐
│ count(distinct department)   │
├──────────────────────────────┤
│                            5 │
└──────────────────────────────┘
```
