---
title: DAYS_DIFF (Lakehouse v2)
description: DAYS_DIFF — zwraca liczbę dni między dwiema datami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-diff.md
---

Zwraca liczbę dni między dwiema datami.

## Składnia Analyze

```python
func.days_diff(<end_date>, <start_date>)
```

## Przykłady Analyze

```python
func.days_diff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## Składnia SQL

```sql
DAYS_DIFF(<end_date>, <start_date>)
```

## Przykłady SQL

```sql
SELECT DAYS_DIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```
