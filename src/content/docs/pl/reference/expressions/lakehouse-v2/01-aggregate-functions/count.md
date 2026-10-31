---
title: COUNT (Lakehouse v2)
description: COUNT — zwraca liczbę wierszy lub wartości innych niż NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count.md
---

Zwraca liczbę wierszy lub wartości innych niż NULL.

## Składnia Analyze

```python
func.count()
```

## Przykłady Analyze

```python
func.count()
```

## Składnia SQL

```sql
COUNT()
```

## Przykłady SQL

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
