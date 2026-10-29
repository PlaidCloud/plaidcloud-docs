---
title: YEARS_DIFF (Lakehouse v2)
description: YEARS_DIFF — zwraca liczbę lat między dwiema datami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-diff.md
---

Zwraca liczbę lat między dwiema datami.

## Składnia Analyze

```python
func.years_diff(<end_date>, <start_date>)
```

## Przykłady Analyze

```python
func.years_diff('2029-01-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## Składnia SQL

```sql
YEARS_DIFF(<end_date>, <start_date>)
```

## Przykłady SQL

```sql
SELECT YEARS_DIFF('2029-01-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
