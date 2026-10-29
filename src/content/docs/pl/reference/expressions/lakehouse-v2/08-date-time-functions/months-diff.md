---
title: MONTHS_DIFF (Lakehouse v2)
description: MONTHS_DIFF — zwraca liczbę miesięcy między dwiema datami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-diff.md
---

Zwraca liczbę miesięcy między dwiema datami.

## Składnia Analyze

```python
func.months_diff(<end_date>, <start_date>)
```

## Przykłady Analyze

```python
func.months_diff('2024-06-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## Składnia SQL

```sql
MONTHS_DIFF(<end_date>, <start_date>)
```

## Przykłady SQL

```sql
SELECT MONTHS_DIFF('2024-06-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
